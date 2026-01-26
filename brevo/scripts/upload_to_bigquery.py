#!/usr/bin/env python3
"""
Module pour uploader les données Brevo vers BigQuery
"""

import yaml
from google.cloud import bigquery
from google.oauth2 import service_account
from typing import List, Dict, Any
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_bigquery_client(config: dict) -> bigquery.Client:
    """
    Crée un client BigQuery

    Args:
        config: Configuration complète

    Returns:
        Client BigQuery
    """
    import os

    project_id = config['google_cloud']['project_id']
    credentials_file = config['google_cloud']['credentials_file']

    # Vérifier si GOOGLE_APPLICATION_CREDENTIALS est défini (cas Cloud Run)
    gcp_creds_env = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

    if gcp_creds_env and Path(gcp_creds_env).exists():
        # Utiliser les credentials montés par Cloud Run (via Secret Manager)
        logger.info(f"🔑 Utilisation des credentials depuis: {gcp_creds_env}")
        credentials = service_account.Credentials.from_service_account_file(
            gcp_creds_env
        )
        client = bigquery.Client(
            project=project_id,
            credentials=credentials
        )
    elif Path(credentials_file).exists():
        # Utiliser les credentials du fichier de config (exécution locale)
        logger.info(f"🔑 Utilisation des credentials depuis: {credentials_file}")
        credentials = service_account.Credentials.from_service_account_file(
            str(credentials_file)
        )
        client = bigquery.Client(
            project=project_id,
            credentials=credentials
        )
    else:
        # Utiliser Application Default Credentials (ADC)
        logger.info("🔑 Utilisation des Application Default Credentials")
        client = bigquery.Client(project=project_id)

    return client


def upload_events(data: List[Dict[str, Any]], config: dict):
    """
    Upload les événements vers BigQuery

    Args:
        data: Liste des événements
        config: Configuration
    """
    if not data:
        logger.warning("⚠️  Aucune donnée d'événements à uploader")
        return

    client = get_bigquery_client(config)
    project_id = config['google_cloud']['project_id']
    dataset_id = config['google_cloud']['datasets']['brevo']
    table_id = 'brevo_events'

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    logger.info(f"📤 Upload de {len(data)} événements vers {table_ref}...")

    # Configuration de l'upload
    # Note: On désactive autodetect pour éviter les conflits de schéma
    # BigQuery utilisera le schéma existant de la table
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
        autodetect=False  # Important: utiliser le schéma de la table existante
    )

    try:
        job = client.load_table_from_json(
            data,
            table_ref,
            job_config=job_config
        )
        job.result()  # Attendre la fin
        logger.info(f"✅ {len(data)} événements uploadés avec succès")

    except Exception as e:
        logger.error(f"❌ Erreur lors de l'upload des événements: {e}")
        raise


def upload_campaigns(data: List[Dict[str, Any]], config: dict):
    """
    Upload les campagnes vers BigQuery

    Args:
        data: Liste des campagnes
        config: Configuration
    """
    if not data:
        logger.warning("⚠️  Aucune donnée de campagnes à uploader")
        return

    client = get_bigquery_client(config)
    project_id = config['google_cloud']['project_id']
    dataset_id = config['google_cloud']['datasets']['brevo']
    table_id = 'brevo_campaigns'

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    logger.info(f"📤 Upload de {len(data)} campagnes vers {table_ref}...")

    # Configuration de l'upload avec WRITE_TRUNCATE pour les campagnes
    # (on remplace tout car c'est un snapshot complet)
    # Note: schema_update_options n'est pas compatible avec WRITE_TRUNCATE sur table non partitionnée
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True
    )

    try:
        job = client.load_table_from_json(
            data,
            table_ref,
            job_config=job_config
        )
        job.result()
        logger.info(f"✅ {len(data)} campagnes uploadées avec succès")

    except Exception as e:
        logger.error(f"❌ Erreur lors de l'upload des campagnes: {e}")
        raise


def upload_contacts_lists(data: List[Dict[str, Any]], config: dict):
    """
    Upload les listes de contacts vers BigQuery

    Args:
        data: Liste des listes de contacts
        config: Configuration
    """
    if not data:
        logger.warning("⚠️  Aucune donnée de listes à uploader")
        return

    client = get_bigquery_client(config)
    project_id = config['google_cloud']['project_id']
    dataset_id = config['google_cloud']['datasets']['brevo']
    table_id = 'brevo_contacts_lists'

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    logger.info(f"📤 Upload de {len(data)} listes vers {table_ref}...")

    # Mode APPEND pour conserver l'historique des listes
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
        autodetect=True
    )

    try:
        job = client.load_table_from_json(
            data,
            table_ref,
            job_config=job_config
        )
        job.result()
        logger.info(f"✅ {len(data)} listes uploadées avec succès")

    except Exception as e:
        logger.error(f"❌ Erreur lors de l'upload des listes: {e}")
        raise


def upload_smtp_reports(data: List[Dict[str, Any]], config: dict):
    """
    Upload les rapports SMTP vers BigQuery

    Args:
        data: Liste des rapports
        config: Configuration
    """
    if not data:
        logger.warning("⚠️  Aucune donnée de rapports SMTP à uploader")
        return

    client = get_bigquery_client(config)
    project_id = config['google_cloud']['project_id']
    dataset_id = config['google_cloud']['datasets']['brevo']
    table_id = 'brevo_smtp_reports'

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    logger.info(f"📤 Upload de {len(data)} rapports vers {table_ref}...")

    # Pour les rapports, on utilise WRITE_APPEND avec déduplication possible
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
        autodetect=True
    )

    try:
        job = client.load_table_from_json(
            data,
            table_ref,
            job_config=job_config
        )
        job.result()
        logger.info(f"✅ {len(data)} rapports uploadés avec succès")

    except Exception as e:
        logger.error(f"❌ Erreur lors de l'upload des rapports: {e}")
        raise


def main():
    """Fonction de test"""
    config = load_config()
    logger.info("✅ Configuration chargée")
    logger.info(f"  Projet: {config['google_cloud']['project_id']}")
    logger.info(f"  Dataset: {config['google_cloud']['datasets']['brevo']}")

    # Test de connexion BigQuery
    try:
        client = get_bigquery_client(config)
        logger.info(f"✅ Connexion BigQuery réussie")
    except Exception as e:
        logger.error(f"❌ Erreur de connexion BigQuery: {e}")


if __name__ == "__main__":
    main()
