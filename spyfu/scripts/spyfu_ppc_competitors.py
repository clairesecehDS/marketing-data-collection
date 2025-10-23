#!/usr/bin/env python3
"""
SpyFu PPC Competitors Collector
Récupère les principaux concurrents PPC pour une liste de domaines
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



class SpyFuPPCCompetitorsCollector:
    """Collecteur de concurrents PPC depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/competitors_api/v2/ppc"



    # Paramètres par défaut
    DEFAULT_PARAMS = {
        "countryCode": "FR",
        "pageSize": 100,
        "startingRow": 1,
        "sortBy": "CommonTerms",
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

    def get_top_competitors(
        self,
        domain: str,
        country_code: str = "FR",
        page_size: int = 100,
        sort_by: str = "CommonTerms"
    ) -> List[Dict]:
        """
        Récupère les principaux concurrents PPC pour un domaine

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, DE, GB, FR, etc.)
            page_size: Nombre de résultats par page
            sort_by: Tri (CommonTerms, Rank)

        Returns:
            Liste des concurrents PPC avec leurs métriques
        """
        endpoint = f"{self.BASE_URL}/getTopCompetitors"

        params = {
            "domain": domain,
            "countryCode": country_code,
            "pageSize": page_size,
            "startingRow": 1,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "api_key": self.api_key
        }

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"🎯 Récupération des concurrents PPC pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            competitors = data.get("results", [])

            print(f"✓ {len(competitors)} concurrents PPC récupérés pour {domain}")
            return competitors

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    def parse_competitor_data(self, competitor_data: Dict, domain: str, country_code: str) -> Dict:
        """
        Parse les données d'un concurrent au format BigQuery

        Args:
            competitor_data: Données brutes du concurrent depuis l'API
            domain: Domaine analysé
            country_code: Code pays

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        return {
            # Identifiants
            "domain": domain,
            "competitor_domain": competitor_data.get("domain"),

            # Métriques de compétition
            "common_terms": competitor_data.get("commonTerms"),
            "rank": competitor_data.get("rank"),

            # Métadonnées
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_all_domains(
        self,
        domains: List[str],
        country_code: str = "FR"
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines à analyser
            country_code: Code pays

        Returns:
            Liste de tous les concurrents formatés
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")
        all_competitors = []

        for domain in domains:
            raw_competitors = self.get_top_competitors(
                domain=domain,
                country_code=country_code
            )

            for comp in raw_competitors:
                parsed = self.parse_competitor_data(comp, domain, country_code)
                all_competitors.append(parsed)

        return all_competitors

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
        table_id: str = "ppc_competitors",
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
            credentials = service_account.Credentials.from_service_account_file(
                credentials_path,
                scopes=["https://www.googleapis.com/auth/bigquery"]
            )

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
            print("🔍 Types avant conversion:")
            print(df.dtypes)
            
            # 1. Gérer les colonnes datetime en premier
            if 'retrieved_at' in df.columns:
                df['retrieved_at'] = pd.to_datetime(df['retrieved_at'], utc=True)

            # 2. Convertir les colonnes numériques explicitement
            numeric_columns = {
                'common_terms': 'int64',  # Utiliser int64 standard au lieu de Int64
                'rank': 'float64'
            }
            
            for col, dtype in numeric_columns.items():
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce').astype(dtype)

            # 3. Convertir les colonnes string - forcer en objet simple
            string_columns = ['domain', 'competitor_domain', 'country_code']
            for col in string_columns:
                if col in df.columns:
                    # Convertir en object (compatible Parquet)
                    df[col] = df[col].astype(object)

            print("🔍 Types après conversion:")
            print(df.dtypes)
            print("🔍 Premiers exemples:")
            print(df.head(2))
            print("🔍 Vérification des valeurs nulles:")
            print(df.isnull().sum())
            
            # Créer une copie pour éviter les problèmes de référence
            df_upload = df.copy()

            table_full_id = f"{project_id}.{dataset_id}.{table_id}"

            print(f"📤 Upload de {len(df_upload)} lignes vers {table_full_id}...")

            pandas_gbq.to_gbq(
                df_upload,
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

    # ============================================================
    # CHARGEMENT DE LA CONFIGURATION
    # ============================================================
    print("📋 Chargement de la configuration...")
    config = load_config()

    # Récupérer les configurations
    spyfu_config = config.get_spyfu_config()
    google_config = config.get_google_cloud_config()

    API_KEY = spyfu_config['api_key']
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config["datasets"]["spyfu"]
    CREDENTIALS_PATH = google_config["credentials_file"]

    # Configuration ppc_competitors
    specific_config = spyfu_config.get('ppc_competitors', {})
    if not specific_config.get('enabled', True):
        print("⚠️  ppc_competitors désactivé dans la configuration")
        return


    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_ppc_competitors.py upload <json_filename>")
            print("Exemple: python spyfu_ppc_competitors.py upload spyfu_ppc_competitors_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("=" * 60)
        print("SpyFu PPC Competitors - Upload depuis JSON")
        print("=" * 60)

        collector = SpyFuPPCCompetitorsCollector(api_key=API_KEY)

        # Charger depuis JSON
        competitors_data = collector.load_from_json(json_filename)

        if competitors_data:
            # Upload vers BigQuery
            collector.upload_to_bigquery(
                data=competitors_data,
                project_id=PROJECT_ID,
                dataset_id=DATASET_ID,
                credentials_path=CREDENTIALS_PATH
            )
            print("\n✓ Upload terminé")
        else:
            print("\n✗ Aucune donnée à uploader")

    else:
        # Mode collection normal
        # Domaines à analyser (à personnaliser)
        DOMAINS = spyfu_config["domains"]["all"]

        # Initialiser le collecteur
        collector = SpyFuPPCCompetitorsCollector(api_key=API_KEY)

        # Collecter les données
        print("=" * 60)
        print("SpyFu PPC Competitors Collection")
        print("=" * 60)

        competitors_data = collector.collect_all_domains(
            domains=DOMAINS,
            country_code="FR"
        )

        print(f"\n✓ Total: {len(competitors_data)} concurrents PPC collectés")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_ppc_competitors_{timestamp}.json"
        collector.export_to_json(competitors_data, json_filename)

        # Demander confirmation avant upload BigQuery
        print(f"\n✓ Données sauvegardées: ../data/{json_filename}")

        # Upload automatique vers BigQuery
        print("\n📤 Upload vers BigQuery...")
        collector.upload_to_bigquery(
            data=competitors_data,
            project_id=PROJECT_ID,
                dataset_id=DATASET_ID,
                credentials_path=CREDENTIALS_PATH
        )
        print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
