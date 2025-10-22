-- =====================================================
-- LinkedIn Page Statistics Schema for BigQuery
-- =====================================================
-- Table: linkedin_page_statistics
-- Dataset: linkedin_page
-- =====================================================

-- =====================================================
-- Main Table: LinkedIn Page Statistics
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.linkedin_page.linkedin_page_statistics` (
  -- Identifiers
  organization_id STRING NOT NULL,
  organization_urn STRING,

  -- Time Dimension
  stat_date DATE,
  time_granularity STRING,  -- DAILY, MONTHLY, ALL

  -- Metric Type & Context
  metric_category STRING NOT NULL,  -- FOLLOWER, SHARE, PAGE_VIEW
  pivot_type STRING,  -- share, industry, jobFunction, seniority, country, region, etc.
  pivot_value STRING,  -- Specific value for the pivot (e.g., share URN, industry name)

  -- Follower Metrics
  follower_count INT64,
  follower_gains INT64,
  follower_losses INT64,
  follower_growth_rate FLOAT64,

  -- Follower Demographics (when pivoted)
  industry STRING,
  job_function STRING,
  seniority STRING,
  country STRING,
  region STRING,

  -- Share/Post Metrics
  share_urn STRING,
  share_title STRING,
  impressions INT64,
  unique_impressions INT64,
  clicks INT64,
  likes INT64,
  comments INT64,
  shares INT64,

  -- Calculated Engagement Metrics
  click_through_rate FLOAT64,  -- (Clicks ÷ Impressions) × 100
  engagement_rate FLOAT64,  -- ((Likes + Comments + Shares) ÷ Impressions) × 100
  total_engagements INT64,  -- Likes + Comments + Shares

  -- Page View Metrics
  page_views_unique_count INT64,
  page_views_total_count INT64,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY stat_date
CLUSTER BY organization_id, metric_category, time_granularity;

-- =====================================================
-- Useful Views
-- =====================================================

-- View: Overall Page Performance Summary
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_page_performance_summary` AS
WITH latest_data AS (
  SELECT *
  FROM `project-id.linkedin_page.linkedin_page_statistics`
  WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.linkedin_page_statistics`)
)
SELECT
  organization_id,
  -- Followers
  MAX(CASE WHEN metric_category = 'FOLLOWER' AND time_granularity = 'ALL' THEN follower_count END) AS total_followers,
  SUM(CASE WHEN metric_category = 'FOLLOWER' AND time_granularity = 'MONTHLY' THEN follower_gains END) AS monthly_new_followers,

  -- Page Views
  SUM(CASE WHEN metric_category = 'PAGE_VIEW' AND time_granularity = 'MONTHLY' THEN page_views_unique_count END) AS monthly_unique_page_views,

  -- Engagement (Monthly)
  SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN impressions END) AS monthly_impressions,
  SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN clicks END) AS monthly_clicks,
  SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN likes END) AS monthly_likes,
  SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN comments END) AS monthly_comments,
  SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN shares END) AS monthly_shares,

  -- Calculated Rates
  ROUND(SAFE_DIVIDE(
    SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN clicks END),
    SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN impressions END)
  ) * 100, 2) AS monthly_ctr,
  ROUND(SAFE_DIVIDE(
    SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN likes + comments + shares END),
    SUM(CASE WHEN metric_category = 'SHARE' AND time_granularity = 'MONTHLY' THEN impressions END)
  ) * 100, 2) AS monthly_engagement_rate
FROM latest_data
GROUP BY organization_id;

-- View: Top Performing Posts
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_top_posts` AS
SELECT
  organization_id,
  share_urn,
  share_title,
  impressions,
  clicks,
  likes,
  comments,
  shares,
  total_engagements,
  engagement_rate,
  click_through_rate,
  stat_date,
  retrieved_at
FROM `project-id.linkedin_page.linkedin_page_statistics`
WHERE metric_category = 'SHARE'
  AND pivot_type = 'share'
  AND share_urn IS NOT NULL
  AND DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.linkedin_page_statistics`)
ORDER BY engagement_rate DESC
LIMIT 50;

-- View: Follower Demographics Breakdown
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_follower_demographics` AS
SELECT
  organization_id,
  pivot_type,
  COALESCE(industry, job_function, seniority, country, region, pivot_value) AS demographic_value,
  follower_count,
  ROUND(SAFE_DIVIDE(follower_count, SUM(follower_count) OVER (PARTITION BY organization_id, pivot_type)) * 100, 2) AS percentage,
  retrieved_at
FROM `project-id.linkedin_page.linkedin_page_statistics`
WHERE metric_category = 'FOLLOWER'
  AND pivot_type IN ('industry', 'jobFunction', 'seniority', 'country', 'region')
  AND DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `project-id.linkedin_page.linkedin_page_statistics`)
ORDER BY organization_id, pivot_type, follower_count DESC;

-- View: Growth Trends Over Time
CREATE OR REPLACE VIEW `project-id.linkedin_page.v_growth_trends` AS
WITH daily_stats AS (
  SELECT
    organization_id,
    stat_date,
    MAX(CASE WHEN metric_category = 'FOLLOWER' THEN follower_gains END) AS daily_follower_gains,
    SUM(CASE WHEN metric_category = 'SHARE' THEN impressions END) AS daily_impressions,
    SUM(CASE WHEN metric_category = 'SHARE' THEN total_engagements END) AS daily_engagements,
    MAX(CASE WHEN metric_category = 'PAGE_VIEW' THEN page_views_unique_count END) AS daily_page_views
  FROM `project-id.linkedin_page.linkedin_page_statistics`
  WHERE time_granularity = 'DAILY'
    AND stat_date IS NOT NULL
  GROUP BY organization_id, stat_date
)
SELECT
  organization_id,
  stat_date,
  daily_follower_gains,
  daily_impressions,
  daily_engagements,
  daily_page_views,
  -- 7-day rolling averages
  AVG(daily_follower_gains) OVER (
    PARTITION BY organization_id
    ORDER BY stat_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7day_avg_follower_gains,
  AVG(daily_impressions) OVER (
    PARTITION BY organization_id
    ORDER BY stat_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7day_avg_impressions,
  AVG(daily_engagements) OVER (
    PARTITION BY organization_id
    ORDER BY stat_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7day_avg_engagements
FROM daily_stats
ORDER BY organization_id, stat_date DESC;

-- =====================================================
-- Example Queries
-- =====================================================

-- Query 1: Overall page health snapshot
/*
SELECT *
FROM `project-id.linkedin_page.v_page_performance_summary`
WHERE organization_id = '5509810';
*/

-- Query 2: Best performing posts this month
/*
SELECT
  share_title,
  impressions,
  engagement_rate,
  total_engagements,
  stat_date
FROM `project-id.linkedin_page.v_top_posts`
WHERE stat_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
ORDER BY engagement_rate DESC
LIMIT 10;
*/

-- Query 3: Follower demographics
/*
SELECT
  pivot_type,
  demographic_value,
  follower_count,
  percentage
FROM `project-id.linkedin_page.v_follower_demographics`
WHERE organization_id = '5509810'
ORDER BY pivot_type, follower_count DESC;
*/

-- Query 4: Weekly growth trends
/*
SELECT
  DATE_TRUNC(stat_date, WEEK) AS week,
  SUM(daily_follower_gains) AS weekly_follower_gains,
  AVG(daily_impressions) AS avg_daily_impressions,
  SUM(daily_engagements) AS weekly_total_engagements
FROM `project-id.linkedin_page.v_growth_trends`
WHERE organization_id = '5509810'
  AND stat_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY week
ORDER BY week DESC;
*/

-- Query 5: Engagement breakdown by post
/*
SELECT
  share_title,
  likes,
  comments,
  shares,
  ROUND(SAFE_DIVIDE(likes, total_engagements) * 100, 1) AS pct_likes,
  ROUND(SAFE_DIVIDE(comments, total_engagements) * 100, 1) AS pct_comments,
  ROUND(SAFE_DIVIDE(shares, total_engagements) * 100, 1) AS pct_shares
FROM `project-id.linkedin_page.v_top_posts`
WHERE total_engagements > 0
ORDER BY total_engagements DESC
LIMIT 20;
*/
