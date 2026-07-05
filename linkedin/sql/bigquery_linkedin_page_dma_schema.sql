-- =====================================================
-- LinkedIn Page (Data Portability API) Schema for BigQuery
-- =====================================================
-- Dataset: linkedin_page
-- Script: linkedin_page_dma_scraper.py
-- API Version: 202511
-- =====================================================

-- =====================================================
-- ANALYTICS TABLES
-- =====================================================

-- Table: page_statistics
-- Description: Statistiques complètes de la page (métriques de contenu + audience)
-- Source: Fusion de dmaOrganizationalPageContentAnalytics + dmaOrganizationalPageEdgeAnalytics
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.page_statistics` (
  -- Identifiers
  organization_id STRING NOT NULL,

  -- Audience Metrics (depuis Edge Analytics)
  page_follower_count INT64,          -- Nombre total de followers (non disponible via DMA)
  visitor_count INT64,                -- Nombre de visiteurs uniques
  new_follower_count INT64,           -- Nouveaux followers acquis durant la période

  -- Content Performance Metrics (depuis Content Analytics)
  impression_count INT64,
  unique_impression_count INT64,
  click_count INT64,
  comment_count INT64,
  reaction_count INT64,
  repost_count INT64,
  engagement_rate FLOAT64,
  acquired_follows INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id;

-- Table: page_edge_analytics
-- Description: Analytics des relations followers (membres et pages)
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.page_edge_analytics` (
  -- Identifiers
  organization_id STRING NOT NULL,
  edge_type STRING NOT NULL,  -- MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE | PAGE_FOLLOWS_ORGANIZATIONAL_PAGE

  -- Metrics
  visitor_count INT64,
  page_follower_count INT64,
  active_follower_count INT64,
  new_follower_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, edge_type;

-- Table: page_content_analytics
-- Description: Analytics détaillées par contenu publié
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.page_content_analytics` (
  -- Identifiers
  organization_id STRING NOT NULL,
  content_urn STRING,

  -- Metrics
  impression_count INT64,
  reaction_count INT64,
  comment_count INT64,
  repost_count INT64,
  click_count INT64,

  -- Demographics (JSON)
  demographics_breakdown STRING,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, content_urn;

-- Table: search_appearance_analytics
-- Description: Analytics des apparitions dans les recherches LinkedIn
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.search_appearance_analytics` (
  -- Identifiers
  organization_id STRING NOT NULL,

  -- Metrics
  search_impressions INT64,
  search_clicks INT64,
  impression_to_click_ratio FLOAT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id;

-- =====================================================
-- FEED & CONTENT TABLES
-- =====================================================

-- Table: posts
-- Description: Tous les posts publiés par la page
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.posts` (
  -- Identifiers
  organization_id STRING NOT NULL,
  post_id STRING NOT NULL,  -- URN du post

  -- Content
  text STRING,
  author STRING,
  visibility STRING,

  -- Timestamps
  created_time TIMESTAMP,

  -- Metrics
  comment_count INT64,
  reaction_count INT64,
  repost_count INT64,
  click_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, post_id;

-- Table: comments
-- Description: Tous les commentaires sur les posts de la page
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.comments` (
  -- Identifiers
  organization_id STRING NOT NULL,
  comment_id STRING NOT NULL,  -- URN du commentaire

  -- Content
  text STRING,
  author STRING,
  author_name STRING,  -- Si membre a opt-in pour partage de données

  -- Timestamps
  created_time TIMESTAMP,

  -- Metrics
  reaction_count INT64,

  -- Status
  status STRING,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, comment_id;

-- Table: reactions
-- Description: Toutes les réactions sur les contenus de la page
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.reactions` (
  -- Identifiers
  organization_id STRING NOT NULL,
  reaction_id STRING NOT NULL,  -- URN de la réaction

  -- Reaction Details
  reactor STRING,  -- URN de la personne
  reaction_type STRING,  -- LIKE, PRAISE, APPRECIATION, EMPATHY, INTEREST, ENTERTAINMENT
  content_urn STRING,  -- URN du contenu

  -- Timestamps
  created_time TIMESTAMP,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, reaction_type, content_urn;

-- =====================================================
-- FOLLOWERS TABLE
-- =====================================================

-- Table: followers
-- Description: Liste complète des followers de la page
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.followers` (
  -- Identifiers
  organization_id STRING NOT NULL,
  follow_id STRING NOT NULL,  -- URN du follow
  follower STRING,  -- URN du follower (person ou page)

  -- Follower Info (si opt-in)
  follower_name STRING,
  follower_headline STRING,

  -- Timestamps
  followed_on TIMESTAMP,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, follow_id;

-- =====================================================
-- PROFILE TABLE
-- =====================================================

-- Table: page_profile
-- Description: Informations de profil de la page
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.page_profile` (
  -- Identifiers
  organization_id STRING NOT NULL,
  page_id STRING,

  -- Basic Info
  name STRING,
  profile_url STRING,
  tagline STRING,
  description STRING,
  website STRING,

  -- Rich Data (JSON)
  logo STRING,
  industry_categories STRING,  -- JSON array
  specialities STRING,  -- JSON array
  locations STRING,  -- JSON array

  -- Metrics
  follower_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id;

-- =====================================================
-- LEAD GENERATION TABLE
-- =====================================================

-- Table: lead_gen_forms
-- Description: Formulaires de génération de leads
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.lead_gen_forms` (
  -- Identifiers
  organization_id STRING NOT NULL,
  form_id STRING NOT NULL,  -- URN du formulaire

  -- Form Details
  form_name STRING,
  headline STRING,
  description STRING,

  -- Questions (JSON)
  questions STRING,  -- JSON array

  -- Timestamps
  created_time TIMESTAMP,
  last_modified_time TIMESTAMP,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, form_id;

-- =====================================================
-- EVENTS TABLE
-- =====================================================

-- Table: events
-- Description: Événements organisés par la page
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.events` (
  -- Identifiers
  organization_id STRING NOT NULL,
  event_id STRING NOT NULL,  -- URN de l'événement

  -- Event Details
  title STRING,
  description STRING,
  start_date STRING,
  end_date STRING,

  -- Location (JSON)
  location STRING,

  -- Organizer
  organizer_urn STRING,

  -- Metrics
  registration_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, event_id;

-- =====================================================
-- PUBLISHING TABLES
-- =====================================================

-- Table: content_series
-- Description: Séries de contenu (newsletters)
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.content_series` (
  -- Identifiers
  organization_id STRING NOT NULL,
  series_id STRING NOT NULL,  -- URN de la série

  -- Series Details
  name STRING,
  description STRING,
  cadence STRING,

  -- Metrics
  subscriber_count INT64,
  issue_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, series_id;

-- Table: original_articles
-- Description: Articles originaux publiés
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.original_articles` (
  -- Identifiers
  organization_id STRING NOT NULL,
  article_id STRING NOT NULL,  -- URN de l'article

  -- Article Content
  title STRING,
  article_body STRING,  -- HTML
  published_date STRING,

  -- Media (JSON)
  cover_image STRING,
  authors STRING,  -- JSON array

  -- Metrics
  view_count INT64,
  like_count INT64,
  comment_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY organization_id, article_id;

-- =====================================================
-- USEFUL VIEWS
-- =====================================================

-- View: Page Performance Dashboard
-- Description: Vue d'ensemble des performances de la page
-- =====================================================
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_page_dashboard` AS
WITH latest_stats AS (
  SELECT *
  FROM `project-id.linkedin_page.page_statistics`
  WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.page_statistics`)
),
latest_profile AS (
  SELECT *
  FROM `project-id.linkedin_page.page_profile`
  WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.page_profile`)
),
recent_posts AS (
  SELECT
    organization_id,
    COUNT(DISTINCT post_id) as posts_count,
    SUM(comment_count) as total_comments,
    SUM(reaction_count) as total_reactions,
    SUM(repost_count) as total_reposts,
    SUM(click_count) as total_clicks
  FROM `project-id.linkedin_page.posts`
  WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  GROUP BY organization_id
)
SELECT
  p.organization_id,
  p.name as page_name,
  p.profile_url,
  s.page_follower_count,
  s.impression_count,
  s.click_count,
  rp.posts_count as posts_last_30_days,
  rp.total_comments,
  rp.total_reactions,
  rp.total_reposts,
  ROUND(SAFE_DIVIDE(rp.total_clicks, s.impression_count) * 100, 2) as ctr_percentage,
  s.retrieved_at
FROM latest_profile p
LEFT JOIN latest_stats s ON p.organization_id = s.organization_id
LEFT JOIN recent_posts rp ON p.organization_id = rp.organization_id;

-- View: Top Performing Posts
-- Description: Posts les plus performants
-- =====================================================
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_top_posts` AS
SELECT
  organization_id,
  post_id,
  LEFT(text, 100) as text_excerpt,
  created_time,
  comment_count,
  reaction_count,
  repost_count,
  click_count,
  COALESCE(comment_count, 0) + COALESCE(reaction_count, 0) + COALESCE(repost_count, 0) as total_engagement,
  CASE
    WHEN click_count > 0 THEN ROUND(SAFE_DIVIDE(
      COALESCE(comment_count, 0) + COALESCE(reaction_count, 0) + COALESCE(repost_count, 0),
      click_count
    ) * 100, 2)
    ELSE NULL
  END as engagement_rate,
  RANK() OVER (PARTITION BY organization_id ORDER BY COALESCE(comment_count, 0) + COALESCE(reaction_count, 0) + COALESCE(repost_count, 0) DESC) as engagement_rank,
  retrieved_at
FROM `project-id.linkedin_page.posts`
WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.posts`)
  AND (COALESCE(comment_count, 0) + COALESCE(reaction_count, 0) + COALESCE(repost_count, 0)) > 0
ORDER BY total_engagement DESC
LIMIT 100;

-- View: Engagement Trends
-- Description: Tendances d'engagement au fil du temps
-- =====================================================
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_engagement_trends` AS
SELECT
  organization_id,
  DATE(created_time) as post_date,
  COUNT(DISTINCT post_id) as posts_count,
  SUM(comment_count) as total_comments,
  SUM(reaction_count) as total_reactions,
  SUM(repost_count) as total_reposts,
  SUM(COALESCE(comment_count, 0) + COALESCE(reaction_count, 0) + COALESCE(repost_count, 0)) as total_engagement,
  ROUND(AVG(CASE
    WHEN click_count > 0 THEN SAFE_DIVIDE(
      COALESCE(comment_count, 0) + COALESCE(reaction_count, 0) + COALESCE(repost_count, 0),
      click_count
    ) * 100
    ELSE NULL
  END), 2) as avg_engagement_rate
FROM `project-id.linkedin_page.posts`
WHERE created_time IS NOT NULL
GROUP BY organization_id, post_date
ORDER BY post_date DESC;

-- View: Reaction Type Distribution
-- Description: Distribution des types de réactions
-- =====================================================
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_reaction_distribution` AS
SELECT
  organization_id,
  reaction_type,
  COUNT(*) as reaction_count,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY organization_id), 2) as percentage
FROM `project-id.linkedin_page.reactions`
WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.reactions`)
GROUP BY organization_id, reaction_type
ORDER BY organization_id, reaction_count DESC;

-- View: Follower Growth
-- Description: Croissance des followers au fil du temps
-- =====================================================
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_follower_growth` AS
WITH daily_followers AS (
  SELECT
    organization_id,
    DATE(followed_on) as follow_date,
    COUNT(*) as new_followers
  FROM `project-id.linkedin_page.followers`
  WHERE followed_on IS NOT NULL
  GROUP BY organization_id, follow_date
)
SELECT
  organization_id,
  follow_date,
  new_followers,
  SUM(new_followers) OVER (PARTITION BY organization_id ORDER BY follow_date) as cumulative_followers
FROM daily_followers
ORDER BY organization_id, follow_date DESC;

-- View: Content Analytics Summary
-- Description: Résumé des analytics de contenu
-- =====================================================
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_content_analytics_summary` AS
SELECT
  organization_id,
  content_urn,
  impression_count,
  reaction_count,
  comment_count,
  repost_count,
  click_count,
  ROUND(SAFE_DIVIDE(click_count, impression_count) * 100, 2) as ctr,
  ROUND(SAFE_DIVIDE(reaction_count + comment_count + repost_count, impression_count) * 100, 2) as engagement_rate,
  retrieved_at
FROM `project-id.linkedin_page.page_content_analytics`
WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.page_content_analytics`)
  AND impression_count > 0
ORDER BY engagement_rate DESC;

-- =====================================================
-- EXAMPLE QUERIES
-- =====================================================

-- Query 1: Page Performance Dashboard
/*
SELECT *
FROM `project-id.linkedin_page.v_page_dashboard`
WHERE organization_id = '12345678';
*/

-- Query 2: Top 10 Posts par Engagement
/*
SELECT
  text_excerpt,
  created_time,
  total_engagement,
  engagement_rate
FROM `project-id.linkedin_page.v_top_posts`
WHERE organization_id = '12345678'
LIMIT 10;
*/

-- Query 3: Engagement Trends (30 derniers jours)
/*
SELECT
  post_date,
  posts_count,
  total_engagement,
  avg_engagement_rate
FROM `project-id.linkedin_page.v_engagement_trends`
WHERE organization_id = '12345678'
  AND post_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
ORDER BY post_date DESC;
*/

-- Query 4: Distribution des types de réactions
/*
SELECT
  reaction_type,
  reaction_count,
  percentage
FROM `project-id.linkedin_page.v_reaction_distribution`
WHERE organization_id = '12345678';
*/

-- Query 5: Croissance des followers (6 derniers mois)
/*
SELECT
  follow_date,
  new_followers,
  cumulative_followers
FROM `project-id.linkedin_page.v_follower_growth`
WHERE organization_id = '12345678'
  AND follow_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
ORDER BY follow_date DESC;
*/

-- Query 6: Analyse des commentaires les plus réactifs
/*
SELECT
  LEFT(text, 100) as comment_excerpt,
  author_name,
  reaction_count,
  created_time
FROM `project-id.linkedin_page.comments`
WHERE organization_id = '12345678'
  AND reaction_count > 0
ORDER BY reaction_count DESC
LIMIT 20;
*/

-- Query 7: Performance des formulaires lead gen
/*
SELECT
  form_name,
  headline,
  created_time,
  last_modified_time
FROM `project-id.linkedin_page.lead_gen_forms`
WHERE organization_id = '12345678'
ORDER BY created_time DESC;
*/

-- Query 8: Événements à venir
/*
SELECT
  title,
  start_date,
  end_date,
  registration_count
FROM `project-id.linkedin_page.events`
WHERE organization_id = '12345678'
  AND start_date >= FORMAT_DATE('%Y-%m-%d', CURRENT_DATE())
ORDER BY start_date;
*/

-- Query 9: Performance des articles
/*
SELECT
  title,
  published_date,
  view_count,
  like_count,
  comment_count,
  total_engagement
FROM `project-id.linkedin_page.original_articles`
WHERE organization_id = '12345678'
ORDER BY total_engagement DESC
LIMIT 10;
*/

-- Query 10: Statistiques par série de contenu
/*
SELECT
  name,
  subscriber_count,
  issue_count,
  cadence
FROM `project-id.linkedin_page.content_series`
WHERE organization_id = '12345678'
ORDER BY subscriber_count DESC;
*/
