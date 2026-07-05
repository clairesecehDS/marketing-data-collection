#!/usr/bin/env python3
"""
Script pour générer automatiquement la documentation des tables BigQuery.
Ce script liste tous les datasets, tables et leurs schémas (colonnes/métriques).
"""

from google.cloud import bigquery
from google.oauth2 import service_account
import json
from typing import Dict, List
from collections import defaultdict

# Configuration
PROJECT_ID = "ecoledesponts"
CREDENTIALS_PATH = "account-key.json"


def get_bigquery_client():
    """Crée un client BigQuery avec les credentials."""
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/bigquery"]
    )
    return bigquery.Client(credentials=credentials, project=PROJECT_ID)


def get_all_datasets(client: bigquery.Client) -> List[str]:
    """Liste tous les datasets du projet."""
    datasets = list(client.list_datasets())
    return [dataset.dataset_id for dataset in datasets]


def get_tables_in_dataset(client: bigquery.Client, dataset_id: str) -> List[str]:
    """Liste toutes les tables d'un dataset."""
    tables = client.list_tables(dataset_id)
    return [table.table_id for table in tables]


def get_table_schema(client: bigquery.Client, dataset_id: str, table_id: str) -> List[Dict]:
    """Récupère le schéma d'une table."""
    table_ref = f"{PROJECT_ID}.{dataset_id}.{table_id}"
    table = client.get_table(table_ref)

    schema_info = []
    for field in table.schema:
        schema_info.append({
            'name': field.name,
            'type': field.field_type,
            'mode': field.mode,
            'description': field.description or ''
        })

    return schema_info


def generate_markdown_documentation(data: Dict) -> str:
    """Génère la documentation Markdown."""
    markdown = []
    markdown.append("## 📊 Schémas des Tables BigQuery\n")
    markdown.append(f"**Projet:** `{PROJECT_ID}`\n")
    markdown.append("")

    # Trier les datasets par nom
    for dataset_id in sorted(data.keys()):
        tables = data[dataset_id]
        markdown.append(f"### Dataset: `{dataset_id}`\n")

        # Trier les tables par nom
        for table_id in sorted(tables.keys()):
            schema = tables[table_id]
            markdown.append(f"#### Table: `{table_id}`\n")
            markdown.append(f"**Nombre de colonnes:** {len(schema)}\n")
            markdown.append("")

            # Tableau des colonnes
            markdown.append("| Colonne | Type | Mode | Description |")
            markdown.append("|---------|------|------|-------------|")

            for field in schema:
                name = field['name']
                field_type = field['type']
                mode = field['mode']
                description = field['description'] or '-'
                markdown.append(f"| `{name}` | {field_type} | {mode} | {description} |")

            markdown.append("")

        markdown.append("---\n")

    return "\n".join(markdown)


def main():
    """Fonction principale."""
    print(f"🔍 Connexion au projet BigQuery: {PROJECT_ID}")

    try:
        client = get_bigquery_client()
        print("✅ Connexion réussie\n")

        # Collecter toutes les informations
        all_data = defaultdict(dict)

        print("📦 Récupération des datasets...")
        datasets = get_all_datasets(client)
        print(f"   Trouvé {len(datasets)} dataset(s): {', '.join(datasets)}\n")

        for dataset_id in datasets:
            print(f"📋 Dataset: {dataset_id}")
            tables = get_tables_in_dataset(client, dataset_id)
            print(f"   Trouvé {len(tables)} table(s)")

            for table_id in tables:
                print(f"   - {table_id}...", end=" ")
                try:
                    schema = get_table_schema(client, dataset_id, table_id)
                    all_data[dataset_id][table_id] = schema
                    print(f"✅ ({len(schema)} colonnes)")
                except Exception as e:
                    print(f"❌ Erreur: {e}")

            print()

        # Générer la documentation
        print("📝 Génération de la documentation Markdown...")
        markdown_doc = generate_markdown_documentation(all_data)

        # Sauvegarder dans un fichier
        output_file = "BIGQUERY_SCHEMAS.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_doc)

        print(f"✅ Documentation générée: {output_file}")
        print(f"\n💡 Vous pouvez maintenant copier le contenu de {output_file} dans votre README.md")

        # Afficher un aperçu
        print("\n" + "="*80)
        print("APERÇU DE LA DOCUMENTATION:")
        print("="*80)
        print(markdown_doc[:1000] + "\n... (tronqué)")

    except FileNotFoundError:
        print(f"❌ Erreur: Fichier de credentials non trouvé: {CREDENTIALS_PATH}")
        print("   Vérifiez que le fichier existe dans le répertoire courant.")
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
