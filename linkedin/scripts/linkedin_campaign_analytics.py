import requests
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os
import sys
import time

# Ajouter le répertoire parent au path pour importer config_loader
# Support pour Cloud Functions (config dans le dossier parent) et local (config à la racine)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class LinkedInCampaignAnalytics:
    """
    Client pour récupérer les analytics des campagnes LinkedIn via l'API Marketing
    Documentation: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting
    """

    def __init__(self, access_token: str, account_id: Optional[str] = None,
                 project_id: Optional[str] = None, dataset_id: str = "linkedin_ads_advertising",
                 credentials_path: Optional[str] = None):
        """
        Initialise le client avec le token d'accès

        Args:
            access_token: Token OAuth 2.0 LinkedIn avec les permissions marketing
            account_id: ID du compte publicitaire (optionnel)
            project_id: ID du projet Google Cloud (optionnel, utilise GOOGLE_CLOUD_PROJECT si non fourni)
            dataset_id: ID du dataset BigQuery (défaut: linkedin_ads_advertising)
            credentials_path: Chemin vers le fichier JSON des credentials GCP (optionnel)
        """
        self.access_token = access_token
        self.account_id = account_id
        self.base_url = "https://api.linkedin.com/rest"

        # Configuration BigQuery
        self.project_id = project_id or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.dataset_id = dataset_id
        self.credentials_path = credentials_path
        self.bq_client = None

    def _get_headers(self) -> Dict[str, str]:
        """Retourne les headers requis pour l'API LinkedIn Marketing"""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "LinkedIn-Version": "202601",
            "X-Restli-Protocol-Version": "2.0.0"
        }

    def get_ad_accounts(self) -> List[Dict]:
        """
        Récupère la liste des comptes publicitaires accessibles

        Returns:
            list: Liste des comptes publicitaires
        """
        url = f"{self.base_url}/adAccounts"
        query_params = "q=search&search=(status:(values:List(ACTIVE,CANCELED,DRAFT,REMOVED)))&count=100"
        full_url = f"{url}?{query_params}"

        response = requests.get(full_url, headers=self._get_headers())

        if response.status_code != 200:
            print(f"Erreur API: {response.status_code} - {response.text}")
            response.raise_for_status()

        data = response.json()
        return data.get("elements", [])

    def get_campaigns(self, account_id: Optional[str] = None) -> List[Dict]:
        """
        Récupère la liste des campagnes

        Args:
            account_id: ID du compte publicitaire (optionnel, utilise self.account_id par défaut)

        Returns:
            list: Liste des campagnes avec leurs détails
        """
        acc_id = account_id or self.account_id

        if not acc_id:
            raise ValueError("account_id est requis. Passez-le en paramètre ou lors de l'initialisation.")

        url = f"{self.base_url}/adAccounts/{acc_id}/adCampaigns"
        # Le finder q=search requiert un critère explicite — sans search=(status:...) l'API retourne []
        # L'URL est construite manuellement car requests encode les parenthèses que LinkedIn refuse
        all_campaigns = []
        start = 0
        count = 100
        max_campaigns = 2000

        while start < max_campaigns:
            query_params = (
                f"q=search"
                f"&search=(status:(values:List(ACTIVE,PAUSED,COMPLETED)))"
                f"&start={start}&count={count}"
            )
            full_url = f"{url}?{query_params}"

            response = requests.get(full_url, headers=self._get_headers())

            if response.status_code != 200:
                print(f"Erreur API: {response.status_code} - {response.text}")
                response.raise_for_status()

            data = response.json()
            elements = data.get("elements", [])
            all_campaigns.extend(elements)

            if len(elements) < count:
                break
            start += count

        return all_campaigns

    def get_analytics(self,
                      campaign_urns: List[str],
                      start_date: datetime,
                      end_date: datetime,
                      pivot: str = "CAMPAIGN",
                      time_granularity: str = "ALL",
                      fields: Optional[List[str]] = None) -> Dict:
        """
        Récupère les analytics pour une ou plusieurs campagnes (une par une)

        Args:
            campaign_urns: Liste des URNs des campagnes (ex: ['urn:li:sponsoredCampaign:123456'])
            start_date: Date de début
            end_date: Date de fin
            pivot: Niveau d'agrégation (CAMPAIGN, CREATIVE, ACCOUNT, CAMPAIGN_GROUP)
            time_granularity: Granularité temporelle (ALL, DAILY, MONTHLY, YEARLY)
            fields: Liste des champs à récupérer (si None, récupère les principaux)

        Returns:
            dict: Données analytics (combinées de toutes les campagnes)
        """
        # Utiliser le format REST selon la doc officielle
        url = f"{self.base_url}/adAnalytics"

        # Champs par défaut si non spécifiés
        if fields is None:
            fields = [
                "pivotValues",  # IMPORTANT: nécessaire pour identifier les campagnes/creatives
                "dateRange",    # IMPORTANT: période des données
                "impressions",
                "clicks",
                "costInUsd",
                "landingPageClicks",
                "reactions",
                "comments",
                "shares",
                "oneClickLeads",
                "externalWebsiteConversions",
                "externalWebsitePostClickConversions",
                "externalWebsitePostViewConversions"
            ]

        # Récupérer les analytics campagne par campagne
        all_elements = []
        total_campaigns = len(campaign_urns)

        for idx, campaign_urn in enumerate(campaign_urns, 1):
            # Format selon la doc officielle LinkedIn
            # https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting
            # Exemple: GET https://api.linkedin.com/rest/adAnalytics?q=analytics&pivot=CREATIVE&timeGranularity=ALL&dateRange=(start:(year:2024,month:1,day:1))&campaigns=List(urn%3Ali%3AsponsoredCampaign%3A1234567)

            # LinkedIn n'accepte PAS l'encodage URL standard pour dateRange et campaigns
            # Il faut construire l'URL manuellement en n'encodant que les URNs
            campaign_urn_encoded = campaign_urn.replace(':', '%3A')
            date_range_str = (
                f"(start:(year:{start_date.year},month:{start_date.month},day:{start_date.day}),"
                f"end:(year:{end_date.year},month:{end_date.month},day:{end_date.day}))"
            )
            campaigns_str = f"List({campaign_urn_encoded})"

            # Construire les fields (si spécifiés)
            fields_str = ""
            if fields:
                # Format: fields=field1,field2,field3 (pas de List() !)
                fields_list = ",".join(fields)
                fields_str = f"&fields={fields_list}"

            # Construire l'URL complète sans utiliser params
            query_params = f"q=analytics&pivot={pivot}&dateRange={date_range_str}&timeGranularity={time_granularity}&campaigns={campaigns_str}{fields_str}"
            full_url = f"{url}?{query_params}"
            
            # Log de la requête pour diagnostic
            if idx == 1:  # Afficher seulement pour la première campagne pour ne pas surcharger les logs
                print(f"\n🔍 DEBUG - Première requête API:")
                print(f"   Pivot: {pivot}")
                print(f"   Fields demandés: {fields if fields else 'TOUS (aucun field spécifié)'}")
                print(f"   URL (tronquée): {full_url[:150]}...")

            # Retry logic avec backoff pour gérer le rate limiting
            max_retries = 3
            retry_delay = 2  # secondes

            for attempt in range(max_retries):
                try:
                    response = requests.get(
                        full_url,
                        headers=self._get_headers(),
                        timeout=30
                    )

                    # Si rate limited (429) ou erreur serveur (5xx), attendre et réessayer
                    if response.status_code == 429:
                        retry_after = int(response.headers.get('Retry-After', retry_delay * (attempt + 1)))
                        print(f"  [{idx}/{total_campaigns}] Rate limit atteint, pause de {retry_after}s...")
                        time.sleep(retry_after)
                        continue

                    if response.status_code >= 500:
                        if attempt < max_retries - 1:
                            time.sleep(retry_delay * (attempt + 1))
                            continue

                    if response.status_code == 200:
                        campaign_data = response.json()
                        elements = campaign_data.get("elements", [])

                        if elements:
                            # Log détaillé des données reçues pour diagnostic
                            print(f"  [{idx}/{total_campaigns}] ✓ {len(elements)} élément(s) reçu(s) pour {campaign_urn}")
                            
                            # Log des métriques d'engagement du premier élément pour diagnostic
                            if elements and len(elements) > 0:
                                first_elem = elements[0]
                                reactions = first_elem.get("reactions", "ABSENT")
                                comments = first_elem.get("comments", "ABSENT")
                                shares = first_elem.get("shares", "ABSENT")
                                impressions = first_elem.get("impressions", "ABSENT")
                                clicks = first_elem.get("clicks", "ABSENT")
                                
                                print(f"  ├─ Métriques engagement: reactions={reactions}, comments={comments}, shares={shares}")
                                print(f"  └─ Métriques base: impressions={impressions}, clicks={clicks}")
                            
                            all_elements.extend(elements)
                        else:
                            print(f"  [{idx}/{total_campaigns}] ⚠️  Aucun élément reçu pour {campaign_urn}")
                        break  # Succès, sortir de la boucle de retry

                    # Autre erreur, passer à la campagne suivante
                    break

                except requests.exceptions.RequestException as e:
                    if attempt < max_retries - 1:
                        print(f"  [{idx}/{total_campaigns}] Erreur réseau, retry {attempt + 1}/{max_retries}...")
                        time.sleep(retry_delay * (attempt + 1))
                    else:
                        print(f"  [{idx}/{total_campaigns}] ✗ Erreur finale après {max_retries} tentatives")
                        break

            # Pause entre chaque requête pour respecter le rate limit (2 secondes)
            if idx < total_campaigns:
                time.sleep(2)

        # Retourner un dict avec tous les éléments combinés
        print(f"\n📊 STATISTIQUES DE COLLECTE:")
        print(f"   Total éléments récupérés: {len(all_elements)}")
        
        # Compter combien d'éléments ont des métriques d'engagement
        elements_with_engagement = 0
        elements_with_reactions = 0
        elements_with_comments = 0
        elements_with_shares = 0
        
        for elem in all_elements:
            reactions = elem.get("reactions", 0)
            comments = elem.get("comments", 0)
            shares = elem.get("shares", 0)
            
            if reactions > 0 or comments > 0 or shares > 0:
                elements_with_engagement += 1
            if reactions > 0:
                elements_with_reactions += 1
            if comments > 0:
                elements_with_comments += 1
            if shares > 0:
                elements_with_shares += 1
        
        print(f"   Éléments avec engagement > 0: {elements_with_engagement}/{len(all_elements)}")
        print(f"   Éléments avec reactions > 0: {elements_with_reactions}/{len(all_elements)}")
        print(f"   Éléments avec comments > 0: {elements_with_comments}/{len(all_elements)}")
        print(f"   Éléments avec shares > 0: {elements_with_shares}/{len(all_elements)}")
        
        return {"elements": all_elements}

    def calculate_metrics(self, analytics_data: Dict) -> List[Dict]:
        """
        Calcule les métriques dérivées à partir des données brutes

        Args:
            analytics_data: Données brutes de l'API analytics

        Returns:
            list: Liste de dictionnaires avec métriques calculées
        """
        results = []

        for element in analytics_data.get("elements", []):
            # Extraire le pivotValue (l'API retourne pivotValues en array)
            pivot_values = element.get("pivotValues", [])
            pivot_value = pivot_values[0] if pivot_values else ""

            # Extraire les métriques de base
            impressions = element.get("impressions", 0)
            clicks = element.get("clicks", 0)
            # costInUsd est retourné comme string par l'API
            cost_raw = element.get("costInUsd", 0)
            cost = float(cost_raw) if cost_raw else 0
            reactions = element.get("reactions", 0)
            comments = element.get("comments", 0)
            shares = element.get("shares", 0)
            
            # Log de diagnostic pour les métriques d'engagement à 0
            if impressions > 0 and reactions == 0 and comments == 0 and shares == 0:
                print(f"⚠️  DIAGNOSTIC - Element avec engagement à 0:")
                print(f"   pivotValue: {pivot_value}")
                print(f"   impressions: {impressions}, clicks: {clicks}")
                print(f"   Clés disponibles dans element: {list(element.keys())}")
                # Vérifier si les métriques sont présentes mais avec valeur None ou autre
                print(f"   reactions (brut): {element.get('reactions', 'ABSENT')}")
                print(f"   comments (brut): {element.get('comments', 'ABSENT')}")
                print(f"   shares (brut): {element.get('shares', 'ABSENT')}")

            # Calculer les métriques dérivées
            ctr = (clicks / impressions * 100) if impressions > 0 else 0
            cpc = (cost / clicks) if clicks > 0 else 0
            cpm = (cost / impressions * 1000) if impressions > 0 else 0
            total_engagements = reactions + comments + shares
            engagement_rate = (total_engagements / impressions * 100) if impressions > 0 else 0

            # Construire le dictionnaire de résultats
            # pivotValue contient l'URN (campaign ou creative selon le pivot)
            result = {
                "pivotValue": pivot_value,  # Utiliser pivotValues[0] de l'API
                "date_range": element.get("dateRange", {}),
                "impressions": impressions,
                "clicks": clicks,
                "costInUsd": cost,
                "ctr": round(ctr, 2),
                "cpc": round(cpc, 2),
                "cpm": round(cpm, 2),
                "reactions": reactions,
                "comments": comments,
                "shares": shares,
                "totalEngagements": total_engagements,
                "engagementRate": round(engagement_rate, 2),
                "landingPageClicks": element.get("landingPageClicks", 0),
                "oneClickLeads": element.get("oneClickLeads", 0),
                "externalWebsiteConversions": element.get("externalWebsiteConversions", 0),
                "externalWebsitePostClickConversions": element.get("externalWebsitePostClickConversions", 0),
                "externalWebsitePostViewConversions": element.get("externalWebsitePostViewConversions", 0),
                "videoViews": element.get("videoViews", 0),
                "videoStarts": element.get("videoStarts", 0),
                "videoCompletions": element.get("videoCompletions", 0),
            }

            results.append(result)

        return results

    def export_to_csv(self, data: List[Dict], filename: str):
        """
        Exporte les données au format CSV

        Args:
            data: Données à exporter
            filename: Nom du fichier de sortie
        """
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Données exportées vers {filename}")

    def export_to_json(self, data: List[Dict], filename: str):
        """
        Exporte les données au format JSON

        Args:
            data: Données à exporter
            filename: Nom du fichier de sortie
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Données exportées vers {filename}")

    def _get_bigquery_client(self) -> bigquery.Client:
        """Initialise et retourne le client BigQuery"""
        if self.bq_client is None:
            if self.credentials_path:
                # Utiliser le fichier de credentials spécifié
                from google.oauth2 import service_account
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
                self.bq_client = bigquery.Client(
                    credentials=credentials,
                    project=self.project_id or credentials.project_id
                )
            elif self.project_id:
                self.bq_client = bigquery.Client(project=self.project_id)
            else:
                self.bq_client = bigquery.Client()
        return self.bq_client

    def check_date_exists(self, table_name: str, date_to_check: datetime) -> bool:
        """Vérifie si des données existent déjà pour cette date dans la table"""
        try:
            client = self._get_bigquery_client()
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            date_str = date_to_check.strftime("%Y-%m-%d")
            query = f"""
                SELECT COUNT(*) as count
                FROM `{table_id}`
                WHERE DATE(date_range_start) = '{date_str}'
            """

            result = client.query(query).result()
            row = next(iter(result), None)

            if row and row.count > 0:
                print(f"ℹ️  Données existantes pour {date_str} dans {table_name} ({row.count} ligne(s))")
                return True
            return False

        except Exception as e:
            # Table n'existe pas encore ou autre erreur
            print(f"ℹ️  Vérification impossible pour {table_name}: {e}")
            return False

    def get_last_sync_date(self, table_name: str) -> Optional[datetime]:
        """Récupère la dernière date de synchronisation depuis BigQuery"""
        try:
            client = self._get_bigquery_client()
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            query = f"""
                SELECT MAX(DATE(date_range_start)) as last_date
                FROM `{table_id}`
            """

            result = client.query(query).result()
            row = next(iter(result), None)

            if row and row.last_date:
                print(f"✓ Dernière sync {table_name}: {row.last_date}")
                return row.last_date
            else:
                print(f"ℹ️  Aucune donnée existante dans {table_name}, première synchronisation")
                return None

        except Exception as e:
            print(f"ℹ️  Table {table_name} non trouvée: {e}")
            print("   Première synchronisation")
            return None

    def upload_to_bigquery(self, data: List[Dict], table_name: str,
                          write_disposition: str = "WRITE_APPEND") -> None:
        """
        Upload les données vers BigQuery

        Args:
            data: Données à uploader (liste de dictionnaires)
            table_name: Nom de la table (campaign_analytics ou creative_analytics)
            write_disposition: Mode d'écriture (WRITE_APPEND, WRITE_TRUNCATE, WRITE_EMPTY)
        """
        if not data:
            print(f"⚠️  Aucune donnée à uploader pour {table_name}")
            return

        try:
            client = self._get_bigquery_client()

            # Préparer les données pour BigQuery
            df = pd.DataFrame(data)

            # Déterminer le pivot basé sur le nom de la table
            is_creative_pivot = 'creative' in table_name.lower()

            # Convertir les colonnes pour BigQuery selon le pivot
            if 'pivotValue' in df.columns:
                # pivotValue contient l'URN (campaign ou creative selon le pivot)
                urns = df['pivotValue'].astype(str)

                if is_creative_pivot:
                    # Pour CREATIVE pivot: le pivotValue contient urn:li:sponsoredCreative:XXXXX
                    df['creative_urn'] = urns
                    df['creative_id'] = urns.str.split(':').str[-1]
                else:
                    # Pour CAMPAIGN pivot: le pivotValue contient urn:li:sponsoredCampaign:XXXXX
                    df['campaign_urn'] = urns
                    df['campaign_id'] = urns.str.split(':').str[-1]
                    # Ne PAS ajouter creative_id et creative_urn pour ce pivot (pas dans le schéma)

            # Ajouter retrieved_at si absent
            if 'retrieved_at' not in df.columns:
                df['retrieved_at'] = datetime.now()

            # Renommer les colonnes pour correspondre au schéma BigQuery (snake_case)
            column_mapping = {
                'costInUsd': 'cost_in_usd',
                'totalEngagements': 'total_engagements',
                'engagementRate': 'engagement_rate',
                'landingPageClicks': 'landing_page_clicks',
                'oneClickLeads': 'one_click_leads',
                'externalWebsiteConversions': 'external_website_conversions',
                'externalWebsitePostClickConversions': 'external_website_post_click_conversions',
                'externalWebsitePostViewConversions': 'external_website_post_view_conversions',
                'videoViews': 'video_views',
                'videoStarts': 'video_starts',
                'videoCompletions': 'video_completions',
                'approximateMemberReach': 'approximate_member_reach',
                'date_range': 'date_range_temp'
            }

            df.rename(columns=column_mapping, inplace=True)

            # Décomposer date_range en date_range_start et date_range_end si présent
            if 'date_range_temp' in df.columns:
                def extract_date(date_dict, key):
                    if not isinstance(date_dict, dict):
                        return None
                    date_obj = date_dict.get(key, {})
                    if not date_obj:
                        return None
                    year = date_obj.get('year', 0)
                    month = date_obj.get('month', 1)
                    day = date_obj.get('day', 1)
                    if year > 0:
                        try:
                            return pd.Timestamp(year=year, month=month, day=day).date()
                        except:
                            return None
                    return None

                df['date_range_start'] = df['date_range_temp'].apply(lambda x: extract_date(x, 'start'))
                df['date_range_end'] = df['date_range_temp'].apply(lambda x: extract_date(x, 'end'))
                df.drop('date_range_temp', axis=1, inplace=True)

            # Convertir les colonnes date en type datetime.date pour BigQuery
            for col in ['date_range_start', 'date_range_end']:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce').dt.date

            # Supprimer les colonnes non utilisées
            columns_to_drop = ['pivotValue']
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

            # Construire le nom complet de la table
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            # Configuration du job
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED",  # Valeur correcte pour BigQuery
                autodetect=False
            )

            # Upload vers BigQuery
            print(f"\n→ Upload vers BigQuery: {table_id}")
            print(f"  Nombre de lignes: {len(df)}")

            job = client.load_table_from_dataframe(
                df,
                table_id,
                job_config=job_config
            )

            # Attendre la fin du job
            job.result()

            # Vérifier le résultat
            table = client.get_table(table_id)
            print(f"✓ Upload réussi! Total lignes dans la table: {table.num_rows:,}")

        except Exception as e:
            print(f"✗ Erreur lors de l'upload vers BigQuery: {e}")
            import traceback
            traceback.print_exc()
            raise


    def get_analytics_by_account(self,
                                  account_id: str,
                                  start_date: datetime,
                                  end_date: datetime,
                                  pivot: str = "CAMPAIGN",
                                  time_granularity: str = "DAILY",
                                  fields: Optional[List[str]] = None) -> Dict:
        """
        Récupère les analytics pour tout le compte en un seul appel (via accounts=List(...)).
        Bien plus efficace que de lister les campagnes puis d'interroger chacune.
        """
        url = f"{self.base_url}/adAnalytics"
        account_urn_encoded = f"urn:li:sponsoredAccount:{account_id}".replace(':', '%3A')

        date_range_str = (
            f"(start:(year:{start_date.year},month:{start_date.month},day:{start_date.day}),"
            f"end:(year:{end_date.year},month:{end_date.month},day:{end_date.day}))"
        )

        fields_str = f"&fields={','.join(fields)}" if fields else ""

        all_elements = []
        start = 0
        count = 500  # LinkedIn permet jusqu'à 500 par page pour adAnalytics
        known_total = None
        num_days = (end_date - start_date).days + 1
        # Cap de sécurité: LinkedIn pagine parfois circulairement après les vraies données
        safety_cap = max(50_000, num_days * 2000)

        while True:
            query_params = (
                f"q=analytics&pivot={pivot}"
                f"&dateRange={date_range_str}"
                f"&timeGranularity={time_granularity}"
                f"&accounts=List({account_urn_encoded})"
                f"&start={start}&count={count}"
                f"{fields_str}"
            )
            full_url = f"{url}?{query_params}"

            if start == 0:
                print(f"\n🔍 URL analytics (tronquée): {full_url[:150]}...")

            response = requests.get(full_url, headers=self._get_headers(), timeout=30)

            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 10))
                print(f"  Rate limit, pause de {retry_after}s...")
                time.sleep(retry_after)
                continue

            if response.status_code != 200:
                print(f"  Erreur API: {response.status_code} - {response.text[:300]}")
                response.raise_for_status()

            data = response.json()

            # Récupérer paging.total si disponible (arrêt propre sans pagination circulaire)
            paging = data.get("paging", {})
            if known_total is None and "total" in paging:
                known_total = paging["total"]
                print(f"  📊 Total annoncé par LinkedIn: {known_total}")

            elements = data.get("elements", [])
            all_elements.extend(elements)
            print(f"  Page {start // count + 1}: {len(elements)} élément(s) — total: {len(all_elements)}")

            # Arrêt si page incomplète
            if len(elements) < count:
                break

            start += count

            # Arrêt basé sur paging.total (évite pagination circulaire)
            if known_total is not None and start >= known_total:
                print(f"  ✓ Fin des données (start={start} >= total={known_total})")
                break

            # Arrêt de sécurité si LinkedIn pagine circulairement
            if len(all_elements) >= safety_cap:
                print(f"  ⚠️  Cap de sécurité atteint ({len(all_elements)} éléments pour {num_days} jours)")
                break

        return {"elements": all_elements}


def main():
    """
    Exemple d'utilisation du client LinkedIn Campaign Analytics
    """

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    # Détecter si on est dans Cloud Functions (pas besoin de fichier credentials)
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config_path = os.path.join(os.path.dirname(__file__), '../../config.yaml' if not is_cloud_function else '../config.yaml')
    config = load_config(config_path, skip_credentials_check=is_cloud_function)

    # Récupérer les configurations
    linkedin_config = config.get_linkedin_config()
    google_config = config.get_google_cloud_config()

    # Récupérer l'access token depuis la configuration
    ACCESS_TOKEN = linkedin_config.get('access_token')
    if not ACCESS_TOKEN:
        print("❌ ERREUR: access_token LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'access_token' dans la section linkedin.oauth")
        return

    ACCOUNT_ID = linkedin_config['account_id']

    # Configuration BigQuery
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['linkedin']
    CREDENTIALS_PATH = None if is_cloud_function else google_config.get('credentials_file')

    yesterday = datetime.now() - timedelta(days=1)
    START_DATE = (datetime.now() - timedelta(days=9)).strftime('%Y-%m-%d')
    END_DATE = yesterday.strftime('%Y-%m-%d')
    GRANULARITY = 'DAILY'
    PIVOTS = linkedin_config['pivots']

    print("=" * 70)
    print("LINKEDIN CAMPAIGN ANALYTICS")
    print("=" * 70)
    print(f"\nCompte publicitaire: {ACCOUNT_ID}")
    print(f"Période: {START_DATE} → {END_DATE}")
    print(f"Granularité: {GRANULARITY}")
    print(f"Pivots: {', '.join(PIVOTS)}")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}")
    print(f"Environment: {'Cloud Function' if is_cloud_function else 'Local'}\n")

    # Initialiser le client avec l'account_id et BigQuery
    client = LinkedInCampaignAnalytics(
        access_token=ACCESS_TOKEN,
        account_id=ACCOUNT_ID,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH  # Utiliser le chemin du fichier JSON
    )

    # Vérifier si les données existent déjà pour hier
    campaign_exists = client.check_date_exists("campaign_analytics", yesterday)
    creative_exists = client.check_date_exists("creative_analytics", yesterday)

    if campaign_exists and creative_exists:
        print("\n⚠️  Données déjà collectées pour hier.")
        print("   Pour éviter les doublons en automatisation, le script s'arrête ici.")
        print("\n" + "=" * 70)
        print("✓ SCRIPT TERMINÉ (pas de nouvelles données à collecter)")
        print("=" * 70)
        return

    # Récupérer les analytics directement par compte (sans lister les campagnes)
    print("=" * 70)
    print("Récupération des analytics via account-level query")
    print("=" * 70)

    try:
        start_date = datetime.strptime(START_DATE, '%Y-%m-%d')
        end_date = datetime.strptime(END_DATE, '%Y-%m-%d')

        print(f"\nPériode: {start_date.date()} à {end_date.date()}")
        print(f"Compte: urn:li:sponsoredAccount:{ACCOUNT_ID}\n")

        # approximateMemberReach n'est disponible qu'en granularité ALL, pas DAILY
        all_fields = [
            "pivotValues",
            "dateRange",
            "impressions",
            "clicks",
            "costInUsd",
            "landingPageClicks",
            "reactions",
            "comments",
            "shares",
            "oneClickLeads",
            "externalWebsiteConversions",
            "externalWebsitePostClickConversions",
            "externalWebsitePostViewConversions",
            "videoViews",
            "videoStarts",
            "videoCompletions",
        ]
        if GRANULARITY == "ALL":
            all_fields.append("approximateMemberReach")

        # PARTIE 1: Analytics par CAMPAIGN
        print("\n→ Récupération des analytics par CAMPAIGN...")
        analytics_campaign = client.get_analytics_by_account(
            account_id=ACCOUNT_ID,
            start_date=start_date,
            end_date=end_date,
            pivot="CAMPAIGN",
            time_granularity=GRANULARITY,
            fields=all_fields
        )

        metrics_campaign = client.calculate_metrics(analytics_campaign)
        print(f"✓ {len(metrics_campaign)} entrées campaign avec données\n")

        print("Résumé des performances par CAMPAIGN:")
        print("-" * 70)

        total_impressions = sum(m["impressions"] for m in metrics_campaign)
        total_clicks = sum(m["clicks"] for m in metrics_campaign)
        total_cost = sum(m["costInUsd"] for m in metrics_campaign)
        total_engagements = sum(m["totalEngagements"] for m in metrics_campaign)
        total_reactions = sum(m["reactions"] for m in metrics_campaign)
        total_comments = sum(m["comments"] for m in metrics_campaign)
        total_shares = sum(m["shares"] for m in metrics_campaign)

        campaigns_with_engagement = sum(1 for m in metrics_campaign if m["totalEngagements"] > 0)
        campaigns_with_reactions = sum(1 for m in metrics_campaign if m["reactions"] > 0)
        campaigns_with_comments = sum(1 for m in metrics_campaign if m["comments"] > 0)
        campaigns_with_shares = sum(1 for m in metrics_campaign if m["shares"] > 0)

        print(f"Total Impressions: {total_impressions:,}")
        print(f"Total Clicks: {total_clicks:,}")
        print(f"Total Cost: ${total_cost:,.2f}")
        print(f"Total Engagements: {total_engagements:,}")
        print(f"  ├─ Reactions: {total_reactions:,}")
        print(f"  ├─ Comments: {total_comments:,}")
        print(f"  └─ Shares: {total_shares:,}")
        print(f"Campagnes avec engagement: {campaigns_with_engagement}/{len(metrics_campaign)}")
        print(f"  ├─ avec reactions: {campaigns_with_reactions}/{len(metrics_campaign)}")
        print(f"  ├─ avec comments: {campaigns_with_comments}/{len(metrics_campaign)}")
        print(f"  └─ avec shares: {campaigns_with_shares}/{len(metrics_campaign)}")
        print(f"Average CTR: {(total_clicks/total_impressions*100):.2f}%" if total_impressions > 0 else "N/A")
        print(f"Average CPC: ${(total_cost/total_clicks):.2f}" if total_clicks > 0 else "N/A")

        client.export_to_json(metrics_campaign, "campaign_analytics.json")
        client.export_to_csv(metrics_campaign, "campaign_analytics.csv")
        print("✓ Données exportées: campaign_analytics.json / campaign_analytics.csv")

        client.upload_to_bigquery(metrics_campaign, "campaign_analytics")

        # PARTIE 2: Analytics par CREATIVE
        print("\n→ Récupération des analytics par CREATIVE...")
        analytics_creative = client.get_analytics_by_account(
            account_id=ACCOUNT_ID,
            start_date=start_date,
            end_date=end_date,
            pivot="CREATIVE",
            time_granularity=GRANULARITY,
            fields=all_fields
        )

        metrics_creative = client.calculate_metrics(analytics_creative)
        print(f"✓ {len(metrics_creative)} entrées creative avec données\n")

        print("Résumé des performances par CREATIVE:")
        print("-" * 70)

        total_impressions_cr = sum(m["impressions"] for m in metrics_creative)
        total_clicks_cr = sum(m["clicks"] for m in metrics_creative)
        total_cost_cr = sum(m["costInUsd"] for m in metrics_creative)
        total_engagements_cr = sum(m["totalEngagements"] for m in metrics_creative)
        total_reactions_cr = sum(m["reactions"] for m in metrics_creative)
        total_comments_cr = sum(m["comments"] for m in metrics_creative)
        total_shares_cr = sum(m["shares"] for m in metrics_creative)

        creatives_with_engagement = sum(1 for m in metrics_creative if m["totalEngagements"] > 0)
        creatives_with_reactions = sum(1 for m in metrics_creative if m["reactions"] > 0)
        creatives_with_comments = sum(1 for m in metrics_creative if m["comments"] > 0)
        creatives_with_shares = sum(1 for m in metrics_creative if m["shares"] > 0)

        print(f"Total Impressions: {total_impressions_cr:,}")
        print(f"Total Clicks: {total_clicks_cr:,}")
        print(f"Total Cost: ${total_cost_cr:,.2f}")
        print(f"Total Engagements: {total_engagements_cr:,}")
        print(f"  ├─ Reactions: {total_reactions_cr:,}")
        print(f"  ├─ Comments: {total_comments_cr:,}")
        print(f"  └─ Shares: {total_shares_cr:,}")
        print(f"Creatives avec engagement: {creatives_with_engagement}/{len(metrics_creative)}")
        print(f"  ├─ avec reactions: {creatives_with_reactions}/{len(metrics_creative)}")
        print(f"  ├─ avec comments: {creatives_with_comments}/{len(metrics_creative)}")
        print(f"  └─ avec shares: {creatives_with_shares}/{len(metrics_creative)}")
        print(f"Average CTR: {(total_clicks_cr/total_impressions_cr*100):.2f}%" if total_impressions_cr > 0 else "N/A")
        print(f"Average CPC: ${(total_cost_cr/total_clicks_cr):.2f}" if total_clicks_cr > 0 else "N/A")

        client.export_to_json(metrics_creative, "creative_analytics.json")
        client.export_to_csv(metrics_creative, "creative_analytics.csv")
        print("✓ Données exportées: creative_analytics.json / creative_analytics.csv")

        client.upload_to_bigquery(metrics_creative, "creative_analytics")

        print("\n" + "=" * 70)
        print("✓ ANALYSE COMPLÈTE TERMINÉE!")
        print("=" * 70)
        print(f"📊 Fichiers locaux créés:")
        print(f"   - campaign_analytics.json / .csv")
        print(f"   - creative_analytics.json / .csv")
        print(f"☁️  Données uploadées dans BigQuery:")
        print(f"   - {PROJECT_ID}.{DATASET_ID}.campaign_analytics")
        print(f"   - {PROJECT_ID}.{DATASET_ID}.creative_analytics")

    except Exception as e:
        print(f"✗ Erreur: {e}")


if __name__ == "__main__":
    main()
