-- ============================================================================
-- SCHEMA BIGQUERY POUR BREVO SMTP REPORTS
-- Dataset: brevo
-- ============================================================================

-- Table: brevo_smtp_reports
-- Cette table stocke les rapports agrégés d'emails par jour
-- Documentation: https://developers.brevo.com/reference/get-aggregated-smtp-report
CREATE TABLE IF NOT EXISTS `ecoledesponts.brevo.brevo_smtp_reports` (
  -- Période du rapport
  report_date DATE NOT NULL OPTIONS(description="Date du rapport"),

  -- Statistiques d'envoi
  requests INT64 OPTIONS(description="Nombre total de requêtes d'envoi"),
  delivered INT64 OPTIONS(description="Nombre d'emails délivrés"),
  hard_bounces INT64 OPTIONS(description="Nombre de hard bounces"),
  soft_bounces INT64 OPTIONS(description="Nombre de soft bounces"),
  clicks INT64 OPTIONS(description="Nombre de clics"),
  unique_clicks INT64 OPTIONS(description="Nombre de clics uniques"),
  opens INT64 OPTIONS(description="Nombre d'ouvertures"),
  unique_opens INT64 OPTIONS(description="Nombre d'ouvertures uniques"),
  spam_reports INT64 OPTIONS(description="Nombre de signalements spam"),
  blocked INT64 OPTIONS(description="Nombre d'emails bloqués"),
  invalid INT64 OPTIONS(description="Nombre d'adresses invalides"),
  unsubscribed INT64 OPTIONS(description="Nombre de désabonnements"),

  -- Taux calculés
  delivery_rate FLOAT64 OPTIONS(description="Taux de délivrance (%)"),
  open_rate FLOAT64 OPTIONS(description="Taux d'ouverture (%)"),
  click_rate FLOAT64 OPTIONS(description="Taux de clic (%)"),
  bounce_rate FLOAT64 OPTIONS(description="Taux de bounce total (%)"),
  unsubscribe_rate FLOAT64 OPTIONS(description="Taux de désabonnement (%)"),

  -- Métadonnées de traitement
  retrieved_at TIMESTAMP NOT NULL OPTIONS(description="Date et heure de récupération des données"),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Date de dernière mise à jour dans BigQuery")
)
PARTITION BY report_date
OPTIONS(
  description="Rapports SMTP agrégés par jour Brevo. Données récupérées via l'API Brevo /v3/smtp/statistics/aggregatedReport.",
  labels=[("source", "brevo_api"), ("data_type", "smtp_reports"), ("frequency", "daily")]
);
