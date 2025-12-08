#!/usr/bin/env python3
"""
SpyFu Domain Stats Collector
Récupère les statistiques complètes de domaine (SEO + PPC) pour tous les périodes historiques
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import List, Dict
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class SpyFuDomainStatsCollector:
    """Collecteur de statistiques de domaine depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/domain_stats_api/v2"

    def __init__(self, api_key: str):
        """
        Initialise le collecteur SpyFu

        Args:
            api_key: Clé API SpyFu (Secret Key)
        """
        self.api_key = api_key
        self.session = requests.Session()

    def get_all_domain_stats(
        self,
        domain: str,
        country_code: str = "US"
    ) -> Dict:
        """
        Récupère toutes les statistiques d'un domaine (historique complet)

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, FR, GB, etc.)

        Returns:
            Dictionnaire avec les statistiques complètes du domaine
        """
        endpoint = f"{self.BASE_URL}/getAllDomainStats"

        params = {
            "domain": domain,
            "countryCode": country_code,
            "api_key": self.api_key
        }

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"📊 Récupération des stats complètes pour {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()

            print(f"✓ Stats récupérées pour {domain}")
            return data

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return {}

    def parse_domain_stats(self, stats_data: Dict, domain: str, country_code: str) -> Dict:
        """
        Parse les statistiques d'un domaine au format BigQuery
        L'API retourne un array 'results' avec des données mensuelles historiques
        On prend le dernier mois (données les plus récentes)

        Args:
            stats_data: Données brutes depuis l'API
            domain: Domaine analysé
            country_code: Code pays

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        # L'API retourne results comme array de données mensuelles
        results = stats_data.get("results", [])
        
        # Prendre les données du dernier mois (plus récent)
        latest_stats = results[0] if results else {}
        
        # Extraire les données principales
        result = {
            # Identifiants
            "domain": domain,
            "country_code": country_code,

            # Statistiques PPC (depuis les données mensuelles)
            "total_ad_keywords": latest_stats.get("totalAdsPurchased"),  # Nombre d'annonces achetées
            "total_ad_budget": latest_stats.get("monthlyBudget"),
            "total_ad_clicks": int(latest_stats.get("monthlyPaidClicks", 0)),
            "ad_history_months": len(results),  # Nombre de mois d'historique

            # Statistiques SEO
            "total_seo_keywords": latest_stats.get("totalOrganicResults"),
            "total_organic_keywords": latest_stats.get("totalOrganicResults"),  # Même valeur
            "total_organic_traffic": int(latest_stats.get("monthlyOrganicClicks", 0)),
            "total_organic_value": latest_stats.get("monthlyOrganicValue"),

            # Statistiques de domaine
            "domain_rank": int(latest_stats.get("averageOrganicRank", 0)),
            "domain_authority": latest_stats.get("strength"),  # Score de force 0-100

            # Données brutes JSON (pour les données historiques complètes)
            "raw_stats": json.dumps(stats_data),

            # Métadonnées
            "retrieved_at": datetime.now()
        }

        return result

    def collect_all_domains(
        self,
        domains: List[str],
        country_code: str = "US"
    ) -> List[Dict]:
        """
        Collecte les statistiques pour tous les domaines

        Args:
            domains: Liste des domaines à analyser
            country_code: Code pays

        Returns:
            Liste de toutes les stats formatées
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")

        print(f"🌐 Traitement de {len(domains)} domaines...")
        all_stats = []

        for i, domain in enumerate(domains, 1):
            print(f"\n[{i}/{len(domains)}] Domaine: {domain}")
            raw_stats = self.get_all_domain_stats(
                domain=domain,
                country_code=country_code
            )

            if raw_stats:
                parsed = self.parse_domain_stats(raw_stats, domain, country_code)
                all_stats.append(parsed)
                print(f"  ✓ Données récupérées et parsées")
            else:
                print(f"  ⚠️  Aucune donnée retournée par l'API")

        print(f"\n📊 Résumé: {len(all_stats)}/{len(domains)} domaines avec données")
        return all_stats

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
        table_id: str = "domain_stats",
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
                if df[col].dtype == 'object' and col != 'raw_stats':
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
            import traceback
            traceback.print_exc()


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

    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_domain_stats.py upload <json_filename>")
            sys.exit(1)

        json_filename = sys.argv[2]
        print("SpyFu Domain Stats - Upload depuis JSON")

        collector = SpyFuDomainStatsCollector(api_key=API_KEY)
        stats_data = collector.load_from_json(json_filename)

        if stats_data:
            collector.upload_to_bigquery(
                data=stats_data,
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

        print("SpyFu Domain Stats Collection")
        print(f"📍 Pays: {COUNTRY_CODE}")
        print(f"🌐 Domaines: {', '.join(DOMAINS)}")

        # Initialiser le collecteur
        collector = SpyFuDomainStatsCollector(api_key=API_KEY)

        # Collecter les données
        stats_data = collector.collect_all_domains(
            domains=DOMAINS,
            country_code=COUNTRY_CODE
        )

        print(f"\n✓ Total: {len(stats_data)} domaines analysés")

        # Exporter en JSON
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_domain_stats_{timestamp}.json"
        collector.export_to_json(stats_data, json_filename)
        print(f"✓ Données sauvegardées: ../data/{json_filename}")

        # Upload vers BigQuery
        print("\n📤 Upload vers BigQuery...")
        collector.upload_to_bigquery(
            data=stats_data,
            project_id=PROJECT_ID,
            dataset_id=DATASET_ID,
            credentials_path=CREDENTIALS_PATH
        )
        print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
