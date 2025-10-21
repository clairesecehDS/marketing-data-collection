-- =====================================================
-- LinkedIn Lead Forms Tables Schema for BigQuery
-- =====================================================
-- Tables: lead_forms, lead_form_responses, lead_form_metrics
-- Dataset: linkedin_leadgen_form
-- =====================================================

-- =====================================================
-- Table 1: Lead Forms
-- =====================================================
CREATE TABLE IF NOT EXISTS `linkedin_leadgen_form.lead_forms` (
  -- Identifiants
  form_id STRING NOT NULL,
  lead_form_urn STRING,
  organization_id STRING,
  ad_account_id STRING,

  -- Informations du formulaire
  name STRING,
  locale STRING,
  status STRING,  -- ACTIVE, PAUSED, ARCHIVED
  lead_type STRING,

  -- Configuration
  privacy_policy_url STRING,
  custom_disclaimer STRING,
  confirmation_message STRING,

  -- Metadata
  created_at TIMESTAMP,
  last_modified_at TIMESTAMP,
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY form_id, organization_id;

-- =====================================================
-- Table 2: Lead Form Responses
-- =====================================================
CREATE TABLE IF NOT EXISTS `linkedin_leadgen_form.lead_form_responses` (
  -- Identifiants
  lead_response_id STRING NOT NULL,
  form_id STRING NOT NULL,
  organization_id STRING,
  ad_account_id STRING,
  lead_type STRING,

  -- Timing
  submitted_at TIMESTAMP,
  notification_received_at TIMESTAMP,
  fetched_at TIMESTAMP,

  -- Lead Information
  first_name STRING,
  last_name STRING,
  email_address STRING,
  phone_number STRING,
  company_name STRING,
  job_title STRING,
  country STRING,

  -- Campaign Attribution
  campaign_id STRING,
  campaign_group_id STRING,
  creative_id STRING,
  device_type STRING,

  -- Custom & Consent
  custom_fields JSON,
  consent_granted BOOLEAN,

  -- Full Form Data
  form_data JSON,

  -- Metadata
  retrieved_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(submitted_at)
CLUSTER BY form_id, campaign_id, submitted_at;

-- =====================================================
-- Table 3: Lead Form Metrics (Aggregated)
-- =====================================================
CREATE TABLE IF NOT EXISTS `linkedin_leadgen_form.lead_form_metrics` (
  -- Identifiants
  form_id STRING NOT NULL,
  campaign_id STRING,
  date DATE NOT NULL,

  -- Volume Metrics
  total_leads INT64,
  impressions INT64,
  clicks INT64,
  ad_spend FLOAT64,

  -- Calculated Metrics
  submission_rate FLOAT64,  -- (Total Leads ÷ Impressions) × 100
  conversion_rate FLOAT64,  -- (Total Leads ÷ Clicks) × 100
  cost_per_lead FLOAT64,    -- Ad Spend ÷ Total Leads

  -- Timing Metrics
  avg_time_to_first_notification FLOAT64,  -- Average seconds from submission to webhook
  avg_time_to_full_fetch FLOAT64,          -- Average seconds from webhook to fetch

  -- Quality Metrics
  field_completion_rate FLOAT64,  -- (Leads with all required fields ÷ Total Leads) × 100
  consent_opt_in_rate FLOAT64,    -- (Leads who granted consent ÷ Total Leads) × 100
  email_validity_rate FLOAT64,    -- (Leads with valid business email ÷ Total Leads) × 100
  lead_quality_score FLOAT64,     -- Composite score (0-100)

  -- Conversion Metrics
  lead_to_opportunity_count INT64,
  lead_to_opportunity_rate FLOAT64,  -- (Opportunities ÷ Total Leads) × 100

  -- SLA & Anomalies
  sla_breach_count INT64,
  anomaly_detected BOOLEAN,
  anomaly_description STRING,

  -- Metadata
  calculated_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY date
CLUSTER BY form_id, campaign_id, date;

-- =====================================================
-- Useful Views
-- =====================================================

-- View: Real-time Lead Quality Dashboard
CREATE OR REPLACE VIEW `linkedin_leadgen_form.v_lead_quality_dashboard` AS
WITH lead_stats AS (
  SELECT
    form_id,
    COUNT(*) AS total_leads,
    -- Field Completion
    COUNTIF(
      first_name IS NOT NULL AND
      last_name IS NOT NULL AND
      email_address IS NOT NULL
    ) AS complete_leads,
    -- Email Validity (business emails)
    COUNTIF(
      email_address IS NOT NULL AND
      NOT REGEXP_CONTAINS(email_address, r'@(gmail|yahoo|hotmail|outlook|aol)\.com$')
    ) AS valid_business_emails,
    -- Consent
    COUNTIF(consent_granted = TRUE) AS consented_leads,
    -- Timing
    AVG(TIMESTAMP_DIFF(notification_received_at, submitted_at, SECOND)) AS avg_notification_time,
    AVG(TIMESTAMP_DIFF(fetched_at, notification_received_at, SECOND)) AS avg_fetch_time
  FROM `linkedin_leadgen_form.lead_form_responses`
  WHERE submitted_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
  GROUP BY form_id
)
SELECT
  lf.form_id,
  lf.name AS form_name,
  lf.status,
  ls.total_leads,
  ROUND(SAFE_DIVIDE(ls.complete_leads, ls.total_leads) * 100, 2) AS field_completion_rate,
  ROUND(SAFE_DIVIDE(ls.valid_business_emails, ls.total_leads) * 100, 2) AS email_validity_rate,
  ROUND(SAFE_DIVIDE(ls.consented_leads, ls.total_leads) * 100, 2) AS consent_opt_in_rate,
  ROUND(
    (SAFE_DIVIDE(ls.complete_leads, ls.total_leads) * 40 +
     SAFE_DIVIDE(ls.valid_business_emails, ls.total_leads) * 40 +
     SAFE_DIVIDE(ls.consented_leads, ls.total_leads) * 20) * 100,
    2
  ) AS lead_quality_score,
  ROUND(ls.avg_notification_time, 2) AS avg_notification_time_seconds,
  ROUND(ls.avg_fetch_time, 2) AS avg_fetch_time_seconds
FROM `linkedin_leadgen_form.lead_forms` lf
LEFT JOIN lead_stats ls ON lf.form_id = ls.form_id
WHERE DATE(lf.retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `linkedin_leadgen_form.lead_forms`)
ORDER BY ls.total_leads DESC;

-- View: Lead Performance by Campaign
CREATE OR REPLACE VIEW `linkedin_leadgen_form.v_lead_performance_by_campaign` AS
WITH campaign_stats AS (
  SELECT
    lfr.form_id,
    lfr.campaign_id,
    COUNT(*) AS total_leads,
    COUNT(DISTINCT DATE(lfr.submitted_at)) AS active_days,
    MIN(lfr.submitted_at) AS first_lead,
    MAX(lfr.submitted_at) AS last_lead
  FROM `linkedin_leadgen_form.lead_form_responses` lfr
  WHERE lfr.campaign_id IS NOT NULL
    AND lfr.submitted_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
  GROUP BY lfr.form_id, lfr.campaign_id
),
campaign_analytics AS (
  SELECT
    campaign_id,
    SUM(impressions) AS impressions,
    SUM(clicks) AS clicks,
    SUM(cost_in_usd) AS ad_spend
  FROM `linkedin_ads_advertising.campaign_analytics`
  WHERE date_range_start >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  GROUP BY campaign_id
)
SELECT
  cs.campaign_id,
  cs.form_id,
  lf.name AS form_name,
  cs.total_leads,
  ca.impressions,
  ca.clicks,
  ca.ad_spend,
  ROUND(SAFE_DIVIDE(cs.total_leads, ca.impressions) * 100, 4) AS submission_rate,
  ROUND(SAFE_DIVIDE(cs.total_leads, ca.clicks) * 100, 2) AS conversion_rate,
  ROUND(SAFE_DIVIDE(ca.ad_spend, cs.total_leads), 2) AS cost_per_lead,
  cs.active_days,
  cs.first_lead,
  cs.last_lead
FROM campaign_stats cs
LEFT JOIN `linkedin_leadgen_form.lead_forms` lf ON cs.form_id = lf.form_id
LEFT JOIN campaign_analytics ca ON cs.campaign_id = ca.campaign_id
WHERE DATE(lf.retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `linkedin_leadgen_form.lead_forms`)
ORDER BY cs.total_leads DESC;

-- View: SLA Monitoring
CREATE OR REPLACE VIEW `linkedin_leadgen_form.v_lead_sla_monitoring` AS
WITH sla_thresholds AS (
  SELECT
    300 AS notification_sla_seconds,  -- 5 minutes
    600 AS fetch_sla_seconds          -- 10 minutes
)
SELECT
  form_id,
  lead_response_id,
  submitted_at,
  notification_received_at,
  fetched_at,
  TIMESTAMP_DIFF(notification_received_at, submitted_at, SECOND) AS notification_latency_seconds,
  TIMESTAMP_DIFF(fetched_at, notification_received_at, SECOND) AS fetch_latency_seconds,
  CASE
    WHEN TIMESTAMP_DIFF(notification_received_at, submitted_at, SECOND) > (SELECT notification_sla_seconds FROM sla_thresholds)
      THEN TRUE
    WHEN TIMESTAMP_DIFF(fetched_at, notification_received_at, SECOND) > (SELECT fetch_sla_seconds FROM sla_thresholds)
      THEN TRUE
    ELSE FALSE
  END AS sla_breached
FROM `linkedin_leadgen_form.lead_form_responses`
WHERE submitted_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
ORDER BY submitted_at DESC;

-- View: Anomaly Detection (Volume Spikes/Drops)
CREATE OR REPLACE VIEW `linkedin_leadgen_form.v_lead_volume_anomalies` AS
WITH daily_volumes AS (
  SELECT
    form_id,
    DATE(submitted_at) AS date,
    COUNT(*) AS daily_leads
  FROM `linkedin_leadgen_form.lead_form_responses`
  WHERE submitted_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
  GROUP BY form_id, DATE(submitted_at)
),
rolling_avg AS (
  SELECT
    form_id,
    date,
    daily_leads,
    AVG(daily_leads) OVER (
      PARTITION BY form_id
      ORDER BY date
      ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING
    ) AS rolling_7day_avg
  FROM daily_volumes
)
SELECT
  ra.form_id,
  lf.name AS form_name,
  ra.date,
  ra.daily_leads,
  ROUND(ra.rolling_7day_avg, 2) AS rolling_7day_avg,
  ROUND(SAFE_DIVIDE(ra.daily_leads - ra.rolling_7day_avg, ra.rolling_7day_avg) * 100, 2) AS pct_change,
  CASE
    WHEN SAFE_DIVIDE(ABS(ra.daily_leads - ra.rolling_7day_avg), ra.rolling_7day_avg) > 0.3 THEN TRUE
    ELSE FALSE
  END AS anomaly_detected,
  CASE
    WHEN ra.daily_leads > ra.rolling_7day_avg * 1.3 THEN 'SPIKE'
    WHEN ra.daily_leads < ra.rolling_7day_avg * 0.7 THEN 'DROP'
    ELSE 'NORMAL'
  END AS anomaly_type
FROM rolling_avg ra
LEFT JOIN `linkedin_leadgen_form.lead_forms` lf ON ra.form_id = lf.form_id
WHERE DATE(lf.retrieved_at) = (SELECT MAX(DATE(retrieved_at)) FROM `linkedin_leadgen_form.lead_forms`)
  AND ra.rolling_7day_avg IS NOT NULL
ORDER BY ra.date DESC, ABS(SAFE_DIVIDE(ra.daily_leads - ra.rolling_7day_avg, ra.rolling_7day_avg)) DESC;

-- =====================================================
-- Example Queries
-- =====================================================

-- Query 1: Complete Lead Quality Report
/*
SELECT
  form_id,
  form_name,
  total_leads,
  field_completion_rate,
  email_validity_rate,
  consent_opt_in_rate,
  lead_quality_score,
  avg_notification_time_seconds,
  avg_fetch_time_seconds
FROM `linkedin_leadgen_form.v_lead_quality_dashboard`
ORDER BY lead_quality_score DESC;
*/

-- Query 2: Campaign ROI Analysis
/*
SELECT
  campaign_id,
  form_name,
  total_leads,
  impressions,
  clicks,
  submission_rate,
  conversion_rate,
  cost_per_lead,
  ad_spend,
  ROUND(ad_spend / NULLIF(total_leads, 0), 2) AS actual_cpl
FROM `linkedin_leadgen_form.v_lead_performance_by_campaign`
WHERE total_leads > 0
ORDER BY cost_per_lead ASC;
*/

-- Query 3: SLA Breach Report
/*
SELECT
  form_id,
  COUNT(*) AS total_leads,
  COUNTIF(sla_breached) AS sla_breaches,
  ROUND(SAFE_DIVIDE(COUNTIF(sla_breached), COUNT(*)) * 100, 2) AS sla_breach_rate,
  AVG(notification_latency_seconds) AS avg_notification_latency,
  AVG(fetch_latency_seconds) AS avg_fetch_latency
FROM `linkedin_leadgen_form.v_lead_sla_monitoring`
GROUP BY form_id
ORDER BY sla_breach_rate DESC;
*/

-- Query 4: Detect Recent Anomalies
/*
SELECT
  form_name,
  date,
  daily_leads,
  rolling_7day_avg,
  pct_change,
  anomaly_type
FROM `linkedin_leadgen_form.v_lead_volume_anomalies`
WHERE anomaly_detected = TRUE
  AND date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
ORDER BY date DESC, ABS(pct_change) DESC;
*/
