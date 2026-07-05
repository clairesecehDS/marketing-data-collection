#!/usr/bin/env python3
"""
Script pour uploader un fichier JSON existant vers BigQuery
Usage: python upload_json_to_bigquery.py [chemin_vers_fichier.json]
"""

import sys
import os
import json
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from config_loader import load_config


def upload_json_to_bigquery(json_file: str):
    """
    Upload les données d'un fichier JSON vers BigQuery

    Args:
        json_file: Chemin vers le fichier JSON
    """
    # Charger la configuration
    print("📋 Chargement de la configuration...")
    config_loader = load_config()
    
    google_config = config_loader.get_google_cloud_config()
    linkedin_config = config_loader.get_linkedin_config()
    
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['linkedin_ads_library']
    CREDENTIALS_PATH = google_config.get('credentials_file')
    
    table_id = f"{PROJECT_ID}.{DATASET_ID}.ads_library"
    
    print(f"📂 Lecture du fichier: {json_file}")
    
    # Charger les données JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        print("⚠️  Le fichier JSON est vide")
        return
    
    print(f"✓ {len(data)} enregistrements chargés")
    
    # Convertir en DataFrame
    df = pd.DataFrame(data)
    
    # Convertir les colonnes date
    for col in ['first_impression_date', 'latest_impression_date']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.date
    
    # Convertir retrieved_at en timestamp UTC
    if 'retrieved_at' in df.columns:
        df['retrieved_at'] = pd.to_datetime(df['retrieved_at'], utc=True)
    
    # Initialiser le client BigQuery
    print(f"\n☁️  Connexion à BigQuery...")
    if CREDENTIALS_PATH and os.path.exists(CREDENTIALS_PATH):
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_PATH,
            scopes=["https://www.googleapis.com/auth/bigquery"]
        )
        client = bigquery.Client(
            credentials=credentials,
            project=PROJECT_ID or credentials.project_id
        )
    else:
        client = bigquery.Client(project=PROJECT_ID)
    
    # Définir le schéma
    schema = [
        bigquery.SchemaField("keyword", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("countries", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("date_range", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("paging_context", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("ad_url", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("is_restricted", "BOOLEAN", mode="NULLABLE"),
        bigquery.SchemaField("restriction_details", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("advertiser_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("advertiser_url", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("ad_payer", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("facet_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("is_inclusive", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("inclusive_segments", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("is_exclusive", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("exclusive_segments", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("first_impression_date", "DATE", mode="NULLABLE"),
        bigquery.SchemaField("latest_impression_date", "DATE", mode="NULLABLE"),
        bigquery.SchemaField("total_impressions_range", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("impressions_distribution_by_country", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("ad_type", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("retrieved_at", "TIMESTAMP", mode="NULLABLE"),
    ]
    
    # Configuration du job
    job_config = bigquery.LoadJobConfig(
        schema=schema,
        write_disposition="WRITE_APPEND",
        create_disposition="CREATE_IF_NEEDED"
    )
    
    # Upload vers BigQuery
    print(f"\n→ Upload vers BigQuery: {table_id}")
    print(f"  Nombre de lignes: {len(df)}")
    
    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )
    
    # Attendre la fin du job
    job.result()
    
    # Vérifier le résultat
    table = client.get_table(table_id)
    print(f"✓ Upload réussi! Total de lignes dans la table: {table.num_rows:,}")
    
    # Déduplication
    print(f"\n→ Déduplication en cours...")
    
    dedup_query = f"""
    MERGE `{table_id}` T
    USING (
        SELECT * EXCEPT(row_num)
        FROM (
            SELECT
                *,
                ROW_NUMBER() OVER (
                    PARTITION BY ad_url
                    ORDER BY retrieved_at DESC, latest_impression_date DESC NULLS LAST
                ) as row_num
            FROM `{table_id}`
        )
        WHERE row_num = 1
    ) S
    ON T.ad_url = S.ad_url 
       AND T.retrieved_at = S.retrieved_at
    WHEN NOT MATCHED BY SOURCE THEN DELETE
    """
    
    dedup_job = client.query(dedup_query)
    dedup_job.result()
    
    # Vérifier le résultat après déduplication
    table = client.get_table(table_id)
    print(f"✓ Déduplication terminée! Lignes uniques: {table.num_rows:,}")
    
    print("\n" + "=" * 70)
    print("✅ Upload terminé avec succès!")
    print("=" * 70)


if __name__ == "__main__":
    # Déterminer le fichier JSON à utiliser
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        # Par défaut, utiliser ads_library.json dans le répertoire courant
        json_file = "ads_library.json"
    
    if not os.path.exists(json_file):
        print(f"❌ Erreur: Le fichier {json_file} n'existe pas")
        print(f"\nUsage: python upload_json_to_bigquery.py [chemin_vers_fichier.json]")
        print(f"       (par défaut: ads_library.json)")
        sys.exit(1)
    
    print("=" * 70)
    print("🚀 Upload JSON vers BigQuery")
    print("=" * 70)
    print()
    
    try:
        upload_json_to_bigquery(json_file)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
