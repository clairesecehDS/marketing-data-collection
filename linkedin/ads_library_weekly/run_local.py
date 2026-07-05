#!/usr/bin/env python3
"""
Script pour exécuter LinkedIn Ads Library en local
"""

import sys
import os

# Ajouter le dossier scripts au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 Démarrage de LinkedIn Ads Library (LOCAL)")
    print("=" * 70)
    print("")

    try:
        from scripts import linkedin_ads_library
        print("🔍 Lancement de la collecte Ads Library...")
        linkedin_ads_library.main()
        print("")
        print("=" * 70)
        print("✅ Collecte terminée avec succès!")
        print("=" * 70)
    except Exception as e:
        print("")
        print("=" * 70)
        print(f"❌ Erreur: {str(e)}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        sys.exit(1)
