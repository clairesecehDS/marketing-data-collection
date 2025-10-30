import requests
from datetime import datetime
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os
import sys

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class ClarityAnalyticsClient:
    """
    Client simplifié pour Microsoft Clarity suivant le schéma officiel
    """

    def __init__(self, api_token: str, project_id: str,
                 bq_project_id: Optional[str] = None,
                 dataset_id: str = "microsoft_clarity",
                 credentials_path: Optional[str] = None):
        self.api_token = api_token
        self.clarity_project_id = project_id
        self.base_url = "https://www.clarity.ms/export-data/api/v1"

        self.bq_project_id = bq_project_id or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.dataset_id = dataset_id
        self.credentials_path = credentials_path
        self.bq_client = None

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def get_live_insights(self, num_of_days: int = 1) -> Dict:
        """Récupère les insights Clarity"""
        url = f"{self.base_url}/project-live-insights"
        params = {"numOfDays": str(num_of_days)}

        response = requests.get(url, params=params, headers=self._get_headers())

        if response.status_code != 200:
            print(f"⚠️  Erreur API: {response.status_code} - {response.text}")
            response.raise_for_status()

        return response.json()

    def _format_markdown_table(self, info_list: List[Dict], col1_name: str, col2_name: str = "Sessions") -> str:
        """
        Formate une liste d'informations en tableau Markdown
        """
        if not info_list:
            return None

        lines = [f"{col1_name} | {col2_name}", "--- | ---"]

        for item in info_list:
            # Adapter selon le type de métrique
            name = item.get("name") or item.get("url") or item.get("title") or "Unknown"
            count = item.get("sessionsCount") or item.get("visitsCount") or item.get("count") or "0"
            lines.append(f"{name} | {count}")

        return "\n".join(lines)

    def parse_to_official_format(self, data) -> List[Dict]:
        """
        Parse les données API Clarity (format metricName/information)
        API returns a list of metrics with metricName and information fields
        """
        current_time = datetime.now()
        date_str = current_time.strftime("%Y-%m-%d")

        consolidated = {
            "date": current_time,
            "name": f"Clarity Data - {date_str}",
            "url": None,
            "page_titles": None,
            "popular_pages": None,
            "referrer_urls": None,
            "total_sessions": None,
            "total_users": None,
            "page_views": None,
            "avg_engagement_time": None,
            "scroll_depth": None,
            "dead_clicks": None,
            "rage_clicks": None,
            "quick_backs": None,
            "excessive_scrolling": None,
            "error_clicks": None,
            "script_errors": None,
            "browser_breakdown": None,
            "device_breakdown": None,
            "os_breakdown": None,
            "user_geography": None,
        }

        # L'API retourne directement une liste de métriques avec metricName
        if isinstance(data, list):
            for metric in data:
                metric_name = metric.get("metricName", "")
                info_list = metric.get("information", [])

                # information est une liste, on prend le premier élément s'il existe
                info = info_list[0] if info_list else {}

                if metric_name == "DeadClickCount":
                    consolidated["dead_clicks"] = int(info.get("subTotal", 0)) if info.get("subTotal") else 0
                elif metric_name == "ExcessiveScroll":
                    consolidated["excessive_scrolling"] = int(info.get("subTotal", 0)) if info.get("subTotal") else 0
                elif metric_name == "RageClickCount":
                    consolidated["rage_clicks"] = int(info.get("subTotal", 0)) if info.get("subTotal") else 0
                elif metric_name == "QuickbackClick":
                    consolidated["quick_backs"] = int(info.get("subTotal", 0)) if info.get("subTotal") else 0
                elif metric_name == "ScriptErrorCount":
                    consolidated["script_errors"] = int(info.get("subTotal", 0)) if info.get("subTotal") else 0
                elif metric_name == "ErrorClickCount":
                    consolidated["error_clicks"] = int(info.get("subTotal", 0)) if info.get("subTotal") else 0
                elif metric_name == "ScrollDepth":
                    consolidated["scroll_depth"] = float(info.get("averageScrollDepth", 0)) if info.get("averageScrollDepth") else 0.0
                elif metric_name == "Traffic":
                    consolidated["total_sessions"] = int(info.get("totalSessionCount", 0)) if info.get("totalSessionCount") else 0
                    consolidated["total_users"] = int(info.get("distinctUserCount", 0)) if info.get("distinctUserCount") else 0
                elif metric_name == "EngagementTime":
                    consolidated["avg_engagement_time"] = float(info.get("averageEngagementTime", 0)) if info.get("averageEngagementTime") else 0.0
                elif metric_name == "PopularPages":
                    consolidated["popular_pages"] = self._format_markdown_table(info_list, "Page")
                elif metric_name == "PageViews":
                    consolidated["page_views"] = int(info.get("totalPageViews", 0)) if info.get("totalPageViews") else 0
                elif metric_name == "PageTitles":
                    consolidated["page_titles"] = self._format_markdown_table(info_list, "Name")
                elif metric_name == "ReferrerUrls":
                    consolidated["referrer_urls"] = self._format_markdown_table(info_list, "URL")
                elif metric_name == "Browser":
                    consolidated["browser_breakdown"] = self._format_markdown_table(info_list, "Browser")
                elif metric_name == "Device":
                    consolidated["device_breakdown"] = self._format_markdown_table(info_list, "Device")
                elif metric_name == "OS":
                    consolidated["os_breakdown"] = self._format_markdown_table(info_list, "OS")
                elif metric_name == "Geography":
                    consolidated["user_geography"] = self._format_markdown_table(info_list, "Country")

        return [consolidated]

    def export_to_json(self, data: List[Dict], filename: str):
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"✓ Exporté: {filename}")

    def _get_bigquery_client(self) -> bigquery.Client:
        if self.bq_client is None:
            if self.credentials_path:
                from google.oauth2 import service_account
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
                self.bq_client = bigquery.Client(
                    credentials=credentials,
                    project=self.bq_project_id or credentials.project_id
                )
            else:
                self.bq_client = bigquery.Client(project=self.bq_project_id)
        return self.bq_client

    def upload_to_bigquery(self, data: List[Dict],
                          write_disposition: str = "WRITE_APPEND") -> None:
        if not data:
            print(f"⚠️  Aucune donnée à uploader")
            return

        try:
            client = self._get_bigquery_client()
            df = pd.DataFrame(data)

            # Ajouter retrieved_at
            if 'retrieved_at' not in df.columns:
                df['retrieved_at'] = datetime.now()

            # Convertir date en TIMESTAMP
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])

            # Upload
            table_id = f"{self.bq_project_id}.{self.dataset_id}.clarity_metrics"
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED",
                autodetect=False
            )

            print(f"\n→ Upload BigQuery: {table_id}")
            print(f"  Lignes: {len(df)}")

            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
            job.result()

            table = client.get_table(table_id)
            print(f"✓ Succès! Total: {table.num_rows:,} lignes")

        except Exception as e:
            print(f"✗ Erreur: {e}")
            import traceback
            traceback.print_exc()
            raise


def main():
    # Charger la configuration
    print("📋 Chargement de la configuration...")
    # Chemin absolu vers le fichier de configuration à la racine du projet
    config_path = os.path.join(os.path.dirname(__file__), '../../config.yaml')
    config = load_config(config_path)

    # Récupérer les configurations
    clarity_config = config.get_clarity_config()
    google_config = config.get_google_cloud_config()

    CLARITY_API_TOKEN = clarity_config['api_key']
    CLARITY_PROJECT_ID = clarity_config['project_id']
    NUM_OF_DAYS = clarity_config['num_of_days']

    BQ_PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['microsoft_clarity']
    CREDENTIALS_PATH = google_config['credentials_file']

    print("=" * 70)
    print("MICROSOFT CLARITY DATA EXPORT")
    print("=" * 70)
    print(f"\nProjet: {CLARITY_PROJECT_ID}")
    print(f"Période: {NUM_OF_DAYS} jours")
    print(f"BigQuery: {BQ_PROJECT_ID}.{DATASET_ID}\n")

    client = ClarityAnalyticsClient(
        api_token=CLARITY_API_TOKEN,
        project_id=CLARITY_PROJECT_ID,
        bq_project_id=BQ_PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

    # Récupération des données
    print("→ Récupération des données Clarity...")
    raw_data = client.get_live_insights(num_of_days=NUM_OF_DAYS)

    # DEBUG: Afficher la structure des données
    print("\n=== DEBUG: Structure des données reçues ===")
    print(json.dumps(raw_data, indent=2, default=str)[:2000])  # Premiers 2000 caractères
    print("=" * 70 + "\n")

    # Parse vers format officiel
    print("→ Parsing vers format BigQuery...")
    parsed_data = client.parse_to_official_format(raw_data)
    print(f"✓ {len(parsed_data)} enregistrement(s) parsé(s)")

    # Export
    client.export_to_json(parsed_data, "clarity_metrics.json")
    client.upload_to_bigquery(parsed_data)

    print("\n" + "=" * 70)
    print("✓ TERMINÉ!")
    print("=" * 70)


if __name__ == "__main__":
    main()
