#!/usr/bin/env python3
"""
Script de synchronisation LinkedIn → BigQuery
Récupère les statistiques de followers et de page views par dimensions
"""

import requests
import json
from datetime import datetime
from urllib.parse import quote
from typing import List, Dict
from google.cloud import bigquery
from google.oauth2 import service_account
import sys
import os

# Works both locally (linkedin/) and in cloud container (scripts/)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from config_loader import load_config


class LinkedInStatsCollector:
    """Collecteur de statistiques LinkedIn"""
    
    def __init__(self, access_token: str, organization_id: str):
        self.access_token = access_token
        self.organization_id = organization_id
        self.base_url = 'https://api.linkedin.com/rest'
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'LinkedIn-Version': '202511',
            'X-Restli-Protocol-Version': '2.0.0',
        }
        self.org_urn = f'urn:li:organization:{organization_id}'
        self.org_urn_encoded = quote(self.org_urn, safe='')
        self.urn_cache = {}  # Cache pour éviter de résoudre plusieurs fois le même URN
    
    def _make_request(self, url: str) -> requests.Response:
        """Effectue une requête HTTP"""
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response
    
    def resolve_urn(self, urn: str) -> str:
        """
        Résout un URN LinkedIn vers son nom lisible
        Utilise un cache pour éviter les appels répétés
        
        Args:
            urn: URN à résoudre (ex: 'urn:li:geo:90009496')
            
        Returns:
            Nom résolu ou URN original si la résolution échoue
        """
        # Si déjà dans le cache
        if urn in self.urn_cache:
            return self.urn_cache[urn]
        
        # Si ce n'est pas un URN, retourner tel quel
        if not urn.startswith('urn:li:'):
            self.urn_cache[urn] = urn
            return urn
        
        try:
            # Extraire le type et l'ID de l'URN
            # Format: urn:li:{type}:{id}
            parts = urn.split(':')
            if len(parts) != 4:
                self.urn_cache[urn] = urn
                return urn
            
            urn_type = parts[2]
            urn_id = parts[3]
            
            # Mapping des types vers les endpoints
            endpoint_mapping = {
                'geo': f'/geo/{urn_id}',
                'function': f'/functions/{urn_id}',
                'industry': f'/industries/{urn_id}',
                'seniority': f'/seniorities/{urn_id}'
            }
            
            if urn_type not in endpoint_mapping:
                # Type non supporté, garder l'URN
                self.urn_cache[urn] = urn
                return urn
            
            # Appeler l'endpoint de résolution
            url = f"{self.base_url}{endpoint_mapping[urn_type]}"
            response = self._make_request(url)
            data = response.json()
            
            # Extraire le nom selon le format de réponse
            name = None
            
            if 'defaultLocalizedName' in data:
                # Format pour geo
                name = data['defaultLocalizedName'].get('value')
            elif 'name' in data:
                # Format pour function, industry, seniority
                if isinstance(data['name'], dict):
                    if 'localized' in data['name']:
                        # Prendre la première locale disponible
                        localized = data['name']['localized']
                        if localized:
                            name = list(localized.values())[0]
            
            if name:
                self.urn_cache[urn] = name
                return name
            else:
                # Pas de nom trouvé, garder l'URN
                self.urn_cache[urn] = urn
                return urn
                
        except Exception as e:
            # En cas d'erreur, garder l'URN original
            print(f"    ⚠️  Impossible de résoudre {urn}: {e}")
            self.urn_cache[urn] = urn
            return urn
    
    def get_follower_statistics(self) -> List[Dict]:
        """
        Récupère les statistiques de followers par dimensions
        Retourne une structure pivot avec dimension_type et dimension_value
        """
        print("\n→ Follower Statistics")
        
        url = f"{self.base_url}/organizationalEntityFollowerStatistics?q=organizationalEntity&organizationalEntity={self.org_urn_encoded}"
        
        try:
            response = self._make_request(url)
            data = response.json()
            
            if not data.get('elements'):
                print("  ⚠️  Aucune donnée retournée")
                return []
            
            element = data['elements'][0]
            results = []
            retrieved_at = datetime.now()
            
            # Mapping des dimensions
            dimensions_mapping = {
                'followerCountsByGeoCountry': 'geo_country',
                'followerCountsByGeo': 'geo',
                'followerCountsByFunction': 'function',
                'followerCountsBySeniority': 'seniority',
                'followerCountsByIndustry': 'industry',
                'followerCountsByStaffCountRange': 'staff_count_range',
                'followerCountsByAssociationType': 'association_type'
            }
            
            for api_key, dimension_type in dimensions_mapping.items():
                if api_key in element:
                    items = element[api_key]
                    print(f"  → {dimension_type}: {len(items)} entrées")
                    
                    for item in items:
                        counts = item.get('followerCounts', {})
                        
                        # Extraire la valeur de dimension (geo, function, etc.)
                        dimension_value = None
                        if 'geo' in item:
                            dimension_value = item['geo']
                        elif 'function' in item:
                            dimension_value = item['function']
                        elif 'seniority' in item:
                            dimension_value = item['seniority']
                        elif 'industry' in item:
                            dimension_value = item['industry']
                        elif 'staffCountRange' in item:
                            dimension_value = item['staffCountRange']
                        elif 'associationType' in item:
                            dimension_value = item['associationType']
                        
                        if dimension_value:
                            # Résoudre l'URN pour avoir le nom lisible
                            resolved_value = self.resolve_urn(dimension_value)
                            
                            results.append({
                                'organization_id': self.organization_id,
                                'dimension_type': dimension_type,
                                'dimension_value': resolved_value,
                                'organic_follower_count': counts.get('organicFollowerCount', 0),
                                'paid_follower_count': counts.get('paidFollowerCount', 0),
                                'retrieved_at': retrieved_at
                            })
            
            print(f"  ✓ Total: {len(results)} enregistrements")
            return results
            
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
            return []
    
    def get_page_statistics(self) -> List[Dict]:
        """
        Récupère les statistiques de vues de page par dimensions
        Retourne une structure pivot avec dimension_type et dimension_value
        """
        print("\n→ Page Statistics")
        
        url = f"{self.base_url}/organizationPageStatistics?q=organization&organization={self.org_urn_encoded}"
        
        try:
            response = self._make_request(url)
            data = response.json()
            
            if not data.get('elements'):
                print("  ⚠️  Aucune donnée retournée")
                return []
            
            element = data['elements'][0]
            results = []
            retrieved_at = datetime.now()
            
            # 1. Total page statistics
            if 'totalPageStatistics' in element:
                total_views = element['totalPageStatistics'].get('views', {}).get('allPageViews', {}).get('pageViews', 0)
                results.append({
                    'organization_id': self.organization_id,
                    'dimension_type': 'total',
                    'dimension_value': None,
                    'page_views': total_views,
                    'retrieved_at': retrieved_at
                })
                print(f"  → total: {total_views:,} views")
            
            # Mapping des dimensions
            dimensions_mapping = {
                'pageStatisticsByGeoCountry': ('geo_country', 'geo'),
                'pageStatisticsByGeo': ('geo', 'geo'),
                'pageStatisticsByFunction': ('function', 'function'),
                'pageStatisticsByIndustryV2': ('industry', 'industryV2'),
                'pageStatisticsBySeniority': ('seniority', 'seniority'),
                'pageStatisticsByStaffCountRange': ('staff_count_range', 'staffCountRange')
            }
            
            for api_key, (dimension_type, value_key) in dimensions_mapping.items():
                if api_key in element:
                    items = element[api_key]
                    print(f"  → {dimension_type}: {len(items)} entrées")
                    
                    for item in items:
                        views = item.get('pageStatistics', {}).get('views', {}).get('allPageViews', {}).get('pageViews', 0)
                        dimension_value = item.get(value_key)
                        
                        if dimension_value or views > 0:  # Garder même si dimension_value est None si on a des views
                            # Résoudre l'URN pour avoir le nom lisible
                            resolved_value = self.resolve_urn(dimension_value) if dimension_value else None
                            
                            results.append({
                                'organization_id': self.organization_id,
                                'dimension_type': dimension_type,
                                'dimension_value': resolved_value,
                                'page_views': views,
                                'retrieved_at': retrieved_at
                            })
            
            print(f"  ✓ Total: {len(results)} enregistrements")
            return results
            
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
            return []
    
    def get_content_statistics(self) -> List[Dict]:
        """
        Récupère les statistiques d'engagement sur les contenus partagés par jour
        Utilise timeIntervals pour obtenir les données des 365 derniers jours
        Gère la pagination pour récupérer tous les résultats
        Retourne une liste d'enregistrements (un par jour)
        """
        print("\n→ Content Statistics (365 derniers jours)")
        
        # Calculer les timestamps pour les 365 derniers jours
        from datetime import timedelta
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        
        start_timestamp = int(start_date.timestamp() * 1000)
        end_timestamp = int(end_date.timestamp() * 1000)
        
        # Construire le paramètre timeIntervals
        time_intervals = f"(timeRange:(start:{start_timestamp},end:{end_timestamp}),timeGranularityType:DAY)"
        
        retrieved_at = datetime.now()
        results = []
        start_index = 0
        count_per_page = 100  # Récupérer 100 résultats par page
        
        while True:
            url = (
                f"{self.base_url}/organizationalEntityShareStatistics"
                f"?q=organizationalEntity"
                f"&organizationalEntity={self.org_urn_encoded}"
                f"&timeIntervals={time_intervals}"
                f"&start={start_index}"
                f"&count={count_per_page}"
            )
            
            try:
                response = self._make_request(url)
                data = response.json()
                
                if not data.get('elements'):
                    print(f"  ⚠️  Aucune donnée retournée à start={start_index}")
                    break
                
                # Parcourir les éléments de cette page
                for element in data['elements']:
                    if 'totalShareStatistics' not in element or 'timeRange' not in element:
                        continue
                    
                    stats = element['totalShareStatistics']
                    time_range = element['timeRange']
                    
                    # Convertir les timestamps en dates YYYY-MM-DD
                    time_start = datetime.fromtimestamp(time_range['start'] / 1000).strftime('%Y-%m-%d')
                    time_end = datetime.fromtimestamp(time_range['end'] / 1000).strftime('%Y-%m-%d')
                    
                    # Extraire les métriques
                    click_count = stats.get('clickCount', 0)
                    like_count = stats.get('likeCount', 0)
                    comment_count = stats.get('commentCount', 0)
                    share_count = stats.get('shareCount', 0)
                    impression_count = stats.get('impressionCount', 0)
                    unique_impressions_count = stats.get('uniqueImpressionsCount', 0)
                    
                    # Calculer le taux d'engagement
                    engagement_rate = 0.0
                    if impression_count > 0:
                        total_engagement = click_count + like_count + comment_count + share_count
                        engagement_rate = total_engagement / impression_count
                    
                    results.append({
                        'organization_id': self.organization_id,
                        'time_start': time_start,
                        'time_end': time_end,
                        'unique_impressions_count': unique_impressions_count,
                        'impression_count': impression_count,
                        'click_count': click_count,
                        'like_count': like_count,
                        'comment_count': comment_count,
                        'share_count': share_count,
                        'engagement_rate': engagement_rate,
                        'retrieved_at': retrieved_at
                    })
                
                # Vérifier s'il y a d'autres pages
                paging = data.get('paging', {})
                total = paging.get('total', 0)
                current_count = len(data['elements'])
                
                print(f"  → Page récupérée: {start_index}-{start_index + current_count} / {total}")
                
                # Si on a récupéré tous les résultats ou moins que demandé, on arrête
                if start_index + current_count >= total or current_count < count_per_page:
                    break
                
                # Passer à la page suivante
                start_index += current_count
                
            except Exception as e:
                print(f"  ❌ Erreur à start={start_index}: {e}")
                break
        
        if results:
            total_impressions = sum(r['impression_count'] for r in results)
            total_clicks = sum(r['click_count'] for r in results)
            print(f"  → Jours avec données: {len(results)}")
            print(f"  → Total impressions: {total_impressions:,}")
            print(f"  → Total clics: {total_clicks:,}")
        
        print(f"  ✓ Total: {len(results)} enregistrements")
        return results
    
    def get_follower_statistics_timeseries(self) -> List[Dict]:
        """
        Récupère les gains de followers par jour (sans dimensions)
        Utilise timeIntervals pour obtenir les données des 365 derniers jours
        Gère la pagination pour récupérer tous les résultats
        """
        print("\n→ Follower Statistics Timeseries (365 derniers jours)")
        
        from datetime import timedelta
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        
        start_timestamp = int(start_date.timestamp() * 1000)
        end_timestamp = int(end_date.timestamp() * 1000)
        
        time_intervals = f"(timeRange:(start:{start_timestamp},end:{end_timestamp}),timeGranularityType:DAY)"
        
        retrieved_at = datetime.now()
        results = []
        start_index = 0
        count_per_page = 100
        
        while True:
            url = (
                f"{self.base_url}/organizationalEntityFollowerStatistics"
                f"?q=organizationalEntity"
                f"&organizationalEntity={self.org_urn_encoded}"
                f"&timeIntervals={time_intervals}"
                f"&start={start_index}"
                f"&count={count_per_page}"
            )
            
            try:
                response = self._make_request(url)
                data = response.json()
                
                if not data.get('elements'):
                    break
                
                for element in data['elements']:
                    if 'timeRange' not in element or 'followerGains' not in element:
                        continue
                    
                    time_range = element['timeRange']
                    time_start = datetime.fromtimestamp(time_range['start'] / 1000).strftime('%Y-%m-%d')
                    time_end = datetime.fromtimestamp(time_range['end'] / 1000).strftime('%Y-%m-%d')
                    
                    follower_gains = element['followerGains']
                    
                    results.append({
                        'organization_id': self.organization_id,
                        'time_start': time_start,
                        'time_end': time_end,
                        'organic_follower_gain': follower_gains.get('organicFollowerGain', 0),
                        'paid_follower_gain': follower_gains.get('paidFollowerGain', 0),
                        'retrieved_at': retrieved_at
                    })
                
                paging = data.get('paging', {})
                total = paging.get('total', 0)
                current_count = len(data['elements'])
                
                print(f"  → Page récupérée: {start_index}-{start_index + current_count} / {total}")
                
                if start_index + current_count >= total or current_count < count_per_page:
                    break
                
                start_index += current_count
                
            except Exception as e:
                print(f"  ❌ Erreur à start={start_index}: {e}")
                break
        
        if results:
            total_organic = sum(r['organic_follower_gain'] for r in results)
            total_paid = sum(r['paid_follower_gain'] for r in results)
            print(f"  → Total organic gains: {total_organic:,}")
            print(f"  → Total paid gains: {total_paid:,}")
        
        print(f"  ✓ Total: {len(results)} enregistrements")
        return results
    
    def get_page_statistics_timeseries(self) -> List[Dict]:
        """
        Récupère les statistiques de vues de page par jour (total uniquement)
        Utilise timeIntervals pour obtenir les données des 365 derniers jours
        Gère la pagination pour récupérer tous les résultats
        Note: L'API avec timeIntervals ne retourne que totalPageStatistics, pas les dimensions
        """
        print("\n→ Page Statistics Timeseries (365 derniers jours)")

        from datetime import timedelta
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        start_timestamp = int(start_date.timestamp() * 1000)
        end_timestamp = int(end_date.timestamp() * 1000)

        time_intervals = f"(timeRange:(start:{start_timestamp},end:{end_timestamp}),timeGranularityType:DAY)"

        retrieved_at = datetime.now()
        results = []
        start_index = 0
        count_per_page = 100

        while True:
            url = (
                f"{self.base_url}/organizationPageStatistics"
                f"?q=organization"
                f"&organization={self.org_urn_encoded}"
                f"&timeIntervals={time_intervals}"
                f"&start={start_index}"
                f"&count={count_per_page}"
            )

            try:
                response = self._make_request(url)
                data = response.json()

                if not data.get('elements'):
                    break

                for element in data['elements']:
                    if 'timeRange' not in element:
                        continue

                    time_range = element['timeRange']
                    time_start = datetime.fromtimestamp(time_range['start'] / 1000).strftime('%Y-%m-%d')
                    time_end = datetime.fromtimestamp(time_range['end'] / 1000).strftime('%Y-%m-%d')

                    # Total page views uniquement (pas de dimensions avec timeIntervals)
                    if 'totalPageStatistics' in element:
                        total_views = element['totalPageStatistics'].get('views', {}).get('allPageViews', {}).get('pageViews', 0)
                        results.append({
                            'organization_id': self.organization_id,
                            'time_start': time_start,
                            'time_end': time_end,
                            'page_views': total_views,
                            'retrieved_at': retrieved_at
                        })

                paging = data.get('paging', {})
                total = paging.get('total', 0)
                current_count = len(data['elements'])

                print(f"  → Page récupérée: {start_index}-{start_index + current_count} / {total}")

                if start_index + current_count >= total or current_count < count_per_page:
                    break

                start_index += current_count

            except Exception as e:
                print(f"  ❌ Erreur à start={start_index}: {e}")
                break

        if results:
            total_views = sum(r['page_views'] for r in results)
            print(f"  → Total page views: {total_views:,}")

        print(f"  ✓ Total: {len(results)} enregistrements")
        return results


def upload_to_bigquery(data: List[Dict], table_id: str, project_id: str, dataset_id: str, credentials_path: str):
    """Upload les données vers BigQuery"""
    
    if not data:
        print(f"  ⚠️  Aucune donnée à uploader pour {table_id}")
        return
    
    print(f"\n→ Upload vers BigQuery: {table_id}")
    print(f"  Enregistrements: {len(data)}")
    
    # Schémas BigQuery
    schemas = {
        'followers': [
            bigquery.SchemaField("organization_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("dimension_type", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("dimension_value", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("organic_follower_count", "INT64"),
            bigquery.SchemaField("paid_follower_count", "INT64"),
            bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="REQUIRED"),
        ],
        'page_statistics': [
            bigquery.SchemaField("organization_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("dimension_type", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("dimension_value", "STRING"),
            bigquery.SchemaField("page_views", "INT64"),
            bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="REQUIRED"),
        ],
        'content_statistics': [
            bigquery.SchemaField("organization_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("time_start", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("time_end", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("unique_impressions_count", "INT64"),
            bigquery.SchemaField("impression_count", "INT64"),
            bigquery.SchemaField("click_count", "INT64"),
            bigquery.SchemaField("like_count", "INT64"),
            bigquery.SchemaField("comment_count", "INT64"),
            bigquery.SchemaField("share_count", "INT64"),
            bigquery.SchemaField("engagement_rate", "FLOAT64"),
            bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="REQUIRED"),
        ],
        'followers_timeseries': [
            bigquery.SchemaField("organization_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("time_start", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("time_end", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("organic_follower_gain", "INT64"),
            bigquery.SchemaField("paid_follower_gain", "INT64"),
            bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="REQUIRED"),
        ],
        'page_statistics_timeseries': [
            bigquery.SchemaField("organization_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("time_start", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("time_end", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("page_views", "INT64"),
            bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="REQUIRED"),
        ],
    }
    
    # Initialiser le client BigQuery
    if credentials_path and os.path.exists(credentials_path):
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        client = bigquery.Client(credentials=credentials, project=project_id)
    else:
        client = bigquery.Client(project=project_id)
    
    # Référence à la table
    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    
    # Configuration du job
    job_config = bigquery.LoadJobConfig(
        schema=schemas[table_id],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Supprime et remplace toutes les données
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=False,
    )
    
    # Convertir les datetime en ISO string
    for record in data:
        for key, value in record.items():
            if isinstance(value, datetime):
                record[key] = value.isoformat()
    
    # Upload
    try:
        job = client.load_table_from_json(data, table_ref, job_config=job_config)
        job.result()  # Attendre la fin
        
        table = client.get_table(table_ref)
        print(f"  ✓ Upload réussi: {len(data)} lignes → {table.num_rows} lignes totales")
        
    except Exception as e:
        print(f"  ❌ Erreur d'upload: {e}")


def main():
    """Script principal"""
    
    print("=" * 80)
    print("LINKEDIN STATISTICS → BIGQUERY")
    print("=" * 80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 1. Charger la configuration
    print("📋 Chargement de la configuration...")
    is_cloud = os.getenv('CLOUD_RUN_JOB') is not None or os.getenv('FUNCTION_TARGET') is not None
    _config_path = '/app/config.yaml' if is_cloud else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_epbs.yaml')
    config = load_config(_config_path, skip_credentials_check=is_cloud)
    
    linkedin_config = config.config['linkedin']
    ACCESS_TOKEN = linkedin_config['oauth']['access_token']
    ORGANIZATION_ID = "15092687"  # Organisation avec des données de content statistics
    
    # Configuration BigQuery
    PROJECT_ID = "ecoledesponts"
    DATASET_ID = "linkedin_page"
    CREDENTIALS_PATH = "account-key.json"
    
    print(f"  ✓ Organization: {ORGANIZATION_ID}")
    print(f"  ✓ BigQuery: {PROJECT_ID}.{DATASET_ID}")
    
    # 2. Initialiser le collecteur
    print("\n🔗 Connexion à LinkedIn API...")
    collector = LinkedInStatsCollector(ACCESS_TOKEN, ORGANIZATION_ID)
    
    # 3. Récupérer les données
    print("\n" + "=" * 80)
    print("COLLECTE DES DONNÉES")
    print("=" * 80)

    # Toutes les données
    follower_stats = collector.get_follower_statistics()
    page_stats = collector.get_page_statistics()
    content_stats = collector.get_content_statistics()

    # Time series - commentées pour éviter les doublons
    # followers_ts = collector.get_follower_statistics_timeseries()
    # page_stats_ts = collector.get_page_statistics_timeseries()

    # 4. Sauvegarder en JSON (optionnel - pour debug)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Sauvegarder toutes les données
    if follower_stats:
        with open(f'followers_stats_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump(follower_stats, f, indent=2, ensure_ascii=False, default=str)
        print(f"\n💾 Sauvegarde: followers_stats_{timestamp}.json")

    if page_stats:
        with open(f'page_stats_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump(page_stats, f, indent=2, ensure_ascii=False, default=str)
        print(f"💾 Sauvegarde: page_stats_{timestamp}.json")

    if content_stats:
        with open(f'content_stats_{timestamp}.json', 'w', encoding='utf-8') as f:
            json.dump(content_stats, f, indent=2, ensure_ascii=False, default=str)
        print(f"💾 Sauvegarde: content_stats_{timestamp}.json")

    # Time series - commentées pour éviter les doublons
    # if followers_ts:
    #     with open(f'followers_timeseries_{timestamp}.json', 'w', encoding='utf-8') as f:
    #         json.dump(followers_ts, f, indent=2, ensure_ascii=False, default=str)
    #     print(f"💾 Sauvegarde: followers_timeseries_{timestamp}.json")

    # if page_stats_ts:
    #     with open(f'page_statistics_timeseries_{timestamp}.json', 'w', encoding='utf-8') as f:
    #         json.dump(page_stats_ts, f, indent=2, ensure_ascii=False, default=str)
    #     print(f"💾 Sauvegarde: page_statistics_timeseries_{timestamp}.json")

    # 5. Upload vers BigQuery
    print("\n" + "=" * 80)
    print("UPLOAD VERS BIGQUERY")
    print("=" * 80)

    # Uploader toutes les données
    upload_to_bigquery(follower_stats, 'followers', PROJECT_ID, DATASET_ID, CREDENTIALS_PATH)
    upload_to_bigquery(page_stats, 'page_statistics', PROJECT_ID, DATASET_ID, CREDENTIALS_PATH)
    upload_to_bigquery(content_stats, 'content_statistics', PROJECT_ID, DATASET_ID, CREDENTIALS_PATH)

    # Time series - commentées pour éviter les doublons
    # upload_to_bigquery(followers_ts, 'followers_timeseries', PROJECT_ID, DATASET_ID, CREDENTIALS_PATH)
    # upload_to_bigquery(page_stats_ts, 'page_statistics_timeseries', PROJECT_ID, DATASET_ID, CREDENTIALS_PATH)

    # 6. Résumé
    print("\n" + "=" * 80)
    print("✓ SYNCHRONISATION TERMINÉE")
    print("=" * 80)
    print(f"\nRésumé:")
    print(f"  • Followers: {len(follower_stats)} enregistrements")
    print(f"  • Page Statistics: {len(page_stats)} enregistrements")
    print(f"  • Content Statistics: {len(content_stats)} enregistrements")
    # print(f"  • Followers Timeseries: {len(followers_ts)} enregistrements")
    # print(f"  • Page Statistics Timeseries: {len(page_stats_ts)} enregistrements")


if __name__ == '__main__':
    main()
