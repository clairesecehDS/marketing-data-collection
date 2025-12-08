-- SpyFu PPC Keywords BigQuery Schema
-- Table pour stocker les métriques de mots-clés PPC

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


-- Vue pour les top keywords par domaine (volume de recherche)
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


-- Vue pour analyse du coût par clic
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


-- Vue pour analyse mobile vs desktop
CREATE OR REPLACE VIEW `project-id.spyfu.mobile_vs_desktop` AS
SELECT
  domain,
  keyword,
  search_volume,
  percent_mobile_searches,
  percent_desktop_searches,
  percent_paid_clicks,
  percent_organic_clicks,
  total_monthly_clicks,
  retrieved_at
FROM `project-id.spyfu.ppc_keywords`
WHERE percent_mobile_searches IS NOT NULL
  AND percent_desktop_searches IS NOT NULL
ORDER BY domain, search_volume DESC;


-- Vue pour opportunités (faible difficulté, haut volume)
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
-- Table pour les NOUVEAUX mots-clés PPC
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
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour les nouveaux keywords par domaine
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


-- Vue pour les nouvelles opportunités (nouveaux keywords + faible difficulté)
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
-- Table pour les annonces PPC (Paid SERPs)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.paid_serps` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING,
  term_id INT64,

  -- Métriques d'annonce
  ad_position INT64,
  ad_count INT64,
  date_searched TIMESTAMP,

  -- Contenu de l'annonce
  title STRING,
  body_html STRING,
  ad_domain STRING,  -- Domaine affiché dans l'annonce

  -- Métriques du mot-clé
  search_volume INT64,
  keyword_difficulty FLOAT64,

  -- Flags
  is_nsfw BOOLEAN,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour analyser les annonces par position
CREATE OR REPLACE VIEW `project-id.spyfu.serps_by_position` AS
SELECT
  domain,
  keyword,
  ad_position,
  title,
  ad_domain,
  search_volume,
  keyword_difficulty,
  date_searched,
  retrieved_at
FROM `project-id.spyfu.paid_serps`
ORDER BY domain, ad_position ASC;


-- Vue pour analyser la compétition publicitaire
CREATE OR REPLACE VIEW `project-id.spyfu.ad_competition_analysis` AS
SELECT
  keyword,
  ad_count,
  search_volume,
  keyword_difficulty,
  COUNT(DISTINCT domain) as domains_advertising,
  retrieved_at
FROM `project-id.spyfu.paid_serps`
GROUP BY keyword, ad_count, search_volume, keyword_difficulty, retrieved_at
HAVING ad_count > 3
ORDER BY search_volume DESC;


-- Vue pour les meilleurs titres d'annonces
CREATE OR REPLACE VIEW `project-id.spyfu.top_ad_titles` AS
SELECT
  domain,
  keyword,
  title,
  ad_position,
  search_volume,
  retrieved_at
FROM `project-id.spyfu.paid_serps`
WHERE ad_position <= 3
  AND title IS NOT NULL
ORDER BY domain, search_volume DESC, ad_position ASC;


-- ============================================================
-- Table pour les mots-clés SEO organiques
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

  -- Comparaison (si compareDomain utilisé)
  your_rank INT64,
  your_rank_change INT64,
  your_url STRING,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour les mots-clés SEO les plus précieux
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


-- Vue pour analyser les gains/pertes de trafic SEO
CREATE OR REPLACE VIEW `project-id.spyfu.seo_traffic_changes` AS
SELECT
  domain,
  keyword,
  search_type,
  rank,
  rank_change,
  seo_clicks,
  seo_clicks_change,
  search_volume,
  retrieved_at
FROM `project-id.spyfu.seo_keywords`
WHERE search_type IN ('GainedClicks', 'LostClicks')
  AND seo_clicks_change IS NOT NULL
ORDER BY domain, ABS(seo_clicks_change) DESC;


-- Vue pour les positions SEO
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


-- Vue pour opportunités SEO (faible difficulté, haut volume, pas encore top 10)
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
-- Table pour les mots-clés nouvellement classés (Newly Ranked)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.newly_ranked_keywords` (
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

  -- Comparaison (si compareDomain utilisé)
  your_rank INT64,
  your_rank_change INT64,
  your_url STRING,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour nouveaux keywords par volume
CREATE OR REPLACE VIEW `project-id.spyfu.newly_ranked_by_volume` AS
SELECT
  domain,
  keyword,
  rank,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.newly_ranked_keywords`
ORDER BY domain, search_volume DESC;


-- Vue pour nouveaux keywords bien positionnés
CREATE OR REPLACE VIEW `project-id.spyfu.newly_ranked_top_positions` AS
SELECT
  domain,
  keyword,
  rank,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  broad_cost_per_click,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.newly_ranked_keywords`
WHERE rank IS NOT NULL
  AND rank <= 10
ORDER BY domain, rank ASC, search_volume DESC;


-- Vue pour opportunités parmi les nouveaux keywords
CREATE OR REPLACE VIEW `project-id.spyfu.newly_ranked_opportunities` AS
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
FROM `project-id.spyfu.newly_ranked_keywords`
WHERE keyword_difficulty < 60
  AND search_volume > 200
ORDER BY domain, search_volume DESC, keyword_difficulty ASC;


-- ============================================================
-- Table pour les comparaisons de ranking (Outrank)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.outrank_comparison` (
  -- Identifiants
  domain STRING NOT NULL,
  compare_domain STRING NOT NULL,
  keyword STRING,

  -- Ranking du concurrent
  top_ranked_url STRING,
  rank INT64,
  rank_change INT64,

  -- Votre ranking
  your_rank INT64,
  your_rank_change INT64,
  your_url STRING,

  -- Métriques SEO du concurrent
  seo_clicks INT64,
  seo_clicks_change INT64,

  -- Métriques de recherche
  search_volume INT64,
  keyword_difficulty FLOAT64,
  total_monthly_clicks INT64,

  -- Pourcentages de recherche
  percent_mobile_searches FLOAT64,
  percent_desktop_searches FLOAT64,
  percent_not_clicked FLOAT64,
  percent_paid_clicks FLOAT64,
  percent_organic_clicks FLOAT64,

  -- CPC par match type
  broad_cost_per_click FLOAT64,
  phrase_cost_per_click FLOAT64,
  exact_cost_per_click FLOAT64,

  -- Coûts mensuels par match type
  broad_monthly_cost FLOAT64,
  phrase_monthly_cost FLOAT64,
  exact_monthly_cost FLOAT64,

  -- Métriques de compétition
  paid_competitors INT64,
  ranking_homepages INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, compare_domain, keyword;


-- Vue pour gaps SEO (où vous n'êtes pas classé mais le concurrent oui)
CREATE OR REPLACE VIEW `project-id.spyfu.seo_gaps` AS
SELECT
  domain,
  compare_domain,
  keyword,
  rank as competitor_rank,
  your_rank,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  broad_cost_per_click,
  retrieved_at
FROM `project-id.spyfu.outrank_comparison`
WHERE your_rank IS NULL OR your_rank > 20
ORDER BY domain, compare_domain, search_volume DESC;


-- Vue pour opportunités de rattrapage
CREATE OR REPLACE VIEW `project-id.spyfu.catch_up_opportunities` AS
SELECT
  domain,
  compare_domain,
  keyword,
  rank as competitor_rank,
  your_rank,
  (your_rank - rank) as rank_gap,
  search_volume,
  seo_clicks,
  keyword_difficulty,
  broad_cost_per_click,
  retrieved_at
FROM `project-id.spyfu.outrank_comparison`
WHERE your_rank IS NOT NULL
  AND your_rank > rank
  AND keyword_difficulty < 65
  AND search_volume > 200
ORDER BY domain, search_volume DESC, rank_gap DESC;


-- Vue pour analyse compétitive par concurrent
CREATE OR REPLACE VIEW `project-id.spyfu.competitor_advantage_analysis` AS
SELECT
  domain,
  compare_domain,
  COUNT(*) as total_keywords_ahead,
  AVG(rank) as avg_competitor_rank,
  AVG(your_rank) as avg_your_rank,
  SUM(search_volume) as total_search_volume,
  SUM(seo_clicks) as total_competitor_clicks,
  AVG(keyword_difficulty) as avg_difficulty,
  retrieved_at
FROM `project-id.spyfu.outrank_comparison`
GROUP BY domain, compare_domain, retrieved_at
ORDER BY total_keywords_ahead DESC;


-- ============================================================
-- Table pour les meilleures pages SEO (Top Pages)
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
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, url;


-- Vue pour les pages les plus performantes
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


-- Vue pour pages avec le plus de keywords
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


-- Vue pour analyse de performance par domaine
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
-- Table pour les mots-clés avec gains de ranking (Gained Ranks)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.gained_ranks_keywords` (
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

  -- Comparaison (si compareDomain utilisé)
  your_rank INT64,
  your_rank_change INT64,
  your_url STRING,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour les meilleurs gains de ranking
CREATE OR REPLACE VIEW `project-id.spyfu.top_gained_ranks` AS
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
FROM `project-id.spyfu.gained_ranks_keywords`
WHERE rank_change < 0  -- Amélioration de position (nombre négatif)
ORDER BY domain, rank_change ASC, search_volume DESC;


-- Vue pour gains de ranking les plus impactants
CREATE OR REPLACE VIEW `project-id.spyfu.most_impactful_gains` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  search_volume,
  seo_clicks,
  seo_clicks_change,
  keyword_difficulty,
  broad_cost_per_click,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.gained_ranks_keywords`
WHERE rank_change < 0
  AND seo_clicks_change > 0
  AND search_volume > 500
ORDER BY domain, seo_clicks_change DESC;


-- Vue pour analyse des gains par domaine
CREATE OR REPLACE VIEW `project-id.spyfu.gained_ranks_summary` AS
SELECT
  domain,
  COUNT(*) as total_gained_keywords,
  AVG(rank_change) as avg_rank_improvement,
  SUM(seo_clicks_change) as total_clicks_gained,
  SUM(search_volume) as total_search_volume,
  AVG(keyword_difficulty) as avg_difficulty,
  retrieved_at
FROM `project-id.spyfu.gained_ranks_keywords`
WHERE rank_change < 0
GROUP BY domain, retrieved_at
ORDER BY total_clicks_gained DESC;


-- ============================================================
-- Table pour les mots-clés avec pertes de ranking (Lost Ranks)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.lost_ranks_keywords` (
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

  -- Comparaison (si compareDomain utilisé)
  your_rank INT64,
  your_rank_change INT64,
  your_url STRING,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour les plus grandes pertes de ranking
CREATE OR REPLACE VIEW `project-id.spyfu.top_lost_ranks` AS
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
FROM `project-id.spyfu.lost_ranks_keywords`
WHERE rank_change > 0  -- Perte de position (nombre positif)
ORDER BY domain, rank_change DESC, search_volume DESC;


-- Vue pour pertes de ranking les plus critiques
CREATE OR REPLACE VIEW `project-id.spyfu.most_critical_losses` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  search_volume,
  seo_clicks,
  seo_clicks_change,
  keyword_difficulty,
  broad_cost_per_click,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.lost_ranks_keywords`
WHERE rank_change > 0
  AND seo_clicks_change < 0
  AND search_volume > 500
ORDER BY domain, ABS(seo_clicks_change) DESC;


-- Vue pour analyse des pertes par domaine
CREATE OR REPLACE VIEW `project-id.spyfu.lost_ranks_summary` AS
SELECT
  domain,
  COUNT(*) as total_lost_keywords,
  AVG(rank_change) as avg_rank_decline,
  SUM(seo_clicks_change) as total_clicks_lost,
  SUM(search_volume) as total_search_volume,
  AVG(keyword_difficulty) as avg_difficulty,
  retrieved_at
FROM `project-id.spyfu.lost_ranks_keywords`
WHERE rank_change > 0
GROUP BY domain, retrieved_at
ORDER BY ABS(total_clicks_lost) DESC;


-- Vue pour keywords à reconquérir (haute valeur perdue)
CREATE OR REPLACE VIEW `project-id.spyfu.keywords_to_recover` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  search_volume,
  seo_clicks,
  seo_clicks_change,
  keyword_difficulty,
  broad_cost_per_click,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.lost_ranks_keywords`
WHERE rank_change > 0
  AND search_volume > 1000
  AND keyword_difficulty < 70
  AND ABS(seo_clicks_change) > 50
ORDER BY domain, search_volume DESC, ABS(seo_clicks_change) DESC;


-- ============================================================
-- Table pour les mots-clés avec pertes de clics (Lost Clicks)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.lost_clicks_keywords` (
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

  -- Comparaison (si compareDomain utilisé)
  your_rank INT64,
  your_rank_change INT64,
  your_url STRING,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, keyword;


-- Vue pour les plus grandes pertes de clics
CREATE OR REPLACE VIEW `project-id.spyfu.top_lost_clicks` AS
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
FROM `project-id.spyfu.lost_clicks_keywords`
WHERE seo_clicks_change < 0  -- Perte de clics (nombre négatif)
ORDER BY domain, seo_clicks_change ASC, search_volume DESC;


-- Vue pour pertes de clics les plus critiques
CREATE OR REPLACE VIEW `project-id.spyfu.most_critical_click_losses` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  search_volume,
  seo_clicks,
  seo_clicks_change,
  keyword_difficulty,
  broad_cost_per_click,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.lost_clicks_keywords`
WHERE seo_clicks_change < 0
  AND search_volume > 1000
  AND ABS(seo_clicks_change) > 100
ORDER BY domain, seo_clicks_change ASC;


-- Vue pour analyse des pertes de clics par domaine
CREATE OR REPLACE VIEW `project-id.spyfu.lost_clicks_summary` AS
SELECT
  domain,
  COUNT(*) as total_keywords_losing_clicks,
  SUM(seo_clicks_change) as total_clicks_lost,
  AVG(seo_clicks_change) as avg_clicks_lost,
  SUM(search_volume) as total_search_volume,
  AVG(rank_change) as avg_rank_change,
  AVG(keyword_difficulty) as avg_difficulty,
  retrieved_at
FROM `project-id.spyfu.lost_clicks_keywords`
WHERE seo_clicks_change < 0
GROUP BY domain, retrieved_at
ORDER BY total_clicks_lost ASC;


-- Vue pour opportunités de récupération de clics
CREATE OR REPLACE VIEW `project-id.spyfu.clicks_recovery_opportunities` AS
SELECT
  domain,
  keyword,
  rank,
  rank_change,
  search_volume,
  seo_clicks,
  seo_clicks_change,
  keyword_difficulty,
  broad_cost_per_click,
  (search_volume * broad_cost_per_click) as estimated_monthly_value,
  top_ranked_url,
  retrieved_at
FROM `project-id.spyfu.lost_clicks_keywords`
WHERE seo_clicks_change < 0
  AND search_volume > 500
  AND keyword_difficulty < 75
  AND ABS(seo_clicks_change) > 50
ORDER BY domain, ABS(seo_clicks_change) DESC, estimated_monthly_value DESC;


-- ============================================================
-- Table pour les concurrents PPC
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.ppc_competitors` (
  -- Identifiants
  domain STRING NOT NULL,
  competitor_domain STRING NOT NULL,

  -- Métriques de compétition
  common_terms INT64,
  rank INT64,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, competitor_domain;


-- Vue pour les principaux concurrents par domaine
CREATE OR REPLACE VIEW `project-id.spyfu.top_ppc_competitors` AS
SELECT
  domain,
  competitor_domain,
  common_terms,
  rank,
  retrieved_at
FROM `project-id.spyfu.ppc_competitors`
ORDER BY domain, common_terms DESC;


-- Vue pour analyse de la concurrence PPC
CREATE OR REPLACE VIEW `project-id.spyfu.ppc_competition_intensity` AS
SELECT
  domain,
  COUNT(DISTINCT competitor_domain) as total_competitors,
  AVG(common_terms) as avg_common_terms,
  MAX(common_terms) as max_common_terms,
  MIN(common_terms) as min_common_terms,
  retrieved_at
FROM `project-id.spyfu.ppc_competitors`
GROUP BY domain, retrieved_at
ORDER BY total_competitors DESC;


-- Vue pour concurrents communs entre domaines
CREATE OR REPLACE VIEW `project-id.spyfu.shared_ppc_competitors` AS
SELECT
  c1.competitor_domain,
  COUNT(DISTINCT c1.domain) as competing_with_count,
  STRING_AGG(DISTINCT c1.domain, ', ') as competing_domains,
  AVG(c1.common_terms) as avg_common_terms,
  c1.retrieved_at
FROM `project-id.spyfu.ppc_competitors` c1
GROUP BY c1.competitor_domain, c1.retrieved_at
HAVING competing_with_count > 1
ORDER BY competing_with_count DESC, avg_common_terms DESC;


-- ============================================================
-- Table pour les concurrents combinés (SEO + PPC)
-- ============================================================

CREATE TABLE IF NOT EXISTS `project-id.spyfu.combined_competitors` (
  -- Identifiants
  domain STRING NOT NULL,
  competitor_domain STRING NOT NULL,

  -- Ranking combiné (FLOAT car l'API renvoie des scores normalisés entre 0 et 1)
  combined_rank FLOAT64,

  -- Métriques PPC (FLOAT car l'API peut renvoyer des scores normalisés)
  ppc_common_terms FLOAT64,
  ppc_rank FLOAT64,

  -- Métriques SEO (FLOAT car l'API peut renvoyer des scores normalisés)
  seo_common_terms FLOAT64,
  seo_rank FLOAT64,

  -- Métadonnées
  country_code STRING DEFAULT 'FR',
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain, competitor_domain;


-- Vue pour les principaux concurrents combinés
CREATE OR REPLACE VIEW `project-id.spyfu.top_combined_competitors` AS
SELECT
  domain,
  competitor_domain,
  combined_rank,
  ppc_common_terms,
  seo_common_terms,
  (COALESCE(ppc_common_terms, 0) + COALESCE(seo_common_terms, 0)) as total_common_terms,
  retrieved_at
FROM `project-id.spyfu.combined_competitors`
ORDER BY domain, combined_rank ASC;


-- Vue pour analyse de la présence des concurrents (SEO vs PPC)
CREATE OR REPLACE VIEW `project-id.spyfu.competitor_channel_analysis` AS
SELECT
  domain,
  competitor_domain,
  combined_rank,
  CASE
    WHEN ppc_common_terms IS NOT NULL AND seo_common_terms IS NOT NULL THEN 'Both SEO & PPC'
    WHEN ppc_common_terms IS NOT NULL THEN 'PPC Only'
    WHEN seo_common_terms IS NOT NULL THEN 'SEO Only'
    ELSE 'Unknown'
  END as channel_presence,
  ppc_common_terms,
  seo_common_terms,
  retrieved_at
FROM `project-id.spyfu.combined_competitors`
ORDER BY domain, combined_rank ASC;


-- Vue pour score de menace concurrentielle
CREATE OR REPLACE VIEW `project-id.spyfu.competitor_threat_score` AS
SELECT
  domain,
  competitor_domain,
  combined_rank,
  ppc_common_terms,
  seo_common_terms,
  (COALESCE(ppc_common_terms, 0) + COALESCE(seo_common_terms, 0)) as total_common_terms,
  -- Score de menace (pondéré: plus le rank est bas et plus de termes communs = plus menaçant)
  ROUND(
    (COALESCE(ppc_common_terms, 0) + COALESCE(seo_common_terms, 0)) /
    NULLIF(combined_rank, 0),
    2
  ) as threat_score,
  retrieved_at
FROM `project-id.spyfu.combined_competitors`
WHERE combined_rank IS NOT NULL
ORDER BY domain, threat_score DESC;


-- Vue pour résumé de la concurrence par domaine
CREATE OR REPLACE VIEW `project-id.spyfu.combined_competition_summary` AS
SELECT
  domain,
  COUNT(DISTINCT competitor_domain) as total_competitors,
  SUM(CASE WHEN ppc_common_terms IS NOT NULL AND seo_common_terms IS NOT NULL THEN 1 ELSE 0 END) as competitors_both_channels,
  SUM(CASE WHEN ppc_common_terms IS NOT NULL AND seo_common_terms IS NULL THEN 1 ELSE 0 END) as competitors_ppc_only,
  SUM(CASE WHEN seo_common_terms IS NOT NULL AND ppc_common_terms IS NULL THEN 1 ELSE 0 END) as competitors_seo_only,
  AVG(ppc_common_terms) as avg_ppc_common_terms,
  AVG(seo_common_terms) as avg_seo_common_terms,
  retrieved_at
FROM `project-id.spyfu.combined_competitors`
GROUP BY domain, retrieved_at
ORDER BY total_competitors DESC;
