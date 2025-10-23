import requests
from datetime import datetime
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os
import sys
import time
from urllib.parse import urlencode

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class LinkedInAdsLibraryClient:
    """
    Client pour rechercher et analyser les publicités via LinkedIn Ads Library API
    Documentation: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/ads-library
    
    Cette API permet de :
    - Rechercher les publicités par mot-clé
    - Rechercher les publicités d'un annonceur spécifique
    - Obtenir des insights sur les campagnes concurrentes
    """

    def __init__(self, access_token: str, project_id: Optional[str] = None,
                 dataset_id: str = "linkedin_ads_library",
                 credentials_path: Optional[str] = None,
                 request_delay: float = 1.0):
        """
        Initialise le client avec le token d'accès

        Args:
            access_token: Token OAuth 2.0 LinkedIn avec permissions Ads Library
            project_id: ID du projet Google Cloud
            dataset_id: ID du dataset BigQuery (défaut: linkedin_ads_library)
            credentials_path: Chemin vers le fichier JSON des credentials GCP
            request_delay: Délai en secondes entre chaque requête API (défaut: 1.0)
        """
        self.access_token = access_token
        self.base_url = "https://api.linkedin.com/rest"

        # Configuration BigQuery
        self.project_id = project_id or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.dataset_id = dataset_id
        self.credentials_path = credentials_path
        self.bq_client = None

        # Configuration du rate limiting
        self.request_delay = request_delay
        self.last_request_time = 0

    def _get_headers(self) -> Dict[str, str]:
        """Retourne les headers requis pour l'API LinkedIn Ads Library"""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "LinkedIn-Version": "202509",
            "X-Restli-Protocol-Version": "2.0.0"
        }

    def _wait_for_rate_limit(self):
        """Attend le délai nécessaire entre les requêtes pour respecter le rate limit"""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time

        if time_since_last_request < self.request_delay:
            sleep_time = self.request_delay - time_since_last_request
            print(f"⏱️  Attente de {sleep_time:.1f}s pour respecter le rate limit...")
            time.sleep(sleep_time)

        self.last_request_time = time.time()

    def _make_request_with_retry(self, url: str, max_retries: int = 3) -> requests.Response:
        """
        Effectue une requête HTTP avec retry en cas d'erreur 429

        Args:
            url: URL à requêter
            max_retries: Nombre maximum de tentatives

        Returns:
            Response object
        """
        for attempt in range(max_retries):
            # Respecter le rate limit
            self._wait_for_rate_limit()

            response = requests.get(url, headers=self._get_headers())

            # Succès
            if response.status_code == 200:
                return response

            # Rate limit dépassé
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f"⚠️  Rate limit atteint (tentative {attempt + 1}/{max_retries})")
                print(f"⏱️  Attente de {retry_after}s avant nouvelle tentative...")
                time.sleep(retry_after)
                continue

            # Autre erreur
            print(f"⚠️  Erreur API: {response.status_code}")
            print(f"URL: {response.url}")
            print(f"Réponse: {response.text}")
            response.raise_for_status()

        # Toutes les tentatives ont échoué
        print(f"❌ Échec après {max_retries} tentatives")
        response.raise_for_status()
        return response

    def _build_countries_param(self, countries: List[str]) -> str:
        """
        Construit le paramètre countries au format LinkedIn
        Format attendu: (value:List(urn:li:country:us,urn:li:country:fr))
        L'API LinkedIn utilise un format spécifique pour les listes avec un objet contenant "value"

        Args:
            countries: Liste de codes pays ISO à 2 lettres (ex: ["FR", "US"])

        Returns:
            str: Paramètre formaté (non encodé, requests.get() s'en charge)

        Example:
            >>> _build_countries_param(["FR", "US"])
            "(value:List(urn:li:country:fr,urn:li:country:us))"
        """
        # Créer les URNs avec codes pays en minuscule
        country_urns = [f"urn:li:country:{country.lower()}" for country in countries]

        # Format requis par l'API: (value:List(...))
        # requests.get() va automatiquement l'encoder en URL
        return f"(value:List({','.join(country_urns)}))"

    def search_ads_by_keyword(self, keyword: str, countries: Optional[List[str]] = None,
                               start: int = 0, count: int = 25) -> Dict:
        """
        Recherche des publicités par mot-clé

        Args:
            keyword: Mot-clé à rechercher
            countries: Liste de codes pays (ex: ["FR", "US"])
            start: Index de départ pour la pagination
            count: Nombre de résultats (max 25)

        Returns:
            dict: Réponse de l'API avec les publicités trouvées
        """
        base_url = f"{self.base_url}/adLibrary"

        # Construire les paramètres de base
        params = {
            "q": "criteria",
            "keyword": keyword,
            "start": start,
            "count": min(count, 25)  # Maximum 25 par requête
        }

        # Construire l'URL de base avec urlencode pour les params standards
        url = f"{base_url}?{urlencode(params)}"

        # Ajouter le filtre pays si spécifié
        # Format LinkedIn API: countries=(value:List(urn%3Ali%3Acountry%3Afr))
        # Note: on encode manuellement les ":" en "%3A" mais pas les parenthèses/virgules
        if countries:
            country_urns = [f"urn%3Ali%3Acountry%3A{country.lower()}" for country in countries]
            countries_param = f"(value:List({','.join(country_urns)}))"
            url += f"&countries={countries_param}"

        response = self._make_request_with_retry(url)

        return response.json()

    def search_ads_by_advertiser(self, advertiser: str, countries: Optional[List[str]] = None,
                                  start: int = 0, count: int = 25) -> Dict:
        """
        Recherche des publicités d'un annonceur spécifique

        Args:
            advertiser: Nom de l'annonceur
            countries: Liste de codes pays (ex: ["FR", "US"])
            start: Index de départ pour la pagination
            count: Nombre de résultats (max 25)

        Returns:
            dict: Réponse de l'API avec les publicités trouvées
        """
        base_url = f"{self.base_url}/adLibrary"

        # Construire les paramètres de base
        params = {
            "q": "criteria",
            "advertiser": advertiser,
            "start": start,
            "count": min(count, 25)  # Maximum 25 par requête
        }

        # Construire l'URL de base avec urlencode pour les params standards
        url = f"{base_url}?{urlencode(params)}"

        # Ajouter le filtre pays si spécifié
        # Format LinkedIn API: countries=(value:List(urn%3Ali%3Acountry%3Afr))
        # Note: on encode manuellement les ":" en "%3A" mais pas les parenthèses/virgules
        if countries:
            country_urns = [f"urn%3Ali%3Acountry%3A{country.lower()}" for country in countries]
            countries_param = f"(value:List({','.join(country_urns)}))"
            url += f"&countries={countries_param}"

        response = self._make_request_with_retry(url)

        return response.json()

    def extract_ads_data(self, api_response: Dict, keyword: str = None, 
                        advertiser_search: str = None) -> List[Dict]:
        """
        Extrait et formate les données des publicités depuis la réponse API

        Args:
            api_response: Réponse brute de l'API
            keyword: Mot-clé utilisé pour la recherche (optionnel)
            advertiser_search: Nom de l'annonceur recherché (optionnel)

        Returns:
            list: Liste de dictionnaires avec les données formatées
        """
        results = []

        # L'API retourne un dict avec "elements"
        elements = api_response.get("elements", [])

        for ad in elements:
            try:
                # URL de la publicité (champ racine)
                ad_url = ad.get("adUrl")
                is_restricted = ad.get("isRestricted", False)
                restriction_details = ad.get("restrictionDetails")

                # Détails de la publicité
                details = ad.get("details", {})

                # Informations sur l'annonceur (dans details.advertiser)
                advertiser_info = details.get("advertiser", {})
                advertiser_name = advertiser_info.get("advertiserName")
                advertiser_url = advertiser_info.get("advertiserUrl")

                # Ad payer (pas dans la doc, mettre advertiser par défaut)
                ad_payer = advertiser_name

                # Type de publicité (dans details.type)
                ad_type = details.get("type")

                # Statistiques (dans details.adStatistics)
                ad_statistics = details.get("adStatistics", {})

                # Dates d'impression (timestamps en millisecondes)
                first_impression = ad_statistics.get("firstImpressionAt")
                latest_impression = ad_statistics.get("latestImpressionAt")

                first_impression_date = None
                latest_impression_date = None

                if first_impression:
                    first_impression_date = datetime.fromtimestamp(first_impression / 1000).date()

                if latest_impression:
                    latest_impression_date = datetime.fromtimestamp(latest_impression / 1000).date()

                # Impressions
                total_impressions = ad_statistics.get("totalImpressions", {})
                total_impressions_range = None
                if total_impressions:
                    impressions_from = total_impressions.get("from", 0)
                    impressions_to = total_impressions.get("to", 0)
                    total_impressions_range = f"{impressions_from}-{impressions_to}"

                # Distribution par pays
                impressions_by_country = ad_statistics.get("impressionsDistributionByCountry", [])
                impressions_distribution = json.dumps(impressions_by_country) if impressions_by_country else None

                # Targeting / Facets (dans details.adTargeting - c'est une liste)
                ad_targeting = details.get("adTargeting", [])
                facet_name = None
                is_inclusive = None
                inclusive_segments = None
                is_exclusive = None
                exclusive_segments = None

                if ad_targeting:
                    # Prendre le premier targeting (peut être étendu pour gérer plusieurs)
                    targeting = ad_targeting[0]
                    facet_name = targeting.get("facetName")

                    if targeting.get("isIncluded"):
                        is_inclusive = "true"
                        included_segs = targeting.get("includedSegments", [])
                        inclusive_segments = json.dumps(included_segs) if included_segs else None

                    if targeting.get("isExcluded"):
                        is_exclusive = "true"
                        excluded_segs = targeting.get("excludedSegments", [])
                        exclusive_segments = json.dumps(excluded_segs) if excluded_segs else None

                # Contexte de pagination
                paging_context = None
                if isinstance(api_response, dict):
                    paging = api_response.get("paging")
                    if isinstance(paging, dict):
                        links = paging.get("links")
                        if isinstance(links, list):
                            # Chercher le lien avec rel='next'
                            for link in links:
                                if isinstance(link, dict) and link.get("rel") == "next":
                                    paging_context = link.get("href")
                                    break
                        elif isinstance(links, dict):
                            paging_context = links.get("next")

                # Date range (si spécifiée dans la recherche)
                date_range = None
                if isinstance(api_response, dict) and api_response.get("metadata"):
                    date_range = api_response.get("metadata", {}).get("dateRange")

                # Pays (depuis les paramètres de recherche)
                countries = None
                if isinstance(api_response, dict) and api_response.get("metadata"):
                    countries_list = api_response.get("metadata", {}).get("countries", [])
                    if countries_list:
                        countries = ",".join(countries_list)

                result = {
                    "keyword": keyword,
                    "countries": countries,
                    "advertiser": advertiser_search,
                    "date_range": date_range,
                    "paging_context": paging_context,
                    "ad_url": ad_url,
                    "is_restricted": is_restricted,
                    "restriction_details": restriction_details,
                    "advertiser_name": advertiser_name,
                    "advertiser_url": advertiser_url,
                    "ad_payer": ad_payer,
                    "facet_name": facet_name,
                    "is_inclusive": is_inclusive,
                    "inclusive_segments": inclusive_segments,
                    "is_exclusive": is_exclusive,
                    "exclusive_segments": exclusive_segments,
                    "first_impression_date": first_impression_date,
                    "latest_impression_date": latest_impression_date,
                    "total_impressions_range": total_impressions_range,
                    "impressions_distribution_by_country": impressions_distribution,
                    "ad_type": ad_type,
                    "retrieved_at": datetime.now(),
                }

                results.append(result)

            except Exception as e:
                print(f"❌ Erreur lors du traitement d'une publicité: {e}")
                print(f"   URL de la publicité: {ad.get('adUrl', 'N/A')}")
                continue  # Continuer avec la publicité suivante au lieu de tout arrêter
        
        return results

    def search_all_ads(self, keyword: str = None, advertiser: str = None,
                      countries: Optional[List[str]] = None, 
                      max_results: int = 500) -> List[Dict]:
        """
        Recherche toutes les publicités avec pagination automatique

        Args:
            keyword: Mot-clé à rechercher (optionnel)
            advertiser: Nom de l'annonceur (optionnel)
            countries: Liste de codes pays
            max_results: Nombre maximum de résultats à récupérer

        Returns:
            list: Liste complète des publicités formatées
        """
        all_ads = []
        start = 0
        count = 25  # Maximum par requête selon l'API LinkedIn
        
        while start < max_results:
            print(f"  → Récupération des résultats {start} à {start + count}...")
            
            if keyword:
                response = self.search_ads_by_keyword(
                    keyword=keyword,
                    countries=countries,
                    start=start,
                    count=count
                )
            elif advertiser:
                response = self.search_ads_by_advertiser(
                    advertiser=advertiser,
                    countries=countries,
                    start=start,
                    count=count
                )
            else:
                raise ValueError("Vous devez spécifier soit un keyword, soit un advertiser")
            
            # Extraire les données
            ads = self.extract_ads_data(response, keyword=keyword, advertiser_search=advertiser)
            
            if not ads:
                print(f"  ✓ Aucune publicité supplémentaire trouvée")
                break
            
            all_ads.extend(ads)
            print(f"  ✓ {len(ads)} publicité(s) récupérée(s)")
            
            # Vérifier s'il y a d'autres résultats
            if isinstance(response, dict):
                paging = response.get("paging")
                has_next = False

                if isinstance(paging, dict):
                    links = paging.get("links")
                    if isinstance(links, list):
                        # Chercher un lien avec rel='next'
                        has_next = any(
                            link.get("rel") == "next"
                            for link in links
                            if isinstance(link, dict)
                        )
                    elif isinstance(links, dict):
                        has_next = bool(links.get("next"))

                if not has_next:
                    print(f"  ✓ Toutes les publicités ont été récupérées")
                    break
            else:
                # Pas de pagination disponible dans la réponse
                print(f"  ✓ Toutes les publicités ont été récupérées")
                break
            
            start += count
        
        return all_ads

    def export_to_csv(self, data: List[Dict], filename: str):
        """Exporte les données au format CSV"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"✓ Données exportées: {filename}")

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données au format JSON"""
        if not data:
            print(f"⚠️  Aucune donnée à exporter")
            return
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"✓ Données exportées: {filename}")

    def _get_bigquery_client(self) -> bigquery.Client:
        """Initialise et retourne le client BigQuery"""
        if self.bq_client is None:
            if self.credentials_path:
                from google.oauth2 import service_account
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
                self.bq_client = bigquery.Client(
                    credentials=credentials,
                    project=self.project_id or credentials.project_id
                )
            elif self.project_id:
                self.bq_client = bigquery.Client(project=self.project_id)
            else:
                self.bq_client = bigquery.Client()
        return self.bq_client

    def upload_to_bigquery(self, data: List[Dict], table_name: str = "ads_library",
                          write_disposition: str = "WRITE_APPEND") -> None:
        """
        Upload les données vers BigQuery

        Args:
            data: Données à uploader (liste de dictionnaires)
            table_name: Nom de la table (défaut: ads_library)
            write_disposition: Mode d'écriture (WRITE_APPEND, WRITE_TRUNCATE, WRITE_EMPTY)
        """
        if not data:
            print(f"⚠️  Aucune donnée à uploader")
            return

        try:
            client = self._get_bigquery_client()

            # Préparer les données pour BigQuery
            df = pd.DataFrame(data)

            # Convertir les colonnes date
            for col in ['first_impression_date', 'latest_impression_date']:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce').dt.date

            # Convertir retrieved_at en timestamp UTC (type TIMESTAMP pour BigQuery)
            if 'retrieved_at' in df.columns:
                df['retrieved_at'] = pd.to_datetime(df['retrieved_at'], utc=True)

            # Construire le nom complet de la table
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            # Définir le schéma explicitement pour éviter les conflits de types
            schema = [
                bigquery.SchemaField("keyword", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("countries", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("advertiser", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("date_range", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("paging_context", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("ad_url", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("is_restricted", "BOOLEAN", mode="NULLABLE"),
                bigquery.SchemaField("restriction_details", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("advertiser_name", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("advertiser_url", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("ad_payer", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("facet_name", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("is_inclusive", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("inclusive_segments", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("is_exclusive", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("exclusive_segments", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("first_impression_date", "DATE", mode="NULLABLE"),
                bigquery.SchemaField("latest_impression_date", "DATE", mode="NULLABLE"),
                bigquery.SchemaField("total_impressions_range", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("impressions_distribution_by_country", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("ad_type", "STRING", mode="NULLABLE"),
                bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="NULLABLE"),
            ]

            # Configuration du job
            job_config = bigquery.LoadJobConfig(
                schema=schema,
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED"
            )

            # Upload vers BigQuery
            print(f"\n→ Upload vers BigQuery: {table_id}")
            print(f"  Nombre de lignes: {len(df)}")

            job = client.load_table_from_dataframe(
                df,
                table_id,
                job_config=job_config
            )

            # Attendre la fin du job
            job.result()

            # Vérifier le résultat
            table = client.get_table(table_id)
            print(f"✓ Upload réussi! Total lignes dans la table: {table.num_rows:,}")

        except Exception as e:
            print(f"✗ Erreur lors de l'upload vers BigQuery: {e}")
            import traceback
            traceback.print_exc()
            raise


def main():
    """
    Exemple d'utilisation du client LinkedIn Ads Library
    """

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    config = load_config()

    # Récupérer les configurations
    linkedin_config = config.get_linkedin_config()
    google_config = config.get_google_cloud_config()

    # Récupérer l'access token depuis la configuration
    ACCESS_TOKEN = linkedin_config.get('access_token')
    if not ACCESS_TOKEN:
        print("❌ ERREUR: access_token LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'access_token' dans la section linkedin.oauth")
        return

    # Configuration BigQuery
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['linkedin_ads_library']
    CREDENTIALS_PATH = google_config['credentials_file']

    # Configuration de la recherche depuis le YAML
    ads_library_config = linkedin_config.get('ads_library', {})
    KEYWORDS = ads_library_config.get('keywords', [])
    ADVERTISERS = ads_library_config.get('advertisers', [])
    COUNTRIES = ads_library_config.get('countries', ['fr'])
    MAX_RESULTS_PER_SEARCH = ads_library_config.get('max_results_per_search', 500)
    REQUEST_DELAY = ads_library_config.get('request_delay', 2.0)  # Délai entre requêtes en secondes

    print("=" * 70)
    print("LINKEDIN ADS LIBRARY - RECHERCHE PUBLICITAIRE")
    print("=" * 70)
    print(f"\nBigQuery: {PROJECT_ID}.{DATASET_ID}")
    print(f"\nConfiguration de recherche:")
    print(f"  - Mots-clés: {len(KEYWORDS)} ({', '.join(KEYWORDS[:3])}{'...' if len(KEYWORDS) > 3 else ''})")
    print(f"  - Annonceurs: {len(ADVERTISERS)} ({', '.join(ADVERTISERS[:3])}{'...' if len(ADVERTISERS) > 3 else 'Aucun'})")
    print(f"  - Pays: {', '.join(COUNTRIES)}")
    print(f"  - Max résultats/recherche: {MAX_RESULTS_PER_SEARCH}")
    print(f"  - Délai entre requêtes: {REQUEST_DELAY}s\n")

    # Initialiser le client
    client = LinkedInAdsLibraryClient(
        access_token=ACCESS_TOKEN,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH,
        request_delay=REQUEST_DELAY
    )

    # Vérifier qu'au moins une recherche est configurée
    if not KEYWORDS and not ADVERTISERS:
        print("⚠️  Aucun critère de recherche configuré !")
        print("   Veuillez ajouter des keywords ou des advertisers dans config.yaml")
        print("   Section: linkedin.ads_library.keywords ou linkedin.ads_library.advertisers")
        return

    all_results = []

    # Étape 1: Recherche par mots-clés
    if KEYWORDS:
        print("=" * 70)
        print("1. Recherche par mots-clés")
        print("=" * 70)
        print(f"   {len(KEYWORDS)} mot(s)-clé(s) à rechercher\n")
        
        for keyword in KEYWORDS:
            print(f"\n→ Recherche pour le mot-clé: '{keyword}'")
            
            try:
                ads = client.search_all_ads(
                    keyword=keyword,
                    countries=COUNTRIES,
                    max_results=MAX_RESULTS_PER_SEARCH
                )
                
                print(f"✓ Total: {len(ads)} publicité(s) trouvée(s)")
                all_results.extend(ads)
                
            except Exception as e:
                print(f"✗ Erreur pour '{keyword}': {e}")

    # Étape 2: Recherche par annonceurs
    if ADVERTISERS:
        print("\n" + "=" * 70)
        print("2. Recherche par annonceurs")
        print("=" * 70)
        print(f"   {len(ADVERTISERS)} annonceur(s) à surveiller\n")
        
        for advertiser in ADVERTISERS:
            print(f"\n→ Recherche pour l'annonceur: '{advertiser}'")
            
            try:
                ads = client.search_all_ads(
                    advertiser=advertiser,
                    countries=COUNTRIES,
                    max_results=MAX_RESULTS_PER_SEARCH
                )
                
                print(f"✓ Total: {len(ads)} publicité(s) trouvée(s)")
                all_results.extend(ads)
                
            except Exception as e:
                print(f"✗ Erreur pour '{advertiser}': {e}")

    # Étape 3: Export et Upload
    if all_results:
        print("\n" + "=" * 70)
        print("3. Export et Upload")
        print("=" * 70)
        
        print(f"\n✓ Total collecté: {len(all_results)} publicité(s)")
        
        # Dédupliquer par ad_url
        unique_ads = {}
        for ad in all_results:
            ad_url = ad.get('ad_url')
            if ad_url and ad_url not in unique_ads:
                unique_ads[ad_url] = ad
        
        deduplicated_results = list(unique_ads.values())
        print(f"✓ Après déduplication: {len(deduplicated_results)} publicité(s) unique(s)")
        
        # Exporter
        client.export_to_json(deduplicated_results, "ads_library.json")
        client.export_to_csv(deduplicated_results, "ads_library.csv")
        
        # Upload vers BigQuery
        client.upload_to_bigquery(deduplicated_results)
        
        print("\n" + "=" * 70)
        print("✓ COLLECTE TERMINÉE!")
        print("=" * 70)
        print(f"📊 Fichiers locaux créés:")
        print(f"   - ads_library.json / .csv")
        print(f"☁️  Données uploadées dans BigQuery:")
        print(f"   - {PROJECT_ID}.{DATASET_ID}.ads_library")
    else:
        print("\n⚠️  Aucune publicité trouvée")


if __name__ == "__main__":
    main()
