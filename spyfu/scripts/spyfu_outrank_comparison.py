#!/usr/bin/env python3
"""
SpyFu Outrank Comparison Collector
Compare où les concurrents surclassent votre domaine en SEO
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



class SpyFuOutrankCollector:
    """Collecteur de comparaisons de ranking SEO depuis l'API SpyFu"""

    BASE_URL = "https://api.spyfu.com/apis/serp_api/v2/seo"

    # Comparaisons à effectuer (votre domaine vs concurrents)
    COMPARISONS = [
        {"domain": "your-domain.com", "compare_domain": "competitor1.com"},
        {"domain": "your-domain.com", "compare_domain": "competitor2.com"},
    ]

    # Paramètres par défaut
    DEFAULT_PARAMS = {
        "countryCode": "FR",
        "pageSize": 10000,
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

    def get_where_outrank_you(
        self,
        domain: str,
        compare_domain: str,
        country_code: str = "FR",
        page_size: int = 1000,
        min_search_volume: Optional[int] = None,
        min_seo_clicks: Optional[int] = None,
        sort_by: str = "SearchVolume"
    ) -> List[Dict]:
        """
        Récupère les mots-clés où le concurrent surclasse votre domaine

        Args:
            domain: Votre domaine
            compare_domain: Domaine concurrent à comparer
            country_code: Code pays (US, DE, GB, FR, etc.)
            page_size: Nombre de résultats par page (max 10000)
            min_search_volume: Volume de recherche minimum
            min_seo_clicks: Nombre minimum de clics SEO
            sort_by: Tri (SearchVolume, KeywordDifficulty, Rank, etc.)

        Returns:
            Liste des mots-clés où le concurrent est mieux classé
        """
        endpoint = f"{self.BASE_URL}/getWhereTheyOutRankYou"

        params = {
            "query": domain,
            "compareDomain": compare_domain,
            "countryCode": country_code,
            "pageSize": min(page_size, 10000),
            "startingRow": 1,
            "sortBy": sort_by,
            "sortOrder": "Descending",
            "adultFilter": True,
            "api_key": self.api_key
        }

        # Filtres optionnels
        if min_search_volume:
            params["searchVolume.min"] = min_search_volume
        if min_seo_clicks:
            params["seoClicks.min"] = min_seo_clicks

        headers = {
            "Accept": "application/json"
        }

        try:
            print(f"⚔️  Comparaison: {compare_domain} vs {domain}...")
            response = self.session.get(endpoint, params=params, headers=headers, timeout=60)
            response.raise_for_status()

            data = response.json()
            keywords = data.get("results", [])

            print(f"✓ {len(keywords)} keywords où {compare_domain} surclasse {domain}")
            return keywords

        except requests.exceptions.RequestException as e:
            print(f"✗ Erreur API pour {domain} vs {compare_domain}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Détails: {e.response.text}")
            return []

    def parse_keyword_data(
        self,
        keyword_data: Dict,
        domain: str,
        compare_domain: str,
        country_code: str
    ) -> Dict:
        """
        Parse les données d'un mot-clé au format BigQuery

        Args:
            keyword_data: Données brutes du mot-clé depuis l'API
            domain: Votre domaine
            compare_domain: Domaine concurrent
            country_code: Code pays

        Returns:
            Dictionnaire formaté pour BigQuery
        """
        return {
            # Identifiants
            "domain": domain,
            "compare_domain": compare_domain,
            "keyword": keyword_data.get("keyword"),

            # Ranking du concurrent
            "top_ranked_url": keyword_data.get("topRankedUrl"),
            "rank": keyword_data.get("rank"),
            "rank_change": keyword_data.get("rankChange"),

            # Votre ranking
            "your_rank": keyword_data.get("yourRank"),
            "your_rank_change": keyword_data.get("yourRankChange"),
            "your_url": keyword_data.get("yourUrl"),

            # Métriques SEO du concurrent
            "seo_clicks": keyword_data.get("seoClicks"),
            "seo_clicks_change": keyword_data.get("seoClicksChange"),

            # Métriques de recherche
            "search_volume": keyword_data.get("searchVolume"),
            "keyword_difficulty": keyword_data.get("keywordDifficulty"),
            "total_monthly_clicks": keyword_data.get("totalMonthlyClicks"),

            # Pourcentages de recherche
            "percent_mobile_searches": keyword_data.get("percentMobileSearches"),
            "percent_desktop_searches": keyword_data.get("percentDesktopSearches"),
            "percent_not_clicked": keyword_data.get("percentNotClicked"),
            "percent_paid_clicks": keyword_data.get("percentPaidClicks"),
            "percent_organic_clicks": keyword_data.get("percentOrganicClicks"),

            # CPC par match type
            "broad_cost_per_click": keyword_data.get("broadCostPerClick"),
            "phrase_cost_per_click": keyword_data.get("phraseCostPerClick"),
            "exact_cost_per_click": keyword_data.get("exactCostPerClick"),

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

    def collect_all_comparisons(
        self,
        comparisons: Optional[List[Dict]] = None,
        country_code: str = "FR",
        min_search_volume: Optional[int] = None
    ) -> List[Dict]:
        """
        Collecte les données pour toutes les comparaisons

        Args:
            comparisons: Liste des comparaisons {domain, compare_domain}
            country_code: Code pays
            min_search_volume: Volume de recherche minimum

        Returns:
            Liste de tous les mots-clés formatés
        """
        comparisons = comparisons or self.COMPARISONS
        all_keywords = []

        for comp in comparisons:
            domain = comp["domain"]
            compare_domain = comp["compare_domain"]

            raw_keywords = self.get_where_outrank_you(
                domain=domain,
                compare_domain=compare_domain,
                country_code=country_code,
                min_search_volume=min_search_volume
            )

            for kw in raw_keywords:
                parsed = self.parse_keyword_data(kw, domain, compare_domain, country_code)
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
        table_id: str = "outrank_comparison",
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

    # Configuration outrank_comparison
    specific_config = spyfu_config.get('outrank_comparison', {})
    if not specific_config.get('enabled', True):
        print("⚠️  outrank_comparison désactivé dans la configuration")
        return


    # Mode: "collect" ou "upload"
    mode = sys.argv[1] if len(sys.argv) > 1 else "collect"

    if mode == "upload":
        # Mode upload depuis JSON existant
        if len(sys.argv) < 3:
            print("Usage: python spyfu_outrank_comparison.py upload <json_filename>")
            print("Exemple: python spyfu_outrank_comparison.py upload spyfu_outrank_20250114_123456.json")
            sys.exit(1)

        json_filename = sys.argv[2]

        print("=" * 60)
        print("SpyFu Outrank Comparison - Upload depuis JSON")
        print("=" * 60)

        collector = SpyFuOutrankCollector(api_key=API_KEY)

        # Charger depuis JSON
        keywords_data = collector.load_from_json(json_filename)

        if keywords_data:
            # Upload vers BigQuery
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
        # Récupérer les comparaisons depuis la configuration
        COMPARISONS = spyfu_config.get('comparisons', [])
        
        if not COMPARISONS:
            print("⚠️  Aucune comparaison configurée dans config.yaml")
            print("   Ajoutez des comparaisons dans la section 'spyfu.comparisons'")
            print("   Exemple:")
            print("   comparisons:")
            print("     - domain: 'votredomaine.com'")
            print("       compare_domain: 'concurrent1.com'")
            print("     - domain: 'votredomaine.com'")
            print("       compare_domain: 'concurrent2.com'")
            return

        print(f"📊 {len(COMPARISONS)} comparaison(s) configurée(s)")
        for comp in COMPARISONS:
            print(f"   • {comp['domain']} vs {comp['compare_domain']}")

        # Initialiser le collecteur
        collector = SpyFuOutrankCollector(api_key=API_KEY)
        collector.COMPARISONS = COMPARISONS

        # Collecter les données
        print("=" * 60)
        print("SpyFu Outrank Comparison Collection")
        print("=" * 60)

        keywords_data = collector.collect_all_comparisons(
            country_code="FR",
            min_search_volume=100  # Optionnel: filtrer par volume minimum
        )

        print(f"\n✓ Total: {len(keywords_data)} comparaisons collectées")

        # Exporter en JSON (TOUJOURS avant BigQuery)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_filename = f"spyfu_outrank_{timestamp}.json"
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
