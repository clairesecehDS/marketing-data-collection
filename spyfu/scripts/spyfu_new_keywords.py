#!/usr/bin/env python3
"""
SpyFu New Keywords Collector
Récupère les nouveaux mots-clés PPC pour une liste de domaines
"""

import os
import json
import requests
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account


class SpyFuNewKeywordsCollector:
    """Collecteur de nouveaux mots-clés PPC depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/keyword_api/v2/ppc"

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
        "sortBy": "SearchVolume",
        "sortOrder": "Descending"
    }

    def __init__(self, api_key: str):
        """
        Initialise le collecteur SpyFu

        Args:
            api_key: Clé API SpyFu (Secret Key)
        """
        self.api_key = api_key
        self.session = requests.Session()

    def get_new_keywords(
        self,
        domain: str,
        country_code: str = "FR",
        page_size: int = 1000,
        min_search_volume: Optional[int] = None,
        max_cost_per_click: Optional[float] = None,
        is_question: Optional[bool] = None,
        is_transactional: Optional[bool] = None
    ) -> List[Dict]:
        """
        Récupère les nouveaux mots-clés PPC pour un domaine

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, DE, GB, FR, etc.)
            page_size: Nombre de résultats par page (max 10000)
            min_search_volume: Volume de recherche minimum
            max_cost_per_click: CPC maximum
            is_question: Filtrer sur les questions (True/False)
            is_transactional: Filtrer sur l'intention transactionnelle

        Returns:
            Liste des nouveaux mots-clés avec leurs métriques
        """
        endpoint = f"{self.BASE_URL}/getNewKeywords"

        params = {
            "query": domain,
            "countryCode": country_code,
            "pageSize": min(page_size, 10000),
            "startingRow": 1,
            "sortBy": "SearchVolume",
            "sortOrder": "Descending",
            "api_key": self.api_key
        }

        # Filtres optionnels
        if min_search_volume:
            params["searchVolume.min"] = min_search_volume
        if max_cost_per_click:
            params["costPerClick.max"] = max_cost_per_click
        if is_question is not None:
            params["isQuestion"] = str(is_question).lower()
        if is_transactional is not None:
            params["isTransactionalIntent"] = str(is_transactional).lower()

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"🆕 Récupération des nouveaux keywords pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            keywords = data.get("results", [])

            print(f"✓ {len(keywords)} nouveaux keywords récupérés pour {domain}")
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
            "keyword": keyword_data.get("term"),

            # Métriques de recherche
            "search_volume": keyword_data.get("searchVolume"),
            "live_search_volume": keyword_data.get("liveSearchVolume"),
            "ranking_difficulty": keyword_data.get("rankingDifficulty"),
            "total_monthly_clicks": keyword_data.get("totalMonthlyClicks"),

            # Pourcentages de recherche
            "percent_mobile_searches": keyword_data.get("percentMobileSearches"),
            "percent_desktop_searches": keyword_data.get("percentDesktopSearches"),
            "percent_searches_not_clicked": keyword_data.get("percentSearchesNotClicked"),
            "percent_paid_clicks": keyword_data.get("percentPaidClicks"),
            "percent_organic_clicks": keyword_data.get("percentOrganicClicks"),

            # CPC par match type
            "broad_cost_per_click": keyword_data.get("broadCostPerClick"),
            "phrase_cost_per_click": keyword_data.get("phraseCostPerClick"),
            "exact_cost_per_click": keyword_data.get("exactCostPerClick"),

            # Clics mensuels par match type
            "broad_monthly_clicks": keyword_data.get("broadMonthlyClicks"),
            "phrase_monthly_clicks": keyword_data.get("phraseMonthlyClicks"),
            "exact_monthly_clicks": keyword_data.get("exactMonthlyClicks"),

            # Coûts mensuels par match type
            "broad_monthly_cost": keyword_data.get("broadMonthlyCost"),
            "phrase_monthly_cost": keyword_data.get("phraseMonthlyCost"),
            "exact_monthly_cost": keyword_data.get("exactMonthlyCost"),

            # Métriques de compétition
            "paid_competitors": keyword_data.get("paidCompetitors"),
            "distinct_competitors": keyword_data.get("distinctCompetitors"),
            "ranking_homepages": keyword_data.get("rankingHomepages"),

            # Informations SERP
            "serp_features_csv": keyword_data.get("serpFeaturesCsv"),
            "serp_first_result": keyword_data.get("serpFirstResult"),

            # Flags
            "is_question": keyword_data.get("isQuestion"),
            "is_not_safe_for_work": keyword_data.get("isNotSafeForWork"),

            # Métadonnées
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_all_domains(
        self,
        domains: Optional[List[str]] = None,
        country_code: str = "FR",
        min_search_volume: Optional[int] = None
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines (utilise self.DOMAINS si None)
            country_code: Code pays
            min_search_volume: Volume de recherche minimum

        Returns:
            Liste de tous les nouveaux mots-clés formatés
        """
        domains = domains or self.DOMAINS
        all_keywords = []

        for domain in domains:
            raw_keywords = self.get_new_keywords(
                domain=domain,
                country_code=country_code,
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
        table_id: str = "new_keywords",
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
            print("Usage: python spyfu_new_keywords.py upload <json_filename>")
            print("Exemple: python spyfu_new_keywords.py upload spyfu_new_keywords_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("=" * 60)
        print("SpyFu New Keywords - Upload depuis JSON")
        print("=" * 60)

        collector = SpyFuNewKeywordsCollector(api_key=API_KEY)

        # Charger depuis JSON
        keywords_data = collector.load_from_json(json_filename)

        if keywords_data:
            # Upload vers BigQuery
            collector.upload_to_bigquery(
                data=keywords_data,
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
        collector = SpyFuNewKeywordsCollector(api_key=API_KEY)
        collector.DOMAINS = DOMAINS

        # Collecter les données
        print("=" * 60)
        print("SpyFu New Keywords Collection")
        print("=" * 60)

        keywords_data = collector.collect_all_domains(
            country_code="FR",
            min_search_volume=100  # Optionnel: filtrer par volume minimum
        )

        print(f"\n✓ Total: {len(keywords_data)} nouveaux mots-clés collectés")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_new_keywords_{timestamp}.json"
        collector.export_to_json(keywords_data, json_filename)

        # Demander confirmation avant upload BigQuery
        print(f"\n✓ Données sauvegardées: ../data/{json_filename}")
        print("\n📤 Uploader maintenant vers BigQuery ? [y/n]")
        choice = input("Choix: ").strip().lower()

        if choice == 'y':
            collector.upload_to_bigquery(
                data=keywords_data,
                project_id=PROJECT_ID
            )
            print("\n✓ Collection et upload terminés")
        else:
            print(f"\n✓ Pour uploader plus tard:")
            print(f"   python spyfu_new_keywords.py upload {json_filename}")


if __name__ == "__main__":
    main()
