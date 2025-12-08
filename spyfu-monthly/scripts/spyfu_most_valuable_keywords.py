#!/usr/bin/env python3
"""
SpyFu Most Valuable Keywords Collector
Récupère les mots-clés SEO les plus précieux pour une liste de domaines
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

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class SpyFuMostValuableCollector:
    """Collecteur de mots-clés SEO les plus précieux depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/serp_api/v2/seo"

    def __init__(self, api_key: str):
        """
        Initialise le collecteur SpyFu

        Args:
            api_key: Clé API SpyFu (Secret Key)
        """
        self.api_key = api_key
        self.session = requests.Session()

    def get_most_valuable_keywords(
        self,
        domain: str,
        country_code: str = "US",
        rowcount: int = 25,
        min_search_volume: Optional[int] = None,
        sort_by: str = "SearchVolume"
    ) -> List[Dict]:
        """
        Récupère les mots-clés SEO les plus précieux pour un domaine

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, FR, GB, etc.)
            rowcount: Nombre de résultats (max 25 selon budget)
            min_search_volume: Volume de recherche minimum
            sort_by: Tri (SearchVolume, KeywordDifficulty, etc.)

        Returns:
            Liste des mots-clés avec leurs métriques
        """
        endpoint = f"{self.BASE_URL}/getMostValuableKeywords"

        params = {
            "Query": domain,  # API utilise Query au lieu de domain
            "countryCode": country_code,
            "rowcount": rowcount,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "api_key": self.api_key
        }

        # Filtres optionnels
        if min_search_volume:
            params["searchVolume.min"] = min_search_volume

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"💎 Récupération des keywords les plus précieux pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            keywords = data.get("results", [])

            print(f"✓ {len(keywords)} keywords précieux récupérés pour {domain}")
            return keywords

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    def parse_keyword_data(self, keyword_data: Dict, domain: str, country_code: str) -> Dict:
        """
        Parse les données d'un mot-clé au format BigQuery

        Args:
            keyword_data: Données brutes du mot-clé depuis l'API
            domain: Domaine analysé
            country_code: Code pays

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        return {
            # Identifiants
            "domain": domain,
            "keyword": keyword_data.get("keyword"),

            # Ranking
            "top_ranked_url": keyword_data.get("topRankedUrl"),
            "rank": keyword_data.get("rank"),
            "rank_change": keyword_data.get("rankChange"),

            # Métriques de recherche
            "search_volume": keyword_data.get("searchVolume"),
            "keyword_difficulty": keyword_data.get("keywordDifficulty"),

            # CPC par match type
            "broad_cost_per_click": keyword_data.get("broadCostPerClick"),
            "phrase_cost_per_click": keyword_data.get("phraseCostPerClick"),
            "exact_cost_per_click": keyword_data.get("exactCostPerClick"),

            # Métriques SEO
            "seo_clicks": keyword_data.get("seoClicks"),
            "seo_clicks_change": keyword_data.get("seoClicksChange"),
            "total_monthly_clicks": keyword_data.get("totalMonthlyClicks"),

            # Pourcentages de recherche
            "percent_mobile_searches": keyword_data.get("percentMobileSearches"),
            "percent_desktop_searches": keyword_data.get("percentDesktopSearches"),
            "percent_not_clicked": keyword_data.get("percentNotClicked"),
            "percent_paid_clicks": keyword_data.get("percentPaidClicks"),
            "percent_organic_clicks": keyword_data.get("percentOrganicClicks"),

            # Coûts mensuels par match type
            "broad_monthly_cost": keyword_data.get("broadMonthlyCost"),
            "phrase_monthly_cost": keyword_data.get("phraseMonthlyCost"),
            "exact_monthly_cost": keyword_data.get("exactMonthlyCost"),

            # Métriques de compétition
            "paid_competitors": keyword_data.get("paidCompetitors"),
            "ranking_homepages": keyword_data.get("rankingHomepages"),

            # Métadonnées
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_all_domains(
        self,
        domains: List[str],
        country_code: str = "US",
        rowcount: int = 25,
        min_search_volume: Optional[int] = None
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines à analyser
            country_code: Code pays
            rowcount: Nombre de résultats par domaine
            min_search_volume: Volume de recherche minimum

        Returns:
            Liste de tous les mots-clés formatés
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")

        all_keywords = []

        for domain in domains:
            raw_keywords = self.get_most_valuable_keywords(
                domain=domain,
                country_code=country_code,
                rowcount=rowcount,
                min_search_volume=min_search_volume
            )

            for kw in raw_keywords:
                parsed = self.parse_keyword_data(kw, domain, country_code)
                all_keywords.append(parsed)

        return all_keywords

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données en JSON"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return

        # Skip export en Cloud Functions
        if os.getenv('FUNCTION_TARGET'):
            return

        filepath = f"../data/{filename}"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)

    def load_from_json(self, filename: str) -> List[Dict]:
        """
        Charge les données depuis un fichier JSON

        Args:
            filename: Nom du fichier JSON (dans ../data/)

        Returns:
            Liste des données
        """
        filepath = f"../data/{filename}"

        if not os.path.exists(filepath):
            print(f"✗ Fichier non trouvé: {filepath}")
            return []

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"✓ {len(data)} lignes chargées depuis {filepath}")
        return data

    def upload_to_bigquery(
        self,
        data: List[Dict],
        project_id: str,
        dataset_id: str = "spyfu",
        table_id: str = "most_valuable_keywords",
        credentials_path: str = "../../account-key.json"
    ):
        """
        Upload les données vers BigQuery

        Args:
            data: Données à uploader
            project_id: ID du projet GCP
            dataset_id: ID du dataset BigQuery
            table_id: ID de la table
            credentials_path: Chemin vers les credentials GCP
        """
        if not data:
            print(f"⚠️  Aucune donnée à uploader")
            return

        try:
            # Préparer les credentials
            if os.getenv('FUNCTION_TARGET'):
                credentials = None
            elif credentials_path and os.path.exists(credentials_path):
                credentials = service_account.Credentials.from_service_account_file(
                    credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
            else:
                credentials = None

            # Convertir en DataFrame
            df = pd.DataFrame(data)

            # Filtrer les lignes avec domain NULL
            initial_count = len(df)
            df = df.dropna(subset=['domain'])
            filtered_count = initial_count - len(df)

            if filtered_count > 0:
                print(f"⚠️  {filtered_count} ligne(s) filtrée(s) (champ domain null)")

            if len(df) == 0:
                print(f"⚠️  Aucune donnée valide à uploader après filtrage")
                return

            # Conversion des types pour BigQuery
            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except (ValueError, TypeError):
                        df[col] = df[col].astype(str)
                        df[col] = df[col].replace('None', None)

            # Gérer les colonnes datetime
            if 'retrieved_at' in df.columns:
                df['retrieved_at'] = pd.to_datetime(df['retrieved_at'], utc=True)

            table_full_id = f"{project_id}.{dataset_id}.{table_id}"

            print(f"📤 Upload de {len(df)} lignes vers {table_full_id}...")

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

    # Charger la configuration
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config = load_config(skip_credentials_check=is_cloud_function)

    # Récupérer les configurations
    spyfu_config = config.get_spyfu_config()
    google_config = config.get_google_cloud_config()

    API_KEY = spyfu_config['api_key']
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['spyfu']
    CREDENTIALS_PATH = google_config['credentials_file']
    COUNTRY_CODE = spyfu_config.get('country_code', 'US')

    # Paramètres depuis le fichier .odt
    ROWCOUNT = 25  # Selon le document .odt

    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_most_valuable_keywords.py upload <json_filename>")
            sys.exit(1)

        json_filename = sys.argv[2]
        print("SpyFu Most Valuable Keywords - Upload depuis JSON")

        collector = SpyFuMostValuableCollector(api_key=API_KEY)
        keywords_data = collector.load_from_json(json_filename)

        if keywords_data:
            collector.upload_to_bigquery(
                data=keywords_data,
                project_id=PROJECT_ID,
                dataset_id=DATASET_ID,
                credentials_path=CREDENTIALS_PATH
            )
            print("\n✓ Upload terminé")
        else:
            print("\n✗ Aucune donnée à uploader")

    else:
        # Mode collection normal
        DOMAINS = spyfu_config['domains']['all']

        print(f"SpyFu Most Valuable Keywords Collection")
        print(f"📍 Pays: {COUNTRY_CODE}")
        print(f"🌐 Domaines: {', '.join(DOMAINS)}")
        print(f"📊 Rowcount: {ROWCOUNT} par domaine")

        # Initialiser le collecteur
        collector = SpyFuMostValuableCollector(api_key=API_KEY)

        # Collecter les données
        keywords_data = collector.collect_all_domains(
            domains=DOMAINS,
            country_code=COUNTRY_CODE,
            rowcount=ROWCOUNT
        )

        print(f"\n✓ Total: {len(keywords_data)} keywords précieux collectés")

        # Exporter en JSON
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_most_valuable_keywords_{timestamp}.json"
        collector.export_to_json(keywords_data, json_filename)
        print(f"✓ Données sauvegardées: ../data/{json_filename}")

        # Upload vers BigQuery
        print("\n📤 Upload vers BigQuery...")
        collector.upload_to_bigquery(
            data=keywords_data,
            project_id=PROJECT_ID,
            dataset_id=DATASET_ID,
            credentials_path=CREDENTIALS_PATH
        )
        print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
