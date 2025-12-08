"""
Cloud Function pour exécuter LinkedIn Ads Library de manière hebdomadaire
Déploiement: gcloud functions deploy linkedin-weekly-ads-library --runtime python311 --trigger-http --entry-point main
"""

import functions_framework
import sys
import os

# Ajouter le path pour importer les modules
sys.path.insert(0, os.path.dirname(__file__))

@functions_framework.http
def main(request):
    """Point d'entrée HTTP pour Cloud Functions - Exécute Ads Library (hebdomadaire)"""

    results = {
        "ads_library": None
    }

    # Script : Ads Library
    try:
        from scripts import linkedin_ads_library

        print("\n" + "=" * 70)
        print("🚀 Démarrage de la synchronisation Ads Library (hebdomadaire)...")
        print("=" * 70)
        linkedin_ads_library.main()
        results["ads_library"] = "success"
        print("\n✅ Ads Library terminé avec succès\n")

    except Exception as e:
        print(f"\n❌ Erreur Ads Library: {str(e)}")
        import traceback
        traceback.print_exc()
        results["ads_library"] = f"error: {str(e)}"

    # Résumé final
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DE LA SYNCHRONISATION HEBDOMADAIRE")
    print("=" * 70)
    for script_name, status in results.items():
        icon = "✅" if status == "success" else "❌"
        print(f"{icon} {script_name}: {status}")
    print("=" * 70 + "\n")

    # Déterminer le statut global
    if results["ads_library"] == "success":
        return {
            "status": "success",
            "message": "Ads Library exécuté avec succès",
            "details": results
        }, 200
    else:
        return {
            "status": "error",
            "message": "Ads Library a échoué",
            "details": results
        }, 500
