-- ============================================================================
-- SCHEMA BIGQUERY POUR BREVO MARKETING EVENTS
-- Dataset: brevo
-- ============================================================================

-- Table: brevo_events
-- Cette table stocke les événements marketing de Brevo
-- Documentation: https://developers.brevo.com/reference/get-email-event-report
CREATE TABLE IF NOT EXISTS `ecoledesponts.brevo.brevo_events` (
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
  description="Événements marketing Brevo (spam, opened, click, bounces, unsubscribe, etc.). Données récupérées via l'API Brevo /v3/smtp/statistics/events.",
  labels=[("source", "brevo_api"), ("data_type", "marketing_events"), ("frequency", "daily")]
);

-- ============================================================================
-- INDEX RECOMMANDÉS
-- ============================================================================
-- Les partitions par date et le clustering par event et email permettent
-- d'optimiser les requêtes fréquentes sur:
-- - Les événements d'un type spécifique (event)
-- - Les événements d'un email donné
-- - Les événements dans une période donnée (date)

-- ============================================================================
-- EXEMPLE DE REQUÊTES UTILES
-- ============================================================================

-- Compter les événements par type
-- SELECT event, COUNT(*) as count
-- FROM `ecoledesponts.brevo.brevo_events`
-- WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
-- GROUP BY event
-- ORDER BY count DESC;

-- Taux d'ouverture par campagne (basé sur subject)
-- SELECT
--   subject,
--   COUNTIF(event = 'delivered') as delivered,
--   COUNTIF(event = 'opened') as opened,
--   SAFE_DIVIDE(COUNTIF(event = 'opened'), COUNTIF(event = 'delivered')) * 100 as open_rate
-- FROM `ecoledesponts.brevo.brevo_events`
-- WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
-- GROUP BY subject
-- HAVING delivered > 0
-- ORDER BY open_rate DESC;

-- Analyse des bounces par email
-- SELECT
--   email,
--   COUNTIF(event = 'hard_bounce') as hard_bounces,
--   COUNTIF(event = 'soft_bounce') as soft_bounces
-- FROM `ecoledesponts.brevo.brevo_events`
-- WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
--   AND event IN ('hard_bounce', 'soft_bounce')
-- GROUP BY email
-- ORDER BY hard_bounces DESC, soft_bounces DESC;
