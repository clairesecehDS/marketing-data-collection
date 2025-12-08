#!/usr/bin/env python3
"""
Point d'entrée pour Cloud Function - SpyFu Quarterly Sync
Exécute les scripts SpyFu trimestriels (1x/trimestre)

Scripts inclus:
- getDomainAdHistory - rowcount=23 + dates (3 derniers mois)
- getTermAdHistoryWithStats - rowcount=7 + dates (3 derniers mois)

Coût estimé: ~$0.001 par concurrent/trimestre (selon document .odt)
"""

import functions_framework
import sys
import os

# Ajouter le dossier scripts au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))
sys.path.insert(0, os.path.dirname(__file__))


@functions_framework.http
def main_quarterly(request):
    """Point d'entrée HTTP pour Cloud Functions - Exécute les scripts SpyFu trimestriels"""

    print("=" * 80)
    print("🚀 Démarrage de la synchronisation SpyFu (trimestrielle)")
    print("=" * 80)
    print("")

    # Liste des scripts à exécuter dans l'ordre
    scripts = [
        ("domain_ad_history", "Historique des annonces par domaine (getDomainAdHistory)"),
        ("term_ad_history", "Historique des annonces par mot-clé (getTermAdHistoryWithStats)")
    ]

    results = {}
    successful = 0
    failed = 0

    for script_name, description in scripts:
        module_name = f"spyfu_{script_name}"
        print("")
        print("=" * 80)
        print(f"📊 [{successful + failed + 1}/{len(scripts)}] {description}")
        print("=" * 80)

        try:
            # Importer dynamiquement le module
            module = __import__(module_name)

            # Exécuter la fonction main du module
            print(f"🔍 Démarrage de {module_name}...")
            module.main()

            results[script_name] = "success"
            successful += 1
            print(f"✅ {description} exécuté avec succès")

        except Exception as e:
            print(f"❌ Erreur {description}: {str(e)}")
            import traceback
            traceback.print_exc()
            results[script_name] = f"error: {str(e)}"
            failed += 1

    # Résumé final
    print("")
    print("=" * 80)
    print("📊 Résumé de l'exécution trimestrielle SpyFu")
    print("=" * 80)
    print(f"✅ Succès: {successful}/{len(scripts)}")
    print(f"❌ Échecs: {failed}/{len(scripts)}")
    print("")

    for script_name, description in scripts:
        status = results.get(script_name, "unknown")
        emoji = "✅" if status == "success" else "❌"
        print(f"{emoji} {description}: {status}")

    print("")
    print("=" * 80)

    # Retourner le statut
    if failed == 0:
        return {
            "status": "success",
            "message": f"Tous les scripts SpyFu trimestriels exécutés avec succès ({successful}/{len(scripts)})",
            "results": results
        }, 200
    elif successful > 0:
        return {
            "status": "partial",
            "message": f"Exécution partielle: {successful} succès, {failed} échecs",
            "results": results
        }, 207  # Multi-Status
    else:
        return {
            "status": "error",
            "message": f"Tous les scripts ont échoué ({failed}/{len(scripts)})",
            "results": results
        }, 500


if __name__ == "__main__":
    # Pour test local
    class MockRequest:
        pass

    main_quarterly(MockRequest())
