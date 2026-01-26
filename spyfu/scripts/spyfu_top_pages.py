#!/usr/bin/env python3
"""
SpyFu Top Pages Collector
Récupère les pages les plus performantes en SEO pour une liste de domaines
"""

import os
import sys
import json
import requests
import time
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config



class SpyFuTopPagesCollector:
    """Collecteur des meilleures pages SEO depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/serp_api/v2/seo"



    # Types de recherche disponibles
    SEARCH_TYPES = [
        "MostTraffic",  # Pages générant le plus de trafic organique
        "New"           # Pages récemment découvertes avec trafic significatif
    ]

    # Paramètres par défaut
    DEFAULT_PARAMS = {
        "searchType": "MostTraffic",
        "countryCode": "FR",
        "pageSize": 10,  # Limité à 10 selon budget
        "startingRow": 1,
        "sortBy": "SeoClicks",
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

    def get_top_pages(
        self,
        domain: str,
        search_type: str = "MostTraffic",
        country_code: str = "FR",
        page_size: int = 10,
        min_seo_clicks: Optional[int] = None,
        keyword_filter: Optional[str] = None,
        sort_by: str = "SeoClicks",
        max_retries: int = 3
    ) -> List[Dict]:
        """
        Récupère les pages les plus performantes en SEO pour un domaine

        Args:
            domain: Domaine à analyser
            search_type: Type de recherche (MostTraffic ou New) - OBLIGATOIRE
            country_code: Code pays (US, DE, GB, FR, etc.)
            page_size: Nombre de résultats par page (max 10 selon budget)
            min_seo_clicks: Nombre minimum de clics SEO mensuels
            keyword_filter: Filtre sur les mots-clés (optionnel)
            sort_by: Tri (SeoClicks est le seul supporté)
            max_retries: Nombre maximum de tentatives en cas de rate limit

        Returns:
            Liste des pages avec leurs métriques SEO
        """
        endpoint = f"{self.BASE_URL}/getTopPages"

        params = {
            "query": domain,
            "searchType": search_type,  # STRING requis: "MostTraffic" ou "New"
            "countryCode": country_code,  # STRING: code pays (US, FR, etc.)
            "pageSize": min(page_size, 10),
            "startingRow": 1,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "api_key": self.api_key
        }

        # Filtres optionnels
        if min_seo_clicks:
            params["seoClicks.min"] = min_seo_clicks
        if keyword_filter:
            params["keywordFilter"] = keyword_filter

        headers = {
            "Accept": "application/json"
        }

        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    print(f"🔄 Tentative {attempt + 1}/{max_retries} pour {domain}...")
                else:
                    print(f"📄 Récupération des top pages pour {domain}...")

                response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
                response.raise_for_status()

                data = response.json()
                pages = data.get("results", [])

                print(f"✓ {len(pages)} pages récupérées pour {domain}")
                return pages

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:
                    # Rate limit atteint
                    retry_after = 2  # Délai par défaut
                    try:
                        error_data = e.response.json()
                        retry_after = error_data.get("retryAfter", 2)
                    except:
                        pass

                    if attempt < max_retries - 1:
                        print(f"⏳ Rate limit atteint pour {domain}. Attente de {retry_after}s avant nouvelle tentative...")
                        time.sleep(retry_after)
                        continue
                    else:
                        print(f"✗ Rate limit atteint pour {domain} après {max_retries} tentatives")
                        return []
                else:
                    print(f"✗ Erreur HTTP {e.response.status_code} pour {domain}: {e}")
                    if hasattr(e, 'response') and e.response is not None:
                        print(f"  Détails: {e.response.text}")
                    return []

            except requests.exceptions.RequestException as e:
                print(f"✗ Erreur API pour {domain}: {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"  Détails: {e.response.text}")
                return []

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
        domains: List[str],
        search_type: str = "MostTraffic",
        country_code: str = "FR",
        page_size: int = 10,
        min_seo_clicks: Optional[int] = None,
        delay_between_domains: float = 1.5
    ) -> List[Dict]:
        """
        Collecte les données pour tous les domaines

        Args:
            domains: Liste des domaines à analyser
            search_type: Type de recherche (MostTraffic ou New)
            country_code: Code pays
            page_size: Nombre de pages à récupérer par domaine
            min_seo_clicks: Nombre minimum de clics SEO mensuels
            delay_between_domains: Délai en secondes entre chaque domaine

        Returns:
            Liste de toutes les pages formatées
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")
        all_pages = []

        for i, domain in enumerate(domains):
            # Ajouter un délai entre les domaines (sauf pour le premier)
            if i > 0 and delay_between_domains > 0:
                time.sleep(delay_between_domains)

            raw_pages = self.get_top_pages(
                domain=domain,
                search_type=search_type,
                country_code=country_code,
                page_size=page_size,
                min_seo_clicks=min_seo_clicks
            )

            for page in raw_pages:
                parsed = self.parse_page_data(page, domain, country_code)
                all_pages.append(parsed)

        return all_pages

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données en JSON"""
        if not data:
            print("⚠️  Aucune donnée à exporter")
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
        table_id: str = "top_pages",
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
    # Détecter Cloud Functions
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config = load_config(skip_credentials_check=is_cloud_function)

    # Récupérer les configurations
    spyfu_config = config.get_spyfu_config()
    google_config = config.get_google_cloud_config()

    API_KEY = spyfu_config['api_key']
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config["datasets"]["spyfu"]
    CREDENTIALS_PATH = google_config["credentials_file"]
    # Essayer d'abord spyfu.global.country_code, puis spyfu.country_code, par défaut US
    COUNTRY_CODE = spyfu_config.get('global', {}).get('country_code') or spyfu_config.get('country_code', 'US')

    # Configuration top_pages
    specific_config = spyfu_config.get('top_pages', {})
    if not specific_config.get('enabled', True):
        print("⚠️  top_pages désactivé dans la configuration")
        return


    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_top_pages.py upload <json_filename>")
            print("Exemple: python spyfu_top_pages.py upload spyfu_top_pages_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("SpyFu Top Pages - Upload depuis JSON")

        collector = SpyFuTopPagesCollector(api_key=API_KEY)

        # Charger depuis JSON
        pages_data = collector.load_from_json(json_filename)

        if pages_data:
            # Upload vers BigQuery
            collector.upload_to_bigquery(
                data=pages_data,
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
        collector = SpyFuTopPagesCollector(api_key=API_KEY)

        # Collecter les données
        print("SpyFu Top Pages Collection")
    
        pages_data = collector.collect_all_domains(
            domains=DOMAINS,
            search_type="MostTraffic",  # "MostTraffic" ou "New"
            country_code=COUNTRY_CODE,
            min_seo_clicks=None  # Pas de filtre minimum pour avoir tous les résultats
        )

        print(f"\n✓ Total: {len(pages_data)} pages collectées")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_top_pages_{timestamp}.json"
        collector.export_to_json(pages_data, json_filename)

        # Demander confirmation avant upload BigQuery
        print(f"\n✓ Données sauvegardées: ../data/{json_filename}")

        # Upload automatique vers BigQuery
        print("\n📤 Upload vers BigQuery...")
        collector.upload_to_bigquery(
            data=pages_data,
            project_id=PROJECT_ID,
                dataset_id=DATASET_ID,
                credentials_path=CREDENTIALS_PATH
        )
        print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
