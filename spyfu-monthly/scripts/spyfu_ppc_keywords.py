#!/usr/bin/env python3
"""
SpyFu PPC Keywords Collector
Récupère les mots-clés PPC les plus performants pour une liste de domaines
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


class SpyFuPPCCollector:
    """Collecteur de données PPC depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/keyword_api/v2/ppc"



    # Paramètres par défaut (rowcount limité à 20 selon budget)
    DEFAULT_PARAMS = {
        "countryCode": "US",
        "pageSize": 20,
        "startingRow": 0,
        "sortBy": "SearchVolume",
        "sortOrder": "Descending"
    }

    def __init__(self, api_key: str):
        """
        Initialise le collecteur SpyFu

        Args:
            api_key: Clé API SpyFu
        """
        self.api_key = api_key
        self.session = requests.Session()

    def get_most_successful_keywords(
        self,
        domain: str,
        country_code: str = "US",
        page_size: int = 20,
        min_search_volume: Optional[int] = None,
        max_cost_per_click: Optional[float] = None
    ) -> List[Dict]:
        """
        Récupère les mots-clés PPC les plus performants pour un domaine

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, DE, GB, etc.)
            page_size: Nombre de résultats par page (max 20 selon budget)
            min_search_volume: Volume de recherche minimum
            max_cost_per_click: CPC maximum

        Returns:
            Liste des mots-clés avec leurs métriques
        """
        endpoint = f"{self.BASE_URL}/getMostSuccessful"

        params = {
            "query": domain,
            "countryCode": country_code,
            "pageSize": min(page_size, 20),  # Limité à 20 selon budget
            "startingRow": 1,  # SpyFu commence à 1, pas 0
            "sortBy": "SearchVolume",
            "sortOrder": "Descending"
        }

        # Filtres optionnels
        if min_search_volume:
            params["searchVolume.min"] = min_search_volume
        if max_cost_per_click:
            params["costPerClick.max"] = max_cost_per_click

        # SpyFu utilise Basic Auth avec la secret key
        headers = {
            "Accept": "application/json"
        }

        # Authentification via params (format SpyFu)
        params["api_key"] = self.api_key

        try:
            print(f"📊 Récupération des keywords pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            keywords = data.get("results", [])

            print(f"✓ {len(keywords)} keywords récupérés pour {domain}")
            return keywords

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain}: {e}")
            if hasattr(e.response, 'text'):
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
        domains: List[str],
        country_code: str = "US",
        min_search_volume: Optional[int] = None
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines à analyser
            country_code: Code pays
            min_search_volume: Volume de recherche minimum

        Returns:
            Liste de tous les mots-clés formatés
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")
        all_keywords = []

        for domain in domains:
            raw_keywords = self.get_most_successful_keywords(
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
        
        # Skip export en Cloud Functions
        if os.getenv('FUNCTION_TARGET'):
                return
        
        # Skip export en Cloud Functions
        if os.getenv('FUNCTION_TARGET'):
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
        table_id: str = "ppc_keywords",
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
            # En Cloud Functions, utiliser l'authentification par défaut
            if os.getenv('FUNCTION_TARGET'):
                credentials = None  # Utilise l'authentification par défaut
            elif credentials_path and os.path.exists(credentials_path):
                credentials = service_account.Credentials.from_service_account_file(
                    credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
            else:
                credentials = None

            # Convertir en DataFrame
            df = pd.DataFrame(data)

            # Filtrer uniquement les lignes avec domain NULL (requis par le schéma)
            initial_count = len(df)
            df = df.dropna(subset=['domain'])
            filtered_count = initial_count - len(df)

            if filtered_count > 0:
                print(f"⚠️  {filtered_count} ligne(s) filtrée(s) (champ domain null)")

            if len(df) == 0:
                print(f"⚠️  Aucune donnée valide à uploader après filtrage")
                return

            # Conversion des types pour BigQuery
            import json
            for col in df.columns:
                if df[col].dtype == 'object':
                    # Vérifier si la colonne contient des listes ou dicts
                    sample = df[col].dropna().iloc[0] if len(df[col].dropna()) > 0 else None
                    if isinstance(sample, (list, dict)):
                        # Convertir en JSON string
                        df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x)
                        df[col] = df[col].astype(str)
                    else:
                        # Pour les autres colonnes object, essayer de convertir en numérique
                        try:
                            df[col] = pd.to_numeric(df[col])
                        except (ValueError, TypeError):
                            # Garder comme string si conversion échoue
                            df[col] = df[col].astype(str)
                            # Remplacer 'None' string par None réel
                            df[col] = df[col].replace('None', None)

            # Gérer les colonnes datetime
            if 'retrieved_at' in df.columns:
                df['retrieved_at'] = pd.to_datetime(df['retrieved_at'], utc=True)

            # Convertir les colonnes INT64 (arrondir les FLOAT pour éviter erreur Parquet)
            int_columns = [
                'search_volume', 'total_monthly_clicks',
                'broad_monthly_clicks', 'phrase_monthly_clicks', 'exact_monthly_clicks',
                'paid_competitors', 'ranking_homepages'
            ]
            for col in int_columns:
                if col in df.columns:
                    df[col] = df[col].fillna(0).round().astype('Int64')

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
            print(f"\nTypes de colonnes:")
            for col in df.columns:
                print(f"  - {col}: {df[col].dtype}")
            print(f"\nPremière ligne (sample):")
            print(df.iloc[0] if len(df) > 0 else "Aucune donnée")
            import traceback
            traceback.print_exc()


def main():
    """Point d'entrée principal"""

    # Charger la configuration
    # Détecter Cloud Functions
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config = load_config(skip_credentials_check=is_cloud_function)

    # Récupérer les configurations
    spyfu_config = config.get_spyfu_config()
    google_config = config.get_google_cloud_config()
    ppc_config = spyfu_config['endpoints']['ppc_keywords']

    API_KEY = spyfu_config['api_key']
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config["datasets"]["spyfu"]
    CREDENTIALS_PATH = google_config["credentials_file"]
    DATASET_ID = google_config['datasets']['spyfu']
    CREDENTIALS_FILE = google_config['credentials_file']
    COUNTRY_CODE = spyfu_config.get('country_code', 'US')
    PAGE_SIZE = spyfu_config.get('page_size', 1000)

    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_ppc_keywords.py upload <json_filename>")
            print("Exemple: python spyfu_ppc_keywords.py upload spyfu_ppc_keywords_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("SpyFu PPC Keywords - Upload depuis JSON")

        collector = SpyFuPPCCollector(api_key=API_KEY)

        # Charger depuis JSON
        keywords_data = collector.load_from_json(json_filename)

        if keywords_data:
            # Upload vers BigQuery
            collector.upload_to_bigquery(
                data=keywords_data,
                project_id=PROJECT_ID,
                dataset_id=DATASET_ID,
                credentials_path=CREDENTIALS_FILE
            )
            print("\n✓ Upload terminé")
        else:
            print("\n✗ Aucune donnée à uploader")

    else:
        # Mode collection normal
        # Vérifier que le endpoint est activé
        if not ppc_config.get('enabled', True):
            print("⚠️  PPC Keywords endpoint désactivé dans la configuration")
            sys.exit(0)

        # Domaines depuis la configuration
        DOMAINS = spyfu_config['domains']['all']

        # Filtres depuis la configuration
        filters = ppc_config.get('filters', {})
        min_search_volume = filters.get('min_search_volume', spyfu_config['filters'].get('min_search_volume'))

        # Initialiser le collecteur
        collector = SpyFuPPCCollector(api_key=API_KEY)
        collector.DOMAINS = DOMAINS

        # Collecter les données
        print("SpyFu PPC Keywords Collection")
        print(f"📍 Pays: {COUNTRY_CODE}")
        print(f"🌐 Domaines: {', '.join(DOMAINS)}")
        print(f"🔍 Filtre volume min: {min_search_volume or 'Aucun'}")
    
        keywords_data = collector.collect_all_domains(
            domains=DOMAINS,
            country_code=COUNTRY_CODE,
            min_search_volume=min_search_volume
        )

        print(f"\n✓ Total: {len(keywords_data)} mots-clés collectés")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_ppc_keywords_{timestamp}.json"
        collector.export_to_json(keywords_data, json_filename)

        # Demander confirmation avant upload BigQuery
        print(f"\n✓ Données sauvegardées: ../data/{json_filename}")

        # Upload automatique vers BigQuery
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
