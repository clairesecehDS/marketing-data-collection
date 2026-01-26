#!/usr/bin/env python3
"""
Script pour récupérer les campagnes email Brevo
Documentation: https://developers.brevo.com/reference/get-email-campaigns
"""

import requests
import yaml
from datetime import datetime
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def fetch_all_campaigns(api_key: str) -> List[Dict[str, Any]]:
    """
    Récupère toutes les campagnes email depuis l'API Brevo

    Args:
        api_key: Clé API Brevo

    Returns:
        Liste de toutes les campagnes
    """
    url = 'https://api.brevo.com/v3/emailCampaigns'
    headers = {
        'api-key': api_key,
        'accept': 'application/json'
    }

    all_campaigns = []
    limit = 50  # Maximum par page
    offset = 0

    logger.info("📥 Récupération des campagnes Brevo...")

    while True:
        params = {
            'limit': limit,
            'offset': offset
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()
            campaigns = data.get('campaigns', [])

            if not campaigns:
                break

            all_campaigns.extend(campaigns)
            logger.info(f"  ✓ Récupéré {len(campaigns)} campagnes (total: {len(all_campaigns)})")

            # Si moins de résultats que la limite, on a tout récupéré
            if len(campaigns) < limit:
                break

            offset += limit

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Erreur lors de la récupération des campagnes: {e}")
            break

    logger.info(f"✅ Total de campagnes récupérées: {len(all_campaigns)}")
    return all_campaigns


def transform_campaign(campaign: Dict[str, Any], retrieved_at: datetime) -> Dict[str, Any]:
    """
    Transforme une campagne brute en format BigQuery

    Args:
        campaign: Données brutes de la campagne
        retrieved_at: Timestamp de récupération

    Returns:
        Campagne formatée pour BigQuery
    """
    statistics = campaign.get('statistics', {})

    # Les vraies stats sont dans campaignStats, pas dans globalStats
    # On agrège les stats de toutes les listes
    campaign_stats = statistics.get('campaignStats', [])

    # Agréger les statistiques de toutes les listes
    aggregated = {
        'uniqueClicks': 0,
        'clickers': 0,
        'complaints': 0,
        'delivered': 0,
        'sent': 0,
        'softBounces': 0,
        'hardBounces': 0,
        'uniqueViews': 0,
        'trackableViews': 0,
        'unsubscriptions': 0,
        'viewed': 0,
        'deferred': 0
    }

    for stat in campaign_stats:
        for key in aggregated.keys():
            aggregated[key] += stat.get(key, 0)

    # Calcul des taux
    sent = aggregated['sent']
    delivered = aggregated['delivered']

    open_rate = (aggregated['uniqueViews'] / delivered * 100) if delivered > 0 else 0
    click_rate = (aggregated['uniqueClicks'] / delivered * 100) if delivered > 0 else 0
    bounce_rate = ((aggregated['hardBounces'] + aggregated['softBounces']) / sent * 100) if sent > 0 else 0
    unsubscribe_rate = (aggregated['unsubscriptions'] / delivered * 100) if delivered > 0 else 0

    return {
        # Identifiants
        'id': campaign.get('id'),
        'name': campaign.get('name'),

        # Sujet et contenu
        'subject': campaign.get('subject'),
        'preview_text': campaign.get('previewText'),

        # Type et statut
        'type': campaign.get('type'),
        'status': campaign.get('status'),

        # Configuration d'envoi
        'sender_name': campaign.get('sender', {}).get('name'),
        'sender_email': campaign.get('sender', {}).get('email'),
        'reply_to': campaign.get('replyTo'),
        'to_field': campaign.get('toField'),

        # HTML et contenu
        'html_content': campaign.get('htmlContent'),

        # Planification
        'scheduled_at': campaign.get('scheduledAt'),
        'sent_date': campaign.get('sentDate'),

        # A/B Testing
        'ab_testing': campaign.get('abTesting', False),
        'subject_a': campaign.get('subjectA'),
        'subject_b': campaign.get('subjectB'),

        # Tags
        'tag': campaign.get('tag'),

        # Statistiques (agrégées depuis campaignStats)
        'stats_unique_clicks': aggregated['uniqueClicks'] if aggregated['uniqueClicks'] > 0 else None,
        'stats_clickers': aggregated['clickers'] if aggregated['clickers'] > 0 else None,
        'stats_complaints': aggregated['complaints'] if aggregated['complaints'] > 0 else None,
        'stats_delivered': aggregated['delivered'] if aggregated['delivered'] > 0 else None,
        'stats_sent': aggregated['sent'] if aggregated['sent'] > 0 else None,
        'stats_soft_bounces': aggregated['softBounces'] if aggregated['softBounces'] > 0 else None,
        'stats_hard_bounces': aggregated['hardBounces'] if aggregated['hardBounces'] > 0 else None,
        'stats_unique_views': aggregated['uniqueViews'] if aggregated['uniqueViews'] > 0 else None,
        'stats_trackable_views': aggregated['trackableViews'] if aggregated['trackableViews'] > 0 else None,
        'stats_unsubscriptions': aggregated['unsubscriptions'] if aggregated['unsubscriptions'] > 0 else None,
        'stats_viewed': aggregated['viewed'] if aggregated['viewed'] > 0 else None,
        'stats_deferred': aggregated['deferred'] if aggregated['deferred'] > 0 else None,

        # Taux calculés
        'open_rate': round(open_rate, 2),
        'click_rate': round(click_rate, 2),
        'bounce_rate': round(bounce_rate, 2),
        'unsubscribe_rate': round(unsubscribe_rate, 2),

        # Métadonnées
        'retrieved_at': retrieved_at.isoformat(),
        'created_at': campaign.get('createdAt'),
        'modified_at': campaign.get('modifiedAt')
    }


def main():
    """Fonction principale"""
    config = load_config()
    api_key = config['brevo']['api_key']

    # Récupérer toutes les campagnes
    campaigns = fetch_all_campaigns(api_key)

    # Transformer les données
    retrieved_at = datetime.now()
    transformed_campaigns = [transform_campaign(c, retrieved_at) for c in campaigns]

    logger.info(f"\n📊 Résumé:")
    logger.info(f"  Total: {len(transformed_campaigns)} campagnes")

    # Statistiques par statut
    status_count = {}
    for c in transformed_campaigns:
        status = c.get('status', 'unknown')
        status_count[status] = status_count.get(status, 0) + 1

    for status, count in sorted(status_count.items()):
        logger.info(f"  {status}: {count}")

    return transformed_campaigns


if __name__ == "__main__":
    campaigns = main()

    # Afficher quelques exemples
    if campaigns:
        logger.info("\n📋 Exemple de campagne:")
        example = campaigns[0]
        logger.info(f"  ID: {example['id']}")
        logger.info(f"  Nom: {example['name']}")
        logger.info(f"  Sujet: {example['subject']}")
        logger.info(f"  Statut: {example['status']}")
        logger.info(f"  Envoyée: {example['sent_date']}")
        logger.info(f"  Stats: {example['stats_delivered']} délivrés, {example['stats_unique_views']} ouvertures")
