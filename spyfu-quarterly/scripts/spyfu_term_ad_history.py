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
    ) -> List[Dict]:
        """Récupère l'historique des annonces pour un mot-clé"""
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
            print(f"🔍 Récupération de l'historique des annonces pour '{keyword}'...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            ads = data.get("results", [])

            print(f"✓ {len(ads)} annonces récupérées pour '{keyword}'")
            return ads

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour '{keyword}': {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    # Alias pour compatibilité
    def get_term_ad_history_with_stats(self, *args, **kwargs):
        """Alias pour get_term_ad_history"""
        return self.get_term_ad_history(*args, **kwargs)

    def parse_ad_data(self, ad_data: Dict, keyword: str, country_code: str) -> Dict:
        """Parse les données d'une annonce au format BigQuery"""
        return {
            "keyword": keyword,
            "domain": ad_data.get("domain"),
            "ad_id": ad_data.get("adId"),
            "headline": ad_data.get("headline"),
            "description": ad_data.get("description"),
            "display_url": ad_data.get("displayUrl"),
            "destination_url": ad_data.get("destinationUrl"),
            "first_seen_date": ad_data.get("firstSeenDate"),
            "last_seen_date": ad_data.get("lastSeenDate"),
            "days_seen": ad_data.get("daysSeen"),
            "search_volume": ad_data.get("searchVolume"),
            "cost_per_click": ad_data.get("costPerClick"),
            "position": ad_data.get("position"),
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
    ) -> List[Dict]:
        """Collecte les données pour tous les mots-clés"""
        if not keywords:
            raise ValueError("La liste de mots-clés ne peut pas être vide")

        all_ads = []

        for keyword in keywords:
            raw_ads = self.get_term_ad_history(
                keyword=keyword,
                country_code=country_code,
                rowcount=rowcount,
                min_date=min_date,
                max_date=max_date
            )

            for ad in raw_ads:
                parsed = self.parse_ad_data(ad, keyword, country_code)
                all_ads.append(parsed)

        return all_ads

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

    # Liste de mots-clés à surveiller (à configurer)
    KEYWORDS = [
        "travel security",
        "medical assistance",
        "crisis management"
    ]

    print(f"SpyFu Term Ad History Collection")
    print(f"📍 Pays: {COUNTRY_CODE}")
    print(f"🔑 Mots-clés: {', '.join(KEYWORDS)}")
    print(f"📊 Rowcount: {ROWCOUNT} par mot-clé")
    print(f"📅 Période: {MIN_DATE} à {MAX_DATE}")

    collector = SpyFuTermAdHistoryCollector(api_key=API_KEY)

    ads_data = collector.collect_keywords(
        keywords=KEYWORDS,
        country_code=COUNTRY_CODE,
        rowcount=ROWCOUNT,
        min_date=MIN_DATE,
        max_date=MAX_DATE
    )

    print(f"\n✓ Total: {len(ads_data)} annonces collectées")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f"spyfu_term_ad_history_{timestamp}.json"
    collector.export_to_json(ads_data, json_filename)
    print(f"✓ Données sauvegardées: ../data/{json_filename}")

    print("\n📤 Upload vers BigQuery...")
    collector.upload_to_bigquery(
        data=ads_data,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )
    print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
