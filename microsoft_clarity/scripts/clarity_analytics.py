import requests
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os
import sys

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
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

    def parse_to_bigquery_format(self, data, project_name: str = None) -> List[Dict]:
        """Parse les données brutes vers le format BigQuery - une ligne par URL"""
        current_date = datetime.now().date()
        retrieved_at = datetime.now()
        
        rows = []
        
        # Collecter les métriques globales
        metrics = {
            'scroll_depth': None,
            'engagement_time': None,
            'traffic': None,
            'browser': [],
            'device': [],
            'os': [],
            'country': [],
            'page_title': [],
            'referrer_url': [],
            'dead_clicks': None,
            'excessive_scroll': None,
            'rage_clicks': None,
            'quickback_clicks': None,
            'script_errors': None,
            'error_clicks': None,
            'popular_pages': []
        }
        
        if not isinstance(data, list):
            return rows
        
        # Collecter les métriques
        for metric in data:
            metric_name = metric.get("metricName", "")
            info_list = metric.get("information", [])
            info = info_list[0] if info_list else {}
            
            if metric_name == "ScrollDepth":
                metrics['scroll_depth'] = {
                    'percentage_0_10': None,
                    'percentage_11_25': None,
                    'percentage_26_50': None,
                    'percentage_51_75': None,
                    'percentage_76_100': None,
                    'average_scroll_depth': float(info.get('averageScrollDepth', 0))
                }
            elif metric_name == "EngagementTime":
                metrics['engagement_time'] = {
                    'total_time': float(info.get('totalTime', 0)),
                    'active_time': float(info.get('activeTime', 0))
                }
            elif metric_name == "Traffic":
                metrics['traffic'] = {
                    'total_session_count': int(info.get('totalSessionCount', 0)),
                    'total_bot_session_count': int(info.get('totalBotSessionCount', 0)),
                    'distinct_user_count': int(info.get('distinctUserCount', 0)),
                    'pages_per_session': float(info.get('pagesPerSessionPercentage', 0))
                }
            elif metric_name == "PopularPages":
                metrics['popular_pages'] = info_list
            elif metric_name == "Browser":
                metrics['browser'] = [
                    {'name': item.get('name'), 'sessions_count': int(item.get('sessionsCount', 0))}
                    for item in info_list
                ]
            elif metric_name == "Device":
                metrics['device'] = [
                    {'name': item.get('name'), 'sessions_count': int(item.get('sessionsCount', 0))}
                    for item in info_list
                ]
            elif metric_name == "OS":
                metrics['os'] = [
                    {'name': item.get('name'), 'sessions_count': int(item.get('sessionsCount', 0))}
                    for item in info_list
                ]
            elif metric_name == "Country":
                metrics['country'] = [
                    {'name': item.get('name'), 'sessions_count': int(item.get('sessionsCount', 0))}
                    for item in info_list
                ]
            elif metric_name == "PageTitle":
                metrics['page_title'] = [
                    {'name': item.get('name'), 'sessions_count': int(item.get('sessionsCount', 0))}
                    for item in info_list
                ]
            elif metric_name == "ReferrerUrl":
                metrics['referrer_url'] = [
                    {'name': item.get('name'), 'sessions_count': int(item.get('sessionsCount', 0))}
                    for item in info_list
                ]
            elif metric_name == "DeadClickCount":
                metrics['dead_clicks'] = {
                    'sessions_count': int(info.get('sessionsCount', 0)),
                    'sessions_with_metric_percentage': float(info.get('sessionsWithMetricPercentage', 0)),
                    'sessions_without_metric_percentage': float(info.get('sessionsWithoutMetricPercentage', 0)),
                    'pages_views': int(info.get('pagesViews', 0)),
                    'sub_total': int(info.get('subTotal', 0))
                }
            elif metric_name == "ExcessiveScroll":
                metrics['excessive_scroll'] = {
                    'sessions_count': int(info.get('sessionsCount', 0)),
                    'sessions_with_metric_percentage': float(info.get('sessionsWithMetricPercentage', 0)),
                    'sessions_without_metric_percentage': float(info.get('sessionsWithoutMetricPercentage', 0)),
                    'pages_views': int(info.get('pagesViews', 0)),
                    'sub_total': int(info.get('subTotal', 0))
                }
            elif metric_name == "RageClickCount":
                metrics['rage_clicks'] = {
                    'sessions_count': int(info.get('sessionsCount', 0)),
                    'sessions_with_metric_percentage': float(info.get('sessionsWithMetricPercentage', 0)),
                    'sessions_without_metric_percentage': float(info.get('sessionsWithoutMetricPercentage', 0)),
                    'pages_views': int(info.get('pagesViews', 0)),
                    'sub_total': int(info.get('subTotal', 0))
                }
            elif metric_name == "QuickbackClick":
                metrics['quickback_clicks'] = {
                    'sessions_count': int(info.get('sessionsCount', 0)),
                    'sessions_with_metric_percentage': float(info.get('sessionsWithMetricPercentage', 0)),
                    'sessions_without_metric_percentage': float(info.get('sessionsWithoutMetricPercentage', 0)),
                    'pages_views': int(info.get('pagesViews', 0)),
                    'sub_total': int(info.get('subTotal', 0))
                }
            elif metric_name == "ScriptErrorCount":
                metrics['script_errors'] = {
                    'sessions_count': int(info.get('sessionsCount', 0)),
                    'sessions_with_metric_percentage': float(info.get('sessionsWithMetricPercentage', 0)),
                    'sessions_without_metric_percentage': float(info.get('sessionsWithoutMetricPercentage', 0)),
                    'pages_views': int(info.get('pagesViews', 0)),
                    'sub_total': int(info.get('subTotal', 0))
                }
            elif metric_name == "ErrorClickCount":
                metrics['error_clicks'] = {
                    'sessions_count': int(info.get('sessionsCount', 0)),
                    'sessions_with_metric_percentage': float(info.get('sessionsWithMetricPercentage', 0)),
                    'sessions_without_metric_percentage': float(info.get('sessionsWithoutMetricPercentage', 0)),
                    'pages_views': int(info.get('pagesViews', 0)),
                    'sub_total': int(info.get('subTotal', 0))
                }
        
        # Créer une ligne par URL
        for page in metrics['popular_pages']:
            row = {
                'date': current_date,
                'retrieved_at': retrieved_at,
                'project_name': project_name,
                'url': page.get('url'),
                'visits_count': int(page.get('visitsCount', 0)),
                'scroll_depth': metrics['scroll_depth'],
                'engagement_time': metrics['engagement_time'],
                'traffic': metrics['traffic'],
                'browser': metrics['browser'],
                'device': metrics['device'],
                'os': metrics['os'],
                'country': metrics['country'],
                'page_title': metrics['page_title'],
                'referrer_url': metrics['referrer_url'],
                'dead_clicks': metrics['dead_clicks'],
                'excessive_scroll': metrics['excessive_scroll'],
                'rage_clicks': metrics['rage_clicks'],
                'quickback_clicks': metrics['quickback_clicks'],
                'script_errors': metrics['script_errors'],
                'error_clicks': metrics['error_clicks']
            }
            rows.append(row)
        
        return rows

    def export_to_json(self, data: List[Dict], filename: str):
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"✓ Exporté: {filename}")

    def _get_bigquery_client(self) -> bigquery.Client:
        if self.bq_client is None:
            if self.credentials_path and os.path.exists(self.credentials_path):
                # Essayer de charger le fichier credentials
                try:
                    from google.oauth2 import service_account
                    credentials = service_account.Credentials.from_service_account_file(
                        self.credentials_path,
                        scopes=["https://www.googleapis.com/auth/bigquery"]
                    )
                    self.bq_client = bigquery.Client(
                        credentials=credentials,
                        project=self.bq_project_id or credentials.project_id
                    )
                except Exception as e:
                    # Si le fichier n'est pas un service account valide, utiliser ADC
                    print(f"⚠️  Credentials file invalide ({e}), utilisation de gcloud ADC...")
                    self.bq_client = bigquery.Client(project=self.bq_project_id)
            else:
                # Utiliser Application Default Credentials (gcloud)
                self.bq_client = bigquery.Client(project=self.bq_project_id)
        return self.bq_client

    def check_date_exists(self, date_to_check: datetime) -> bool:
        """Vérifie si des données existent déjà pour cette date"""
        try:
            client = self._get_bigquery_client()
            table_id = f"{self.bq_project_id}.{self.dataset_id}.clarity_metrics"

            date_str = date_to_check.strftime("%Y-%m-%d")
            query = f"""
                SELECT COUNT(*) as count
                FROM `{table_id}`
                WHERE DATE(date) = '{date_str}'
            """

            result = client.query(query).result()
            row = next(iter(result), None)

            if row and row.count > 0:
                print(f"ℹ️  Données existantes pour {date_str} ({row.count} ligne(s))")
                return True
            return False

        except Exception:
            # Table n'existe pas encore
            return False

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
    # Chemin vers le fichier de configuration (dans le dossier parent pour Cloud Functions)
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')

    # Détecter si on est dans Cloud Functions (pas besoin de fichier credentials)
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config = load_config(config_path, skip_credentials_check=is_cloud_function)

    # Récupérer les configurations
    clarity_config = config.get_clarity_config()
    google_config = config.get_google_cloud_config()

    CLARITY_API_TOKEN = clarity_config['api_key']
    CLARITY_PROJECT_ID = clarity_config['project_id']
    NUM_OF_DAYS = clarity_config['num_of_days']

    BQ_PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['microsoft_clarity']

    # Pour Cloud Functions : utiliser l'authentification par défaut (pas de fichier JSON)
    # Pour local : utiliser le fichier credentials
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    CREDENTIALS_PATH = None if is_cloud_function else google_config.get('credentials_file')

    print("=" * 70)
    print("MICROSOFT CLARITY DATA EXPORT")
    print("=" * 70)
    print(f"\nProjet: {CLARITY_PROJECT_ID}")
    print(f"Période: {NUM_OF_DAYS} jours")
    print(f"BigQuery: {BQ_PROJECT_ID}.{DATASET_ID}")
    print(f"Environment: {'Cloud Function' if is_cloud_function else 'Local'}\n")

    client = ClarityAnalyticsClient(
        api_token=CLARITY_API_TOKEN,
        project_id=CLARITY_PROJECT_ID,
        bq_project_id=BQ_PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

    # Vérifier si des données existent déjà pour aujourd'hui
    today = datetime.now()
    if client.check_date_exists(today):
        print("\n⚠️  Données déjà collectées pour aujourd'hui.")
        print("   Voulez-vous continuer ? (cela créera des doublons)")
        print("   Pour éviter les doublons en automatisation, le script s'arrête ici.")
        print("\n" + "=" * 70)
        print("✓ SCRIPT TERMINÉ (pas de nouvelles données à collecter)")
        print("=" * 70)
        return

    # Récupération des données
    print("→ Récupération des données Clarity...")
    raw_data = client.get_live_insights(num_of_days=NUM_OF_DAYS)

    # DEBUG: Afficher la structure des données
    print("\n=== DEBUG: Structure des données reçues ===")
    print(json.dumps(raw_data, indent=2, default=str))  # Données complètes
    print("=" * 70 + "\n")

    # DEBUG: Afficher les metricNames disponibles
    if isinstance(raw_data, list):
        metric_names = [m.get("metricName") for m in raw_data]
        print(f"=== Métriques disponibles ({len(metric_names)}): ===")
        for mn in metric_names:
            print(f"  - {mn}")
        print("=" * 70 + "\n")

    # Parse vers format BigQuery
    print("→ Parsing vers format BigQuery...")
    project_name = clarity_config.get('name', CLARITY_PROJECT_ID)
    parsed_data = client.parse_to_bigquery_format(raw_data, project_name=project_name)
    print(f"✓ {len(parsed_data)} ligne(s) parsée(s) (une par URL)")

    # Export
    client.export_to_json(parsed_data, "clarity_metrics.json")
    client.upload_to_bigquery(parsed_data)

    print("\n" + "=" * 70)
    print("✓ TERMINÉ!")
    print("=" * 70)


if __name__ == "__main__":
    main()
