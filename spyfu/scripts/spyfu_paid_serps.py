#!/usr/bin/env python3
"""
SpyFu Paid SERPs Collector
Récupère les annonces payantes (PPC ads) pour une liste de domaines
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



class SpyFuPaidSerpsCollector:
    """Collecteur d'annonces PPC depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/serp_api/v2/ppc"



    # Paramètres par défaut
    DEFAULT_PARAMS = {
        "countryCode": "FR",
        "pageSize": 1000,
        "startingRow": 1,
        "sortBy": "SearchVolume",
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

    def get_paid_serps(
        self,
        domain: str,
        country_code: str = "FR",
        page_size: int = 1000,
        min_search_volume: Optional[int] = None,
        min_ad_count: Optional[int] = None,
        sort_by: str = "SearchVolume"
    ) -> List[Dict]:
        """
        Récupère les annonces PPC (SERPs payantes) pour un domaine

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, DE, GB, FR, etc.)
            page_size: Nombre de résultats par page
            min_search_volume: Volume de recherche minimum
            min_ad_count: Nombre minimum d'annonces
            sort_by: Tri (SearchVolume, KeywordDifficulty, AdPosition, AdCount, DateSearched)

        Returns:
            Liste des annonces avec leurs métriques
        """
        endpoint = f"{self.BASE_URL}/getPaidSerps"

        params = {
            "query": domain,
            "countryCode": country_code,
            "pageSize": page_size,
            "startingRow": 1,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "adultFilter": True,
            "api_key": self.api_key
        }

        # Filtres optionnels
        if min_search_volume:
            params["searchVolume.min"] = min_search_volume
        if min_ad_count:
            params["adCount.min"] = min_ad_count

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"📢 Récupération des annonces PPC pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            serps = data.get("results", [])

            print(f"✓ {len(serps)} annonces PPC récupérées pour {domain}")
            return serps

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    def parse_serp_data(self, serp_data: Dict, domain: str, country_code: str) -> Dict:
        """
        Parse les données d'une annonce au format BigQuery

        Args:
            serp_data: Données brutes de l'annonce depuis l'API
            domain: Domaine analysé
            country_code: Code pays

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        return {
            # Identifiants
            "domain": domain,
            "keyword": serp_data.get("keyword"),
            "term_id": serp_data.get("termId"),

            # Métriques d'annonce
            "ad_position": serp_data.get("adPosition"),
            "ad_count": serp_data.get("adCount"),
            "date_searched": serp_data.get("dateSearched"),

            # Contenu de l'annonce
            "title": serp_data.get("title"),
            "body_html": serp_data.get("bodyHtml"),
            "ad_domain": serp_data.get("domain"),  # Domaine affiché dans l'annonce

            # Métriques du mot-clé
            "search_volume": serp_data.get("searchVolume"),
            "keyword_difficulty": serp_data.get("keywordDifficulty"),

            # Flags
            "is_nsfw": serp_data.get("isNsfw"),

            # Métadonnées
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

    def collect_all_domains(
        self,
        domains: List[str],
        country_code: str = "FR",
        min_search_volume: Optional[int] = None
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines à analyser
            country_code: Code pays
            min_search_volume: Volume de recherche minimum

        Returns:
            Liste de toutes les annonces formatées
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")
        all_serps = []

        for domain in domains:
            raw_serps = self.get_paid_serps(
                domain=domain,
                country_code=country_code,
                min_search_volume=min_search_volume
            )

            for serp in raw_serps:
                parsed = self.parse_serp_data(serp, domain, country_code)
                all_serps.append(parsed)

        return all_serps

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
        table_id: str = "paid_serps",
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
            if 'date_searched' in df.columns:
                df['date_searched'] = pd.to_datetime(df['date_searched'], errors='coerce')

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

    # Configuration paid_serps
    specific_config = spyfu_config.get('paid_serps', {})
    if not specific_config.get('enabled', True):
        print("⚠️  paid_serps désactivé dans la configuration")
        return


    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_paid_serps.py upload <json_filename>")
            print("Exemple: python spyfu_paid_serps.py upload spyfu_paid_serps_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("=" * 60)
        print("SpyFu Paid SERPs - Upload depuis JSON")
        print("=" * 60)

        collector = SpyFuPaidSerpsCollector(api_key=API_KEY)

        # Charger depuis JSON
        serps_data = collector.load_from_json(json_filename)

        if serps_data:
            # Upload vers BigQuery
            collector.upload_to_bigquery(
                data=serps_data,
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
        collector = SpyFuPaidSerpsCollector(api_key=API_KEY)

        # Collecter les données
        print("=" * 60)
        print("SpyFu Paid SERPs Collection")
        print("=" * 60)

        serps_data = collector.collect_all_domains(
            domains=DOMAINS,
            country_code="FR",
            min_search_volume=100  # Optionnel: filtrer par volume minimum
        )

        print(f"\n✓ Total: {len(serps_data)} annonces PPC collectées")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_paid_serps_{timestamp}.json"
        collector.export_to_json(serps_data, json_filename)

        # Demander confirmation avant upload BigQuery
        print(f"\n✓ Données sauvegardées: ../data/{json_filename}")

        # Upload automatique vers BigQuery
        print("\n📤 Upload vers BigQuery...")
        collector.upload_to_bigquery(
            data=serps_data,
            project_id=PROJECT_ID,
                dataset_id=DATASET_ID,
                credentials_path=CREDENTIALS_PATH
        )
        print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
