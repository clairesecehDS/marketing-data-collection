-- ============================================================================
-- SCHEMA BIGQUERY POUR LINKEDIN ADS ANALYTICS
-- Dataset: linkedin_ads_advertising
-- ============================================================================

-- Table 1: Campaign Analytics
-- Cette table stocke les métriques agrégées par campagne
CREATE TABLE IF NOT EXISTS `project-id.linkedin_ads_advertising.campaign_analytics` (
  -- Identifiants
  campaign_id STRING NOT NULL OPTIONS(description="ID de la campagne LinkedIn"),
  campaign_urn STRING OPTIONS(description="URN complet de la campagne (ex: urn:li:sponsoredCampaign:123456)"),

  -- Période de reporting
  date_range_start DATE OPTIONS(description="Date de début de la période analysée"),
  date_range_end DATE OPTIONS(description="Date de fin de la période analysée"),

  -- Métriques de base
  impressions INT64 OPTIONS(description="Nombre total d'impressions"),
  clicks INT64 OPTIONS(description="Nombre total de clics"),
  cost_in_usd FLOAT64 OPTIONS(description="Coût total en USD"),

  -- Métriques de performance calculées
  ctr FLOAT64 OPTIONS(description="Click-Through Rate en % (clicks/impressions * 100)"),
  cpc FLOAT64 OPTIONS(description="Cost Per Click en USD (cost/clicks)"),
  cpm FLOAT64 OPTIONS(description="Cost Per Mille/1000 impressions en USD"),

  -- Engagement
  reactions INT64 OPTIONS(description="Nombre de réactions (likes, etc.)"),
  comments INT64 OPTIONS(description="Nombre de commentaires"),
  shares INT64 OPTIONS(description="Nombre de partages"),
  total_engagements INT64 OPTIONS(description="Total des engagements (reactions + comments + shares)"),
  engagement_rate FLOAT64 OPTIONS(description="Taux d'engagement en % (engagements/impressions * 100)"),

  -- Conversions
  landing_page_clicks INT64 OPTIONS(description="Clics sur la landing page"),
  one_click_leads INT64 OPTIONS(description="Leads générés en un clic"),
  external_website_conversions INT64 OPTIONS(description="Conversions sur site externe (total)"),
  external_website_post_click_conversions INT64 OPTIONS(description="Conversions après clic"),
  external_website_post_view_conversions INT64 OPTIONS(description="Conversions après vue"),

  -- Vidéo
  video_views INT64 OPTIONS(description="Nombre de vues vidéo"),
  video_starts INT64 OPTIONS(description="Nombre de démarrages vidéo"),
  video_completions INT64 OPTIONS(description="Nombre de lectures vidéo complètes"),

  -- Reach
  approximate_member_reach INT64 OPTIONS(description="Portée approximative (nombre de membres LinkedIn)"),

  -- Métadonnées
  retrieved_at TIMESTAMP NOT NULL OPTIONS(description="Date et heure de récupération des données depuis l'API"),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Date de dernière mise à jour de la ligne")
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY campaign_id, date_range_start
OPTIONS(
  description="Métriques des campagnes publicitaires LinkedIn agrégées par campagne. Données récupérées via LinkedIn Marketing API.",
  labels=[("source", "linkedin_marketing_api"), ("data_type", "campaign_metrics"), ("pivot", "campaign")]
);


-- Table 2: Creative (Ads) Analytics
-- Cette table stocke les métriques détaillées par creative/ad individuel
CREATE TABLE IF NOT EXISTS `project-id.linkedin_ads_advertising.creative_analytics` (
  -- Identifiants
  creative_id STRING NOT NULL OPTIONS(description="ID de la creative LinkedIn"),
  creative_urn STRING OPTIONS(description="URN complet de la creative (ex: urn:li:sponsoredCreative:123456)"),

  -- Période de reporting
  date_range_start DATE OPTIONS(description="Date de début de la période analysée"),
  date_range_end DATE OPTIONS(description="Date de fin de la période analysée"),

  -- Métriques de base
  impressions INT64 OPTIONS(description="Nombre total d'impressions"),
  clicks INT64 OPTIONS(description="Nombre total de clics"),
  cost_in_usd FLOAT64 OPTIONS(description="Coût total en USD"),

  -- Métriques de performance calculées
  ctr FLOAT64 OPTIONS(description="Click-Through Rate en % (clicks/impressions * 100)"),
  cpc FLOAT64 OPTIONS(description="Cost Per Click en USD (cost/clicks)"),
  cpm FLOAT64 OPTIONS(description="Cost Per Mille/1000 impressions en USD"),

  -- Engagement
  reactions INT64 OPTIONS(description="Nombre de réactions (likes, etc.)"),
  comments INT64 OPTIONS(description="Nombre de commentaires"),
  shares INT64 OPTIONS(description="Nombre de partages"),
  total_engagements INT64 OPTIONS(description="Total des engagements (reactions + comments + shares)"),
  engagement_rate FLOAT64 OPTIONS(description="Taux d'engagement en % (engagements/impressions * 100)"),

  -- Conversions
  landing_page_clicks INT64 OPTIONS(description="Clics sur la landing page"),
  one_click_leads INT64 OPTIONS(description="Leads générés en un clic"),
  external_website_conversions INT64 OPTIONS(description="Conversions sur site externe (total)"),
  external_website_post_click_conversions INT64 OPTIONS(description="Conversions après clic"),
  external_website_post_view_conversions INT64 OPTIONS(description="Conversions après vue"),

  -- Vidéo
  video_views INT64 OPTIONS(description="Nombre de vues vidéo"),
  video_starts INT64 OPTIONS(description="Nombre de démarrages vidéo"),
  video_completions INT64 OPTIONS(description="Nombre de lectures vidéo complètes"),

  -- Reach
  approximate_member_reach INT64 OPTIONS(description="Portée approximative (nombre de membres LinkedIn)"),

  -- Métadonnées
  retrieved_at TIMESTAMP NOT NULL OPTIONS(description="Date et heure de récupération des données depuis l'API"),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Date de dernière mise à jour de la ligne")
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY creative_id, date_range_start
OPTIONS(
  description="Métriques des publicités (creatives) LinkedIn détaillées par ad individuel. Données récupérées via LinkedIn Marketing API avec pivot=CREATIVE.",
  labels=[("source", "linkedin_marketing_api"), ("data_type", "creative_metrics"), ("pivot", "creative")]
);


-- ============================================================================
-- OPTIMISATIONS ET BONNES PRATIQUES
-- ============================================================================

-- Les tables sont optimisées avec:
-- 1. PARTITION BY DATE(retrieved_at)
--    - Réduit les coûts de requête en scannant uniquement les dates nécessaires
--    - Idéal pour les requêtes "dernières données" ou "30 derniers jours"
--    - Permet la rétention automatique des données (optionnel)
--
-- 2. CLUSTER BY
--    - campaign_analytics: clusterisé par campaign_id et date_range_start
--    - creative_analytics: clusterisé par campaign_id, creative_id et date_range_start
--    - Améliore les performances des filtres WHERE et des JOINs
--    - Réduit les coûts en scannant moins de données
--
-- 3. Types optimaux
--    - INT64 pour les compteurs (plus efficace que NUMERIC)
--    - FLOAT64 pour les pourcentages et montants (précision suffisante)
--    - STRING pour les IDs (flexible et performant)
--    - TIMESTAMP pour les dates avec timezone


-- ============================================================================
-- VUES UTILES
-- ============================================================================

-- Vue 1: Dernières métriques de campagne
CREATE OR REPLACE VIEW `project-id.linkedin_ads_advertising.v_latest_campaign_metrics` AS
SELECT
  campaign_id,
  campaign_urn,
  impressions,
  clicks,
  cost_in_usd,
  ctr,
  cpc,
  cpm,
  total_engagements,
  engagement_rate,
  one_click_leads,
  external_website_conversions,
  video_views,
  video_completions,
  approximate_member_reach,
  date_range_start,
  date_range_end,
  retrieved_at
FROM `project-id.linkedin_ads_advertising.campaign_analytics`
WHERE DATE(retrieved_at) = (
  SELECT MAX(DATE(retrieved_at))
  FROM `project-id.linkedin_ads_advertising.campaign_analytics`
)
ORDER BY cost_in_usd DESC;


-- Vue 2: Top performing creatives
CREATE OR REPLACE VIEW `project-id.linkedin_ads_advertising.v_top_creatives` AS
SELECT
  creative_id,
  creative_urn,
  impressions,
  clicks,
  cost_in_usd,
  ctr,
  engagement_rate,
  total_engagements
FROM `project-id.linkedin_ads_advertising.creative_analytics`
WHERE DATE(retrieved_at) = (
  SELECT MAX(DATE(retrieved_at))
  FROM `project-id.linkedin_ads_advertising.creative_analytics`
)
AND impressions >= 100  -- Filtrer les creatives avec volume significatif
ORDER BY engagement_rate DESC, ctr DESC
LIMIT 50;


-- Vue 3: Performance globale (toutes campagnes agrégées)
CREATE OR REPLACE VIEW `project-id.linkedin_ads_advertising.v_overall_performance` AS
SELECT
  DATE(retrieved_at) as report_date,
  COUNT(DISTINCT campaign_id) as num_campaigns,
  SUM(impressions) as total_impressions,
  SUM(clicks) as total_clicks,
  SUM(cost_in_usd) as total_cost,
  SAFE_DIVIDE(SUM(clicks), SUM(impressions)) * 100 as overall_ctr,
  SAFE_DIVIDE(SUM(cost_in_usd), SUM(clicks)) as overall_cpc,
  SAFE_DIVIDE(SUM(cost_in_usd), SUM(impressions)) * 1000 as overall_cpm,
  SUM(total_engagements) as total_engagements,
  SAFE_DIVIDE(SUM(total_engagements), SUM(impressions)) * 100 as overall_engagement_rate,
  SUM(one_click_leads) as total_leads,
  SUM(external_website_conversions) as total_conversions
FROM `project-id.linkedin_ads_advertising.campaign_analytics`
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY report_date
ORDER BY report_date DESC;




-- ============================================================================
-- REQUÊTES D'EXEMPLE
-- ============================================================================

-- Exemple 1: Top 20 campagnes par coût (30 derniers jours)
/*
SELECT
  campaign_id,
  SUM(impressions) as total_impressions,
  SUM(clicks) as total_clicks,
  SUM(cost_in_usd) as total_cost,
  AVG(ctr) as avg_ctr,
  AVG(engagement_rate) as avg_engagement_rate,
  SUM(one_click_leads) as total_leads
FROM `project-id.linkedin_ads_advertising.campaign_analytics`
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY campaign_id
ORDER BY total_cost DESC
LIMIT 20;
*/

-- Exemple 2: Evolution temporelle d'une campagne
/*
SELECT
  DATE(retrieved_at) as date,
  impressions,
  clicks,
  ctr,
  cost_in_usd,
  engagement_rate
FROM `project-id.linkedin_ads_advertising.campaign_analytics`
WHERE campaign_id = '129098506'  -- Remplacer par votre campaign_id
  AND DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
ORDER BY date DESC;
*/

-- Exemple 3: Meilleures creatives (par engagement rate et CTR)
/*
SELECT
  creative_id,
  impressions,
  clicks,
  ctr,
  engagement_rate,
  cost_in_usd,
  SAFE_DIVIDE(cost_in_usd, NULLIF(one_click_leads, 0)) as cost_per_lead
FROM `project-id.linkedin_ads_advertising.creative_analytics`
WHERE DATE(retrieved_at) = (
  SELECT MAX(DATE(retrieved_at))
  FROM `project-id.linkedin_ads_advertising.creative_analytics`
)
AND impressions >= 1000  -- Minimum pour significativité statistique
ORDER BY engagement_rate DESC, ctr DESC
LIMIT 50;
*/

-- Exemple 4: Creatives avec meilleur ROI (coût par conversion)
/*
SELECT
  creative_id,
  impressions,
  clicks,
  cost_in_usd,
  external_website_conversions,
  SAFE_DIVIDE(cost_in_usd, NULLIF(external_website_conversions, 0)) as cost_per_conversion,
  SAFE_DIVIDE(external_website_conversions, NULLIF(clicks, 0)) * 100 as conversion_rate
FROM `project-id.linkedin_ads_advertising.creative_analytics`
WHERE DATE(retrieved_at) = (
  SELECT MAX(DATE(retrieved_at))
  FROM `project-id.linkedin_ads_advertising.creative_analytics`
)
AND external_website_conversions > 0
ORDER BY cost_per_conversion ASC
LIMIT 50;
*/

-- Exemple 5: Performances vidéo
/*
SELECT
  campaign_id,
  SUM(video_starts) as total_starts,
  SUM(video_completions) as total_completions,
  SAFE_DIVIDE(SUM(video_completions), NULLIF(SUM(video_starts), 0)) * 100 as completion_rate,
  SUM(cost_in_usd) as total_cost,
  SAFE_DIVIDE(SUM(cost_in_usd), NULLIF(SUM(video_completions), 0)) as cost_per_completion
FROM `project-id.linkedin_ads_advertising.campaign_analytics`
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND video_starts > 0
GROUP BY campaign_id
ORDER BY completion_rate DESC;
*/


-- ============================================================================
-- POLITIQUE DE RÉTENTION (OPTIONNEL)
-- ============================================================================

-- Pour configurer une rétention automatique des données (ex: garder 2 ans):
/*
ALTER TABLE `project-id.linkedin_ads_advertising.campaign_analytics`
SET OPTIONS (
  partition_expiration_days = 730  -- 2 ans
);

ALTER TABLE `project-id.linkedin_ads_advertising.creative_analytics`
SET OPTIONS (
  partition_expiration_days = 730  -- 2 ans
);
*/


-- ============================================================================
-- NOTES D'UTILISATION
-- ============================================================================

/*
1. Création du dataset (si nécessaire):
   CREATE SCHEMA IF NOT EXISTS `linkedin_ads_advertising`
   OPTIONS(location='EU');  -- ou 'US' selon votre région

2. Pour insérer des données depuis Python:
   Utilisez google-cloud-bigquery et pandas:

   from google.cloud import bigquery
   client = bigquery.Client()

   df.to_gbq(
       destination_table='linkedin_ads_advertising.campaign_analytics',
       project_id='your-project-id',
       if_exists='append'
   )

3. Monitoring des coûts:
   - Les requêtes sur tables partitionnées coûtent moins cher
   - Utilisez toujours un filtre WHERE sur retrieved_at
   - Les vues matérialisées peuvent réduire les coûts pour les agrégations fréquentes

4. Best practices:
   - Insérez les données une fois par jour (retrieved_at = même timestamp pour tous les inserts)
   - Utilisez des transactions pour garantir la cohérence
   - Ajoutez des indexes si vous faites beaucoup de JOINs sur campaign_id
*/
