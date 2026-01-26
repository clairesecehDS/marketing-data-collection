-- ============================================================================
-- SCHEMA BIGQUERY POUR BREVO EMAIL CAMPAIGNS
-- Dataset: brevo
-- ============================================================================

-- Table: brevo_campaigns
-- Cette table stocke les informations sur toutes les campagnes email
-- Documentation: https://developers.brevo.com/reference/get-email-campaigns
CREATE TABLE IF NOT EXISTS `ecoledesponts.brevo.brevo_campaigns` (
  -- Identifiants
  id INT64 NOT NULL OPTIONS(description="ID unique de la campagne"),
  name STRING OPTIONS(description="Nom de la campagne"),

  -- Sujet et contenu
  subject STRING OPTIONS(description="Sujet de l'email"),
  preview_text STRING OPTIONS(description="Texte de prévisualisation"),

  -- Type et statut
  type STRING OPTIONS(description="Type de campagne (classic, trigger, etc.)"),
  status STRING OPTIONS(description="Statut (draft, sent, queued, suspended, archive)"),

  -- Configuration d'envoi
  sender_name STRING OPTIONS(description="Nom de l'expéditeur"),
  sender_email STRING OPTIONS(description="Email de l'expéditeur"),
  reply_to STRING OPTIONS(description="Adresse de réponse"),
  to_field STRING OPTIONS(description="Destinataire (nom de la liste ou segment)"),

  -- HTML et contenu
  html_content STRING OPTIONS(description="Contenu HTML de l'email"),

  -- Planification
  scheduled_at TIMESTAMP OPTIONS(description="Date et heure planifiée d'envoi"),
  sent_date TIMESTAMP OPTIONS(description="Date et heure réelle d'envoi"),

  -- A/B Testing
  ab_testing BOOLEAN OPTIONS(description="Indique si la campagne utilise l'A/B testing"),
  subject_a STRING OPTIONS(description="Sujet A pour A/B testing"),
  subject_b STRING OPTIONS(description="Sujet B pour A/B testing"),

  -- Tags et organisation
  tag STRING OPTIONS(description="Tag principal de la campagne"),

  -- Statistiques (snapshot au moment de la récupération)
  stats_unique_clicks INT64 OPTIONS(description="Nombre de clics uniques"),
  stats_clickers INT64 OPTIONS(description="Nombre de personnes ayant cliqué"),
  stats_complaints INT64 OPTIONS(description="Nombre de plaintes"),
  stats_delivered INT64 OPTIONS(description="Nombre d'emails délivrés"),
  stats_sent INT64 OPTIONS(description="Nombre d'emails envoyés"),
  stats_soft_bounces INT64 OPTIONS(description="Nombre de soft bounces"),
  stats_hard_bounces INT64 OPTIONS(description="Nombre de hard bounces"),
  stats_unique_views INT64 OPTIONS(description="Nombre de vues uniques"),
  stats_trackable_views INT64 OPTIONS(description="Nombre de vues trackables"),
  stats_unsubscriptions INT64 OPTIONS(description="Nombre de désabonnements"),
  stats_viewed INT64 OPTIONS(description="Nombre total de vues"),
  stats_deferred INT64 OPTIONS(description="Nombre d'envois différés"),

  -- Taux calculés (pour faciliter les requêtes)
  open_rate FLOAT64 OPTIONS(description="Taux d'ouverture (%)"),
  click_rate FLOAT64 OPTIONS(description="Taux de clic (%)"),
  bounce_rate FLOAT64 OPTIONS(description="Taux de bounce (%)"),
  unsubscribe_rate FLOAT64 OPTIONS(description="Taux de désabonnement (%)"),

  -- Métadonnées de traitement
  retrieved_at TIMESTAMP NOT NULL OPTIONS(description="Date et heure de récupération des données"),
  created_at TIMESTAMP OPTIONS(description="Date de création de la campagne dans Brevo"),
  modified_at TIMESTAMP OPTIONS(description="Date de dernière modification dans Brevo"),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Date de dernière mise à jour dans BigQuery")
)
PARTITION BY DATE(sent_date)
CLUSTER BY status, id
OPTIONS(
  description="Campagnes email Brevo avec statistiques. Données récupérées via l'API Brevo /v3/emailCampaigns.",
  labels=[("source", "brevo_api"), ("data_type", "campaigns"), ("frequency", "daily")]
);
