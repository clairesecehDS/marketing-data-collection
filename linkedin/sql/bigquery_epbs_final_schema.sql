-- =====================================================
-- LinkedIn - Schémas BigQuery Finaux
-- École des Ponts Business School
-- =====================================================
-- Projet: ecoledesponts
-- Dataset: linkedin_page
-- Region: europe-west9
-- =====================================================

-- Table 1: FOLLOWERS
-- Statistiques de followers ventilées par dimensions
-- Source: organizationalEntityFollowerStatistics
-- =====================================================
CREATE TABLE IF NOT EXISTS `ecoledesponts.linkedin_page.followers` (
  organization_id STRING NOT NULL,
  dimension_type STRING NOT NULL,  -- 'geo', 'geo_country', 'function', 'seniority', 'industry', 'staff_count_range', 'association_type'
  dimension_value STRING NOT NULL, -- URN ou valeur (ex: 'urn:li:geo:102787409', 'SIZE_10001_OR_MORE', 'EMPLOYEE')
  organic_follower_count INT64,
  paid_follower_count INT64,
  retrieved_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, dimension_type;

-- Table 2: PAGE_STATISTICS
-- Statistiques de vues de page ventilées par dimensions
-- Source: organizationPageStatistics
-- =====================================================
CREATE TABLE IF NOT EXISTS `ecoledesponts.linkedin_page.page_statistics` (
  organization_id STRING NOT NULL,
  dimension_type STRING NOT NULL,  -- 'geo', 'geo_country', 'function', 'seniority', 'industry', 'staff_count_range', 'total'
  dimension_value STRING,          -- URN ou valeur (NULL pour 'total')
  page_views INT64,                -- allPageViews.pageViews (total desktop + mobile)
  retrieved_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, dimension_type;

-- Table 3: CONTENT_STATISTICS
-- Statistiques d'engagement sur les contenus partagés par jour
-- Source: organizationalEntityShareStatistics avec timeIntervals
-- =====================================================
CREATE TABLE IF NOT EXISTS `ecoledesponts.linkedin_page.content_statistics` (
  organization_id STRING NOT NULL,
  time_start DATE NOT NULL,        -- Date de début de la période (format YYYY-MM-DD)
  time_end DATE NOT NULL,          -- Date de fin de la période (format YYYY-MM-DD)
  unique_impressions_count INT64,  -- Nombre d'impressions uniques
  impression_count INT64,          -- Nombre total d'impressions
  click_count INT64,               -- Nombre de clics
  like_count INT64,                -- Nombre de likes
  comment_count INT64,             -- Nombre de commentaires
  share_count INT64,               -- Nombre de partages
  engagement_rate FLOAT64,         -- Taux d'engagement calculé: (clicks + likes + comments + shares) / impressions
  retrieved_at TIMESTAMP NOT NULL
)
PARTITION BY time_start
CLUSTER BY organization_id, time_start;

-- Table 4: FOLLOWERS_TIMESERIES
-- Gains de followers par jour (sans ventilation par dimensions)
-- Source: organizationalEntityFollowerStatistics avec timeIntervals
-- =====================================================
CREATE TABLE IF NOT EXISTS `ecoledesponts.linkedin_page.followers_timeseries` (
  organization_id STRING NOT NULL,
  time_start DATE NOT NULL,        -- Date de début de la période (format YYYY-MM-DD)
  time_end DATE NOT NULL,          -- Date de fin de la période (format YYYY-MM-DD)
  organic_follower_gain INT64,     -- Nombre de followers organiques gagnés ce jour
  paid_follower_gain INT64,        -- Nombre de followers payés gagnés ce jour
  retrieved_at TIMESTAMP NOT NULL
)
PARTITION BY time_start
CLUSTER BY organization_id, time_start;

CREATE TABLE IF NOT EXISTS `ecoledesponts.linkedin_page.page_statistics_timeseries` (
  organization_id STRING NOT NULL,
  time_start DATE NOT NULL,        -- Date de début de la période (format YYYY-MM-DD)
  time_end DATE NOT NULL,          -- Date de fin de la période (format YYYY-MM-DD)
  page_views INT64,                -- allPageViews.pageViews (total desktop + mobile)
  retrieved_at TIMESTAMP NOT NULL
)
PARTITION BY time_start
CLUSTER BY organization_id, time_start;
