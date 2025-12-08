import requests
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os


class LinkedInPageStatsClient:
    """
    Client pour récupérer les statistiques de page LinkedIn
    Documentation: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/
    """

    def __init__(self, access_token: str, organization_id: Optional[str] = None,
                 project_id: Optional[str] = None, dataset_id: str = "linkedin_page",
                 credentials_path: Optional[str] = None):
        """
        Initialise le client

        Args:
            access_token: Token OAuth 2.0 LinkedIn
            organization_id: ID de l'organisation LinkedIn
            project_id: ID du projet Google Cloud
            dataset_id: ID du dataset BigQuery (défaut: linkedin_page)
            credentials_path: Chemin vers le fichier JSON des credentials GCP
        """
        self.access_token = access_token
        self.organization_id = organization_id
        self.base_url = "https://api.linkedin.com/v2"

        # Configuration BigQuery
        self.project_id = project_id or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.dataset_id = dataset_id
        self.credentials_path = credentials_path
        self.bq_client = None

    def _get_headers(self) -> Dict[str, str]:
        """Retourne les headers requis pour l'API LinkedIn"""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "X-Restli-Protocol-Version": "2.0.0"
        }

    def get_follower_statistics(self, organization_id: Optional[str] = None,
                                time_granularity: str = "ALL",
                                pivot: Optional[str] = None) -> List[Dict]:
        """
        Récupère les statistiques de followers

        Args:
            organization_id: ID de l'organisation
            time_granularity: ALL, DAILY, MONTHLY
            pivot: industry, jobFunction, seniority, country, region

        Returns:
            list: Statistiques de followers
        """
        org_id = organization_id or self.organization_id
        if not org_id:
            raise ValueError("organization_id est requis")

        org_urn = f"urn:li:organization:{org_id}"

        url = f"{self.base_url}/organizationalEntityFollowerStatistics"
        params = {
            "q": "organizationalEntity",
            "organizationalEntity": org_urn,
            "timeGranularity": time_granularity
        }

        if pivot:
            params["pivot"] = pivot

        response = requests.get(url, headers=self._get_headers(), params=params)

        if response.status_code != 200:
            print(f"⚠️  Erreur follower stats: {response.status_code} - {response.text}")
            return []

        data = response.json()
        return self._parse_follower_stats(data, time_granularity, pivot, org_id)

    def get_share_statistics(self, organization_id: Optional[str] = None,
                            time_granularity: str = "DAILY",
                            pivot: Optional[str] = None) -> List[Dict]:
        """
        Récupère les statistiques de partages/posts

        Args:
            organization_id: ID de l'organisation
            time_granularity: DAILY, MONTHLY, ALL
            pivot: share (pour stats par post)

        Returns:
            list: Statistiques de partages
        """
        org_id = organization_id or self.organization_id
        if not org_id:
            raise ValueError("organization_id est requis")

        org_urn = f"urn:li:organization:{org_id}"

        url = f"{self.base_url}/organizationalEntityShareStatistics"
        params = {
            "q": "organizationalEntity",
            "organizationalEntity": org_urn,
            "timeGranularity": time_granularity
        }

        if pivot:
            params["pivot"] = pivot

        response = requests.get(url, headers=self._get_headers(), params=params)

        if response.status_code != 200:
            print(f"⚠️  Erreur share stats: {response.status_code} - {response.text}")
            return []

        data = response.json()
        return self._parse_share_stats(data, time_granularity, pivot, org_id)

    def get_page_statistics(self, organization_id: Optional[str] = None,
                           time_granularity: str = "DAILY") -> List[Dict]:
        """
        Récupère les statistiques de page views

        Args:
            organization_id: ID de l'organisation
            time_granularity: DAILY, MONTHLY

        Returns:
            list: Statistiques de page views
        """
        org_id = organization_id or self.organization_id
        if not org_id:
            raise ValueError("organization_id est requis")

        org_urn = f"urn:li:organization:{org_id}"

        url = f"{self.base_url}/organizationalEntityPageStatistics"
        params = {
            "q": "organizationalEntity",
            "organizationalEntity": org_urn,
            "timeGranularity": time_granularity
        }

        response = requests.get(url, headers=self._get_headers(), params=params)

        if response.status_code != 200:
            print(f"⚠️  Erreur page stats: {response.status_code} - {response.text}")
            return []

        data = response.json()
        return self._parse_page_stats(data, time_granularity, org_id)

    def _parse_follower_stats(self, data: Dict, time_granularity: str,
                             pivot: Optional[str], org_id: str) -> List[Dict]:
        """Parse les données de follower statistics"""
        results = []

        for element in data.get("elements", []):
            # Extraire la date si disponible
            stat_date = None
            time_range = element.get("timeRange", {})
            if time_range.get("start"):
                stat_date = datetime.fromtimestamp(time_range["start"] / 1000).date()

            # Follower counts
            follower_counts = element.get("followerCounts", {})
            organic_follower = follower_counts.get("organicFollowerCount", 0)
            paid_follower = follower_counts.get("paidFollowerCount", 0)
            total_followers = organic_follower + paid_follower

            # Follower gains/losses
            follower_gains = element.get("followerGains", {}).get("organicFollowerGain", 0) + \
                           element.get("followerGains", {}).get("paidFollowerGain", 0) if element.get("followerGains") else None

            follower_losses = element.get("followerLosses", {}).get("organicFollowerLoss", 0) + \
                            element.get("followerLosses", {}).get("paidFollowerLoss", 0) if element.get("followerLosses") else None

            # Demographics (si pivot)
            industry = None
            job_function = None
            seniority = None
            country = None
            region = None
            pivot_value = None

            if pivot:
                pivot_value = element.get(pivot, "")
                if pivot == "industry":
                    industry = pivot_value
                elif pivot == "jobFunction":
                    job_function = pivot_value
                elif pivot == "seniority":
                    seniority = pivot_value
                elif pivot == "country":
                    country = pivot_value
                elif pivot == "region":
                    region = pivot_value

            result = {
                "organization_id": org_id,
                "organization_urn": f"urn:li:organization:{org_id}",
                "stat_date": stat_date,
                "time_granularity": time_granularity,
                "metric_category": "FOLLOWER",
                "pivot_type": pivot,
                "pivot_value": pivot_value,
                "follower_count": total_followers,
                "follower_gains": follower_gains,
                "follower_losses": follower_losses,
                "follower_growth_rate": None,  # À calculer
                "industry": industry,
                "job_function": job_function,
                "seniority": seniority,
                "country": country,
                "region": region,
            }

            results.append(result)

        return results

    def _parse_share_stats(self, data: Dict, time_granularity: str,
                          pivot: Optional[str], org_id: str) -> List[Dict]:
        """Parse les données de share statistics"""
        results = []

        for element in data.get("elements", []):
            # Extraire la date
            stat_date = None
            time_range = element.get("timeRange", {})
            if time_range.get("start"):
                stat_date = datetime.fromtimestamp(time_range["start"] / 1000).date()

            # Share URN (si pivot=share)
            share_urn = None
            share_title = None
            if pivot == "share":
                share_urn = element.get("share", "")
                # Le titre nécessite un appel supplémentaire à l'API UGC

            # Métriques
            impressions = element.get("totalShareStatistics", {}).get("impressionCount", 0)
            unique_impressions = element.get("totalShareStatistics", {}).get("uniqueImpressionsCount", 0)
            clicks = element.get("totalShareStatistics", {}).get("clickCount", 0)
            likes = element.get("totalShareStatistics", {}).get("likeCount", 0)
            comments = element.get("totalShareStatistics", {}).get("commentCount", 0)
            shares = element.get("totalShareStatistics", {}).get("shareCount", 0)

            # Calculs
            total_engagements = likes + comments + shares
            ctr = (clicks / impressions * 100) if impressions > 0 else 0
            engagement_rate = (total_engagements / impressions * 100) if impressions > 0 else 0

            result = {
                "organization_id": org_id,
                "organization_urn": f"urn:li:organization:{org_id}",
                "stat_date": stat_date,
                "time_granularity": time_granularity,
                "metric_category": "SHARE",
                "pivot_type": pivot,
                "pivot_value": share_urn if pivot == "share" else None,
                "share_urn": share_urn,
                "share_title": share_title,
                "impressions": impressions,
                "unique_impressions": unique_impressions,
                "clicks": clicks,
                "likes": likes,
                "comments": comments,
                "shares": shares,
                "click_through_rate": round(ctr, 2),
                "engagement_rate": round(engagement_rate, 2),
                "total_engagements": total_engagements,
            }

            results.append(result)

        return results

    def _parse_page_stats(self, data: Dict, time_granularity: str, org_id: str) -> List[Dict]:
        """Parse les données de page statistics"""
        results = []

        for element in data.get("elements", []):
            # Extraire la date
            stat_date = None
            time_range = element.get("timeRange", {})
            if time_range.get("start"):
                stat_date = datetime.fromtimestamp(time_range["start"] / 1000).date()

            # Page views
            page_views_unique = element.get("totalPageStatistics", {}).get("views", {}).get("uniquePageViews", {}).get("pageViews", 0)
            page_views_total = element.get("totalPageStatistics", {}).get("views", {}).get("allPageViews", {}).get("pageViews", 0)

            result = {
                "organization_id": org_id,
                "organization_urn": f"urn:li:organization:{org_id}",
                "stat_date": stat_date,
                "time_granularity": time_granularity,
                "metric_category": "PAGE_VIEW",
                "pivot_type": None,
                "pivot_value": None,
                "page_views_unique_count": page_views_unique,
                "page_views_total_count": page_views_total,
            }

            results.append(result)

        return results

    def export_to_csv(self, data: List[Dict], filename: str):
        """Exporte les données au format CSV"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter pour {filename}")
            return
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"✓ Données exportées: {filename}")

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données au format JSON"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter pour {filename}")
            return
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

    def upload_to_bigquery(self, data: List[Dict], table_name: str = "linkedin_page_statistics",
                          write_disposition: str = "WRITE_APPEND") -> None:
        """Upload les données vers BigQuery"""
        if not data:
            print(f"⚠️  Aucune donnée à uploader")
            return

        try:
            client = self._get_bigquery_client()
            df = pd.DataFrame(data)

            # Ajouter retrieved_at
            if 'retrieved_at' not in df.columns:
                df['retrieved_at'] = datetime.now()

            # Convertir stat_date en date
            if 'stat_date' in df.columns:
                df['stat_date'] = pd.to_datetime(df['stat_date'], errors='coerce').dt.date

            # Remplir les valeurs manquantes par None pour les colonnes non utilisées
            all_columns = [
                'organization_id', 'organization_urn', 'stat_date', 'time_granularity',
                'metric_category', 'pivot_type', 'pivot_value',
                'follower_count', 'follower_gains', 'follower_losses', 'follower_growth_rate',
                'industry', 'job_function', 'seniority', 'country', 'region',
                'share_urn', 'share_title', 'impressions', 'unique_impressions',
                'clicks', 'likes', 'comments', 'shares',
                'click_through_rate', 'engagement_rate', 'total_engagements',
                'page_views_unique_count', 'page_views_total_count', 'retrieved_at'
            ]

            for col in all_columns:
                if col not in df.columns:
                    df[col] = None

            # Réorganiser les colonnes
            df = df[all_columns]

            # Convertir les colonnes numériques
            numeric_cols = [
                'follower_count', 'follower_gains', 'follower_losses', 'follower_growth_rate',
                'impressions', 'unique_impressions', 'clicks', 'likes', 'comments', 'shares',
                'click_through_rate', 'engagement_rate', 'total_engagements',
                'page_views_unique_count', 'page_views_total_count'
            ]
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')

            # Upload
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED",
                autodetect=False
            )

            print(f"\n→ Upload vers BigQuery: {table_id}")
            print(f"  Nombre de lignes: {len(df)}")

            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
            job.result()

            table = client.get_table(table_id)
            print(f"✓ Upload réussi! Total lignes dans la table: {table.num_rows:,}")

        except Exception as e:
            print(f"✗ Erreur lors de l'upload vers BigQuery: {e}")
            import traceback
            traceback.print_exc()
            raise


def main():
    """Exemple d'utilisation"""
    
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
    from config_loader import load_config

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    config = load_config()

    # Récupérer les configurations
    linkedin_config = config.get_linkedin_config()
    google_config = config.get_google_cloud_config()

    # Récupérer l'access token depuis la configuration
    ACCESS_TOKEN = linkedin_config.get('access_token')
    if not ACCESS_TOKEN:
        print("❌ ERREUR: access_token LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'access_token' dans la section linkedin.oauth")
        return
    
    # Récupérer l'organization_id depuis la config
    ORGANIZATION_ID = linkedin_config.get('organization_id')
    if not ORGANIZATION_ID:
        print("❌ ERREUR: organization_id LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'organization_id' dans la section linkedin")
        return
    
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets'].get('linkedin_page', 'linkedin_page')
    CREDENTIALS_PATH = google_config['credentials_file']

    print("=" * 70)
    print("LINKEDIN PAGE STATISTICS")
    print("=" * 70)
    print(f"\nOrganisation: {ORGANIZATION_ID}")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}\n")

    client = LinkedInPageStatsClient(
        access_token=ACCESS_TOKEN,
        organization_id=ORGANIZATION_ID,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

    all_stats = []

    # 1. Follower Statistics
    print("=" * 70)
    print("1. Statistiques de Followers")
    print("=" * 70)

    # Total followers
    print("\n→ Total followers (ALL)...")
    stats = client.get_follower_statistics(time_granularity="ALL")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    # Monthly follower gains
    print("\n→ Nouveaux followers (MONTHLY)...")
    stats = client.get_follower_statistics(time_granularity="MONTHLY")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    # Follower demographics
    for pivot in ["industry", "jobFunction", "seniority", "country"]:
        print(f"\n→ Followers par {pivot}...")
        stats = client.get_follower_statistics(pivot=pivot)
        all_stats.extend(stats)
        print(f"✓ {len(stats)} enregistrement(s)")

    # 2. Share Statistics
    print("\n" + "=" * 70)
    print("2. Statistiques de Posts/Partages")
    print("=" * 70)

    # Daily share stats
    print("\n→ Stats quotidiennes (DAILY)...")
    stats = client.get_share_statistics(time_granularity="DAILY")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    # Monthly share stats
    print("\n→ Stats mensuelles (MONTHLY)...")
    stats = client.get_share_statistics(time_granularity="MONTHLY")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    # Per-post stats
    print("\n→ Stats par post (pivot=share)...")
    stats = client.get_share_statistics(pivot="share")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    # 3. Page View Statistics
    print("\n" + "=" * 70)
    print("3. Statistiques de Pages Views")
    print("=" * 70)

    print("\n→ Page views quotidiennes (DAILY)...")
    stats = client.get_page_statistics(time_granularity="DAILY")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    print("\n→ Page views mensuelles (MONTHLY)...")
    stats = client.get_page_statistics(time_granularity="MONTHLY")
    all_stats.extend(stats)
    print(f"✓ {len(stats)} enregistrement(s)")

    # Export et Upload
    print("\n" + "=" * 70)
    print("4. Export et Upload")
    print("=" * 70)

    if all_stats:
        client.export_to_json(all_stats, "linkedin_page_statistics.json")
        client.export_to_csv(all_stats, "linkedin_page_statistics.csv")
        client.upload_to_bigquery(all_stats)

        print("\n" + "=" * 70)
        print("✓ COLLECTE TERMINÉE!")
        print("=" * 70)
        print(f"📊 Total: {len(all_stats)} statistiques collectées")
        print(f"📁 Fichiers: linkedin_page_statistics.json / .csv")
        print(f"☁️  BigQuery: {PROJECT_ID}.{DATASET_ID}.linkedin_page_statistics")
    else:
        print("\n⚠️  Aucune statistique collectée")


if __name__ == "__main__":
    main()
