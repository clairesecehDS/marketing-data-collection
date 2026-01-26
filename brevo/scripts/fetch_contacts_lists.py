#!/usr/bin/env python3
"""
Script pour récupérer les listes de contacts Brevo
Documentation: https://developers.brevo.com/reference/get-lists
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


def fetch_all_lists(api_key: str) -> List[Dict[str, Any]]:
    """
    Récupère toutes les listes de contacts depuis l'API Brevo

    Args:
        api_key: Clé API Brevo

    Returns:
        Liste de toutes les listes de contacts
    """
    url = 'https://api.brevo.com/v3/contacts/lists'
    headers = {
        'api-key': api_key,
        'accept': 'application/json'
    }

    all_lists = []
    limit = 50  # Maximum par page
    offset = 0

    logger.info("📥 Récupération des listes de contacts Brevo...")

    while True:
        params = {
            'limit': limit,
            'offset': offset
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()
            lists = data.get('lists', [])

            if not lists:
                break

            all_lists.extend(lists)
            logger.info(f"  ✓ Récupéré {len(lists)} listes (total: {len(all_lists)})")

            # Si moins de résultats que la limite, on a tout récupéré
            if len(lists) < limit:
                break

            offset += limit

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Erreur lors de la récupération des listes: {e}")
            break

    logger.info(f"✅ Total de listes récupérées: {len(all_lists)}")
    return all_lists


def transform_list(contact_list: Dict[str, Any], retrieved_at: datetime) -> Dict[str, Any]:
    """
    Transforme une liste brute en format BigQuery

    Args:
        contact_list: Données brutes de la liste
        retrieved_at: Timestamp de récupération

    Returns:
        Liste formatée pour BigQuery
    """
    return {
        # Identifiants
        'id': contact_list.get('id'),
        'name': contact_list.get('name'),

        # Organisation
        'folder_id': contact_list.get('folderId'),
        'folder_name': None,  # À enrichir si besoin avec l'API folders

        # Statistiques
        'total_subscribers': contact_list.get('totalSubscribers', 0),
        'total_blacklisted': contact_list.get('totalBlacklisted', 0),
        'unique_subscribers': contact_list.get('uniqueSubscribers', 0),

        # Métadonnées
        'created_at': contact_list.get('createdAt'),

        # Métadonnées de traitement
        'retrieved_at': retrieved_at.isoformat()
    }


def main():
    """Fonction principale"""
    config = load_config()
    api_key = config['brevo']['api_key']

    # Récupérer toutes les listes
    lists = fetch_all_lists(api_key)

    # Transformer les données
    retrieved_at = datetime.now()
    transformed_lists = [transform_list(l, retrieved_at) for l in lists]

    logger.info(f"\n📊 Résumé:")
    logger.info(f"  Total: {len(transformed_lists)} listes")

    # Statistiques
    total_subscribers = sum(l.get('total_subscribers', 0) for l in transformed_lists)
    logger.info(f"  Total abonnés: {total_subscribers:,}")

    return transformed_lists


if __name__ == "__main__":
    lists = main()

    # Afficher quelques exemples
    if lists:
        logger.info("\n📋 Top 5 listes par nombre d'abonnés:")
        sorted_lists = sorted(lists, key=lambda x: x.get('total_subscribers', 0), reverse=True)
        for i, lst in enumerate(sorted_lists[:5], 1):
            logger.info(f"  {i}. {lst['name']}: {lst['total_subscribers']:,} abonnés")
