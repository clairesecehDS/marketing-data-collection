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
            "LinkedIn-Version": "202509",
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

    def get_creatives(self, campaign_urns: List[str]) -> List[Dict]:
        """
        Récupère les creatives pour une liste de campagnes

        Args:
            campaign_urns: Liste des URNs des campagnes

        Returns:
            list: Liste des creatives
        """
        all_creatives = []

        for campaign_urn in campaign_urns:
            # Extraire l'ID de la campagne depuis l'URN
            campaign_id = campaign_urn.split(':')[-1]

            url = f"{self.base_url}/adCreatives"
            params = {
                "q": "criteria",
                "criteria.campaigns": f"List({campaign_urn.replace(':', '%3A')})"
            }

            response = requests.get(
                url,
                headers=self._get_headers(),
                params=params
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
                print(f"⚠️  Erreur lors de la récupération des creatives pour {campaign_urn}: {response.status_code}")

        return all_creatives

    def extract_budget_metrics(self, campaigns: List[Dict], pivot: str = "CAMPAIGN") -> List[Dict]:
        """
        Extrait les métriques de budget et bidding des campagnes ou creatives

        Args:
            campaigns: Liste des campagnes ou creatives de l'API
            pivot: Type de données ("CAMPAIGN" ou "CREATIVE")

        Returns:
            list: Liste de dictionnaires avec les métriques de budget
        """
        results = []

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

            # Extraire les données de budget
            total_budget = item.get("totalBudget", {}).get("amount") if item.get("totalBudget") else None
            daily_budget_obj = item.get("dailyBudget", {})
            daily_budget = daily_budget_obj.get("amount") if daily_budget_obj else None

            # Lifetime budget (certaines campagnes utilisent ce champ)
            lifetime_budget = None
            if item.get("runSchedule"):
                run_schedule = item.get("runSchedule", {})
                if run_schedule.get("totalBudget"):
                    lifetime_budget = run_schedule.get("totalBudget", {}).get("amount")

            # Budget spent et remaining (calculés via analytics, on les laisse NULL pour l'instant)
            budget_spent = None
            budget_remaining = None

            # Currency
            billing_currency = None
            if item.get("totalBudget"):
                billing_currency = item.get("totalBudget", {}).get("currencyCode")
            elif item.get("dailyBudget"):
                billing_currency = item.get("dailyBudget", {}).get("currencyCode")

            # Bid information
            unit_cost = item.get("unitCost", {})
            bid_type = item.get("costType")  # CPC, CPM, etc.
            bid_amount = unit_cost.get("amount") if unit_cost else None
            bid_currency = unit_cost.get("currencyCode") if unit_cost else None

            # Bid adjustments
            bid_multiplier = None
            bid_adjustment_type = None
            if item.get("targeting"):
                targeting = item.get("targeting", {})
                # LinkedIn peut avoir des bid adjustments dans le targeting
                # (cette structure peut varier selon l'API)

            # Min/Max bid (si disponible dans optimizationTargetType ou autres champs)
            min_bid = None
            max_bid = None

            # Pacing
            pacing_type = None
            pacing_rate = None
            if item.get("runSchedule"):
                run_schedule = item.get("runSchedule", {})
                pacing_type = run_schedule.get("pacing")  # STANDARD, ACCELERATED

            # Dates
            start_date = None
            end_date = None
            if item.get("runSchedule"):
                run_schedule = item.get("runSchedule", {})
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

    # Configuration
    ACCESS_TOKEN = "AQWzcqB3Ax4ZPIIcaTW5fDylKuVXIgnb3HbO_oCRGsLbfgGfc5LyAs5BdhuwUv7yWD0AKm_HYYphQi0Aec5epLuISR1QcykiyC4UX3PKi4kpYN6AKfNlZ0U4gBCctsRknr_uSHt8u2LYySydWhThF-k3O6HtzQKCi072WB-TkxaaAbMBSgLfIGcbBVhEkAXAFnZTr5lUUqmmJvvcuUuImZfqWVK4tX-1cHHSkpenmNmq_43m0QZqQ_1IRpmdfzJYKE11PKHUgkQUacrYEAGsDJXe1ClHiw9UegDFvsBQ-JIFE0VWeI5yl7D5uE3SxQrUjbrpOQOzVVQvdGsZ3j0bJi-6zddakw"
    ACCOUNT_ID = "503061133"  # École des Ponts Business School_1

    # Configuration BigQuery
    PROJECT_ID = "clean-avatar-466709-a0"
    DATASET_ID = "linkedin_ads_advertising"
    CREDENTIALS_PATH = "./.key.json"

    print("=" * 70)
    print("LINKEDIN BUDGET & BIDDING METRICS")
    print("=" * 70)
    print(f"\nCompte publicitaire: {ACCOUNT_ID}")
    print(f"École des Ponts Business School_1")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}\n")

    # Initialiser le client
    client = LinkedInBudgetClient(
        access_token=ACCESS_TOKEN,
        account_id=ACCOUNT_ID,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

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

    # Étape 2: Extraire les métriques de budget pour les CAMPAIGNS
    print("=" * 70)
    print("2. Extraction des métriques de budget")
    print("=" * 70)

    try:
        # PARTIE 1: Budget des CAMPAIGNS
        print("\n→ Extraction budget par CAMPAIGN...")
        budget_campaigns = client.extract_budget_metrics(campaigns, pivot="CAMPAIGN")
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
        creatives = client.get_creatives(campaign_urns[:10])  # Limiter à 10 campagnes pour le test
        print(f"✓ {len(creatives)} creatives trouvées\n")

        if creatives:
            print("\n→ Extraction budget par CREATIVE...")
            budget_creatives = client.extract_budget_metrics(creatives, pivot="CREATIVE")
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
