#!/usr/bin/env python3
"""
SpyFu Top Pages Collector
Récupère les pages les plus performantes en SEO pour une liste de domaines
"""

import os
import json
import requests
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account


class SpyFuTopPagesCollector:
    """Collecteur des meilleures pages SEO depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/seo_api/v2/seo"

    # Domaines à analyser (à personnaliser)
    DOMAINS = [
        "example.com",
        "competitor1.com",
        "competitor2.com"
    ]

    # Paramètres par défaut
    DEFAULT_PARAMS = {
        "countryCode": "FR",
        "pageSize": 10000,
        "startingRow": 1,
        "sortBy": "EstMonthlySeoClicks",
        "sortOrder": "Descending",
        "adultFilter": True
    }

    def __init__(self, api_key: str):
        """
        Initialise le collecteur SpyFu

        Args:
            api_key: Clé API SpyFu (Secret Key)
        """
        self.api_key = api_key
        self.session = requests.Session()

    def get_top_pages(
        self,
        domain: str,
        country_code: str = "FR",
        page_size: int = 1000,
        min_seo_clicks: Optional[int] = None,
        search_type: Optional[str] = None,
        keyword_filter: Optional[str] = None,
        sort_by: str = "EstMonthlySeoClicks"
    ) -> List[Dict]:
        """
        Récupère les pages les plus performantes en SEO pour un domaine

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, DE, GB, FR, etc.)
            page_size: Nombre de résultats par page (max 10000)
            min_seo_clicks: Nombre minimum de clics SEO mensuels
            search_type: Type de recherche (optionnel)
            keyword_filter: Filtre sur les mots-clés (optionnel)
            sort_by: Tri (EstMonthlySeoClicks, KeywordCount, etc.)

        Returns:
            Liste des pages avec leurs métriques SEO
        """
        endpoint = f"{self.BASE_URL}/getTopPages"

        params = {
            "query": domain,
            "countryCode": country_code,
            "pageSize": min(page_size, 10000),
            "startingRow": 1,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "adultFilter": True,
            "api_key": self.api_key
        }

        # Filtres optionnels
        if min_seo_clicks:
            params["seoClicks.min"] = min_seo_clicks
        if search_type:
            params["searchType"] = search_type
        if keyword_filter:
            params["keywordFilter"] = keyword_filter

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"📄 Récupération des top pages pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            pages = data.get("results", [])

            print(f"✓ {len(pages)} pages récupérées pour {domain}")
            return pages

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    def parse_page_data(self, page_data: Dict, domain: str, country_code: str) -> Dict:
        """
        Parse les données d'une page au format BigQuery

        Args:
            page_data: Données brutes de la page depuis l'API
            domain: Domaine analysé
            country_code: Code pays

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        return {
            # Identifiants
            "domain": domain,
            "url": page_data.get("url"),
            "title": page_data.get("title"),

            # Métriques de la page
            "keyword_count": page_data.get("keywordCount"),
            "est_monthly_seo_clicks": page_data.get("estMonthlySeoClicks"),

            # Top keyword de la page
            "top_keyword": page_data.get("topKeyword"),
            "top_keyword_position": page_data.get("topKeywordPosition"),
            "top_keyword_search_volume": page_data.get("topKeywordSearchVolume"),
            "top_keyword_clicks": page_data.get("topKeywordClicks"),

            # Métadonnées
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_all_domains(
        self,
        domains: Optional[List[str]] = None,
        country_code: str = "FR",
        min_seo_clicks: Optional[int] = None
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines (utilise self.DOMAINS si None)
            country_code: Code pays
            min_seo_clicks: Nombre minimum de clics SEO mensuels

        Returns:
            Liste de toutes les pages formatées
        """
        domains = domains or self.DOMAINS
        all_pages = []

        for domain in domains:
            raw_pages = self.get_top_pages(
                domain=domain,
                country_code=country_code,
                min_seo_clicks=min_seo_clicks
            )

            for page in raw_pages:
                parsed = self.parse_page_data(page, domain, country_code)
                all_pages.append(parsed)

        return all_pages

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données en JSON"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return

        filepath = f"../data/{filename}"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)

        print(f"✓ Données exportées: {filepath}")

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
        table_id: str = "top_pages",
        credentials_path: str = "../../../account-key.json"
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
            credentials = service_account.Credentials.from_service_account_file(
                credentials_path,
                scopes=["https://www.googleapis.com/auth/bigquery"]
            )

            # Convertir en DataFrame
            df = pd.DataFrame(data)

            # Conversion des types pour BigQuery
            for col in df.columns:
                if df[col].dtype == 'object':
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except (ValueError, TypeError):
                        pass

            # Gérer les colonnes datetime
            if 'retrieved_at' in df.columns:
                df['retrieved_at'] = pd.to_datetime(df['retrieved_at'])

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
    import sys

    # Configuration
    API_KEY = "HE3RS5GP"
    PROJECT_ID = "clean-avatar-466709-a0"

    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_top_pages.py upload <json_filename>")
            print("Exemple: python spyfu_top_pages.py upload spyfu_top_pages_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("=" * 60)
        print("SpyFu Top Pages - Upload depuis JSON")
        print("=" * 60)

        collector = SpyFuTopPagesCollector(api_key=API_KEY)

        # Charger depuis JSON
        pages_data = collector.load_from_json(json_filename)

        if pages_data:
            # Upload vers BigQuery
            collector.upload_to_bigquery(
                data=pages_data,
                project_id=PROJECT_ID
            )
            print("\n✓ Upload terminé")
        else:
            print("\n✗ Aucune donnée à uploader")

    else:
        # Mode collection normal
        # Domaines à analyser (à personnaliser)
        DOMAINS = [
            "essca.eu"
        ]

        # Initialiser le collecteur
        collector = SpyFuTopPagesCollector(api_key=API_KEY)
        collector.DOMAINS = DOMAINS

        # Collecter les données
        print("=" * 60)
        print("SpyFu Top Pages Collection")
        print("=" * 60)

        pages_data = collector.collect_all_domains(
            country_code="FR",
            min_seo_clicks=50  # Optionnel: filtrer par clics SEO minimum
        )

        print(f"\n✓ Total: {len(pages_data)} pages collectées")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_top_pages_{timestamp}.json"
        collector.export_to_json(pages_data, json_filename)

        # Demander confirmation avant upload BigQuery
        print(f"\n✓ Données sauvegardées: ../data/{json_filename}")
        print("\n📤 Uploader maintenant vers BigQuery ? [y/n]")
        choice = input("Choix: ").strip().lower()

        if choice == 'y':
            collector.upload_to_bigquery(
                data=pages_data,
                project_id=PROJECT_ID
            )
            print("\n✓ Collection et upload terminés")
        else:
            print(f"\n✓ Pour uploader plus tard:")
            print(f"   python spyfu_top_pages.py upload {json_filename}")


if __name__ == "__main__":
    main()
