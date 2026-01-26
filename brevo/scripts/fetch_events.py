#!/usr/bin/env python3
"""
Script pour récupérer les événements email Brevo
Documentation: https://developers.brevo.com/reference/get-email-event-report
"""

import requests
import yaml
from datetime import datetime, timedelta
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def fetch_events(
    api_key: str,
    days: int = 7,
    event_types: List[str] = None
) -> List[Dict[str, Any]]:
    """
    Récupère les événements email depuis l'API Brevo

    Args:
        api_key: Clé API Brevo
        days: Nombre de jours à récupérer (max 30)
        event_types: Liste des types d'événements à récupérer

    Returns:
        Liste de tous les événements
    """
    url = 'https://api.brevo.com/v3/smtp/statistics/events'
    headers = {
        'api-key': api_key,
        'accept': 'application/json'
    }

    if event_types is None:
        # Utiliser les noms d'événements acceptés par l'API
        # Laisser vide pour récupérer tous les événements
        event_types = []

    # Calculer les dates
    # Important: Utiliser date.today() - timedelta(1) pour éviter les erreurs 500
    # L'API Brevo n'accepte pas la date du jour actuel
    from datetime import date
    end_date = date.today() - timedelta(days=1)  # Hier
    start_date = end_date - timedelta(days=days)

    all_events = []
    limit = 100  # Maximum par requête selon la doc
    offset = 0

    logger.info(f"📥 Récupération des événements Brevo ({days} derniers jours)...")
    logger.info(f"  Période: {start_date.strftime('%Y-%m-%d')} → {end_date.strftime('%Y-%m-%d')}")

    while True:
        params = {
            'limit': limit,
            'offset': offset,
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d'),
            'sort': 'desc'
        }

        # Ajouter le paramètre event seulement si on filtre sur des événements spécifiques
        if event_types:
            params['event'] = ','.join(event_types)

        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()
            events = data.get('events', [])

            if not events:
                break

            all_events.extend(events)
            logger.info(f"  ✓ Récupéré {len(events)} événements (total: {len(all_events)})")

            # Si moins de résultats que la limite, on a tout récupéré
            if len(events) < limit:
                break

            offset += limit

            # Protection contre boucle infinie
            if offset > 10000:  # Max 10k événements par précaution
                logger.warning("⚠️  Limite de 10k événements atteinte")
                break

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Erreur lors de la récupération des événements: {e}")
            break

    logger.info(f"✅ Total d'événements récupérés: {len(all_events)}")
    return all_events


def transform_event(event: Dict[str, Any], retrieved_at: datetime) -> Dict[str, Any]:
    """
    Transforme un événement brut en format BigQuery

    Args:
        event: Données brutes de l'événement
        retrieved_at: Timestamp de récupération

    Returns:
        Événement formaté pour BigQuery
    """
    event_type = event.get('event', '').lower()

    # Compteurs par type d'événement
    event_flags = {
        'spam': 1 if event_type == 'spam' else 0,
        'opened': 1 if event_type in ['opened', 'loadedbyproxy'] else 0,
        'click': 1 if event_type == 'click' else 0,
        'hard_bounce': 1 if event_type == 'hardbounce' else 0,
        'soft_bounce': 1 if event_type == 'softbounce' else 0,
        'delivered': 1 if event_type == 'delivered' else 0,
        'unsubscribe': 1 if event_type == 'unsubscribed' else 0,
        'contact_deleted': 0,  # Pas dans les événements SMTP
        'contact_updated': 0,  # Pas dans les événements SMTP
        'list_addition': 0     # Pas dans les événements SMTP
    }

    return {
        # Informations de l'événement
        'date': event.get('date'),
        'email': event.get('email'),
        'event': event_type,

        # Identifiants
        # Note: L'API events n'a pas d'ID numérique, on met None
        # Le message_id est une string (ex: "abc@brevo.com")
        'id': None,  # Pas d'ID numérique dans cette API
        'message_id': event.get('messageId'),

        # Détails de l'envoi
        'reason': event.get('reason'),
        'sending_ip': event.get('ip'),
        'subject': event.get('subject'),

        # Tags et metadata
        'tag': event.get('tag'),
        'tags': str(event.get('tags', [])) if event.get('tags') else None,
        'template_id': event.get('templateId'),

        # Timestamps
        'ts': event.get('date'),
        'ts_epoch': None,  # Pas disponible dans cette API
        'ts_event': event.get('date'),

        # Champs personnalisés
        'x_mailin_custom': None,

        # Informations sur les clics
        'link': event.get('link'),

        # Autres champs
        's_returnpath': None,

        # Compteurs par type
        **event_flags,

        # Métadonnées de traitement
        'retrieved_at': retrieved_at.isoformat(),
        'export_process_id': None
    }


def main():
    """Fonction principale"""
    config = load_config()
    api_key = config['brevo']['api_key']
    days = config['brevo']['collection'].get('days', 7)

    # Récupérer tous les événements
    events = fetch_events(api_key, days=days)

    # Transformer les données
    retrieved_at = datetime.now()
    transformed_events = [transform_event(e, retrieved_at) for e in events]

    logger.info(f"\n📊 Résumé:")
    logger.info(f"  Total: {len(transformed_events)} événements")

    # Statistiques par type
    event_count = {}
    for e in transformed_events:
        event_type = e.get('event', 'unknown')
        event_count[event_type] = event_count.get(event_type, 0) + 1

    for event_type, count in sorted(event_count.items(), key=lambda x: x[1], reverse=True):
        logger.info(f"  {event_type}: {count}")

    return transformed_events


if __name__ == "__main__":
    events = main()

    # Afficher quelques exemples
    if events:
        logger.info("\n📋 Exemple d'événement:")
        example = events[0]
        logger.info(f"  Type: {example['event']}")
        logger.info(f"  Email: {example['email']}")
        logger.info(f"  Sujet: {example['subject']}")
        logger.info(f"  Date: {example['date']}")
        if example['link']:
            logger.info(f"  Lien: {example['link']}")
