#!/usr/bin/env python3
"""
Script pour synchroniser des données historiques Brevo
Permet de spécifier des dates de début et fin personnalisées
"""

import argparse
import sys
import yaml
import logging
from datetime import datetime, date, timedelta
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


def fetch_events_by_date_range(api_key: str, start_date: date, end_date: date) -> list:
    """
    Récupère les événements pour une plage de dates spécifique

    Args:
        api_key: Clé API Brevo
        start_date: Date de début (incluse)
        end_date: Date de fin (incluse)

    Returns:
        Liste des événements
    """
    import requests

    url = 'https://api.brevo.com/v3/smtp/statistics/events'
    headers = {
        'api-key': api_key,
        'accept': 'application/json'
    }

    all_events = []
    limit = 100
    offset = 0

    logger.info(f"📥 Récupération des événements du {start_date} au {end_date}...")

    while True:
        params = {
            'limit': limit,
            'offset': offset,
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d'),
            'sort': 'desc'
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()
            events = data.get('events', [])

            if not events:
                break

            all_events.extend(events)
            logger.info(f"  ✓ Récupéré {len(events)} événements (total: {len(all_events)})")

            if len(events) < limit:
                break

            offset += limit

            if offset > 10000:
                logger.warning("⚠️  Limite de 10k événements atteinte pour cette période")
                break

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Erreur: {e}")
            break

    logger.info(f"✅ Total récupéré: {len(all_events)} événements")
    return all_events


def sync_historical_events(config: dict, start_date: date, end_date: date):
    """
    Synchronise les événements historiques par tranches de 30 jours
    (limite API Brevo)
    """
    api_key = config['brevo']['api_key']

    # Diviser en tranches de 30 jours maximum
    current_start = start_date
    total_events = 0

    logger.info("=" * 60)
    logger.info(f"📨 SYNCHRONISATION HISTORIQUE DES ÉVÉNEMENTS")
    logger.info(f"  Période totale: {start_date} → {end_date}")
    logger.info("=" * 60)

    while current_start < end_date:
        # Calculer la fin de la tranche (max 30 jours)
        current_end = min(current_start + timedelta(days=30), end_date)

        logger.info(f"\n📅 Tranche: {current_start} → {current_end}")

        # Récupérer les événements
        events = fetch_events_by_date_range(api_key, current_start, current_end)

        if events:
            # Transformer
            retrieved_at = datetime.now()
            transformed = [transform_event(e, retrieved_at) for e in events]

            # Upload vers BigQuery
            upload_events(transformed, config)
            total_events += len(transformed)
        else:
            logger.warning(f"  ⚠️  Aucun événement pour cette période")

        # Passer à la tranche suivante
        current_start = current_end + timedelta(days=1)

    logger.info("\n" + "=" * 60)
    logger.info(f"✅ SYNCHRONISATION HISTORIQUE TERMINÉE")
    logger.info(f"  Total événements synchronisés: {total_events}")
    logger.info("=" * 60)


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(
        description='Synchronise les données historiques Brevo vers BigQuery'
    )
    parser.add_argument(
        '--start-date',
        type=str,
        required=True,
        help='Date de début (format: YYYY-MM-DD, ex: 2025-12-18)'
    )
    parser.add_argument(
        '--end-date',
        type=str,
        default=None,
        help='Date de fin (format: YYYY-MM-DD, défaut: hier)'
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
        '--reports-only',
        action='store_true',
        help='Synchroniser seulement les rapports SMTP'
    )

    args = parser.parse_args()

    # Parser les dates
    try:
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date()
    except ValueError:
        logger.error("❌ Format de date de début invalide. Utilisez YYYY-MM-DD")
        sys.exit(1)

    if args.end_date:
        try:
            end_date = datetime.strptime(args.end_date, '%Y-%m-%d').date()
        except ValueError:
            logger.error("❌ Format de date de fin invalide. Utilisez YYYY-MM-DD")
            sys.exit(1)
    else:
        # Par défaut: hier
        end_date = date.today() - timedelta(days=1)

    # Vérifications
    if start_date >= end_date:
        logger.error("❌ La date de début doit être avant la date de fin")
        sys.exit(1)

    days_diff = (end_date - start_date).days
    if days_diff > 90:
        logger.warning(f"⚠️  Période de {days_diff} jours demandée. Cela peut prendre du temps...")

    # Charger la config
    config = load_config()

    logger.info("\n" + "=" * 60)
    logger.info("🚀 SYNCHRONISATION HISTORIQUE BREVO → BIGQUERY")
    logger.info("=" * 60)
    logger.info(f"  Projet GCP: {config['google_cloud']['project_id']}")
    logger.info(f"  Dataset: {config['google_cloud']['datasets']['brevo']}")
    logger.info(f"  Période: {start_date} → {end_date} ({days_diff} jours)")
    logger.info("=" * 60 + "\n")

    try:
        # Déterminer quoi synchroniser
        sync_all = not any([
            args.events_only,
            args.campaigns_only,
            args.reports_only
        ])

        if sync_all or args.campaigns_only:
            logger.info("📧 Synchronisation des campagnes...")
            api_key = config['brevo']['api_key']
            campaigns = fetch_all_campaigns(api_key)
            if campaigns:
                retrieved_at = datetime.now()
                transformed = [transform_campaign(c, retrieved_at) for c in campaigns]
                upload_campaigns(transformed, config)
                logger.info(f"✅ {len(transformed)} campagnes synchronisées")

        if sync_all or args.events_only:
            sync_historical_events(config, start_date, end_date)

        if sync_all or args.reports_only:
            logger.info("\n📊 Synchronisation des rapports SMTP...")
            api_key = config['brevo']['api_key']
            reports = fetch_smtp_report(api_key, start_date, end_date)
            if reports:
                retrieved_at = datetime.now()
                transformed = [transform_report(r, retrieved_at) for r in reports]
                upload_smtp_reports(transformed, config)
                logger.info(f"✅ {len(transformed)} rapports synchronisés")

        logger.info("\n✅ SYNCHRONISATION HISTORIQUE TERMINÉE AVEC SUCCÈS")

    except Exception as e:
        logger.error(f"\n❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
