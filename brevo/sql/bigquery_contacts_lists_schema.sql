-- ============================================================================
-- SCHEMA BIGQUERY POUR BREVO CONTACTS LISTS
-- Dataset: brevo
-- ============================================================================

-- Table: brevo_contacts_lists
-- Cette table stocke les informations sur les listes de contacts
-- Documentation: https://developers.brevo.com/reference/get-lists
CREATE TABLE IF NOT EXISTS `ecoledesponts.brevo.brevo_contacts_lists` (
  -- Identifiants
  id INT64 NOT NULL OPTIONS(description="ID unique de la liste"),
  name STRING OPTIONS(description="Nom de la liste"),

  -- Organisation
  folder_id INT64 OPTIONS(description="ID du dossier parent"),
  folder_name STRING OPTIONS(description="Nom du dossier parent"),

  -- Statistiques
  total_subscribers INT64 OPTIONS(description="Nombre total d'abonnés dans la liste"),
  total_blacklisted INT64 OPTIONS(description="Nombre de contacts blacklistés"),
  unique_subscribers INT64 OPTIONS(description="Nombre d'abonnés uniques (pas dans d'autres listes)"),

  -- Métadonnées
  created_at TIMESTAMP OPTIONS(description="Date de création de la liste"),

  -- Métadonnées de traitement
  retrieved_at TIMESTAMP NOT NULL OPTIONS(description="Date et heure de récupération des données"),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Date de dernière mise à jour dans BigQuery")
)
CLUSTER BY id
OPTIONS(
  description="Listes de contacts Brevo. Données récupérées via l'API Brevo /v3/contacts/lists.",
  labels=[("source", "brevo_api"), ("data_type", "contacts_lists"), ("frequency", "daily")]
);
