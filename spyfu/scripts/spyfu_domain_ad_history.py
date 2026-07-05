#!/usr/bin/env python3
"""
SpyFu Domain Ad History Collector
Récupère l'historique des annonces publicitaires pour une liste de domaines
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

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class SpyFuDomainAdHistoryCollector:
    """Collecteur d'historique des annonces depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/cloud_ad_history_api/v2/domain"

    def __init__(self, api_key: str):
        """
        Initialise le collecteur SpyFu

        Args:
            api_key: Clé API SpyFu (Secret Key)
        """
        self.api_key = api_key
        self.session = requests.Session()

    def get_domain_ad_history(
        self,
        domain: str,
        country_code: str = "US",
        page_size: int = 100,
        min_date: Optional[str] = None,
        max_date: Optional[str] = None
    ) -> List[Dict]:
        """
        Récupère TOUTES les annonces pour un domaine via pagination complète.
        Aucune limite sur le spend ou le nombre de résultats — on veut chaque ad,
        y compris les petites ads ciblant des termes de marque concurrents.

        Args:
            domain: Domaine à analyser
            country_code: Code pays (US, FR, GB, etc.)
            page_size: Nombre de résultats par page (utilisé pour la pagination)
            min_date: Date minimale (format YYYY-MM-DD)
            max_date: Date maximale (format YYYY-MM-DD)

        Returns:
            Liste complète de toutes les annonces du domaine
        """
        endpoint = f"{self.BASE_URL}/getDomainAdHistory"

        if not max_date:
            max_date = datetime.now().strftime("%Y-%m-%d")
        if not min_date:
            min_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

        headers = {"Accept": "application/json"}
        all_ads = []
        starting_row = 1

        print(f"📜 Récupération complète des annonces pour {domain} ({min_date} à {max_date})...")

        while True:
            params = {
                "domain": domain,
                "countryCode": country_code,
                "rowcount": page_size,
                "startingRow": starting_row,
                "minDate": min_date,
                "maxDate": max_date,
                "api_key": self.api_key
            }

            try:
                response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
                response.raise_for_status()

                data = response.json()
                ads = data.get("results", [])

                if not ads:
                    break

                all_ads.extend(ads)
                print(f"  Lignes {starting_row}-{starting_row + len(ads) - 1}: {len(ads)} annonces")

                # Vérifier s'il reste des pages via resultCount si disponible
                total = data.get("resultCount")
                if total is not None and len(all_ads) >= total:
                    break

                if len(ads) < page_size:
                    break

                starting_row += page_size

            except requests.exceptions.RequestException as e:
                print(f"✗ Erreur API pour {domain} (ligne {starting_row}): {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"  Détails: {e.response.text}")
                break

        print(f"✓ {len(all_ads)} annonces récupérées au total pour {domain}")
        return all_ads

    def get_keyword_metrics(
        self,
        domain: str,
        keyword: str,
        country_code: str = "US"
    ) -> Dict:
        """
        Récupère les métriques d'un keyword spécifique via l'API PPC Keywords

        Args:
            domain: Domaine analysé
            keyword: Mot-clé à rechercher
            country_code: Code pays

        Returns:
            Dict avec search_volume, cost_per_click, monthly_cost (ou None si non trouvé)
        """
        # Vérifier le cache
        cache_key = f"{domain}:{keyword}:{country_code}"
        if not hasattr(self, '_keyword_cache'):
            self._keyword_cache = {}

        if cache_key in self._keyword_cache:
            return self._keyword_cache[cache_key]

        # Appel API
        endpoint = "https://api.spyfu.com/apis/keyword_api/v2/ppc/getMostSuccessful"

        params = {
            "query": domain,
            "countryCode": country_code,
            "pageSize": 20,
            "startingRow": 1,
            "sortBy": "SearchVolume",
            "sortOrder": "Descending",
            "api_key": self.api_key
        }

        headers = {"Accept": "application/json"}

        try:
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            keywords_data = data.get("results", [])

            # Chercher le keyword spécifique (insensible à la casse)
            for kw_data in keywords_data:
                if kw_data.get("keyword", "").lower() == keyword.lower():
                    metrics = {
                        "search_volume": kw_data.get("searchVolume"),
                        "cost_per_click": kw_data.get("broadCostPerClick"),
                        "monthly_cost": kw_data.get("broadMonthlyCost")
                    }
                    self._keyword_cache[cache_key] = metrics
                    return metrics

            # Si non trouvé dans les résultats
            default_metrics = {"search_volume": None, "cost_per_click": None, "monthly_cost": None}
            self._keyword_cache[cache_key] = default_metrics
            return default_metrics

        except requests.exceptions.RequestException as e:
            print(f"  ⚠️  Erreur lors de la récupération des métriques pour '{keyword}': {e}")
            return {"search_volume": None, "cost_per_click": None, "monthly_cost": None}

    def parse_ad_data(self, ad_data: Dict, domain: str, country_code: str, enrich: bool = True) -> Dict:
        """
        Parse les données d'une annonce au format BigQuery avec enrichissement

        Args:
            ad_data: Données brutes de l'annonce depuis l'API
            domain: Domaine analysé
            country_code: Code pays
            enrich: Si True, enrichit avec les métriques du keyword (search_volume, CPC, etc.)

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        # Convertir searchDateId en date (format YYYYMMDD)
        search_date_id = ad_data.get("searchDateId")
        first_seen = None
        if search_date_id:
            try:
                date_str = str(search_date_id)
                first_seen = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
            except:
                pass

        # Extraire le premier keyword de la liste
        keywords_list = ad_data.get("keywords", [])
        keyword = keywords_list[0] if keywords_list else None

        # Extraire display_url depuis l'URL de destination
        destination_url = ad_data.get("url")
        display_url = None
        if destination_url:
            try:
                from urllib.parse import urlparse
                parsed = urlparse(destination_url)
                # Format: domain.com/path
                display_url = f"{parsed.netloc}{parsed.path}".rstrip("/")
            except:
                display_url = None

        # Structure de base
        parsed_data = {
            # Identifiants
            "domain": domain,
            "ad_id": str(ad_data.get("adId")) if ad_data.get("adId") else None,
            "keyword": keyword,

            # Contenu de l'annonce (l'API utilise title/body au lieu de headline/description)
            "headline": ad_data.get("title"),
            "description": ad_data.get("body"),
            "display_url": display_url,  # Extrait depuis l'URL
            "destination_url": destination_url,

            # Métriques temporelles
            "first_seen_date": first_seen,
            # Note: last_seen_date et days_seen ne sont pas dans le schéma BigQuery actuel

            # Métriques de performance (à enrichir)
            "search_volume": None,
            "cost_per_click": None,
            "monthly_cost": None,
            "position": ad_data.get("position"),

            # Métadonnées
            "country_code": country_code,
            "retrieved_at": datetime.now()
        }

        # Enrichissement avec les métriques du keyword via API PPC
        if enrich and keyword:
            print(f"    🔍 Enrichissement pour keyword '{keyword}'...")
            metrics = self.get_keyword_metrics(domain, keyword, country_code)
            parsed_data["search_volume"] = metrics.get("search_volume")
            parsed_data["cost_per_click"] = metrics.get("cost_per_click")
            parsed_data["monthly_cost"] = metrics.get("monthly_cost")

        return parsed_data

    def collect_all_domains(
        self,
        domains: List[str],
        country_code: str = "US",
        page_size: int = 100,
        min_date: Optional[str] = None,
        max_date: Optional[str] = None,
        enrich: bool = True
    ) -> List[Dict]:
        """
        Collecte TOUTES les annonces pour chaque domaine (pagination complète, sans filtre de taille).

        Args:
            domains: Liste des domaines à analyser
            country_code: Code pays
            page_size: Taille de page pour la pagination interne
            min_date: Date minimale
            max_date: Date maximale
            enrich: Si True, enrichit avec les métriques des keywords (recommandé)

        Returns:
            Liste de toutes les annonces formatées
        """
        if not domains:
            raise ValueError("La liste de domaines ne peut pas être vide")

        all_ads = []

        for domain in domains:
            print(f"\n{'='*80}")
            print(f"📍 Traitement de {domain}")
            print(f"{'='*80}")

            raw_ads = self.get_domain_ad_history(
                domain=domain,
                country_code=country_code,
                page_size=page_size,
                min_date=min_date,
                max_date=max_date
            )

            for ad in raw_ads:
                parsed = self.parse_ad_data(ad, domain, country_code, enrich)
                all_ads.append(parsed)

            print(f"✓ {len(raw_ads)} annonces traitées pour {domain}")

        return all_ads

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
        """Charge les données depuis un fichier JSON"""
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
        table_id: str = "domain_ad_history",
        credentials_path: str = "../../account-key.json"
    ):
        """Upload les données vers BigQuery"""
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
                if df[col].dtype == 'object' and col not in ['first_seen_date']:
                    try:
                        df[col] = pd.to_numeric(df[col])
                    except (ValueError, TypeError):
                        df[col] = df[col].astype(str)
                        df[col] = df[col].replace('None', None)

            # Gérer les colonnes datetime
            date_columns = ['retrieved_at', 'first_seen_date']
            for col in date_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], utc=True, errors='coerce')

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
    # Essayer d'abord spyfu.global.country_code, puis spyfu.country_code, par défaut US
    COUNTRY_CODE = spyfu_config.get('global', {}).get('country_code') or spyfu_config.get('country_code', 'US')

    # Dates: 3 derniers mois par défaut
    MAX_DATE = datetime.now().strftime("%Y-%m-%d")
    MIN_DATE = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        if len(sys.argv) < 3:
            print("Usage: python spyfu_domain_ad_history.py upload <json_filename>")
            sys.exit(1)

        json_filename = sys.argv[2]
        print("SpyFu Domain Ad History - Upload depuis JSON")

        collector = SpyFuDomainAdHistoryCollector(api_key=API_KEY)
        ads_data = collector.load_from_json(json_filename)

        if ads_data:
            collector.upload_to_bigquery(
                data=ads_data,
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

        print("=" * 80)
        print("  SpyFu Domain Ad History Collection - VERSION ENRICHIE")
        print("=" * 80)
        print(f"📍 Pays: {COUNTRY_CODE}")
        print(f"🌐 Domaines: {', '.join(DOMAINS)}")
        print(f"📅 Période: {MIN_DATE} à {MAX_DATE}")
        print("\n🔍 Enrichissement activé:")
        print("   ✅ display_url: Extrait depuis l'URL de destination")
        print("   ✅ search_volume, cost_per_click, monthly_cost: Via API PPC Keywords")
        print("   ✅ Pagination complète — toutes les ads sans filtre de taille")
        print("=" * 80)

        # Initialiser le collecteur
        collector = SpyFuDomainAdHistoryCollector(api_key=API_KEY)

        # Collecter toutes les données avec pagination complète
        ads_data = collector.collect_all_domains(
            domains=DOMAINS,
            country_code=COUNTRY_CODE,
            min_date=MIN_DATE,
            max_date=MAX_DATE,
            enrich=True
        )

        print(f"\n✓ Total: {len(ads_data)} annonces collectées")

        # Exporter en JSON
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_domain_ad_history_{timestamp}.json"
        collector.export_to_json(ads_data, json_filename)
        print(f"✓ Données sauvegardées: ../data/{json_filename}")

        # Upload vers BigQuery
        print("\n📤 Upload vers BigQuery...")
        collector.upload_to_bigquery(
            data=ads_data,
            project_id=PROJECT_ID,
            dataset_id=DATASET_ID,
            credentials_path=CREDENTIALS_PATH
        )
        print("\n✓ Collection et upload terminés")


if __name__ == "__main__":
    main()
