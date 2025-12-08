#!/usr/bin/env python3
"""
Point d'entrée pour Cloud Function - LinkedIn Ads Library (hebdomadaire)
Exécute uniquement le script ads_library
"""

import functions_framework
import sys
import os

# Ajouter le dossier scripts au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

@functions_framework.http
def main(request):
    """Point d'entrée HTTP pour Cloud Functions - Exécute Ads Library (hebdomadaire)"""

    print("=" * 70)
    print("🚀 Démarrage de la synchronisation LinkedIn Ads Library (hebdomadaire)")
    print("=" * 70)
    print("")

    results = {"ads_library": None}

    # Script: Ads Library
    try:
        from scripts import linkedin_ads_library
        print("🔍 Démarrage de la synchronisation Ads Library...")
        linkedin_ads_library.main()
        results["ads_library"] = "success"
        print("✅ Ads Library exécuté avec succès")
    except Exception as e:
        print(f"❌ Erreur Ads Library: {str(e)}")
        import traceback
        traceback.print_exc()
        results["ads_library"] = f"error: {str(e)}"

    print("")
    print("=" * 70)
    print("📊 Résumé de l'exécution hebdomadaire")
    print("=" * 70)

    if results["ads_library"] == "success":
        print("✅ Ads Library: Succès")
        return {"status": "success", "message": "Ads Library exécuté avec succès", "results": results}, 200
    else:
        print(f"❌ Ads Library: {results['ads_library']}")
        return {"status": "error", "message": "Ads Library a échoué", "results": results}, 500
