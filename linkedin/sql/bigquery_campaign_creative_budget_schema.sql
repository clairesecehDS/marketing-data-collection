-- =====================================================
-- LinkedIn Budget Tables Schema for BigQuery
-- =====================================================
-- Tables: campaign_budget, creative_budget
-- Dataset: linkedin_ads_advertising
-- =====================================================

-- =====================================================
-- Table 1: Campaign Budget
-- =====================================================
CREATE TABLE IF NOT EXISTS `linkedin_ads_advertising.campaign_budget` (
  -- Identifiants
  campaign_id STRING NOT NULL,
  campaign_urn STRING,

  -- Budget metrics
  total_budget FLOAT64,
  daily_budget FLOAT64,
  lifetime_budget FLOAT64,
  budget_remaining FLOAT64,
  budget_spent FLOAT64,
  billing_currency STRING,

  -- Bid metrics
  bid_type STRING,
  bid_amount FLOAT64,
  bid_multiplier FLOAT64,
  bid_adjustment_type STRING,
  min_bid FLOAT64,
  max_bid FLOAT64,

  -- Pacing
  pacing_type STRING,
  pacing_rate FLOAT64,

  -- Dates
  start_date DATE,
  end_date DATE,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY campaign_id, start_date;

-- =====================================================
-- Table 2: Creative Budget
-- =====================================================
CREATE TABLE IF NOT EXISTS `linkedin_ads_advertising.creative_budget` (
  -- Identifiants
  creative_id STRING NOT NULL,
  creative_urn STRING,
  campaign_id STRING,
  campaign_urn STRING,

  -- Budget metrics
  total_budget FLOAT64,
  daily_budget FLOAT64,
  lifetime_budget FLOAT64,
  budget_remaining FLOAT64,
  budget_spent FLOAT64,
  billing_currency STRING,

  -- Bid metrics
  bid_type STRING,
  bid_amount FLOAT64,
  bid_multiplier FLOAT64,
  bid_adjustment_type STRING,
  min_bid FLOAT64,
  max_bid FLOAT64,

  -- Pacing
  pacing_type STRING,
  pacing_rate FLOAT64,

  -- Dates
  start_date DATE,
  end_date DATE,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY creative_id, campaign_id, start_date;

-- =====================================================
-- Useful Views
-- =====================================================

-- View: Active campaigns with budget status
CREATE OR REPLACE VIEW `linkedin_ads_advertising.v_active_campaign_budgets` AS
SELECT
  campaign_id,
  campaign_urn,
  daily_budget,
  lifetime_budget,
  budget_spent,
  budget_remaining,
  SAFE_DIVIDE(budget_spent, lifetime_budget) * 100 AS budget_utilization_pct,
  billing_currency,
  bid_type,
  bid_amount,
  start_date,
  end_date,
  CURRENT_DATE() BETWEEN start_date AND COALESCE(end_date, '2099-12-31') AS is_currently_active,
  retrieved_at
FROM `linkedin_ads_advertising.campaign_budget`
WHERE DATE(retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `linkedin_ads_advertising.campaign_budget`)
ORDER BY budget_spent DESC;

-- View: Budget summary by campaign
CREATE OR REPLACE VIEW `linkedin_ads_advertising.v_campaign_budget_summary` AS
SELECT
  campaign_id,
  COUNT(*) AS data_points,
  MIN(retrieved_at) AS first_seen,
  MAX(retrieved_at) AS last_seen,
  MAX(budget_spent) AS current_budget_spent,
  MAX(budget_remaining) AS current_budget_remaining,
  MAX(lifetime_budget) AS lifetime_budget,
  AVG(daily_budget) AS avg_daily_budget,
  MAX(bid_amount) AS current_bid_amount
FROM `linkedin_ads_advertising.campaign_budget`
GROUP BY campaign_id
ORDER BY current_budget_spent DESC;

-- =====================================================
-- Example Queries
-- =====================================================

-- Query 1: Campaigns approaching budget limit (>90% spent)
/*
SELECT
  campaign_id,
  budget_spent,
  lifetime_budget,
  budget_remaining,
  SAFE_DIVIDE(budget_spent, lifetime_budget) * 100 AS pct_spent,
  end_date
FROM `linkedin_ads_advertising.campaign_budget`
WHERE DATE(retrieved_at) = CURRENT_DATE()
  AND SAFE_DIVIDE(budget_spent, lifetime_budget) > 0.9
ORDER BY pct_spent DESC;
*/

-- Query 2: Daily budget vs actual spend tracking
/*
SELECT
  campaign_id,
  DATE(retrieved_at) AS date,
  daily_budget,
  budget_spent,
  budget_spent - LAG(budget_spent) OVER (PARTITION BY campaign_id ORDER BY retrieved_at) AS daily_actual_spend
FROM `linkedin_ads_advertising.campaign_budget`
WHERE campaign_id = 'YOUR_CAMPAIGN_ID'
ORDER BY retrieved_at DESC;
*/

-- Query 3: Compare bid amounts across active campaigns
/*
SELECT
  campaign_id,
  bid_type,
  bid_amount,
  min_bid,
  max_bid,
  budget_spent,
  CURRENT_DATE() BETWEEN start_date AND COALESCE(end_date, '2099-12-31') AS is_active
FROM `linkedin_ads_advertising.campaign_budget`
WHERE DATE(retrieved_at) = CURRENT_DATE()
ORDER BY bid_amount DESC;
*/

-- Query 4: Budget pacing analysis
/*
SELECT
  campaign_id,
  start_date,
  end_date,
  DATE_DIFF(COALESCE(end_date, CURRENT_DATE()), start_date, DAY) AS total_days,
  DATE_DIFF(CURRENT_DATE(), start_date, DAY) AS days_elapsed,
  lifetime_budget,
  budget_spent,
  SAFE_DIVIDE(budget_spent, lifetime_budget) * 100 AS pct_budget_spent,
  SAFE_DIVIDE(DATE_DIFF(CURRENT_DATE(), start_date, DAY),
              DATE_DIFF(COALESCE(end_date, CURRENT_DATE()), start_date, DAY)) * 100 AS pct_time_elapsed,
  pacing_type,
  pacing_rate
FROM `linkedin_ads_advertising.campaign_budget`
WHERE DATE(retrieved_at) = CURRENT_DATE()
  AND start_date <= CURRENT_DATE()
  AND (end_date IS NULL OR end_date >= CURRENT_DATE())
ORDER BY campaign_id;
*/
