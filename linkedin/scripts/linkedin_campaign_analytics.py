import requests
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os
import sys

# Ajouter le répertoire parent au path pour importer config_loader
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
            "LinkedIn-Version": "202509",
            "X-Restli-Protocol-Version": "2.0.0"
        }

    def get_ad_accounts(self) -> List[Dict]:
        """
        Récupère la liste des comptes publicitaires accessibles

        Returns:
            list: Liste des comptes publicitaires
        """
        url = f"{self.base_url}/adAccounts"
        params = {"q": "search"}

        response = requests.get(
            url,
            headers=self._get_headers(),
            params=params
        )

        if response.status_code != 200:
            print(f"Erreur API: {response.status_code}")
            print(f"URL: {response.url}")
            print(f"Réponse: {response.text}")
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
        # Utiliser l'account_id passé en paramètre ou celui de l'instance
        acc_id = account_id or self.account_id

        if not acc_id:
            raise ValueError("account_id est requis. Passez-le en paramètre ou lors de l'initialisation.")

        # Nouvelle URL avec account_id dans le path
        url = f"{self.base_url}/adAccounts/{acc_id}/adCampaigns"
        params = {"q": "search"}

        response = requests.get(
            url,
            headers=self._get_headers(),
            params=params
        )

        if response.status_code != 200:
            print(f"Erreur API: {response.status_code}")
            print(f"URL: {response.url}")
            print(f"Réponse: {response.text}")
            response.raise_for_status()

        data = response.json()
        return data.get("elements", [])

    def get_analytics(self,
                      campaign_urns: List[str],
                      start_date: datetime,
                      end_date: datetime,
                      pivot: str = "CAMPAIGN",
                      time_granularity: str = "ALL",
                      fields: Optional[List[str]] = None) -> Dict:
        """
        Récupère les analytics pour une ou plusieurs campagnes

        Args:
            campaign_urns: Liste des URNs des campagnes (ex: ['urn:li:sponsoredCampaign:123456'])
            start_date: Date de début
            end_date: Date de fin
            pivot: Niveau d'agrégation (CAMPAIGN, CREATIVE, ACCOUNT, CAMPAIGN_GROUP)
            time_granularity: Granularité temporelle (ALL, DAILY, MONTHLY, YEARLY)
            fields: Liste des champs à récupérer (si None, récupère les principaux)

        Returns:
            dict: Données analytics
        """
        # Utiliser le format REST selon la doc officielle
        url = f"{self.base_url}/adAnalytics"

        # Champs par défaut si non spécifiés
        if fields is None:
            fields = [
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

        # Format qui FONCTIONNE selon le curl qui a marché
        # Format dateRange: seulement start (pas de end)
        date_range_str = f"(start:(year:{start_date.year},month:{start_date.month},day:{start_date.day}))"

        # Encoder les URNs dans campaigns (remplacer : par %3A)
        campaigns_urns_encoded = ','.join([urn.replace(':', '%3A') for urn in campaign_urns])
        campaigns_str = f"List({campaigns_urns_encoded})"

        # Construire l'URL manuellement (garder les parenthèses et deux-points de la structure)
        query_string = f"q=analytics&pivot={pivot}&timeGranularity={time_granularity}&dateRange={date_range_str}&campaigns={campaigns_str}"
        full_url = f"{url}?{query_string}"

        response = requests.get(
            full_url,
            headers=self._get_headers()
        )

        if response.status_code != 200:
            print(f"Erreur API: {response.status_code}")
            print(f"URL: {response.url}")
            print(f"Réponse: {response.text}")
            response.raise_for_status()

        return response.json()

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
            # Extraire les métriques de base
            impressions = element.get("impressions", 0)
            clicks = element.get("clicks", 0)
            cost = element.get("costInUsd", 0)
            reactions = element.get("reactions", 0)
            comments = element.get("comments", 0)
            shares = element.get("shares", 0)

            # Calculer les métriques dérivées
            ctr = (clicks / impressions * 100) if impressions > 0 else 0
            cpc = (cost / clicks) if clicks > 0 else 0
            cpm = (cost / impressions * 1000) if impressions > 0 else 0
            total_engagements = reactions + comments + shares
            engagement_rate = (total_engagements / impressions * 100) if impressions > 0 else 0

            # Construire le dictionnaire de résultats
            # pivotValue contient l'URN (campaign ou creative selon le pivot)
            result = {
                "pivotValue": element.get("pivotValue", ""),  # Garder le pivotValue pour traitement ultérieur
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
                    # Pour les creatives, on n'a pas directement le campaign_id dans pivotValue
                    # Il faudrait le récupérer via l'API ou le laisser vide
                    df['campaign_id'] = None
                    df['campaign_urn'] = None
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


def main():
    """
    Exemple d'utilisation du client LinkedIn Campaign Analytics
    """

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    config = load_config()

    # Récupérer les configurations
    linkedin_config = config.get_linkedin_config()
    google_config = config.get_google_cloud_config()

    # Note: Le token LinkedIn doit être rafraîchi régulièrement (voir token_linkedin.py)
    # Pour une utilisation en production, générer un nouveau token avant chaque exécution
    ACCESS_TOKEN = linkedin_config['refresh_token']  # À remplacer par un access token valide
    ACCOUNT_ID = linkedin_config['account_id']

    # Configuration BigQuery
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['linkedin']
    CREDENTIALS_PATH = google_config['credentials_file']

    # Paramètres de collecte
    START_DATE = linkedin_config['start_date']
    END_DATE = linkedin_config['end_date'] or datetime.now().strftime('%Y-%m-%d')
    GRANULARITY = linkedin_config['granularity']
    PIVOTS = linkedin_config['pivots']

    print("=" * 70)
    print("LINKEDIN CAMPAIGN ANALYTICS")
    print("=" * 70)
    print(f"\nCompte publicitaire: {ACCOUNT_ID}")
    print(f"Période: {START_DATE} → {END_DATE}")
    print(f"Granularité: {GRANULARITY}")
    print(f"Pivots: {', '.join(PIVOTS)}")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}\n")

    # Initialiser le client avec l'account_id et BigQuery
    client = LinkedInCampaignAnalytics(
        access_token=ACCESS_TOKEN,
        account_id=ACCOUNT_ID,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH  # Utiliser le chemin du fichier JSON
    )

    # Étape 1: Récupérer les campagnes
    print("=" * 70)
    print("1. Récupération des campagnes")
    print("=" * 70)

    try:
        campaigns = client.get_campaigns()
        print(f"\n✓ {len(campaigns)} campagne(s) trouvée(s):\n")

        campaign_urns = []

        # Récupérer TOUTES les campagnes
        for campaign in campaigns:
            campaign_id = campaign.get("id")
            campaign_name = campaign.get("name", "Sans nom")
            campaign_status = campaign.get("status", "Unknown")
            campaign_urn = f"urn:li:sponsoredCampaign:{campaign_id}"

            campaign_urns.append(campaign_urn)

        # Afficher un résumé
        print(f"  Total: {len(campaign_urns)} campagnes sélectionnées")

        # Afficher les 5 premières
        for campaign in campaigns[:5]:
            campaign_name = campaign.get("name", "Sans nom")
            campaign_status = campaign.get("status", "Unknown")
            print(f"  - {campaign_name} ({campaign_status})")

        if len(campaigns) > 5:
            print(f"  ... et {len(campaigns) - 5} autres campagnes")
        print()

        if not campaign_urns:
            print("Aucune campagne trouvée.")
            return

    except Exception as e:
        print(f"✗ Erreur: {e}")
        return

    # Étape 2: Récupérer les analytics
    print("=" * 70)
    print("2. Récupération des analytics")
    print("=" * 70)

    try:
        # Utiliser les dates depuis la configuration
        start_date = datetime.strptime(START_DATE, '%Y-%m-%d')
        end_date = datetime.strptime(END_DATE, '%Y-%m-%d')

        print(f"\nPériode: {start_date.date()} à {end_date.date()}")
        print(f"Nombre de campagnes: {len(campaign_urns)}\n")

        # Liste complète des champs disponibles
        all_fields = [
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
            "approximateMemberReach"
        ]

        # PARTIE 1: Analytics par CAMPAIGN
        print("\n→ Récupération des analytics par CAMPAIGN...")
        analytics_campaign = client.get_analytics(
            campaign_urns=campaign_urns,
            start_date=start_date,
            end_date=end_date,
            pivot="CAMPAIGN",
            time_granularity="ALL",
            fields=all_fields
        )

        metrics_campaign = client.calculate_metrics(analytics_campaign)
        print(f"✓ {len(metrics_campaign)} campagnes avec données\n")

        # Afficher un résumé des campagnes
        print("Résumé des performances par CAMPAIGN:")
        print("-" * 70)

        total_impressions = sum(m["impressions"] for m in metrics_campaign)
        total_clicks = sum(m["clicks"] for m in metrics_campaign)
        total_cost = sum(m["costInUsd"] for m in metrics_campaign)
        total_engagements = sum(m["totalEngagements"] for m in metrics_campaign)

        print(f"Total Impressions: {total_impressions:,}")
        print(f"Total Clicks: {total_clicks:,}")
        print(f"Total Cost: ${total_cost:,.2f}")
        print(f"Total Engagements: {total_engagements:,}")
        print(f"Average CTR: {(total_clicks/total_impressions*100):.2f}%" if total_impressions > 0 else "N/A")
        print(f"Average CPC: ${(total_cost/total_clicks):.2f}" if total_clicks > 0 else "N/A")

        # Exporter les résultats par campagne
        client.export_to_json(metrics_campaign, "campaign_analytics.json")
        client.export_to_csv(metrics_campaign, "campaign_analytics.csv")
        print("✓ Données exportées: campaign_analytics.json / campaign_analytics.csv")

        # Upload vers BigQuery
        client.upload_to_bigquery(metrics_campaign, "campaign_analytics")

        # PARTIE 2: Analytics par CREATIVE (ads individuels)
        print("\n→ Récupération des analytics par CREATIVE...")
        analytics_creative = client.get_analytics(
            campaign_urns=campaign_urns,
            start_date=start_date,
            end_date=end_date,
            pivot="CREATIVE",
            time_granularity="ALL",
            fields=all_fields
        )

        metrics_creative = client.calculate_metrics(analytics_creative)
        print(f"✓ {len(metrics_creative)} creatives avec données\n")

        # Afficher un résumé des creatives
        print("Résumé des performances par CREATIVE:")
        print("-" * 70)

        total_impressions_cr = sum(m["impressions"] for m in metrics_creative)
        total_clicks_cr = sum(m["clicks"] for m in metrics_creative)
        total_cost_cr = sum(m["costInUsd"] for m in metrics_creative)
        total_engagements_cr = sum(m["totalEngagements"] for m in metrics_creative)

        print(f"Total Impressions: {total_impressions_cr:,}")
        print(f"Total Clicks: {total_clicks_cr:,}")
        print(f"Total Cost: ${total_cost_cr:,.2f}")
        print(f"Total Engagements: {total_engagements_cr:,}")
        print(f"Average CTR: {(total_clicks_cr/total_impressions_cr*100):.2f}%" if total_impressions_cr > 0 else "N/A")
        print(f"Average CPC: ${(total_cost_cr/total_clicks_cr):.2f}" if total_clicks_cr > 0 else "N/A")

        # Exporter les résultats par creative
        client.export_to_json(metrics_creative, "creative_analytics.json")
        client.export_to_csv(metrics_creative, "creative_analytics.csv")
        print("✓ Données exportées: creative_analytics.json / creative_analytics.csv")

        # Upload vers BigQuery
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
