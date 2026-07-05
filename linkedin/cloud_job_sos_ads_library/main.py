#!/usr/bin/env python3
"""
Point d'entrée pour Cloud Run Job - LinkedIn Ads Library SOS (hebdomadaire)
Exécute le script ads_library avec la config SOS
"""

import sys
import os
import requests
from datetime import datetime
from google.cloud import bigquery
import pandas as pd

# Ajouter les chemins nécessaires
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

# Importer les modules nécessaires
from config_loader import load_config

def main():
    """Point d'entrée pour Cloud Run Job - Exécute Ads Library (hebdomadaire)"""

    print("=" * 70)
    print("🚀 Démarrage de la synchronisation LinkedIn Ads Library SOS (hebdomadaire)")
    print("=" * 70)
    print("")

    try:
        print("📋 Chargement de la configuration...")
        # Charger la configuration depuis /app/config.yaml
        config_path = '/app/config.yaml'
        if not os.path.exists(config_path):
            print(f"❌ Fichier de configuration non trouvé : {config_path}")
            return 1

        config = load_config(config_path, skip_credentials_check=True)

        # Récupérer les configurations
        linkedin_config = config.get_linkedin_config()
        google_config = config.get_google_cloud_config()

        # Importer la classe LinkedInAdsLibraryClient
        from scripts.linkedin_ads_library import LinkedInAdsLibraryClient

        # Récupérer l'access token
        ACCESS_TOKEN = linkedin_config.get('access_token')
        if not ACCESS_TOKEN:
            print("❌ ERREUR: access_token LinkedIn non configuré dans config.yaml")
            return 1

        # Configuration BigQuery
        PROJECT_ID = google_config['project_id']
        DATASET_ID = google_config['datasets']['linkedin_ads_library']

        # Configuration de recherche
        ads_library_config = linkedin_config.get('ads_library', {})
        ADVERTISERS = ads_library_config.get('advertisers', [])
        COUNTRIES = ads_library_config.get('countries', ['us'])
        MAX_RESULTS_PER_SEARCH = ads_library_config.get('max_results_per_search', 500)
        REQUEST_DELAY = ads_library_config.get('request_delay', 2.0)

        print(f"\nBigQuery: {PROJECT_ID}.{DATASET_ID}")
        print(f"\nConfiguration de recherche:")
        print(f"  - Annonceurs: {len(ADVERTISERS)}")
        print(f"  - Pays: {', '.join(COUNTRIES)}")
        print(f"  - Max résultats/recherche: {MAX_RESULTS_PER_SEARCH}")

        # Initialiser le client (credentials automatiques via GOOGLE_APPLICATION_CREDENTIALS)
        client = LinkedInAdsLibraryClient(
            access_token=ACCESS_TOKEN,
            project_id=PROJECT_ID,
            dataset_id=DATASET_ID,
            credentials_path=None,  # Utilise les credentials par défaut
            request_delay=REQUEST_DELAY
        )

        if not ADVERTISERS:
            print("⚠️  Aucun annonceur configuré !")
            return 1

        all_results = []

        # Recherche par annonceurs
        print("\n" + "=" * 70)
        print("Recherche par annonceurs")
        print("=" * 70)

        for advertiser in ADVERTISERS:
            print(f"\n→ Recherche pour: '{advertiser}'")
            try:
                ads = client.search_all_ads(
                    advertiser=advertiser,
                    countries=COUNTRIES,
                    date_range=None,
                    max_results=MAX_RESULTS_PER_SEARCH
                )
                print(f"✓ Total trouvé: {len(ads)} publicité(s)")
                all_results.extend(ads)
            except Exception as e:
                print(f"✗ Erreur pour '{advertiser}': {e}")

        # Export et Upload
        if all_results:
            print(f"\n✓ Total collecté: {len(all_results)} publicité(s)")

            # Dédupliquer
            unique_ads = {}
            for ad in all_results:
                ad_url = ad.get('ad_url')
                if ad_url and ad_url not in unique_ads:
                    unique_ads[ad_url] = ad

            deduplicated_results = list(unique_ads.values())
            print(f"✓ Après déduplication: {len(deduplicated_results)} publicité(s) unique(s)")

            # Upload vers BigQuery — WRITE_TRUNCATE pour rafraîchir toutes les données à chaque run
            client.upload_to_bigquery(deduplicated_results, write_disposition="WRITE_TRUNCATE", deduplicate=False)

            print("\n" + "=" * 70)
            print("✓ COLLECTE TERMINÉE!")
            print("=" * 70)
            print(f"☁️  Données uploadées dans BigQuery:")
            print(f"   - {PROJECT_ID}.{DATASET_ID}.ads_library")
        else:
            print("\n⚠️  Aucune publicité trouvée")

        print("✅ Ads Library exécuté avec succès")
        return 0

    except Exception as e:
        print(f"❌ Erreur Ads Library: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
