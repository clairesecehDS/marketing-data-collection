"""
Cloud Function pour exécuter le script Clarity de manière automatisée
Déploiement: gcloud functions deploy clarity-daily-sync --runtime python311 --trigger-http --entry-point main
"""

import functions_framework
import sys
import os

# Ajouter le path pour importer les modules
sys.path.insert(0, os.path.dirname(__file__))

@functions_framework.http
def main(request):
    """Point d'entrée HTTP pour Cloud Functions"""
    try:
        # Importer et exécuter le script principal
        from scripts import clarity_analytics

        print("🚀 Démarrage de la synchronisation Clarity...")
        clarity_analytics.main()

        return {
            "status": "success",
            "message": "Synchronisation Clarity terminée avec succès"
        }, 200

    except Exception as e:
        print(f"❌ Erreur lors de la synchronisation: {str(e)}")
        import traceback
        traceback.print_exc()

        return {
            "status": "error",
            "message": f"Erreur: {str(e)}"
        }, 500
