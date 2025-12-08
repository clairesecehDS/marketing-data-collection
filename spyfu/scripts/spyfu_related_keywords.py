#!/usr/bin/env python3
"""
SpyFu Related Keywords Collector
Récupère les mots-clés associés pour une liste de mots-clés
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class SpyFuRelatedKeywordsCollector:
    """Collecteur de mots-clés associés depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/keyword_api/v2/related"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()

    def get_related_keywords(
        self,
        keyword: str,
        country_code: str = "US",
        rowcount: int = 11,
        sort_by: str = "SearchVolume"
    ) -> List[Dict]:
        """Récupère les mots-clés associés pour un mot-clé"""
        endpoint = f"{self.BASE_URL}/getRelatedKeywords"

        params = {
            "Query": keyword,  # L'API utilise "Query" pas "keyword"
            "countryCode": country_code,
            "rowcount": rowcount,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "api_key": self.api_key
        }

        headers = {"Accept": "application/json"}

        try:
            print(f"🔗 Récupération des mots-clés associés pour '{keyword}'...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            related = data.get("results", [])

            print(f"✓ {len(related)} mots-clés associés récupérés pour '{keyword}'")
            return related

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour '{keyword}': {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    def parse_keyword_data(self, keyword_data: Dict, source_keyword: str, country_code: str) -> Dict:
        """Parse les données d'un mot-clé au format BigQuery"""
        return {
            "source_keyword": source_keyword,
            "related_keyword": keyword_data.get("keyword"),
            "search_volume": keyword_data.get("searchVolume"),
            "ranking_difficulty": keyword_data.get("rankingDifficulty"),
            "broad_cost_per_click": keyword_data.get("broadCostPerClick"),
            "phrase_cost_per_click": keyword_data.get("phraseCostPerClick"),
            "exact_cost_per_click": keyword_data.get("exactCostPerClick"),
            "paid_competitors": keyword_data.get("paidCompetitors"),
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_keywords(
        self,
        keywords: List[str],
        country_code: str = "US",
        rowcount: int = 11
    ) -> List[Dict]:
        """Collecte les données pour tous les mots-clés"""
        if not keywords:
            raise ValueError("La liste de mots-clés ne peut pas être vide")

        all_related = []

        for keyword in keywords:
            raw_keywords = self.get_related_keywords(
                keyword=keyword,
                country_code=country_code,
                rowcount=rowcount
            )

            for kw in raw_keywords:
                parsed = self.parse_keyword_data(kw, keyword, country_code)
                all_related.append(parsed)

        return all_related

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
        table_id: str = "related_keywords",
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

            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except (ValueError, TypeError):
                        df[col] = df[col].astype(str)
                        df[col] = df[col].replace('None', None)

            if 'retrieved_at' in df.columns:
                df['retrieved_at'] = pd.to_datetime(df['retrieved_at'], utc=True)

            print(f"📤 Upload de {len(df)} lignes vers {project_id}.{dataset_id}.{table_id}...")
            
            # Vérifier que toutes les colonnes requises sont présentes
            required_columns = ['source_keyword', 'related_keyword', 'search_volume', 'country_code', 'retrieved_at']
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Colonnes manquantes dans le DataFrame: {missing_columns}")
            
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

    ROWCOUNT = 11  # Selon le document .odt

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

    print(f"SpyFu Related Keywords Collection")
    print(f"📍 Pays: {COUNTRY_CODE}")
    print(f"🔑 {len(KEYWORDS)} mots-clés sources configurés")
    print(f"📊 Rowcount: {ROWCOUNT} par mot-clé")

    collector = SpyFuRelatedKeywordsCollector(api_key=API_KEY)

    related_data = collector.collect_keywords(
        keywords=KEYWORDS,
        country_code=COUNTRY_CODE,
        rowcount=ROWCOUNT
    )

    print(f"\n✓ Total: {len(related_data)} mots-clés associés collectés")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f"spyfu_related_keywords_{timestamp}.json"
    collector.export_to_json(related_data, json_filename)
    print(f"✓ Données sauvegardées: ../data/{json_filename}")

    print("\n📤 Upload vers BigQuery...")
    collector.upload_to_bigquery(
        data=related_data,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )
    print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
