-- ============================================================
-- SPYFU BIGQUERY SCHEMA COMPLET
-- ============================================================
-- Schéma complet pour toutes les tables et vues SpyFu
-- Remplacez "project-id" par votre vrai project ID:
--   - International SOS: international-sos-479209
--   - École des Ponts: ecoledesponts
-- ============================================================


-- ============================================================
-- TABLE 1: PPC KEYWORDS (getMostSuccessful)
-- ============================================================
-- Scripts mensuels - Mots-clés PPC les plus performants
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.ppc_keywords` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING,

  -- Métriques de recherche
  search_volume INT64,
  live_search_volume INT64,
  ranking_difficulty FLOAT64,
  total_monthly_clicks INT64,

  -- Pourcentages de recherche
  percent_mobile_searches FLOAT64,
  percent_desktop_searches FLOAT64,
  percent_searches_not_clicked FLOAT64,
  percent_paid_clicks FLOAT64,
  percent_organic_clicks FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Clics mensuels par match type
  broad_monthly_clicks INT64,
  phrase_monthly_clicks INT64,
  exact_monthly_clicks INT64,

  -- Coûts mensuels par match type
  broad_monthly_cost FLOAT64,
  phrase_monthly_cost FLOAT64,
  exact_monthly_cost FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,
  distinct_competitors STRING,
  ranking_homepages INT64,

  -- Informations SERP
  serp_features_csv STRING,
  serp_first_result STRING,

  -- Flags
  is_question BOOLEAN,
  is_not_safe_for_work BOOLEAN,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- VUES pour ppc_keywords

CREATE OR REPLACE VIEW `project-id.spyfu.top_keywords_by_volume` AS
SELECT
  domain,
  keyword,
  search_volume,
  live_search_volume,
  ranking_difficulty,
  total_monthly_clicks,
  broad_cost_per_click,
  broad_monthly_cost,
  paid_competitors,
  retrieved_at
FROM `project-id.spyfu.ppc_keywords`
WHERE search_volume IS NOT NULL
ORDER BY domain, search_volume DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.cpc_analysis` AS
SELECT
  domain,
  keyword,
  broad_cost_per_click,
  phrase_cost_per_click,
  exact_cost_per_click,
  broad_monthly_cost,
  phrase_monthly_cost,
  exact_monthly_cost,
  total_monthly_clicks,
  paid_competitors,
  retrieved_at
FROM `project-id.spyfu.ppc_keywords`
WHERE broad_cost_per_click IS NOT NULL
ORDER BY domain, broad_cost_per_click DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.keyword_opportunities` AS
SELECT
  domain,
  keyword,
  search_volume,
  ranking_difficulty,
  broad_cost_per_click,
  paid_competitors,
  total_monthly_clicks,
  retrieved_at
FROM `project-id.spyfu.ppc_keywords`
WHERE ranking_difficulty < 50
  AND search_volume > 1000
ORDER BY domain, search_volume DESC, ranking_difficulty ASC;


-- ============================================================
-- TABLE 2: NEW KEYWORDS (getNewKeywords)
-- ============================================================
-- Scripts mensuels - Nouveaux mots-clés PPC
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.new_keywords` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING,

  -- Métriques de recherche
  search_volume INT64,
  live_search_volume INT64,
  ranking_difficulty FLOAT64,
  total_monthly_clicks INT64,

  -- Pourcentages de recherche
  percent_mobile_searches FLOAT64,
  percent_desktop_searches FLOAT64,
  percent_searches_not_clicked FLOAT64,
  percent_paid_clicks FLOAT64,
  percent_organic_clicks FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Clics mensuels par match type
  broad_monthly_clicks INT64,
  phrase_monthly_clicks INT64,
  exact_monthly_clicks INT64,

  -- Coûts mensuels par match type
  broad_monthly_cost FLOAT64,
  phrase_monthly_cost FLOAT64,
  exact_monthly_cost FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,
  distinct_competitors STRING,
  ranking_homepages INT64,

  -- Informations SERP
  serp_features_csv STRING,
  serp_first_result STRING,

  -- Flags
  is_question BOOLEAN,
  is_not_safe_for_work BOOLEAN,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- VUES pour new_keywords

CREATE OR REPLACE VIEW `project-id.spyfu.new_keywords_by_domain` AS
SELECT
  domain,
  keyword,
  search_volume,
  ranking_difficulty,
  broad_cost_per_click,
  paid_competitors,
  total_monthly_clicks,
  retrieved_at
FROM `project-id.spyfu.new_keywords`
ORDER BY domain, search_volume DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.new_keyword_opportunities` AS
SELECT
  domain,
  keyword,
  search_volume,
  ranking_difficulty,
  broad_cost_per_click,
  paid_competitors,
  total_monthly_clicks,
  is_question,
  retrieved_at
FROM `project-id.spyfu.new_keywords`
WHERE ranking_difficulty < 60
  AND search_volume > 100
ORDER BY domain, search_volume DESC, ranking_difficulty ASC;


-- ============================================================
-- TABLE 3: SEO KEYWORDS (getSeoKeywords)
-- ============================================================
-- Scripts mensuels - Mots-clés SEO organiques
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.seo_keywords` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING,
  search_type STRING,  -- MostValuable, GainedClicks, LostClicks, etc.

  -- Ranking
  top_ranked_url STRING,
  rank INT64,
  rank_change INT64,

  -- Métriques de recherche
  search_volume INT64,
  keyword_difficulty FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Métriques SEO
  seo_clicks INT64,
  seo_clicks_change INT64,
  total_monthly_clicks INT64,

  -- Pourcentages de recherche
  percent_mobile_searches FLOAT64,
  percent_desktop_searches FLOAT64,
  percent_not_clicked FLOAT64,
  percent_paid_clicks FLOAT64,
  percent_organic_clicks FLOAT64,

  -- Coûts mensuels par match type
  broad_monthly_cost FLOAT64,
  phrase_monthly_cost FLOAT64,
  exact_monthly_cost FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,
  ranking_homepages INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- VUES pour seo_keywords

CREATE OR REPLACE VIEW `project-id.spyfu.most_valuable_seo_keywords` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  search_volume,
  seo_clicks,
  seo_clicks_change,
  keyword_difficulty,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.seo_keywords`
WHERE search_type = 'MostValuable'
ORDER BY domain, seo_clicks DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.seo_rankings` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  top_ranked_url,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  retrieved_at
FROM `project-id.spyfu.seo_keywords`
WHERE rank IS NOT NULL
  AND rank <= 20
ORDER BY domain, rank ASC;


CREATE OR REPLACE VIEW `project-id.spyfu.seo_opportunities` AS
SELECT
  domain,
  keyword,
  rank,
  search_volume,
  keyword_difficulty,
  seo_clicks,
  broad_cost_per_click,
  paid_competitors,
  retrieved_at
FROM `project-id.spyfu.seo_keywords`
WHERE keyword_difficulty < 50
  AND search_volume > 500
  AND (rank > 10 OR rank IS NULL)
ORDER BY domain, search_volume DESC, keyword_difficulty ASC;


-- ============================================================
-- TABLE 4: TOP PAGES (getMostTrafficTopPages)
-- ============================================================
-- Scripts mensuels - Pages avec le plus de trafic SEO
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.top_pages` (
  -- Identifiants
  domain STRING NOT NULL,
  url STRING NOT NULL,
  title STRING,

  -- Métriques de la page
  keyword_count INT64,
  est_monthly_seo_clicks INT64,

  -- Top keyword de la page
  top_keyword STRING,
  top_keyword_position INT64,
  top_keyword_search_volume INT64,
  top_keyword_clicks INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, url;


-- VUES pour top_pages

CREATE OR REPLACE VIEW `project-id.spyfu.most_valuable_pages` AS
SELECT
  domain,
  url,
  title,
  est_monthly_seo_clicks,
  keyword_count,
  top_keyword,
  top_keyword_position,
  top_keyword_search_volume,
  retrieved_at
FROM `project-id.spyfu.top_pages`
ORDER BY domain, est_monthly_seo_clicks DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.keyword_rich_pages` AS
SELECT
  domain,
  url,
  title,
  keyword_count,
  est_monthly_seo_clicks,
  top_keyword,
  retrieved_at
FROM `project-id.spyfu.top_pages`
WHERE keyword_count > 10
ORDER BY domain, keyword_count DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.domain_page_performance` AS
SELECT
  domain,
  COUNT(*) as total_pages,
  SUM(keyword_count) as total_keywords,
  SUM(est_monthly_seo_clicks) as total_monthly_clicks,
  AVG(est_monthly_seo_clicks) as avg_clicks_per_page,
  AVG(keyword_count) as avg_keywords_per_page,
  MAX(est_monthly_seo_clicks) as top_page_clicks,
  retrieved_at
FROM `project-id.spyfu.top_pages`
GROUP BY domain, retrieved_at
ORDER BY total_monthly_clicks DESC;


-- ============================================================
-- TABLE 5: DOMAIN STATS (getAllDomainStats)
-- ============================================================
-- Scripts mensuels - Statistiques complètes du domaine
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.domain_stats` (
  -- Identifiants
  domain STRING NOT NULL,
  country_code STRING DEFAULT 'US',

  -- Statistiques PPC
  total_ad_keywords INT64,
  total_ad_budget FLOAT64,
  total_ad_clicks INT64,
  ad_history_months INT64,

  -- Statistiques SEO
  total_seo_keywords INT64,
  total_organic_keywords INT64,
  total_organic_traffic INT64,
  total_organic_value FLOAT64,

  -- Statistiques de domaine
  domain_rank INT64,
  domain_authority FLOAT64,

  -- Données brutes JSON (pour données historiques complètes)
  raw_stats STRING,

  -- Métadonnées
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain;


-- VUES pour domain_stats

CREATE OR REPLACE VIEW `project-id.spyfu.domain_stats_evolution` AS
SELECT
  domain,
  total_ad_keywords,
  total_seo_keywords,
  total_organic_traffic,
  total_ad_budget,
  domain_rank,
  domain_authority,
  retrieved_at
FROM `project-id.spyfu.domain_stats`
ORDER BY domain, retrieved_at DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.domain_stats_comparison` AS
SELECT
  domain,
  total_ad_keywords,
  total_seo_keywords,
  total_organic_traffic,
  total_organic_value,
  total_ad_budget,
  domain_rank,
  domain_authority,
  retrieved_at
FROM `project-id.spyfu.domain_stats`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.domain_stats`)
ORDER BY total_organic_traffic DESC;


-- ============================================================
-- TABLE 6: MOST VALUABLE KEYWORDS (getMostValuableKeywords)
-- ============================================================
-- Scripts mensuels - Mots-clés SEO les plus précieux
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.most_valuable_keywords` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING,

  -- Ranking
  top_ranked_url STRING,
  rank INT64,
  rank_change INT64,

  -- Métriques de recherche
  search_volume INT64,
  keyword_difficulty FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Métriques SEO
  seo_clicks INT64,
  seo_clicks_change INT64,
  total_monthly_clicks INT64,

  -- Pourcentages de recherche
  percent_mobile_searches FLOAT64,
  percent_desktop_searches FLOAT64,
  percent_not_clicked FLOAT64,
  percent_paid_clicks FLOAT64,
  percent_organic_clicks FLOAT64,

  -- Coûts mensuels par match type
  broad_monthly_cost FLOAT64,
  phrase_monthly_cost FLOAT64,
  exact_monthly_cost FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,
  ranking_homepages INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- VUES pour most_valuable_keywords

CREATE OR REPLACE VIEW `project-id.spyfu.top_10_most_valuable` AS
SELECT
  domain,
  keyword,
  rank,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  broad_cost_per_click,
  (seo_clicks * broad_cost_per_click) as estimated_value,
  retrieved_at
FROM `project-id.spyfu.most_valuable_keywords`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.most_valuable_keywords`)
QUALIFY ROW_NUMBER() OVER (PARTITION BY domain ORDER BY seo_clicks DESC) <= 10
ORDER BY domain, seo_clicks DESC;


-- ============================================================
-- TABLE 7: NEWLY RANKED KEYWORDS (getNewlyRankedKeywords)
-- ============================================================
-- Mots-clés SEO nouvellement classés pour les domaines
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.newly_ranked_keywords` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING,

  -- Ranking
  top_ranked_url STRING,
  rank INT64,

  -- Métriques de recherche
  search_volume INT64,
  keyword_difficulty FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Métriques SEO
  seo_clicks INT64,
  seo_clicks_change INT64,
  total_monthly_clicks INT64,

  -- Pourcentages de recherche
  percent_mobile_searches FLOAT64,
  percent_desktop_searches FLOAT64,
  percent_not_clicked FLOAT64,
  percent_paid_clicks FLOAT64,
  percent_organic_clicks FLOAT64,

  -- Coûts mensuels par match type
  broad_monthly_cost FLOAT64,
  phrase_monthly_cost FLOAT64,
  exact_monthly_cost FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,
  ranking_homepages INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, country_code;


-- VUES pour newly_ranked_keywords

CREATE OR REPLACE VIEW `project-id.spyfu.newly_ranked_top_keywords` AS
SELECT
  domain,
  keyword,
  rank,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  broad_cost_per_click,
  (seo_clicks * broad_cost_per_click) as estimated_value,
  retrieved_at
FROM `project-id.spyfu.newly_ranked_keywords`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.newly_ranked_keywords`)
  AND search_volume IS NOT NULL
ORDER BY domain, search_volume DESC;


-- ============================================================
-- TABLE 8: DOMAIN AD HISTORY (getDomainAdHistory)
-- ============================================================
-- Scripts trimestriels - Historique des annonces par domaine
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.domain_ad_history` (
  -- Identifiants
  domain STRING NOT NULL,
  ad_id STRING,
  keyword STRING,

  -- Contenu de l'annonce
  headline STRING,
  description STRING,
  display_url STRING,
  destination_url STRING,

  -- Métriques temporelles
  first_seen_date DATE,
  last_seen_date DATE,
  days_seen INT64,

  -- Métriques de performance
  search_volume INT64,
  cost_per_click FLOAT64,
  monthly_cost FLOAT64,
  position INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- VUES pour domain_ad_history

CREATE OR REPLACE VIEW `project-id.spyfu.top_performing_ads` AS
SELECT
  domain,
  headline,
  description,
  keyword,
  search_volume,
  cost_per_click,
  monthly_cost,
  days_seen,
  position,
  first_seen_date,
  last_seen_date,
  retrieved_at
FROM `project-id.spyfu.domain_ad_history`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.domain_ad_history`)
ORDER BY domain, monthly_cost DESC, days_seen DESC
LIMIT 100;


CREATE OR REPLACE VIEW `project-id.spyfu.active_ads_analysis` AS
SELECT
  domain,
  COUNT(DISTINCT ad_id) as total_ads,
  COUNT(DISTINCT keyword) as total_keywords,
  AVG(cost_per_click) as avg_cpc,
  SUM(monthly_cost) as total_monthly_spend,
  AVG(days_seen) as avg_days_active,
  retrieved_at
FROM `project-id.spyfu.domain_ad_history`
WHERE last_seen_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY domain, retrieved_at
ORDER BY total_monthly_spend DESC;


-- ============================================================
-- TABLE 8: TERM AD HISTORY (getTermAdHistoryWithStats)
-- ============================================================
-- Scripts trimestriels - Historique des annonces par keyword
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.term_ad_history` (
  -- Identifiant principal
  keyword STRING NOT NULL,
  
  -- Identifiants annonce
  ad_id INT64,
  domain_name STRING,
  
  -- Contenu de l'annonce
  title STRING,
  body STRING,
  full_url STRING,
  term STRING,
  
  -- Métriques temporelles
  search_date_id INT64,
  
  -- Métriques de position
  average_position FLOAT64,
  position INT64,
  
  -- Métriques de volume
  average_ad_count FLOAT64,
  ad_count INT64,
  leaderboard_count INT64,
  
  -- Métriques de pourcentage
  percentage_leaderboard FLOAT64,
  percentage_ads_served FLOAT64,
  
  -- Flags
  is_leaderboard_ad BOOLEAN,
  
  -- Métadonnées
  source STRING,
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY keyword, domain_name;


-- VUES pour term_ad_history

CREATE OR REPLACE VIEW `project-id.spyfu.ads_by_keyword` AS
SELECT
  keyword,
  COUNT(DISTINCT domain_name) as advertisers_count,
  COUNT(DISTINCT ad_id) as total_ads,
  AVG(average_position) as avg_position,
  STRING_AGG(DISTINCT domain_name, ', ' ORDER BY domain_name) as competing_domains,
  retrieved_at
FROM `project-id.spyfu.term_ad_history`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.term_ad_history`)
GROUP BY keyword, retrieved_at
ORDER BY advertisers_count DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.best_ad_headlines_by_keyword` AS
SELECT
  keyword,
  domain_name,
  title,
  body,
  full_url,
  position,
  average_position,
  ad_count,
  percentage_ads_served,
  retrieved_at
FROM `project-id.spyfu.term_ad_history`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.term_ad_history`)
  AND position <= 3  -- Top positions
ORDER BY keyword, position ASC;


CREATE OR REPLACE VIEW `project-id.spyfu.leaderboard_ads_by_keyword` AS
SELECT
  keyword,
  domain_name,
  title,
  leaderboard_count,
  percentage_leaderboard,
  is_leaderboard_ad,
  retrieved_at
FROM `project-id.spyfu.term_ad_history`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.term_ad_history`)
  AND (is_leaderboard_ad = TRUE OR leaderboard_count > 0)
ORDER BY keyword, leaderboard_count DESC;


-- ============================================================
-- TABLE 9: TERM DOMAIN STATS (getTermAdHistoryWithStats)
-- ============================================================
-- Scripts trimestriels - Statistiques par domaine pour un keyword
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.term_domain_stats` (
  -- Identifiants
  keyword STRING NOT NULL,
  domain_name STRING NOT NULL,

  -- Métriques budgétaires
  budget FLOAT64,
  coverage FLOAT64,
  percentage_leaderboard FLOAT64,
  
  -- Métriques de volume
  total_ads_purchased INT64,
  ad_count INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY keyword, domain_name;


-- VUES pour term_domain_stats

CREATE OR REPLACE VIEW `project-id.spyfu.domain_spend_by_keyword` AS
SELECT
  keyword,
  domain_name,
  budget,
  total_ads_purchased,
  ad_count,
  coverage,
  percentage_leaderboard,
  retrieved_at
FROM `project-id.spyfu.term_domain_stats`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.term_domain_stats`)
ORDER BY keyword, budget DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.top_spenders_by_keyword` AS
SELECT
  keyword,
  COUNT(DISTINCT domain_name) as competing_domains,
  SUM(budget) as total_keyword_budget,
  AVG(budget) as avg_domain_budget,
  MAX(budget) as top_spender_budget,
  SUM(total_ads_purchased) as total_ads,
  retrieved_at
FROM `project-id.spyfu.term_domain_stats`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.term_domain_stats`)
GROUP BY keyword, retrieved_at
ORDER BY total_keyword_budget DESC;


-- ============================================================
-- TABLE 10: RELATED KEYWORDS (getRelatedKeywords)
-- ============================================================
-- Scripts on-demand - Mots-clés connexes
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.related_keywords` (
  -- Identifiants
  source_keyword STRING NOT NULL,
  related_keyword STRING NOT NULL,

  -- Métriques de recherche
  search_volume INT64,
  ranking_difficulty FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'US',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY source_keyword, related_keyword;


-- VUES pour related_keywords

CREATE OR REPLACE VIEW `project-id.spyfu.keyword_expansion_opportunities` AS
SELECT
  source_keyword,
  related_keyword,
  search_volume,
  ranking_difficulty,
  broad_cost_per_click,
  paid_competitors,
  (search_volume / NULLIF(ranking_difficulty, 0)) as opportunity_score,
  retrieved_at
FROM `project-id.spyfu.related_keywords`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.related_keywords`)
  AND ranking_difficulty < 60
  AND search_volume > 100
ORDER BY opportunity_score DESC;


CREATE OR REPLACE VIEW `project-id.spyfu.keyword_clusters` AS
SELECT
  source_keyword,
  COUNT(*) as related_count,
  AVG(search_volume) as avg_related_volume,
  AVG(ranking_difficulty) as avg_difficulty,
  AVG(broad_cost_per_click) as avg_cpc,
  SUM(search_volume) as total_potential_volume,
  retrieved_at
FROM `project-id.spyfu.related_keywords`
WHERE retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.related_keywords`)
GROUP BY source_keyword, retrieved_at
ORDER BY total_potential_volume DESC;


-- ============================================================
-- VUES GLOBALES CROSS-TABLE
-- ============================================================

-- Vue pour analyse complète de la performance d'un domaine
CREATE OR REPLACE VIEW `project-id.spyfu.domain_performance_overview` AS
SELECT
  d.domain,
  d.total_ad_keywords,
  d.total_seo_keywords,
  d.total_organic_traffic,
  d.total_ad_budget,
  d.domain_rank,
  d.domain_authority,
  COUNT(DISTINCT p.keyword) as ppc_keywords_tracked,
  COUNT(DISTINCT s.keyword) as seo_keywords_tracked,
  COUNT(DISTINCT a.ad_id) as active_ads,
  d.retrieved_at
FROM `project-id.spyfu.domain_stats` d
LEFT JOIN `project-id.spyfu.ppc_keywords` p ON d.domain = p.domain AND DATE(p.retrieved_at) = DATE(d.retrieved_at)
LEFT JOIN `project-id.spyfu.seo_keywords` s ON d.domain = s.domain AND DATE(s.retrieved_at) = DATE(d.retrieved_at)
LEFT JOIN `project-id.spyfu.domain_ad_history` a ON d.domain = a.domain AND DATE(a.retrieved_at) = DATE(d.retrieved_at)
WHERE d.retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.domain_stats`)
GROUP BY d.domain, d.total_ad_keywords, d.total_seo_keywords, d.total_organic_traffic,
         d.total_ad_budget, d.domain_rank, d.domain_authority, d.retrieved_at
ORDER BY d.total_organic_traffic DESC;


-- Vue pour estimation du ROI (basé sur keywords + ads)
CREATE OR REPLACE VIEW `project-id.spyfu.estimated_roi_analysis` AS
SELECT
  p.domain,
  COUNT(DISTINCT p.keyword) as tracked_keywords,
  SUM(p.search_volume) as total_search_volume,
  AVG(p.broad_cost_per_click) as avg_cpc,
  SUM(p.broad_monthly_cost) as estimated_monthly_ppc_spend,
  COUNT(DISTINCT a.ad_id) as active_ads,
  SUM(a.monthly_cost) as actual_monthly_ad_spend,
  SUM(s.seo_clicks) as total_organic_clicks,
  SUM(s.seo_clicks * p.broad_cost_per_click) as estimated_organic_value,
  p.retrieved_at
FROM `project-id.spyfu.ppc_keywords` p
LEFT JOIN `project-id.spyfu.seo_keywords` s ON p.domain = s.domain AND p.keyword = s.keyword AND DATE(s.retrieved_at) = DATE(p.retrieved_at)
LEFT JOIN `project-id.spyfu.domain_ad_history` a ON p.domain = a.domain AND DATE(a.retrieved_at) = DATE(p.retrieved_at)
WHERE p.retrieved_at = (SELECT MAX(retrieved_at) FROM `project-id.spyfu.ppc_keywords`)
GROUP BY p.domain, p.retrieved_at
ORDER BY estimated_organic_value DESC;


-- ============================================================
-- FIN DU SCHÉMA
-- ============================================================
-- Total: 11 tables + 30 vues
-- ============================================================
