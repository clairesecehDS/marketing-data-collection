import requests
from datetime import datetime
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os


class LinkedInBudgetClient:
    """
    Client pour récupérer les données de budget et bidding des campagnes LinkedIn
    Documentation: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns
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

    def get_campaigns(self, account_id: Optional[str] = None) -> List[Dict]:
        """
        Récupère la liste des campagnes avec leurs détails de budget

        Args:
            account_id: ID du compte publicitaire (optionnel, utilise self.account_id par défaut)

        Returns:
            list: Liste des campagnes avec leurs détails
        """
        acc_id = account_id or self.account_id

        if not acc_id:
            raise ValueError("account_id est requis. Passez-le en paramètre ou lors de l'initialisation.")

        url = f"{self.base_url}/adAccounts/{acc_id}/adCampaigns"
        all_campaigns = []
        start = 0
        count = 100
        max_campaigns = 2000

        while start < max_campaigns:
            query_params = (
                f"q=search"
                f"&search=(status:(values:List(ACTIVE,PAUSED,DRAFT,CANCELED,COMPLETED,ARCHIVED)))"
                f"&start={start}&count={count}"
            )
            full_url = f"{url}?{query_params}"

            response = requests.get(full_url, headers=self._get_headers())

            if response.status_code != 200:
                print(f"Erreur API: {response.status_code}")
                print(f"URL: {full_url}")
                print(f"Réponse: {response.text}")
                response.raise_for_status()

            data = response.json()
            elements = data.get("elements", [])
            all_campaigns.extend(elements)

            if len(elements) < count:
                break
            start += count

        return all_campaigns

    def get_creatives(self, campaign_urns: List[str], account_id: Optional[str] = None) -> List[Dict]:
        """
        Récupère les creatives pour une liste de campagnes

        Args:
            campaign_urns: Liste des URNs des campagnes
            account_id: ID du compte publicitaire (optionnel, utilise self.account_id par défaut)

        Returns:
            list: Liste des creatives
        """
        # Utiliser l'account_id passé en paramètre ou celui de l'instance
        acc_id = account_id or self.account_id

        if not acc_id:
            raise ValueError("account_id est requis pour récupérer les creatives")

        all_creatives = []

        for campaign_urn in campaign_urns:
            # Extraire l'ID de la campagne depuis l'URN
            campaign_id = campaign_urn.split(':')[-1]

            # Encoder l'URN pour l'URL (remplacer : par %3A)
            campaign_urn_encoded = campaign_urn.replace(':', '%3A')

            # Nouveau endpoint selon la doc: /adAccounts/{id}/creatives
            url = f"{self.base_url}/adAccounts/{acc_id}/creatives"
            query_params = f"q=criteria&campaigns=List({campaign_urn_encoded})"
            full_url = f"{url}?{query_params}"

            headers = self._get_headers()
            headers['X-RestLi-Method'] = 'FINDER'  # Header supplémentaire requis

            response = requests.get(
                full_url,
                headers=headers
            )

            if response.status_code == 200:
                data = response.json()
                creatives = data.get("elements", [])
                # Ajouter le campaign_urn à chaque creative pour référence
                for creative in creatives:
                    creative['_campaign_urn'] = campaign_urn
                    creative['_campaign_id'] = campaign_id
                all_creatives.extend(creatives)
            else:
                # Afficher l'URL pour debug (première erreur seulement)
                if len(all_creatives) == 0 and not hasattr(self, '_debug_shown'):
                    print(f"⚠️  Erreur {response.status_code} pour {campaign_urn}")
                    print(f"     URL: {response.url}")
                    print(f"     Réponse: {response.text[:200]}")
                    self._debug_shown = True

        return all_creatives

    def calculate_budget_spent_from_analytics(self) -> Dict[str, float]:
        """
        Calcule le budget dépensé pour chaque campagne à partir de la table campaign_analytics dans BigQuery

        Returns:
            dict: Mapping campaign_id -> budget_spent (coût total en USD)
        """
        try:
            client = self._get_bigquery_client()
            table_id = f"{self.project_id}.{self.dataset_id}.campaign_analytics"

            # Requête pour calculer le coût total par campagne
            query = f"""
                SELECT
                    campaign_id,
                    SUM(cost_in_usd) as total_spent
                FROM `{table_id}`
                WHERE campaign_id IS NOT NULL
                GROUP BY campaign_id
            """

            results = client.query(query).result()

            # Créer un dictionnaire campaign_id -> budget_spent
            budget_spent_map = {}
            for row in results:
                budget_spent_map[str(row.campaign_id)] = float(row.total_spent) if row.total_spent else 0.0

            return budget_spent_map

        except Exception as e:
            print(f"⚠️  Impossible de calculer budget_spent depuis BigQuery: {e}")
            return {}

    def get_budget_pricing(self, campaign: Dict, account_id: Optional[str] = None) -> Dict:
        """
        Récupère les recommandations de budget et bid pour une campagne via /adBudgetPricing
        Utilise un ciblage simplifié générique pour obtenir des estimations approximatives

        Args:
            campaign: Dictionnaire contenant les détails de la campagne
            account_id: ID du compte publicitaire (optionnel)

        Returns:
            dict: Contenant min_bid, max_bid, suggested_bid, etc. (ou valeurs None si erreur)
        """
        acc_id = account_id or self.account_id

        if not acc_id:
            return {"min_bid": None, "max_bid": None, "suggested_bid": None}

        try:
            # Extraire les paramètres nécessaires de la campagne
            account_urn = f"urn:li:sponsoredAccount:{acc_id}"
            bid_type = campaign.get("costType", "CPM")  # CPC, CPM, etc.
            objective_type = campaign.get("objectiveType", "BRAND_AWARENESS")
            campaign_type = campaign.get("type", "TEXT_AD")

            # Daily budget (requis pour l'API)
            daily_budget_obj = campaign.get("dailyBudget", {})
            daily_budget_amount = daily_budget_obj.get("amount", "100")
            daily_budget_currency = daily_budget_obj.get("currencyCode", "USD")

            # Construire l'URL avec encodage manuel
            url = f"{self.base_url}/adBudgetPricing"
            account_encoded = account_urn.replace(':', '%3A')

            # Ciblage minimal générique (France + 25-54 ans)
            # Format selon la doc LinkedIn: (include:(and:List((or:(facet:List(value))))))
            targeting_simplified = (
                "(include:(and:List((or:(urn%3Ali%3AadTargetingFacet%3AprofileLocations:"
                "List(urn%3Ali%3Ageo%3A105015875))))))"  # France
            )

            query_params = (
                f"q=criteriaV2"
                f"&account={account_encoded}"
                f"&bidType={bid_type}"
                f"&objectiveType={objective_type}"
                f"&campaignType={campaign_type}"
                f"&dailyBudget=(amount:{daily_budget_amount},currencyCode:{daily_budget_currency})"
                f"&targetingCriteria={targeting_simplified}"
            )

            full_url = f"{url}?{query_params}"

            response = requests.get(
                full_url,
                headers=self._get_headers(),
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                elements = data.get("elements", [])

                if elements:
                    pricing = elements[0]
                    bid_limits = pricing.get("bidLimits", {})
                    suggested_bid = pricing.get("suggestedBid", {})

                    return {
                        "min_bid": bid_limits.get("min", {}).get("amount"),
                        "max_bid": bid_limits.get("max", {}).get("amount"),
                        "suggested_bid_default": suggested_bid.get("default", {}).get("amount"),
                        "suggested_bid_min": suggested_bid.get("min", {}).get("amount"),
                        "suggested_bid_max": suggested_bid.get("max", {}).get("amount")
                    }
            else:
                # Debug: afficher l'erreur pour la première campagne
                if not hasattr(self, '_pricing_debug_shown'):
                    print(f"\n⚠️  Erreur adBudgetPricing: {response.status_code}")
                    print(f"   URL (tronquée): {full_url[:200]}...")
                    print(f"   Réponse: {response.text[:300]}\n")
                    self._pricing_debug_shown = True

            # En cas d'erreur, retourner None
            return {"min_bid": None, "max_bid": None, "suggested_bid": None}

        except Exception as e:
            # Debug: afficher l'erreur pour la première campagne
            if not hasattr(self, '_pricing_error_shown'):
                print(f"\n⚠️  Exception adBudgetPricing: {str(e)[:200]}\n")
                self._pricing_error_shown = True
            return {"min_bid": None, "max_bid": None, "suggested_bid": None}

    def extract_budget_metrics(self, campaigns: List[Dict], pivot: str = "CAMPAIGN",
                              budget_spent_map: Optional[Dict[str, float]] = None,
                              campaigns_map: Optional[Dict[str, Dict]] = None) -> List[Dict]:
        """
        Extrait les métriques de budget et bidding des campagnes ou creatives

        Args:
            campaigns: Liste des campagnes ou creatives de l'API
            pivot: Type de données ("CAMPAIGN" ou "CREATIVE")
            budget_spent_map: Dictionnaire campaign_id -> budget_spent (optionnel)
            campaigns_map: Dictionnaire campaign_id -> campaign_data (pour CREATIVE pivot, optionnel)

        Returns:
            list: Liste de dictionnaires avec les métriques de budget
        """
        results = []

        # Si budget_spent_map n'est pas fourni, créer un dict vide
        if budget_spent_map is None:
            budget_spent_map = {}

        # Si campaigns_map n'est pas fourni, créer un dict vide
        if campaigns_map is None:
            campaigns_map = {}

        for item in campaigns:
            # Données communes
            if pivot == "CAMPAIGN":
                campaign_id_raw = item.get("id", "")
                # L'ID peut être un int ou un URN string
                if isinstance(campaign_id_raw, int):
                    campaign_id = str(campaign_id_raw)
                    campaign_urn = f"urn:li:sponsoredCampaign:{campaign_id}"
                else:
                    campaign_urn = campaign_id_raw
                    campaign_id = campaign_id_raw.split(':')[-1] if campaign_id_raw else ""
                creative_id = None
                creative_urn = None
            else:  # CREATIVE
                creative_id_raw = item.get("id", "")
                if isinstance(creative_id_raw, int):
                    creative_id = str(creative_id_raw)
                    creative_urn = f"urn:li:sponsoredCreative:{creative_id}"
                else:
                    creative_urn = creative_id_raw
                    creative_id = creative_id_raw.split(':')[-1] if creative_id_raw else ""
                campaign_urn = item.get("_campaign_urn", "")
                campaign_id = item.get("_campaign_id", "")

            # Pour CREATIVE pivot, récupérer les données depuis la campagne parent
            if pivot == "CREATIVE" and campaign_id in campaigns_map:
                parent_campaign = campaigns_map[campaign_id]
                # Utiliser les données de la campagne parent
                source_item = parent_campaign
            else:
                # Pour CAMPAIGN pivot, utiliser l'item directement
                source_item = item

            # Extraire les données de budget (depuis source_item)
            total_budget = source_item.get("totalBudget", {}).get("amount") if source_item.get("totalBudget") else None
            daily_budget_obj = source_item.get("dailyBudget", {})
            daily_budget = daily_budget_obj.get("amount") if daily_budget_obj else None

            # Lifetime budget (certaines campagnes utilisent ce champ)
            lifetime_budget = None
            if source_item.get("runSchedule"):
                run_schedule = source_item.get("runSchedule", {})
                if run_schedule.get("totalBudget"):
                    lifetime_budget = run_schedule.get("totalBudget", {}).get("amount")

            # Budget spent (depuis analytics BigQuery)
            budget_spent = budget_spent_map.get(campaign_id, None)

            # Budget remaining (calculé à partir du budget total/lifetime et du budget dépensé)
            budget_remaining = None
            if budget_spent is not None:
                # Utiliser lifetime_budget en priorité, sinon total_budget
                budget_limit = None
                if lifetime_budget:
                    budget_limit = float(lifetime_budget)
                elif total_budget:
                    budget_limit = float(total_budget)

                if budget_limit:
                    budget_remaining = budget_limit - budget_spent
                    # Ne pas avoir de valeur négative
                    if budget_remaining < 0:
                        budget_remaining = 0

            # Currency (depuis source_item)
            billing_currency = None
            if source_item.get("totalBudget"):
                billing_currency = source_item.get("totalBudget", {}).get("currencyCode")
            elif source_item.get("dailyBudget"):
                billing_currency = source_item.get("dailyBudget", {}).get("currencyCode")

            # Bid information (depuis source_item)
            unit_cost = source_item.get("unitCost", {})
            bid_type = source_item.get("costType")  # CPC, CPM, etc.
            bid_amount = unit_cost.get("amount") if unit_cost else None
            bid_currency = unit_cost.get("currencyCode") if unit_cost else None

            # Bid adjustments
            bid_multiplier = None
            bid_adjustment_type = None
            if source_item.get("targeting"):
                targeting = source_item.get("targeting", {})
                # LinkedIn peut avoir des bid adjustments dans le targeting
                # (cette structure peut varier selon l'API)

            # Min/Max bid via API adBudgetPricing (seulement pour CAMPAIGN pivot)
            min_bid = None
            max_bid = None
            if pivot == "CAMPAIGN":
                pricing = self.get_budget_pricing(source_item)
                min_bid = pricing.get("min_bid")
                max_bid = pricing.get("max_bid")

            # Pacing (depuis source_item)
            pacing_type = None
            pacing_rate = None
            if source_item.get("runSchedule"):
                run_schedule = source_item.get("runSchedule", {})
                pacing_type = run_schedule.get("pacing")  # STANDARD, ACCELERATED

            # Dates (depuis source_item)
            start_date = None
            end_date = None
            if source_item.get("runSchedule"):
                run_schedule = source_item.get("runSchedule", {})
                if run_schedule.get("start"):
                    start_ts = run_schedule.get("start")
                    start_date = datetime.fromtimestamp(start_ts / 1000).date()
                if run_schedule.get("end"):
                    end_ts = run_schedule.get("end")
                    end_date = datetime.fromtimestamp(end_ts / 1000).date()

            result = {
                "campaign_id": campaign_id,
                "campaign_urn": campaign_urn,
                "creative_id": creative_id,
                "creative_urn": creative_urn,
                "total_budget": total_budget,
                "daily_budget": daily_budget,
                "lifetime_budget": lifetime_budget,
                "budget_remaining": budget_remaining,
                "budget_spent": budget_spent,
                "billing_currency": billing_currency or bid_currency,
                "bid_type": bid_type,
                "bid_amount": bid_amount,
                "bid_multiplier": bid_multiplier,
                "bid_adjustment_type": bid_adjustment_type,
                "min_bid": min_bid,
                "max_bid": max_bid,
                "pacing_type": pacing_type,
                "pacing_rate": pacing_rate,
                "start_date": start_date,
                "end_date": end_date,
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
        print(f"✓ Données exportées: {filename}")

    def export_to_json(self, data: List[Dict], filename: str):
        """
        Exporte les données au format JSON

        Args:
            data: Données à exporter
            filename: Nom du fichier de sortie
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"✓ Données exportées: {filename}")

    def _get_bigquery_client(self) -> bigquery.Client:
        """Initialise et retourne le client BigQuery"""
        if self.bq_client is None:
            if self.credentials_path:
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

    def check_today_exists(self, table_name: str) -> bool:
        """Vérifie si un snapshot a déjà été pris aujourd'hui"""
        try:
            from datetime import datetime
            client = self._get_bigquery_client()
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            today_str = datetime.now().strftime("%Y-%m-%d")
            query = f"""
                SELECT COUNT(*) as count
                FROM `{table_id}`
                WHERE DATE(retrieved_at) = '{today_str}'
            """

            result = client.query(query).result()
            row = next(iter(result), None)

            if row and row.count > 0:
                print(f"ℹ️  Snapshot déjà pris aujourd'hui pour {table_name} ({row.count} ligne(s))")
                return True
            return False

        except Exception as e:
            # Table n'existe pas encore
            print(f"ℹ️  Vérification impossible pour {table_name}: {e}")
            return False

    def upload_to_bigquery(self, data: List[Dict], table_name: str,
                          write_disposition: str = "WRITE_APPEND") -> None:
        """
        Upload les données vers BigQuery

        Args:
            data: Données à uploader (liste de dictionnaires)
            table_name: Nom de la table (campaign_budget ou creative_budget)
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

            # Pour le pivot CAMPAIGN, ne pas inclure creative_id et creative_urn
            if not is_creative_pivot:
                df = df.drop(columns=['creative_id', 'creative_urn'], errors='ignore')

            # Ajouter retrieved_at si absent
            if 'retrieved_at' not in df.columns:
                df['retrieved_at'] = datetime.now()

            # Convertir les colonnes date en type datetime.date pour BigQuery
            for col in ['start_date', 'end_date']:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce').dt.date

            # Convertir les colonnes numériques (FLOAT64) en float
            numeric_columns = [
                'total_budget', 'daily_budget', 'lifetime_budget',
                'budget_remaining', 'budget_spent', 'bid_amount',
                'bid_multiplier', 'min_bid', 'max_bid', 'pacing_rate'
            ]
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # Construire le nom complet de la table
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            # Configuration du job
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED",
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
    Exemple d'utilisation du client LinkedIn Budget
    """
    
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
    from config_loader import load_config

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    # Détecter si on est dans Cloud Functions
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

    print("=" * 70)
    print("LINKEDIN BUDGET & BIDDING METRICS")
    print("=" * 70)
    print(f"\nCompte publicitaire: {ACCOUNT_ID}")
    print(f"Environment: {'Cloud Function' if is_cloud_function else 'Local'}")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}\n")

    # Initialiser le client
    client = LinkedInBudgetClient(
        access_token=ACCESS_TOKEN,
        account_id=ACCOUNT_ID,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

    # Vérifier si un snapshot a déjà été pris aujourd'hui
    if client.check_today_exists("campaign_budget") and client.check_today_exists("creative_budget"):
        print("\n⚠️  Snapshots déjà pris aujourd'hui pour campaign_budget et creative_budget.")
        print("   Pour éviter les doublons, le script s'arrête ici.")
        print("\n" + "=" * 70)
        print("✓ SCRIPT TERMINÉ (snapshots déjà collectés aujourd'hui)")
        print("=" * 70)
        return

    # Étape 1: Récupérer les campagnes
    print("=" * 70)
    print("1. Récupération des campagnes")
    print("=" * 70)

    try:
        campaigns = client.get_campaigns()
        print(f"\n✓ {len(campaigns)} campagne(s) trouvée(s)\n")

        campaign_urns = [f"urn:li:sponsoredCampaign:{c.get('id').split(':')[-1]}"
                        if ':' in str(c.get('id', ''))
                        else f"urn:li:sponsoredCampaign:{c.get('id')}"
                        for c in campaigns if c.get('id')]

        if not campaigns:
            print("Aucune campagne trouvée.")
            return

    except Exception as e:
        print(f"✗ Erreur: {e}")
        return

    # Étape 2: Calculer budget_spent depuis BigQuery
    print("=" * 70)
    print("2. Calcul du budget dépensé depuis analytics")
    print("=" * 70)

    print("\n→ Récupération des coûts depuis campaign_analytics...")
    budget_spent_map = client.calculate_budget_spent_from_analytics()
    print(f"✓ Budget calculé pour {len(budget_spent_map)} campagne(s)\n")

    # Étape 3: Extraire les métriques de budget pour les CAMPAIGNS
    print("=" * 70)
    print("3. Extraction des métriques de budget et pricing")
    print("=" * 70)

    try:
        # PARTIE 1: Budget des CAMPAIGNS (avec pricing API et budget_spent)
        print("\n→ Extraction budget par CAMPAIGN (avec min/max bid depuis API)...")
        print("   ⏳ Cela peut prendre du temps (appel API adBudgetPricing pour chaque campagne)...\n")
        budget_campaigns = client.extract_budget_metrics(campaigns, pivot="CAMPAIGN", budget_spent_map=budget_spent_map)
        print(f"✓ {len(budget_campaigns)} campagnes traitées\n")

        # Afficher un résumé
        print("Résumé des budgets par CAMPAIGN:")
        print("-" * 70)

        active_budgets = [b for b in budget_campaigns if b['daily_budget'] or b['total_budget'] or b['lifetime_budget']]
        print(f"Campagnes avec budget configuré: {len(active_budgets)}")

        if active_budgets:
            total_daily = sum(float(b['daily_budget']) if b['daily_budget'] and b['daily_budget'] != '' else 0 for b in active_budgets)
            total_lifetime = sum(float(b['lifetime_budget'] or b['total_budget'] or 0) if (b['lifetime_budget'] or b['total_budget']) else 0 for b in active_budgets)
            print(f"Total budgets journaliers: ${total_daily:,.2f}")
            print(f"Total budgets lifetime: ${total_lifetime:,.2f}")

        # Exporter
        client.export_to_json(budget_campaigns, "campaign_budget.json")
        client.export_to_csv(budget_campaigns, "campaign_budget.csv")

        # Upload vers BigQuery
        client.upload_to_bigquery(budget_campaigns, "campaign_budget")

        # PARTIE 2: Budget des CREATIVES
        print("\n→ Récupération des creatives...")
        creatives = client.get_creatives(campaign_urns)
        print(f"✓ {len(creatives)} creatives trouvées\n")

        if creatives:
            # Créer un mapping campaign_id -> campaign_data pour hériter des budgets
            campaigns_map = {str(c.get('id')): c for c in campaigns}

            print("\n→ Extraction budget par CREATIVE (héritage depuis campagnes)...")
            budget_creatives = client.extract_budget_metrics(
                creatives,
                pivot="CREATIVE",
                budget_spent_map=budget_spent_map,
                campaigns_map=campaigns_map
            )
            print(f"✓ {len(budget_creatives)} creatives traitées\n")

            # Exporter
            client.export_to_json(budget_creatives, "creative_budget.json")
            client.export_to_csv(budget_creatives, "creative_budget.csv")

            # Upload vers BigQuery
            client.upload_to_bigquery(budget_creatives, "creative_budget")

        print("\n" + "=" * 70)
        print("✓ EXTRACTION BUDGETS TERMINÉE!")
        print("=" * 70)
        print(f"📊 Fichiers locaux créés:")
        print(f"   - campaign_budget.json / .csv")
        if creatives:
            print(f"   - creative_budget.json / .csv")
        print(f"☁️  Données uploadées dans BigQuery:")
        print(f"   - {PROJECT_ID}.{DATASET_ID}.campaign_budget")
        if creatives:
            print(f"   - {PROJECT_ID}.{DATASET_ID}.creative_budget")

    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
