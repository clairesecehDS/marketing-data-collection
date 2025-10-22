#!/usr/bin/env python3
"""
Script de setup BigQuery - Création des tables et vues
Lit le Project ID depuis config.yaml et génère/exécute les fichiers SQL
"""

import os
import sys
import re
import subprocess
from pathlib import Path
from config_loader import load_config


def replace_project_id_in_sql(sql_content: str, project_id: str) -> str:
    """
    Remplace tous les project IDs hardcodés dans le SQL par le vrai project ID

    Patterns détectés :
    - `project-id.dataset.table`
    - `project-id`.dataset.table
    - project-id.dataset.table
    """
    # Pattern pour détecter les anciens project IDs
    # Cherche des patterns comme clean-avatar-466709-a0, votre-project-id, etc.
    pattern = r'`?[\w\-]+\.(linkedin_|microsoft_|spyfu)'

    def replacer(match):
        # Remplace l'ancien project ID par le nouveau
        matched = match.group(0)
        if matched.startswith('`'):
            return f'`{project_id}.{match.group(1)}'
        else:
            return f'{project_id}.{match.group(1)}'

    # Remplacer tous les patterns trouvés
    updated_sql = re.sub(pattern, replacer, sql_content)

    return updated_sql


def generate_sql_file(source_file: Path, output_file: Path, project_id: str):
    """
    Génère un fichier SQL avec le bon Project ID
    """
    print(f"  → Génération: {source_file.name}")

    # Lire le fichier SQL source
    with open(source_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()

    # Remplacer le project ID
    updated_sql = replace_project_id_in_sql(sql_content, project_id)

    # Écrire le fichier généré
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(updated_sql)

    print(f"  ✓ Généré: {output_file.name}")


def execute_sql_file(sql_file: Path, use_bq_cli: bool = True):
    """
    Exécute un fichier SQL via bq CLI ou affiche les instructions
    """
    if use_bq_cli:
        print(f"  → Exécution: {sql_file.name}")
        try:
            result = subprocess.run(
                ['bq', 'query', '--use_legacy_sql=false'],
                stdin=open(sql_file),
                capture_output=True,
                text=True,
                check=True
            )
            print(f"  ✓ Exécuté: {sql_file.name}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Erreur lors de l'exécution de {sql_file.name}")
            print(f"    {e.stderr}")
            return False
        except FileNotFoundError:
            print("  ⚠️  bq CLI non trouvé. Installez gcloud SDK.")
            print("     https://cloud.google.com/sdk/docs/install")
            return False
    else:
        print(f"  → À exécuter manuellement: {sql_file.name}")
        return None


def main():
    print("=" * 70)
    print("SETUP BIGQUERY - Création des tables et vues")
    print("=" * 70)

    # Charger la configuration
    print("\n1. Chargement de la configuration...")
    try:
        config = load_config()
        google_config = config.get_google_cloud_config()
        project_id = google_config['project_id']
        print(f"   ✓ Project ID: {project_id}")
    except Exception as e:
        print(f"   ✗ Erreur: {e}")
        print("\n   Créez config.yaml depuis config.example.yaml")
        sys.exit(1)

    # Créer le dossier de sortie pour les SQL générés
    output_dir = Path("./generated_sql")
    output_dir.mkdir(exist_ok=True)
    print(f"   ✓ Dossier de sortie: {output_dir}")

    # Liste des fichiers SQL à traiter
    sql_files = [
        ("linkedin/sql/bigquery_campaign_creative_schema.sql", "LinkedIn Ads Advertising (Analytics)"),
        ("linkedin/sql/bigquery_campaign_creative_budget_schema.sql", "LinkedIn Ads Advertising (Budgets)"),
        ("linkedin/sql/bigquery_lead_forms_schema.sql", "LinkedIn Lead Gen Forms"),
        ("linkedin/sql/bigquery_linkedin_page_schema.sql", "LinkedIn Page Statistics"),
        ("linkedin/sql/bigquery_ads_library_schema.sql", "LinkedIn Ads Library"),
        ("microsoft_clarity/sql/bigquery_clarity_schema.sql", "Microsoft Clarity"),
        ("spyfu/sql/bigquery_spyfu_schema.sql", "SpyFu"),
    ]

    print(f"\n2. Génération des fichiers SQL avec Project ID...")
    generated_files = []

    for sql_file, description in sql_files:
        source_path = Path(sql_file)

        if not source_path.exists():
            print(f"  ⚠️  Fichier non trouvé: {sql_file}")
            continue

        output_path = output_dir / source_path.name

        try:
            generate_sql_file(source_path, output_path, project_id)
            generated_files.append((output_path, description))
        except Exception as e:
            print(f"  ✗ Erreur: {e}")

    print(f"\n   ✓ {len(generated_files)} fichiers SQL générés")

    # Demander si on veut exécuter via bq CLI
    print("\n3. Exécution des fichiers SQL")
    print("\nComment voulez-vous exécuter les fichiers SQL ?")
    print("  [1] Via bq CLI (automatique - nécessite gcloud SDK)")
    print("  [2] Manuellement (afficher les instructions)")
    print("  [3] Annuler")

    choice = input("\nChoix (1/2/3): ").strip()

    if choice == '1':
        print("\n→ Exécution automatique via bq CLI...\n")
        success_count = 0
        for sql_file, description in generated_files:
            print(f"  {description}:")
            if execute_sql_file(sql_file, use_bq_cli=True):
                success_count += 1
            print()

        print(f"✓ {success_count}/{len(generated_files)} fichiers exécutés avec succès")

    elif choice == '2':
        print("\n→ Instructions pour exécution manuelle:\n")
        print("Option A - Via bq CLI:")
        print("-" * 70)
        print("# Authentification")
        print("gcloud auth login")
        print(f"gcloud config set project {project_id}\n")

        for sql_file, description in generated_files:
            print(f"# {description}")
            print(f"bq query --use_legacy_sql=false < {sql_file}\n")

        print("\nOption B - Via BigQuery Console:")
        print("-" * 70)
        print("1. Aller sur https://console.cloud.google.com/bigquery")
        print(f"2. Sélectionner le projet: {project_id}")
        print("3. Cliquer sur 'Studio' ou '+'")
        print("4. Pour chaque fichier dans generated_sql/:")
        print("   - Copier le contenu")
        print("   - Coller dans l'éditeur")
        print("   - Cliquer sur 'Run'\n")

        for sql_file, description in generated_files:
            print(f"   • {sql_file.name} - {description}")

    else:
        print("\n✗ Annulé")

    print("\n" + "=" * 70)
    print("TERMINÉ")
    print("=" * 70)
    print(f"\nFichiers SQL générés dans: {output_dir.absolute()}")
    print("Ces fichiers utilisent votre Project ID depuis config.yaml")


if __name__ == "__main__":
    main()
