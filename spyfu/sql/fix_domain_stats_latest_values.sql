-- Script pour corriger les valeurs dans domain_stats
-- Problème: Le code Python prenait results[0] (plus ancien) au lieu de results[-1] (plus récent)
-- Solution: Remplacer les valeurs du plus ancien mois par celles du plus récent mois
-- en extrayant le dernier élément de l'array results dans raw_stats
--
-- STATUT: ✅ CORRECTION APPLIQUÉE AVEC SUCCÈS le 2026-01-27

-- Étape 1: Vérifier les valeurs AVANT correction pour un domaine exemple
SELECT
  domain,
  country_code,
  'AVANT CORRECTION' AS status,
  total_ad_keywords,
  total_ad_budget,
  total_organic_traffic,
  domain_rank,
  domain_authority,
  -- Extraire le premier et dernier mois de raw_stats pour comparaison
  JSON_VALUE(raw_stats, '$.results[0].searchYear') AS first_year,
  JSON_VALUE(raw_stats, '$.results[0].searchMonth') AS first_month,
  JSON_VALUE(raw_stats, '$.results[0].strength') AS first_strength,
  JSON_VALUE(PARSE_JSON(raw_stats), '$.results[ARRAY_LENGTH(JSON_EXTRACT_ARRAY(raw_stats, "$.results"))-1].searchYear') AS last_year,
  JSON_VALUE(PARSE_JSON(raw_stats), '$.results[ARRAY_LENGTH(JSON_EXTRACT_ARRAY(raw_stats, "$.results"))-1].searchMonth') AS last_month,
  JSON_VALUE(PARSE_JSON(raw_stats), '$.results[ARRAY_LENGTH(JSON_EXTRACT_ARRAY(raw_stats, "$.results"))-1].strength') AS last_strength
FROM `international-sos-479209.spyfu.domain_stats`
WHERE domain = 'internationalsos.com'
LIMIT 1;

-- Étape 2: Créer une vue des valeurs corrigées
CREATE OR REPLACE VIEW `international-sos-479209.spyfu.domain_stats_corrected_preview` AS
WITH parsed_data AS (
  SELECT
    domain,
    country_code,
    raw_stats,
    retrieved_at,
    -- Parser le JSON et extraire tous les éléments du tableau results
    JSON_EXTRACT_ARRAY(raw_stats, '$.results') AS results_array
  FROM `international-sos-479209.spyfu.domain_stats`
),
latest_stats AS (
  SELECT
    domain,
    country_code,
    raw_stats,
    retrieved_at,
    -- Prendre le dernier élément (plus récent) du tableau
    results_array[SAFE_OFFSET(ARRAY_LENGTH(results_array) - 1)] AS latest_result,
    ARRAY_LENGTH(results_array) AS ad_history_months
  FROM parsed_data
)
SELECT
  domain,
  country_code,

  -- Extraire les valeurs du dernier élément (plus récent)
  CAST(JSON_VALUE(latest_result, '$.totalAdsPurchased') AS INT64) AS total_ad_keywords,
  CAST(JSON_VALUE(latest_result, '$.monthlyBudget') AS FLOAT64) AS total_ad_budget,
  CAST(JSON_VALUE(latest_result, '$.monthlyPaidClicks') AS INT64) AS total_ad_clicks,
  ad_history_months,

  CAST(JSON_VALUE(latest_result, '$.totalOrganicResults') AS INT64) AS total_seo_keywords,
  CAST(JSON_VALUE(latest_result, '$.totalOrganicResults') AS INT64) AS total_organic_keywords,
  CAST(JSON_VALUE(latest_result, '$.monthlyOrganicClicks') AS INT64) AS total_organic_traffic,
  CAST(JSON_VALUE(latest_result, '$.monthlyOrganicValue') AS FLOAT64) AS total_organic_value,

  CAST(JSON_VALUE(latest_result, '$.averageOrganicRank') AS INT64) AS domain_rank,
  CAST(JSON_VALUE(latest_result, '$.strength') AS FLOAT64) AS domain_authority,

  raw_stats,
  retrieved_at
FROM latest_stats;

-- Étape 3: Comparer AVANT et APRÈS pour validation
SELECT
  'AVANT' AS status,
  domain,
  domain_authority,
  total_ad_keywords,
  domain_rank,
  total_organic_traffic
FROM `international-sos-479209.spyfu.domain_stats`
WHERE domain = 'internationalsos.com'

UNION ALL

SELECT
  'APRÈS' AS status,
  domain,
  domain_authority,
  total_ad_keywords,
  domain_rank,
  total_organic_traffic
FROM `international-sos-479209.spyfu.domain_stats_corrected_preview`
WHERE domain = 'internationalsos.com';

-- Étape 4: Appliquer la correction (DÉCOMMENTEZ APRÈS VALIDATION)
-- ATTENTION: Cette requête SUPPRIME et RECRÉE toute la table avec les valeurs corrigées
/*
CREATE OR REPLACE TABLE `international-sos-479209.spyfu.domain_stats`
PARTITION BY DATE(retrieved_at)
CLUSTER BY domain
AS
SELECT * FROM `international-sos-479209.spyfu.domain_stats_corrected_preview`;
*/
