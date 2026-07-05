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
        rowcount: int = 100,
        min_date: Optional[str] = None,
        max_date: Optional[str] = None
    ) -> List[Dict]:
        """Récupère TOUS les annonceurs et annonces pour un mot-clé via pagination complète.
        Aucun filtre sur le spend — on veut chaque annonceur qui se positionne sur ce terme.
        """
        endpoint = f"{self.BASE_URL}/getTermAdHistoryWithStats"

        if not max_date:
            max_date = datetime.now().strftime("%Y-%m-%d")
        if not min_date:
            min_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

        headers = {"Accept": "application/json"}
        all_ads = []
        seen_ad_ids = set()
        starting_row = 1

        print(f"\n🔍 Récupération complète pour '{keyword}' ({min_date} à {max_date})...")

        while True:
            params = {
                "Term": keyword,
                "countryCode": country_code,
                "rowcount": rowcount,
                "startingRow": starting_row,
                "minDate": min_date,
                "maxDate": max_date,
                "api_key": self.api_key
            }
            if domain:
                params["domain"] = domain

            try:
                response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
                response.raise_for_status()
                data = response.json()

                page_ads = []

                # Extraire depuis "domains" (structure principale)
                if data.get("domains"):
                    for domain_data in data["domains"]:
                        page_ads.extend(domain_data.get("ads", []))

                # Fusionner avec "topAds" (peut contenir des ads absentes de "domains")
                if data.get("topAds"):
                    for ad in data["topAds"]:
                        ad_id = ad.get("adId")
                        if ad_id not in seen_ad_ids:
                            page_ads.append(ad)

                # Dédupliquer par adId sur cette page
                new_ads = []
                for ad in page_ads:
                    ad_id = ad.get("adId")
                    if ad_id not in seen_ad_ids:
                        seen_ad_ids.add(ad_id)
                        new_ads.append(ad)

                if not new_ads:
                    break

                all_ads.extend(new_ads)
                print(f"  Page {starting_row}: {len(new_ads)} nouvelles annonces")

                total = data.get("resultCount")
                if total is not None and len(all_ads) >= total:
                    break

                if len(page_ads) < rowcount:
                    break

                starting_row += rowcount

            except requests.exceptions.RequestException as e:
                print(f"   ✗ Erreur API pour '{keyword}' (ligne {starting_row}): {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"   Détails: {e.response.text}")
                break

        if not all_ads:
            print(f"   ⚠️  Aucune annonce trouvée pour '{keyword}'")

        print(f"   ✓ {len(all_ads)} annonces récupérées pour '{keyword}'")
        return all_ads

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

    def collect_keywords(
        self,
        keywords: List[str],
        country_code: str = "US",
        rowcount: int = 100,
        min_date: Optional[str] = None,
        max_date: Optional[str] = None
    ) -> List[Dict]:
        """Collecte les données pour tous les mots-clés

        Returns:
            List[Dict] - Toutes les annonces
        """
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

            # Parser les annonces
            for ad in raw_ads:
                parsed = self.parse_ad_data(ad, keyword, country_code, source="api")
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

            # Filtrer les lignes avec keyword NULL (champ requis)
            initial_count = len(df)
            df = df.dropna(subset=['keyword'])
            filtered_count = initial_count - len(df)

            if filtered_count > 0:
                print(f"⚠️  {filtered_count} ligne(s) filtrée(s) (champ keyword null)")

            if len(df) == 0:
                print(f"⚠️  Aucune donnée valide à uploader après filtrage")
                return

            # Conversion selon le schéma BigQuery
            # Pour term_ad_history, tout en float64 pour éviter les problèmes
            numeric_cols = ['average_position', 'position', 'average_ad_count', 'leaderboard_count',
                           'percentage_ads_served', 'ad_id', 'search_date_id', 'ad_count']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce').astype('float64')

            # Conversion des booléens
            bool_cols = ['is_leaderboard_ad']
            for col in bool_cols:
                if col in df.columns:
                    df[col] = df[col].fillna(False).astype(bool)

            # Conversion des colonnes texte (ne pas essayer de convertir en numérique)
            text_cols = ['keyword', 'domain_name', 'title', 'body', 'full_url', 'term', 'source', 'country_code']
            for col in text_cols:
                if col in df.columns:
                    # Utiliser une approche plus robuste pour les NaN et None
                    df[col] = df[col].astype(object).where(df[col].notna(), None)
                    df[col] = df[col].apply(lambda x: str(x) if x is not None else None)

            # Gérer les colonnes datetime
            date_columns = ['retrieved_at', 'first_seen_date', 'last_seen_date']
            for col in date_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], utc=True, errors='coerce')

            # S'assurer que toutes les colonnes ont des types compatibles Parquet
            for col in df.columns:
                # Convertir les colonnes object qui ne sont ni texte ni datetime
                if df[col].dtype == 'object' and col not in text_cols + date_columns:
                    # Essayer de détecter et convertir les types appropriés
                    if df[col].notna().any():
                        first_valid = df[col].dropna().iloc[0] if len(df[col].dropna()) > 0 else None
                        if isinstance(first_valid, (int, float)):
                            df[col] = pd.to_numeric(df[col], errors='coerce')
                        else:
                            df[col] = df[col].astype(str).replace('nan', None)

            print(f"📤 Upload de {len(df)} lignes vers {project_id}.{dataset_id}.{table_id}...")

            pandas_gbq.to_gbq(
                df,
                destination_table=f"{dataset_id}.{table_id}",
                project_id=project_id,
                credentials=credentials,
                if_exists='append',
                progress_bar=False,
                table_schema=None  # Ne pas forcer le schéma, laisser BigQuery gérer
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
    # Essayer d'abord spyfu.global.country_code, puis spyfu.country_code, par défaut US
    COUNTRY_CODE = spyfu_config.get('global', {}).get('country_code') or spyfu_config.get('country_code', 'US')

    # Charger la configuration de term_ad_history
    # Dans le YAML, term_ad_history est directement sous spyfu:
    # Le config_loader devrait le placer directement dans spyfu_config
    
    # Debug: voir TOUTES les clés et leurs types
    print(f"\n🔍 Debug configuration:")
    print(f"   Keys dans spyfu_config: {list(spyfu_config.keys())}")
    for key in spyfu_config.keys():
        val = spyfu_config[key]
        print(f"   - {key}: {type(val).__name__} = {val if not isinstance(val, (dict, list)) or len(str(val)) < 100 else f'{type(val).__name__} avec {len(val)} items'}")
    
    # Essayer de lire term_ad_history directement
    term_ad_config = spyfu_config.get('term_ad_history', {})
    
    if term_ad_config:
        print(f"\n   ✓ term_ad_history trouvé!")
        print(f"   Keys: {list(term_ad_config.keys()) if isinstance(term_ad_config, dict) else 'NOT A DICT'}")
        if isinstance(term_ad_config, dict):
            print(f"   Nombre de keywords: {len(term_ad_config.get('keywords', []))}")
    
    # ROWCOUNT - utiliser page_size depuis la config si disponible, sinon 100 (pagination complète)
    ROWCOUNT = term_ad_config.get('page_size', 100) if isinstance(term_ad_config, dict) else 100

    # Dates - utiliser les dates de la config si disponibles, sinon 90 jours par défaut
    if 'end_date' in term_ad_config:
        MAX_DATE = term_ad_config['end_date']
    else:
        MAX_DATE = datetime.now().strftime("%Y-%m-%d")
    
    if 'start_date' in term_ad_config:
        MIN_DATE = term_ad_config['start_date']
    else:
        MIN_DATE = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

    # Charger les keywords depuis la configuration
    # D'abord essayer dans term_ad_history.keywords, puis fallback vers spyfu.keywords
    KEYWORDS = term_ad_config.get('keywords', [])
    
    # Si pas de keywords dans term_ad_history, essayer au niveau spyfu
    if not KEYWORDS:
        KEYWORDS = spyfu_config.get('keywords', [])

    if not KEYWORDS:
        print("⚠️  Aucun keyword configuré dans spyfu.term_ad_history.keywords ou spyfu.keywords")
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

    ads_data = collector.collect_keywords(
        keywords=KEYWORDS,
        country_code=COUNTRY_CODE,
        rowcount=ROWCOUNT,
        min_date=MIN_DATE,
        max_date=MAX_DATE
    )

    print(f"\n✓ Total: {len(ads_data)} annonces collectées")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Sauvegarder les annonces
    json_filename = f"spyfu_term_ad_history_{timestamp}.json"
    collector.export_to_json(ads_data, json_filename)
    print(f"✓ Annonces sauvegardées: ../data/{json_filename}")

    print("\n📤 Upload vers BigQuery...")

    # Upload des annonces vers term_ad_history
    collector.upload_to_bigquery(
        data=ads_data,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="term_ad_history",
        credentials_path=CREDENTIALS_PATH
    )
    
    print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
