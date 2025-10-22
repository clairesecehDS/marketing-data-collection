-- SpyFu PPC Keywords BigQuery Schema
-- Table pour stocker les métriques de mots-clés PPC

CREATE TABLE IF NOT EXISTS `project-id.spyfu.ppc_keywords` (
  -- Identifiants
  domain STRING NOT NULL,
  keyword STRING NOT NULL,

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
  distinct_competitors INT64,
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
  keyword STRING NOT NULL,

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
  distinct_competitors INT64,
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
  keyword STRING NOT NULL,
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
  keyword STRING NOT NULL,
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
  keyword STRING NOT NULL,

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
  keyword STRING NOT NULL,

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
