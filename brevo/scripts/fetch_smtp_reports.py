#!/usr/bin/env python3
"""
Script pour récupérer les rapports SMTP agrégés Brevo
Documentation: https://developers.brevo.com/reference/get-aggregated-smtp-report
"""

import requests
import yaml
from datetime import datetime, timedelta, date
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def fetch_smtp_report(
    api_key: str,
    start_date: date,
    end_date: date
) -> List[Dict[str, Any]]:
    """
    Récupère le rapport SMTP agrégé depuis l'API Brevo

    Args:
        api_key: Clé API Brevo
        start_date: Date de début
        end_date: Date de fin

    Returns:
        Liste des rapports par jour
    """
    url = 'https://api.brevo.com/v3/smtp/statistics/aggregatedReport'
    headers = {
        'api-key': api_key,
        'accept': 'application/json'
    }

    # Note: On ne peut pas utiliser startDate/endDate ET days en même temps
    # On utilise uniquement startDate et endDate
    params = {
        'startDate': start_date.strftime('%Y-%m-%d'),
        'endDate': end_date.strftime('%Y-%m-%d')
    }

    logger.info(f"📥 Récupération du rapport SMTP agrégé...")
    logger.info(f"  Période: {start_date} → {end_date}")

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        reports = data.get('reports', [])

        logger.info(f"✅ Récupéré {len(reports)} rapports")
        return reports

    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Erreur lors de la récupération du rapport: {e}")
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_detail = e.response.json()
                logger.error(f"❌ Détail de l'erreur: {error_detail}")
            except:
                logger.error(f"❌ Réponse brute: {e.response.text}")
        return []


def transform_report(report: Dict[str, Any], retrieved_at: datetime) -> Dict[str, Any]:
    """
    Transforme un rapport brut en format BigQuery

    Args:
        report: Données brutes du rapport
        retrieved_at: Timestamp de récupération

    Returns:
        Rapport formaté pour BigQuery
    """
    # Extraire la date du rapport
    report_date_str = report.get('date')
    if report_date_str:
        # Format: "2025-12-19"
        report_date = datetime.strptime(report_date_str, '%Y-%m-%d').date()
    else:
        report_date = None

    requests_total = report.get('requests', 0) or 0
    delivered = report.get('delivered', 0) or 0

    # Calcul des taux
    delivery_rate = (delivered / requests_total * 100) if requests_total > 0 else 0
    open_rate = (report.get('uniqueOpens', 0) / delivered * 100) if delivered > 0 else 0
    click_rate = (report.get('uniqueClicks', 0) / delivered * 100) if delivered > 0 else 0

    total_bounces = (report.get('hardBounces', 0) or 0) + (report.get('softBounces', 0) or 0)
    bounce_rate = (total_bounces / requests_total * 100) if requests_total > 0 else 0
    unsubscribe_rate = (report.get('unsubscribed', 0) / delivered * 100) if delivered > 0 else 0

    return {
        # Période du rapport
        'report_date': report_date.isoformat() if report_date else None,

        # Statistiques d'envoi
        'requests': report.get('requests'),
        'delivered': report.get('delivered'),
        'hard_bounces': report.get('hardBounces'),
        'soft_bounces': report.get('softBounces'),
        'clicks': report.get('clicks'),
        'unique_clicks': report.get('uniqueClicks'),
        'opens': report.get('opens'),
        'unique_opens': report.get('uniqueOpens'),
        'spam_reports': report.get('spamReports'),
        'blocked': report.get('blocked'),
        'invalid': report.get('invalid'),
        'unsubscribed': report.get('unsubscribed'),

        # Taux calculés
        'delivery_rate': round(delivery_rate, 2),
        'open_rate': round(open_rate, 2),
        'click_rate': round(click_rate, 2),
        'bounce_rate': round(bounce_rate, 2),
        'unsubscribe_rate': round(unsubscribe_rate, 2),

        # Métadonnées de traitement
        'retrieved_at': retrieved_at.isoformat()
    }


def main(days_back: int = 30):
    """
    Fonction principale

    Args:
        days_back: Nombre de jours à récupérer en arrière
    """
    config = load_config()
    api_key = config['brevo']['api_key']

    # Calculer les dates
    end_date = date.today()
    start_date = end_date - timedelta(days=days_back)

    # Récupérer le rapport
    reports = fetch_smtp_report(api_key, start_date, end_date)

    # Transformer les données
    retrieved_at = datetime.now()
    transformed_reports = [transform_report(r, retrieved_at) for r in reports]

    logger.info(f"\n📊 Résumé:")
    logger.info(f"  Total: {len(transformed_reports)} rapports quotidiens")

    # Statistiques globales
    if transformed_reports:
        total_requests = sum(r.get('requests', 0) or 0 for r in transformed_reports)
        total_delivered = sum(r.get('delivered', 0) or 0 for r in transformed_reports)
        total_opens = sum(r.get('unique_opens', 0) or 0 for r in transformed_reports)
        total_clicks = sum(r.get('unique_clicks', 0) or 0 for r in transformed_reports)

        logger.info(f"  Total envois: {total_requests:,}")
        logger.info(f"  Total délivrés: {total_delivered:,}")
        logger.info(f"  Total ouvertures uniques: {total_opens:,}")
        logger.info(f"  Total clics uniques: {total_clicks:,}")

        if total_delivered > 0:
            global_open_rate = (total_opens / total_delivered * 100)
            global_click_rate = (total_clicks / total_delivered * 100)
            logger.info(f"  Taux d'ouverture global: {global_open_rate:.2f}%")
            logger.info(f"  Taux de clic global: {global_click_rate:.2f}%")

    return transformed_reports


if __name__ == "__main__":
    reports = main(days_back=30)

    # Afficher les derniers jours
    if reports:
        logger.info("\n📋 Derniers jours:")
        for report in sorted(reports, key=lambda x: x['report_date'], reverse=True)[:7]:
            logger.info(
                f"  {report['report_date']}: "
                f"{report['delivered']:,} délivrés, "
                f"{report['unique_opens']:,} ouvertures "
                f"({report['open_rate']:.1f}%), "
                f"{report['unique_clicks']:,} clics "
                f"({report['click_rate']:.1f}%)"
            )
