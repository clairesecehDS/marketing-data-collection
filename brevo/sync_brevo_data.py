#!/usr/bin/env python3
"""
Script principal pour synchroniser toutes les données Brevo vers BigQuery

Usage:
    python sync_brevo_data.py                    # Sync complet (tout)
    python sync_brevo_data.py --events-only      # Seulement les événements
    python sync_brevo_data.py --campaigns-only   # Seulement les campagnes
    python sync_brevo_data.py --days 30          # Événements des 30 derniers jours
"""

import argparse
import sys
import yaml
import logging
from datetime import datetime
from pathlib import Path

# Importer nos modules
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

from fetch_campaigns import fetch_all_campaigns, transform_campaign
from fetch_events import fetch_events, transform_event
from fetch_contacts_lists import fetch_all_lists, transform_list
from fetch_smtp_reports import fetch_smtp_report, transform_report
from upload_to_bigquery import (
    upload_campaigns,
    upload_events,
    upload_contacts_lists,
    upload_smtp_reports
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    """Charge la configuration"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def sync_campaigns(config: dict) -> int:
    """
    Synchronise les campagnes

    Returns:
        Nombre de campagnes synchronisées
    """
    logger.info("=" * 60)
    logger.info("📧 SYNCHRONISATION DES CAMPAGNES")
    logger.info("=" * 60)

    api_key = config['brevo']['api_key']

    # Récupérer les campagnes
    campaigns = fetch_all_campaigns(api_key)

    if not campaigns:
        logger.warning("⚠️  Aucune campagne à synchroniser")
        return 0

    # Transformer
    retrieved_at = datetime.now()
    transformed = [transform_campaign(c, retrieved_at) for c in campaigns]

    # Upload vers BigQuery
    upload_campaigns(transformed, config)

    return len(transformed)


def sync_events(config: dict, days: int = 7) -> int:
    """
    Synchronise les événements

    Args:
        days: Nombre de jours à récupérer

    Returns:
        Nombre d'événements synchronisés
    """
    logger.info("=" * 60)
    logger.info(f"📨 SYNCHRONISATION DES ÉVÉNEMENTS ({days} derniers jours)")
    logger.info("=" * 60)

    api_key = config['brevo']['api_key']

    # Récupérer les événements
    events = fetch_events(api_key, days=days)

    if not events:
        logger.warning("⚠️  Aucun événement à synchroniser")
        return 0

    # Transformer
    retrieved_at = datetime.now()
    transformed = [transform_event(e, retrieved_at) for e in events]

    # Upload vers BigQuery
    upload_events(transformed, config)

    return len(transformed)


def sync_contacts_lists(config: dict) -> int:
    """
    Synchronise les listes de contacts

    Returns:
        Nombre de listes synchronisées
    """
    logger.info("=" * 60)
    logger.info("📋 SYNCHRONISATION DES LISTES DE CONTACTS")
    logger.info("=" * 60)

    api_key = config['brevo']['api_key']

    # Récupérer les listes
    lists = fetch_all_lists(api_key)

    if not lists:
        logger.warning("⚠️  Aucune liste à synchroniser")
        return 0

    # Transformer
    retrieved_at = datetime.now()
    transformed = [transform_list(l, retrieved_at) for l in lists]

    # Upload vers BigQuery
    upload_contacts_lists(transformed, config)

    return len(transformed)


def sync_smtp_reports(config: dict, days: int = 30) -> int:
    """
    Synchronise les rapports SMTP

    Args:
        days: Nombre de jours à récupérer

    Returns:
        Nombre de rapports synchronisés
    """
    logger.info("=" * 60)
    logger.info(f"📊 SYNCHRONISATION DES RAPPORTS SMTP ({days} derniers jours)")
    logger.info("=" * 60)

    api_key = config['brevo']['api_key']

    # Calculer les dates
    from datetime import date, timedelta
    # L'API Brevo n'accepte pas la date du jour, on utilise hier comme date de fin
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=days)

    # Récupérer les rapports
    reports = fetch_smtp_report(api_key, start_date, end_date)

    if not reports:
        logger.warning("⚠️  Aucun rapport à synchroniser")
        return 0

    # Transformer
    retrieved_at = datetime.now()
    transformed = [transform_report(r, retrieved_at) for r in reports]

    # Upload vers BigQuery
    upload_smtp_reports(transformed, config)

    return len(transformed)


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(
        description='Synchronise les données Brevo vers BigQuery'
    )
    parser.add_argument(
        '--events-only',
        action='store_true',
        help='Synchroniser seulement les événements'
    )
    parser.add_argument(
        '--campaigns-only',
        action='store_true',
        help='Synchroniser seulement les campagnes'
    )
    parser.add_argument(
        '--lists-only',
        action='store_true',
        help='Synchroniser seulement les listes de contacts'
    )
    parser.add_argument(
        '--reports-only',
        action='store_true',
        help='Synchroniser seulement les rapports SMTP'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=7,
        help='Nombre de jours pour les événements (défaut: 7)'
    )
    parser.add_argument(
        '--report-days',
        type=int,
        default=30,
        help='Nombre de jours pour les rapports SMTP (défaut: 30)'
    )

    args = parser.parse_args()

    # Charger la config
    config = load_config()

    logger.info("\n" + "=" * 60)
    logger.info("🚀 DÉMARRAGE DE LA SYNCHRONISATION BREVO → BIGQUERY")
    logger.info("=" * 60)
    logger.info(f"  Projet GCP: {config['google_cloud']['project_id']}")
    logger.info(f"  Dataset: {config['google_cloud']['datasets']['brevo']}")
    logger.info("=" * 60 + "\n")

    start_time = datetime.now()
    stats = {
        'campaigns': 0,
        'events': 0,
        'lists': 0,
        'reports': 0
    }

    try:
        # Déterminer quoi synchroniser
        sync_all = not any([
            args.events_only,
            args.campaigns_only,
            args.lists_only,
            args.reports_only
        ])

        if sync_all or args.campaigns_only:
            stats['campaigns'] = sync_campaigns(config)

        if sync_all or args.events_only:
            stats['events'] = sync_events(config, days=args.days)

        if sync_all or args.lists_only:
            stats['lists'] = sync_contacts_lists(config)

        if sync_all or args.reports_only:
            stats['reports'] = sync_smtp_reports(config, days=args.report_days)

        # Résumé final
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        logger.info("\n" + "=" * 60)
        logger.info("✅ SYNCHRONISATION TERMINÉE AVEC SUCCÈS")
        logger.info("=" * 60)
        logger.info(f"  📧 Campagnes: {stats['campaigns']}")
        logger.info(f"  📨 Événements: {stats['events']}")
        logger.info(f"  📋 Listes: {stats['lists']}")
        logger.info(f"  📊 Rapports: {stats['reports']}")
        logger.info(f"  ⏱️  Durée: {duration:.1f}s")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"\n❌ ERREUR LORS DE LA SYNCHRONISATION: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
