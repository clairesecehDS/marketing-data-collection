-- Script pour recréer la table brevo_events avec le bon schéma
-- ATTENTION: Cela supprime toutes les données existantes !

-- Supprimer l'ancienne table si elle existe
DROP TABLE IF EXISTS `ecoledesponts.brevo.brevo`;

-- Supprimer la nouvelle table si elle existe
DROP TABLE IF EXISTS `ecoledesponts.brevo.brevo_events`;

-- Créer la table brevo_events avec le bon schéma
CREATE TABLE `ecoledesponts.brevo.brevo_events` (
  -- Informations de l'événement
  date TIMESTAMP OPTIONS(description="Date et heure de l'événement"),
  email STRING OPTIONS(description="Adresse email du contact"),
  event STRING OPTIONS(description="Type d'événement (spam, opened, click, hard_bounce, soft_bounce, delivered, unsubscribe, contact_deleted, contact_updated, list_addition, etc.)"),

  -- Identifiants
  -- Note: id peut être NULL pour les événements de l'API /events
  id INT64 OPTIONS(description="ID de l'événement (peut être NULL)"),
  message_id STRING OPTIONS(description="ID du message - Identifiant principal (ex: <202302241202.77117841982@smtp-relay.mailin.fr>)"),

  -- Détails de l'envoi
  reason STRING OPTIONS(description="Raison de l'événement (ex: sent)"),
  sending_ip STRING OPTIONS(description="IP d'envoi du message"),
  subject STRING OPTIONS(description="Sujet de l'email"),

  -- Tags et metadata
  tag STRING OPTIONS(description="Tag principal associé"),
  tags STRING OPTIONS(description="Liste de tous les tags associés au format JSON array (ex: [\"tag1\",\"tag2\"])"),
  template_id INT64 OPTIONS(description="ID du template utilisé"),

  -- Timestamps
  ts TIMESTAMP OPTIONS(description="Timestamp de l'événement"),
  ts_epoch INT64 OPTIONS(description="Timestamp epoch de l'événement"),
  ts_event TIMESTAMP OPTIONS(description="Timestamp spécifique de l'événement"),

  -- Champs personnalisés
  x_mailin_custom STRING OPTIONS(description="Champs personnalisés X-Mailin"),

  -- Informations sur les clics
  link STRING OPTIONS(description="URL du lien cliqué (pour les événements de type click)"),

  -- Autres champs
  s_returnpath BOOLEAN OPTIONS(description="Indicateur de returnpath"),

  -- Compteurs par type d'événement (pour faciliter les agrégations)
  spam INT64 OPTIONS(description="1 si événement spam, 0 sinon"),
  opened INT64 OPTIONS(description="1 si événement opened, 0 sinon"),
  click INT64 OPTIONS(description="1 si événement click, 0 sinon"),
  hard_bounce INT64 OPTIONS(description="1 si événement hard_bounce, 0 sinon"),
  soft_bounce INT64 OPTIONS(description="1 si événement soft_bounce, 0 sinon"),
  delivered INT64 OPTIONS(description="1 si événement delivered, 0 sinon"),
  unsubscribe INT64 OPTIONS(description="1 si événement unsubscribe, 0 sinon"),
  contact_deleted INT64 OPTIONS(description="1 si événement contact_deleted, 0 sinon"),
  contact_updated INT64 OPTIONS(description="1 si événement contact_updated, 0 sinon"),
  list_addition INT64 OPTIONS(description="1 si événement list_addition, 0 sinon"),

  -- Métadonnées de traitement
  retrieved_at TIMESTAMP NOT NULL OPTIONS(description="Date et heure de récupération des données depuis l'API Brevo"),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Date de dernière mise à jour de la ligne"),
  export_process_id INT64 OPTIONS(description="ID du process d'export Brevo")
)
PARTITION BY DATE(date)
CLUSTER BY event, email
OPTIONS(
  description="Événements marketing hebdomadaires Brevo (spam, opened, click, bounces, unsubscribe, etc.). Données récupérées via Brevo API /v3/smtp/statistics/events.",
  labels=[("source", "brevo_api"), ("data_type", "marketing_events"), ("frequency", "daily")]
);
