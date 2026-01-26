#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de récupération des événements marketing hebdomadaires de Brevo
Documentation: https://developers.brevo.com/docs/fetch-all-your-weekly-marketing-events

Ce script permet de:
1. Déclencher un export d'événements via l'API Brevo
2. Vérifier le statut de l'export
3. Télécharger le fichier CSV généré
4. Parser et uploader les données vers BigQuery
"""

import os
import sys
import time
import yaml
import requests
import csv
import io
import zipfile
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BrevoWeeklyEventsCollector:
    """Collecteur d'événements marketing hebdomadaires Brevo"""
    
    def __init__(self, api_key: str, config: dict):
        """
        Initialise le collecteur Brevo
        
        Args:
            api_key: Clé API Brevo
            config: Configuration complète du projet
        """
        self.api_key = api_key
        self.config = config
        self.base_url = "https://api.brevo.com/v3"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": self.api_key
        }
        
    def request_export(self, event_type: str = "allEvents", days: int = 7, notify_url: str = None) -> Optional[int]:
        """
        Déclenche un export d'événements webhooks
        
        Args:
            event_type: Type d'événement à exporter (allEvents, spam, opened, click, etc.)
            days: Nombre de jours à exporter (max 7)
            notify_url: URL du webhook pour recevoir la notification quand l'export est prêt
            
        Returns:
            process_id si succès, None sinon
        """
        url = f"{self.base_url}/webhooks/export"
        
        payload = {
            "event": event_type,
            "type": "marketing",
            "days": days
        }
        
        # Ajouter le notifyURL si fourni
        if notify_url:
            payload["notifyURL"] = notify_url
            logger.info(f"Webhook de notification: {notify_url}")
        
        try:
            logger.info(f"Demande d'export pour {event_type} sur {days} jours...")
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            process_id = data.get("processId")
            
            if process_id:
                logger.info(f"✓ Export demandé avec succès. Process ID: {process_id}")
                return process_id
            else:
                logger.error("Process ID non trouvé dans la réponse")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"✗ Erreur lors de la demande d'export: {e}")
            if hasattr(e.response, 'text'):
                logger.error(f"Réponse API: {e.response.text}")
            return None
    
    def check_export_status(self, process_id: int) -> Optional[Dict]:
        """
        Vérifie le statut d'un export
        
        Args:
            process_id: ID du processus d'export
            
        Returns:
            Informations sur le processus si trouvé, None sinon
        """
        url = f"{self.base_url}/processes/{process_id}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"✗ Erreur lors de la vérification du statut: {e}")
            return None
    
    def wait_for_export(self, process_id: int, max_wait_seconds: int = 600, check_interval: int = 10) -> Optional[str]:
        """
        Attend que l'export soit terminé et retourne l'URL de téléchargement
        
        Args:
            process_id: ID du processus d'export
            max_wait_seconds: Temps d'attente maximum en secondes
            check_interval: Intervalle entre chaque vérification en secondes
            
        Returns:
            URL de téléchargement si succès, None sinon
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait_seconds:
            status_info = self.check_export_status(process_id)
            
            if not status_info:
                logger.error("Impossible de récupérer le statut")
                return None
            
            status = status_info.get("status")
            logger.info(f"Statut de l'export: {status}")
            
            if status == "completed":
                export_url = status_info.get("export_url")
                if export_url:
                    logger.info(f"✓ Export terminé! URL: {export_url}")
                    return export_url
                else:
                    logger.error("Export terminé mais URL non trouvée")
                    return None
            
            elif status == "failed":
                logger.error("✗ Export échoué")
                return None
            
            logger.info(f"En attente... (vérifie à nouveau dans {check_interval}s)")
            time.sleep(check_interval)
        
        logger.error(f"✗ Timeout après {max_wait_seconds}s")
        return None
    
    def download_and_parse_export(self, export_url: str) -> List[Dict]:
        """
        Télécharge et parse le fichier CSV d'export
        
        Args:
            export_url: URL du fichier à télécharger
            
        Returns:
            Liste de dictionnaires contenant les événements
        """
        try:
            logger.info("Téléchargement du fichier d'export...")
            response = requests.get(export_url)
            response.raise_for_status()
            
            events = []
            
            # Vérifier si c'est un fichier ZIP
            if export_url.endswith('.zip'):
                logger.info("Fichier ZIP détecté, extraction...")
                with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
                    # Traiter tous les fichiers CSV dans le ZIP
                    for file_name in zip_file.namelist():
                        if file_name.endswith('.csv'):
                            logger.info(f"Traitement du fichier: {file_name}")
                            with zip_file.open(file_name) as csv_file:
                                csv_content = csv_file.read().decode('utf-8')
                                events.extend(self._parse_csv_content(csv_content))
            else:
                # Fichier CSV direct
                logger.info("Traitement du fichier CSV...")
                events = self._parse_csv_content(response.text)
            
            logger.info(f"✓ {len(events)} événements extraits")
            return events
            
        except Exception as e:
            logger.error(f"✗ Erreur lors du téléchargement/parsing: {e}")
            return []
    
    def _parse_csv_content(self, csv_content: str) -> List[Dict]:
        """
        Parse le contenu CSV et retourne une liste de dictionnaires
        
        Args:
            csv_content: Contenu du CSV sous forme de string
            
        Returns:
            Liste de dictionnaires
        """
        events = []
        csv_reader = csv.DictReader(io.StringIO(csv_content))
        
        for row in csv_reader:
            # Convertir les champs en format approprié pour BigQuery
            event = self._transform_row(row)
            events.append(event)
        
        return events
    
    def _transform_row(self, row: Dict) -> Dict:
        """
        Transforme une ligne CSV en format BigQuery
        
        Args:
            row: Ligne CSV sous forme de dictionnaire
            
        Returns:
            Dictionnaire formaté pour BigQuery
        """
        # Parser le champ event pour créer les compteurs
        event_type = row.get('event', '').strip()
        
        # Mapping des événements vers les colonnes booléennes
        event_mapping = {
            'spam': 'spam',
            'opened': 'opened',
            'click': 'click',
            'hard_bounce': 'hard_bounce',
            'soft_bounce': 'soft_bounce',
            'delivered': 'delivered',
            'unsubscribe': 'unsubscribe',
            'contact_deleted': 'contact_deleted',
            'contact_updated': 'contact_updated',
            'list_addition': 'list_addition'
        }
        
        # Créer l'objet transformé
        transformed = {
            'date': row.get('date'),
            'email': row.get('email'),
            'event': event_type,
            'id': int(row.get('id', 0)) if row.get('id') else None,
            'message_id': row.get('message-id'),
            'reason': row.get('reason'),
            'sending_ip': row.get('sending_ip'),
            'subject': row.get('subject'),
            'tag': row.get('tag'),
            'tags': row.get('tags'),
            'template_id': int(row.get('template_id', 0)) if row.get('template_id') else None,
            'ts': row.get('ts'),
            'ts_epoch': int(row.get('ts_epoch', 0)) if row.get('ts_epoch') else None,
            'ts_event': row.get('ts_event'),
            'x_mailin_custom': row.get('X-Mailin-custom'),
            'link': row.get('link'),
            's_returnpath': row.get('s_returnpath', '').lower() == 'true',
            'retrieved_at': datetime.utcnow().isoformat(),
            'export_process_id': None  # Sera rempli lors de l'upload
        }
        
        # Ajouter les compteurs d'événements
        for event_key, column_name in event_mapping.items():
            transformed[column_name] = 1 if event_type == event_key else 0
        
        return transformed
    
    def save_to_json(self, events: List[Dict], output_file: str):
        """
        Sauvegarde les événements dans un fichier JSON
        
        Args:
            events: Liste des événements
            output_file: Chemin du fichier de sortie
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(events, f, indent=2, ensure_ascii=False)
            logger.info(f"✓ Données sauvegardées dans {output_file}")
        except Exception as e:
            logger.error(f"✗ Erreur lors de la sauvegarde: {e}")
    
    def upload_to_bigquery(self, events: List[Dict], process_id: int):
        """
        Upload les événements vers BigQuery
        
        Args:
            events: Liste des événements
            process_id: ID du processus d'export
        """
        try:
            from google.cloud import bigquery
            from google.oauth2 import service_account
            
            # Configuration BigQuery
            gcp_config = self.config.get('google_cloud', {})
            project_id = gcp_config.get('project_id')
            credentials_file = gcp_config.get('credentials_file')
            dataset_id = gcp_config.get('datasets', {}).get('brevo', 'brevo')
            table_id = 'brevo'
            
            # Créer le client BigQuery
            credentials = service_account.Credentials.from_service_account_file(credentials_file)
            client = bigquery.Client(credentials=credentials, project=project_id)
            
            # Référence de la table
            table_ref = f"{project_id}.{dataset_id}.{table_id}"
            
            # Ajouter le process_id à chaque événement
            for event in events:
                event['export_process_id'] = process_id
            
            # Configuration du job d'insertion
            job_config = bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
                write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
                schema_update_options=[
                    bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
                ]
            )
            
            # Convertir en NDJSON
            ndjson_data = '\n'.join([json.dumps(event) for event in events])
            
            # Upload
            logger.info(f"Upload de {len(events)} événements vers {table_ref}...")
            job = client.load_table_from_file(
                io.StringIO(ndjson_data),
                table_ref,
                job_config=job_config
            )
            
            job.result()  # Attendre la fin du job
            
            logger.info(f"✓ {len(events)} événements uploadés avec succès vers BigQuery!")
            
        except Exception as e:
            logger.error(f"✗ Erreur lors de l'upload vers BigQuery: {e}")
            raise


def load_config(config_file: str = "config.yaml") -> dict:
    """Charge la configuration depuis le fichier YAML"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Erreur lors du chargement de la configuration: {e}")
        sys.exit(1)


def main():
    """Fonction principale"""
    # Charger la configuration
    config = load_config()
    
    # Récupérer les paramètres Brevo
    brevo_config = config.get('brevo', {})
    api_key = brevo_config.get('api_key')
    notify_url = brevo_config.get('notify_url')
    
    if not api_key:
        logger.error("Clé API Brevo non trouvée dans la configuration")
        sys.exit(1)
    
    if not notify_url or notify_url == "https://webhook.site/YOUR-UNIQUE-ID":
        logger.error("⚠️  Veuillez configurer 'notify_url' dans config.yaml")
        logger.error("   1. Allez sur https://webhook.site")
        logger.error("   2. Copiez votre URL unique")
        logger.error("   3. Collez-la dans brevo.notify_url du config.yaml")
        sys.exit(1)
    
    # Créer le collecteur
    collector = BrevoWeeklyEventsCollector(api_key, config)
    
    logger.info("="*60)
    logger.info("🔔 IMPORTANT: Surveillez votre webhook.site !")
    logger.info(f"   URL: {notify_url}")
    logger.info("   Brevo va y envoyer le lien de téléchargement du CSV")
    logger.info("="*60 + "\n")
    
    # 1. Demander l'export
    process_id = collector.request_export(event_type="allEvents", days=7, notify_url=notify_url)
    
    if not process_id:
        logger.error("Impossible de démarrer l'export")
        sys.exit(1)
    
    # 2. Instructions pour l'utilisateur
    logger.info("\n" + "="*60)
    logger.info("📋 PROCHAINES ÉTAPES:")
    logger.info("="*60)
    logger.info("1. Attendez quelques minutes que Brevo génère l'export")
    logger.info("2. Rafraîchissez votre page webhook.site")
    logger.info("3. Vous recevrez un JSON avec 'url' et 'process_id'")
    logger.info("4. Copiez l'URL du fichier CSV/ZIP")
    logger.info("5. Relancez ce script avec l'URL en paramètre:")
    logger.info(f"   python {sys.argv[0]} --download-url 'URL_DU_FICHIER'")
    logger.info("="*60 + "\n")
    
    # Option: attendre et poller le statut
    logger.info("Ou attendez que le script vérifie automatiquement le statut...")
    export_url = collector.wait_for_export(process_id, max_wait_seconds=600)
    
    if not export_url:
        logger.warning("⚠️  Timeout - Vérifiez votre webhook.site pour récupérer l'URL manuellement")
        logger.info(f"   Process ID: {process_id}")
        sys.exit(0)
    
    # 3. Télécharger et parser les données
    events = collector.download_and_parse_export(export_url)
    
    if not events:
        logger.warning("Aucun événement récupéré")
        sys.exit(0)
    
    # 4. Sauvegarder localement (optionnel)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"brevo_events_{timestamp}.json"
    collector.save_to_json(events, output_file)
    
    # 5. Upload vers BigQuery
    try:
        collector.upload_to_bigquery(events, process_id)
        logger.info("✓ Processus terminé avec succès!")
    except Exception as e:
        logger.error(f"✗ Erreur lors de l'upload: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
