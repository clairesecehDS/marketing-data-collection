#!/usr/bin/env python3
"""
Point d'entrée pour Cloud Run Job - LinkedIn Data Collection EPBS (complet)
Exécute tous les scripts en patchant le chemin de config
"""

import sys
import os
from datetime import datetime

# Ajouter les chemins nécessaires
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

# Chemin de configuration dans le container
CONFIG_PATH = '/app/config.yaml'

# Définir une variable d'environnement pour indiquer qu'on est dans Cloud Run Job
# Cela permet aux scripts de détecter l'environnement correctement
os.environ['CLOUD_RUN_JOB'] = 'true'
os.environ['FUNCTION_TARGET'] = 'cloud_run_job'  # Pour compatibilité avec les scripts existants


def run_script(script_name, script_module_name):
    """
    Exécute un script en important son module et en appelant sa fonction main()

    Args:
        script_name: Nom du script pour l'affichage
        script_module_name: Nom du module à importer (ex: 'scripts.linkedin_ads_library')

    Returns:
        bool: True si succès, False si erreur
    """
    print("\n" + "=" * 70)
    print(f"🔄 Exécution: {script_name}")
    print("=" * 70)

    try:
        # Importer le module
        module = __import__(script_module_name, fromlist=['main'])

        # Appeler la fonction main()
        module.main()

        print(f"✅ {script_name} - Succès")
        return True
    except Exception as e:
        print(f"❌ {script_name} - Erreur: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Point d'entrée pour Cloud Run Job"""

    start_time = datetime.now()

    print("=" * 70)
    print("🚀 Démarrage de la synchronisation LinkedIn EPBS (complète)")
    print("=" * 70)
    print(f"Heure de début: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Chemin config: {CONFIG_PATH}")
    print("")

    # Vérifier que le fichier de config existe
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Fichier de configuration non trouvé: {CONFIG_PATH}")
        return 1

    # Lire la variable d'environnement pour savoir quels scripts exécuter
    # Format: "ads_library,budget,campaign_analytics,lead_forms,page_stats"
    # Si non défini, exécute tous les scripts
    scripts_to_run = os.getenv('LINKEDIN_SCRIPTS', 'all')

    # Définir tous les scripts disponibles
    all_scripts = {
        'ads_library': ("LinkedIn Ads Library", "scripts.linkedin_ads_library"),
        'budget': ("LinkedIn Budget", "scripts.linkedin_budget"),
        'campaign_analytics': ("LinkedIn Campaign Analytics", "scripts.linkedin_campaign_analytics"),
        'lead_forms': ("LinkedIn Lead Forms", "scripts.linkedin_lead_forms"),
        'page_stats': ("LinkedIn Page Stats", "scripts.linkedin_page_stats"),
        'sync_stats': ("LinkedIn Page & Follower Stats", "scripts.sync_linkedin_stats"),
    }

    # Déterminer quels scripts exécuter
    if scripts_to_run == 'all':
        selected_scripts = all_scripts
        print("📋 Mode: Exécution de TOUS les scripts")
    else:
        script_names = [s.strip() for s in scripts_to_run.split(',')]
        selected_scripts = {k: v for k, v in all_scripts.items() if k in script_names}
        print(f"📋 Mode: Exécution sélective de {len(selected_scripts)} script(s)")
        print(f"   Scripts: {', '.join(selected_scripts.keys())}")

    print("")

    # Exécuter les scripts sélectionnés
    results = {}
    for script_key, (script_name, module_name) in selected_scripts.items():
        results[script_key] = run_script(script_name, module_name)

    # Résumé
    end_time = datetime.now()
    duration = end_time - start_time

    print("\n" + "=" * 70)
    print("📊 RÉSUMÉ DE L'EXÉCUTION")
    print("=" * 70)
    print(f"Heure de début: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Heure de fin: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Durée totale: {duration}")
    print("")

    success_count = sum(1 for status in results.values() if status)
    total_scripts = len(results)

    for script_name, status in results.items():
        icon = "✅" if status else "❌"
        print(f"  {icon} {script_name}")

    print("")
    print(f"Taux de réussite: {success_count}/{total_scripts} ({100*success_count/total_scripts:.0f}%)")
    print("=" * 70)

    return 0 if success_count == total_scripts else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
