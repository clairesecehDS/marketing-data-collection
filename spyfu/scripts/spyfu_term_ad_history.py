#!/usr/bin/env python3
"""
SpyFu Term Ad History Collector
Récupère l'historique des annonces pour des mots-clés spécifiques
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class SpyFuTermAdHistoryCollector:
    """Collecteur d'historique des annonces par mot-clé depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/cloud_ad_history_api/v2/term"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()

    def get_term_ad_history(
        self,
        keyword: str,
        domain: Optional[str] = None,
        country_code: str = "US",
        rowcount: int = 7,
        min_date: Optional[str] = None,
        max_date: Optional[str] = None
    ) -> Dict:
        """Récupère l'historique des annonces pour un mot-clé
        
        Returns:
            Dict contenant:
                - 'ads': List[Dict] - Les annonces
                - 'domain_stats': List[Dict] - Les statistiques par domaine
        """
        endpoint = f"{self.BASE_URL}/getTermAdHistoryWithStats"

        if not max_date:
            max_date = datetime.now().strftime("%Y-%m-%d")
        if not min_date:
            min_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
        
        # L'API utilise directement le code pays en LETTRES (US, UK, CA, AU)
        # Pas besoin de conversion numérique contrairement à ce que la doc suggère

        params = {
            "Term": keyword,  # API utilise Term au lieu de keyword
            "countryCode": country_code,  # Code pays en LETTRES (US, UK, CA, AU)
            "rowcount": rowcount,
            "minDate": min_date,
            "maxDate": max_date,
            "api_key": self.api_key
        }

        if domain:
            params["domain"] = domain

        headers = {"Accept": "application/json"}

        try:
            print(f"\n🔍 Récupération de l'historique des annonces pour '{keyword}'...")
            print(f"   📡 Endpoint: {endpoint}")
            print(f"   📋 Paramètres:")
            print(f"      - Term: {params['Term']}")
            print(f"      - countryCode: {params['countryCode']}")
            print(f"      - rowcount: {params['rowcount']}")
            print(f"      - minDate: {params['minDate']}")
            print(f"      - maxDate: {params['maxDate']}")
            if domain:
                print(f"      - domain: {domain}")

            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)

            print(f"   🌐 Status Code: {response.status_code}")

            response.raise_for_status()

            data = response.json()

            # Log détaillé de la réponse
            print(f"   📦 Clés dans la réponse: {list(data.keys())}")

            # L'API retourne les annonces dans "topAds" ET dans "domains"
            # Structure: {"resultCount": N, "domains": [...], "topAds": [...]}

            ads = []
            domain_stats = []

            # Extraire les statistiques des domaines
            if "domains" in data and data["domains"]:
                print(f"   📊 {len(data['domains'])} domaines avec annonces")
                for domain_data in data["domains"]:
                    # Extraire les annonces du domaine
                    domain_ads = domain_data.get("ads", [])
                    ads.extend(domain_ads)
                    
                    # Extraire les statistiques du domaine
                    domain_stats.append({
                        "domain_name": domain_data.get("domainName"),
                        "budget": domain_data.get("budget"),
                        "coverage": domain_data.get("coverage"),
                        "percentage_leaderboard": domain_data.get("percentageLeaderboard"),
                        "total_ads_purchased": domain_data.get("totalAdsPurchased"),
                        "ad_count": domain_data.get("adCount")
                    })
                print(f"   📊 {len(ads)} annonces extraites des domaines")
                print(f"   📊 {len(domain_stats)} domaines avec statistiques")

            # Récupérer aussi depuis topAds si disponible
            if "topAds" in data and data["topAds"]:
                top_ads = data["topAds"]
                print(f"   📊 {len(top_ads)} annonces trouvées dans 'topAds'")
                # On privilégie topAds si ads est vide
                if not ads:
                    ads = top_ads

            # Debug si toujours vide
            if len(ads) == 0:
                print(f"   ⚠️  Réponse complète de l'API:")
                print(f"   {json.dumps(data, indent=2)[:1000]}")  # Premiers 1000 chars

            print(f"   ✓ {len(ads)} annonces récupérées pour '{keyword}'")
            return {"ads": ads, "domain_stats": domain_stats}

        except requests.exceptions.RequestException as e:
            print(f"   ✗ Erreur API pour '{keyword}': {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"   📄 Status: {e.response.status_code}")
                print(f"   📄 Détails: {e.response.text}")
            return {"ads": [], "domain_stats": []}

    # Alias pour compatibilité
    def get_term_ad_history_with_stats(self, *args, **kwargs):
        """Alias pour get_term_ad_history"""
        return self.get_term_ad_history(*args, **kwargs)

    def parse_ad_data(self, ad_data: Dict, keyword: str, country_code: str, source: str = "topAds") -> Dict:
        """
        Parse les données d'une annonce au format BigQuery
        Adapte les données au schéma de la table term_ad_history

        Args:
            ad_data: Données de l'annonce depuis l'API
            keyword: Keyword recherché
            country_code: Code pays
            source: Source des données ("topAds" ou "domains")
        """
        # Schéma complet de term_ad_history
        parsed_data = {
            "keyword": keyword,
            "ad_id": ad_data.get("adId"),
            "domain_name": ad_data.get("domainName"),
            "title": ad_data.get("title"),
            "body": ad_data.get("body"),
            "full_url": ad_data.get("fullUrl"),
            "term": ad_data.get("term"),
            "search_date_id": ad_data.get("searchDateId"),
            "average_position": ad_data.get("averagePosition"),
            "position": ad_data.get("position"),
            "average_ad_count": ad_data.get("averageAdCount"),
            "ad_count": ad_data.get("adCount"),
            "leaderboard_count": ad_data.get("leaderboardCount"),
            "percentage_leaderboard": ad_data.get("percentageLeaderboard"),
            "percentage_ads_served": ad_data.get("percentageAdsServed"),
            "is_leaderboard_ad": ad_data.get("isLeaderboardAd"),
            "source": source,
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }
        
        return parsed_data

    def parse_domain_stats(self, domain_stat: Dict, keyword: str, country_code: str) -> Dict:
        """
        Parse les statistiques d'un domaine au format BigQuery
        
        Args:
            domain_stat: Statistiques du domaine depuis l'API
            keyword: Keyword recherché
            country_code: Code pays
        """
        return {
            "keyword": keyword,
            "domain_name": domain_stat.get("domain_name"),
            "budget": domain_stat.get("budget"),
            "coverage": domain_stat.get("coverage"),
            "percentage_leaderboard": domain_stat.get("percentage_leaderboard"),
            "total_ads_purchased": domain_stat.get("total_ads_purchased"),
            "ad_count": domain_stat.get("ad_count"),
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_keywords(
        self,
        keywords: List[str],
        country_code: str = "US",
        rowcount: int = 7,
        min_date: Optional[str] = None,
        max_date: Optional[str] = None
    ) -> Dict[str, List[Dict]]:
        """Collecte les données pour tous les mots-clés
        
        Returns:
            Dict contenant:
                - 'ads': List[Dict] - Toutes les annonces
                - 'domain_stats': List[Dict] - Toutes les statistiques de domaines
        """
        if not keywords:
            raise ValueError("La liste de mots-clés ne peut pas être vide")

        all_ads = []
        all_domain_stats = []

        for keyword in keywords:
            result = self.get_term_ad_history(
                keyword=keyword,
                country_code=country_code,
                rowcount=rowcount,
                min_date=min_date,
                max_date=max_date
            )

            raw_ads = result.get("ads", [])
            raw_domain_stats = result.get("domain_stats", [])

            # Déterminer la source des annonces
            source = "domains" if raw_domain_stats else "topAds"

            # Parser les annonces
            for ad in raw_ads:
                parsed = self.parse_ad_data(ad, keyword, country_code, source=source)
                all_ads.append(parsed)

            # Parser les statistiques de domaines
            for domain_stat in raw_domain_stats:
                parsed = self.parse_domain_stats(domain_stat, keyword, country_code)
                all_domain_stats.append(parsed)

        return {"ads": all_ads, "domain_stats": all_domain_stats}

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données en JSON"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return

        if os.getenv('FUNCTION_TARGET'):
            return

        filepath = f"../data/{filename}"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)

    def upload_to_bigquery(
        self,
        data: List[Dict],
        project_id: str,
        dataset_id: str = "spyfu",
        table_id: str = "term_ad_history",
        credentials_path: str = "../../account-key.json"
    ):
        """Upload les données vers BigQuery"""
        if not data:
            print(f"⚠️  Aucune donnée à uploader")
            return

        try:
            if os.getenv('FUNCTION_TARGET'):
                credentials = None
            elif credentials_path and os.path.exists(credentials_path):
                credentials = service_account.Credentials.from_service_account_file(
                    credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
            else:
                credentials = None

            df = pd.DataFrame(data)

            # Conversion des types
            for col in df.columns:
                if df[col].dtype == 'object' and col not in ['first_seen_date', 'last_seen_date']:
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except (ValueError, TypeError):
                        df[col] = df[col].astype(str)
                        df[col] = df[col].replace('None', None)

            # Gérer les colonnes datetime
            date_columns = ['retrieved_at', 'first_seen_date', 'last_seen_date']
            for col in date_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], utc=True, errors='coerce')

            print(f"📤 Upload de {len(df)} lignes vers {project_id}.{dataset_id}.{table_id}...")

            pandas_gbq.to_gbq(
                df,
                destination_table=f"{dataset_id}.{table_id}",
                project_id=project_id,
                credentials=credentials,
                if_exists='append',
                progress_bar=False
            )

            print(f"✓ Upload réussi vers BigQuery")

        except Exception as e:
            print(f"✗ Erreur lors de l'upload BigQuery: {e}")


def main():
    """Point d'entrée principal"""
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config = load_config(skip_credentials_check=is_cloud_function)

    spyfu_config = config.get_spyfu_config()
    google_config = config.get_google_cloud_config()

    API_KEY = spyfu_config['api_key']
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['spyfu']
    CREDENTIALS_PATH = google_config['credentials_file']
    COUNTRY_CODE = spyfu_config.get('country_code', 'US')

    ROWCOUNT = 7  # Selon le document .odt

    MAX_DATE = datetime.now().strftime("%Y-%m-%d")
    MIN_DATE = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

    # Charger les keywords depuis la configuration
    KEYWORDS = spyfu_config.get('keywords', [])

    if not KEYWORDS:
        print("⚠️  Aucun keyword configuré dans spyfu.keywords")
        print("   Utilisation des keywords par défaut")
        KEYWORDS = [
            "travel security",
            "medical assistance",
            "crisis management"
        ]

    print(f"SpyFu Term Ad History Collection")
    print(f"📍 Pays: {COUNTRY_CODE}")
    print(f"🔑 {len(KEYWORDS)} mots-clés configurés")
    print(f"📊 Rowcount: {ROWCOUNT} par mot-clé")
    print(f"📅 Période: {MIN_DATE} à {MAX_DATE}")

    collector = SpyFuTermAdHistoryCollector(api_key=API_KEY)

    result = collector.collect_keywords(
        keywords=KEYWORDS,
        country_code=COUNTRY_CODE,
        rowcount=ROWCOUNT,
        min_date=MIN_DATE,
        max_date=MAX_DATE
    )

    ads_data = result["ads"]
    domain_stats_data = result["domain_stats"]

    print(f"\n✓ Total: {len(ads_data)} annonces collectées")
    print(f"✓ Total: {len(domain_stats_data)} statistiques de domaines collectées")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Sauvegarder les annonces
    json_filename = f"spyfu_term_ad_history_{timestamp}.json"
    collector.export_to_json(ads_data, json_filename)
    print(f"✓ Annonces sauvegardées: ../data/{json_filename}")
    
    # Sauvegarder les stats de domaines
    if domain_stats_data:
        domain_stats_filename = f"spyfu_term_domain_stats_{timestamp}.json"
        collector.export_to_json(domain_stats_data, domain_stats_filename)
        print(f"✓ Stats domaines sauvegardées: ../data/{domain_stats_filename}")

    print("\n📤 Upload vers BigQuery...")
    
    # Upload des annonces
    collector.upload_to_bigquery(
        data=ads_data,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="term_ad_history",
        credentials_path=CREDENTIALS_PATH
    )
    
    # Upload des stats de domaines si disponibles
    if domain_stats_data:
        collector.upload_to_bigquery(
            data=domain_stats_data,
            project_id=PROJECT_ID,
            dataset_id=DATASET_ID,
            table_id="term_domain_stats",
            credentials_path=CREDENTIALS_PATH
        )
    
    print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
