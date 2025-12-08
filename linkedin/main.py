"""
Cloud Function pour exécuter plusieurs scripts LinkedIn de manière automatisée
Déploiement: gcloud functions deploy linkedin-daily-sync --runtime python311 --trigger-http --entry-point main
"""

import functions_framework
import sys
import os

# Ajouter le path pour importer les modules
sys.path.insert(0, os.path.dirname(__file__))

@functions_framework.http
def main(request):
    """Point d'entrée HTTP pour Cloud Functions - Exécute 3 scripts LinkedIn quotidiens"""

    results = {
        "campaign_analytics": None,
        "lead_forms": None,
        "budget": None
    }

    # Script 1: Campaign Analytics
    try:
        from scripts import linkedin_campaign_analytics

        print("\n" + "=" * 70)
        print("🚀 [1/3] Démarrage de la synchronisation Campaign Analytics...")
        print("=" * 70)
        linkedin_campaign_analytics.main()
        results["campaign_analytics"] = "success"
        print("\n✅ Campaign Analytics terminé avec succès\n")

    except Exception as e:
        print(f"\n❌ Erreur Campaign Analytics: {str(e)}")
        import traceback
        traceback.print_exc()
        results["campaign_analytics"] = f"error: {str(e)}"

    # Script 2: Lead Forms
    try:
        from scripts import linkedin_lead_forms

        print("\n" + "=" * 70)
        print("🚀 [2/3] Démarrage de la synchronisation Lead Forms...")
        print("=" * 70)
        linkedin_lead_forms.main()
        results["lead_forms"] = "success"
        print("\n✅ Lead Forms terminé avec succès\n")

    except Exception as e:
        print(f"\n❌ Erreur Lead Forms: {str(e)}")
        import traceback
        traceback.print_exc()
        results["lead_forms"] = f"error: {str(e)}"

    # Script 3: Budget & Bidding
    try:
        from scripts import linkedin_budget

        print("\n" + "=" * 70)
        print("🚀 [3/3] Démarrage de la synchronisation Budget & Bidding...")
        print("=" * 70)
        linkedin_budget.main()
        results["budget"] = "success"
        print("\n✅ Budget & Bidding terminé avec succès\n")

    except Exception as e:
        print(f"\n❌ Erreur Budget & Bidding: {str(e)}")
        import traceback
        traceback.print_exc()
        results["budget"] = f"error: {str(e)}"

    # Résumé final
    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DE LA SYNCHRONISATION")
    print("=" * 70)
    for script_name, status in results.items():
        icon = "✅" if status == "success" else "❌"
        print(f"{icon} {script_name}: {status}")
    print("=" * 70 + "\n")

    # Déterminer le statut global
    all_success = all(status == "success" for status in results.values())

    if all_success:
        return {
            "status": "success",
            "message": "Tous les scripts LinkedIn ont été exécutés avec succès",
            "details": results
        }, 200
    else:
        return {
            "status": "partial_success" if any(status == "success" for status in results.values()) else "error",
            "message": "Certains scripts ont échoué",
            "details": results
        }, 207  # 207 = Multi-Status
