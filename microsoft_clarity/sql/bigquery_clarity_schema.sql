-- =====================================================
-- Microsoft Clarity Schema for BigQuery
-- =====================================================
-- Dataset: microsoft_clarity
-- Table unique avec métriques au format RECORD/STRUCT
-- =====================================================

-- =====================================================
-- Main Table: Clarity Metrics (Format Markdown/RECORD)
-- =====================================================
CREATE TABLE IF NOT EXISTS `project-id.microsoft_clarity.clarity_metrics` (
  -- Date et Timestamp
  date DATE NOT NULL,
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
  
  -- URL de la page (dimension principale)
  url STRING,
  visits_count INT64,

  -- Scroll Depth (en pourcentages)
  scroll_depth STRUCT<
    percentage_0_10 INT64,
    percentage_11_25 INT64,
    percentage_26_50 INT64,
    percentage_51_75 INT64,
    percentage_76_100 INT64,
    average_scroll_depth FLOAT64
  >,

  -- Engagement Time
  engagement_time STRUCT<
    total_time FLOAT64,
    active_time FLOAT64
  >,

  -- Traffic
  traffic STRUCT<
    total_session_count INT64,
    total_bot_session_count INT64,
    distinct_user_count INT64,
    pages_per_session FLOAT64
  >,

  -- Browser (tableau de structures)
  browser ARRAY<STRUCT<
    name STRING,
    sessions_count INT64
  >>,

  -- Device (tableau de structures)
  device ARRAY<STRUCT<
    name STRING,
    sessions_count INT64
  >>,

  -- OS (tableau de structures)
  os ARRAY<STRUCT<
    name STRING,
    sessions_count INT64
  >>,

  -- Country/Region (tableau de structures)
  country ARRAY<STRUCT<
    name STRING,
    sessions_count INT64
  >>,

  -- Page Title (tableau de structures)
  page_title ARRAY<STRUCT<
    name STRING,
    sessions_count INT64
  >>,

  -- Referrer URL (tableau de structures)
  referrer_url ARRAY<STRUCT<
    name STRING,
    sessions_count INT64
  >>,

  -- Dead Clicks
  dead_clicks STRUCT<
    sessions_count INT64,
    sessions_with_metric_percentage FLOAT64,
    sessions_without_metric_percentage FLOAT64,
    pages_views INT64,
    sub_total INT64
  >,

  -- Excessive Scroll
  excessive_scroll STRUCT<
    sessions_count INT64,
    sessions_with_metric_percentage FLOAT64,
    sessions_without_metric_percentage FLOAT64,
    pages_views INT64,
    sub_total INT64
  >,

  -- Rage Clicks
  rage_clicks STRUCT<
    sessions_count INT64,
    sessions_with_metric_percentage FLOAT64,
    sessions_without_metric_percentage FLOAT64,
    pages_views INT64,
    sub_total INT64
  >,

  -- Quickback Clicks
  quickback_clicks STRUCT<
    sessions_count INT64,
    sessions_with_metric_percentage FLOAT64,
    sessions_without_metric_percentage FLOAT64,
    pages_views INT64,
    sub_total INT64
  >,

  -- Script Errors
  script_errors STRUCT<
    sessions_count INT64,
    sessions_with_metric_percentage FLOAT64,
    sessions_without_metric_percentage FLOAT64,
    pages_views INT64,
    sub_total INT64
  >,

  -- Error Clicks
  error_clicks STRUCT<
    sessions_count INT64,
    sessions_with_metric_percentage FLOAT64,
    sessions_without_metric_percentage FLOAT64,
    pages_views INT64,
    sub_total INT64
  >,

  -- Metadata
  project_name STRING     -- Nom du projet Clarity (EPBS, SOS, etc.)
)
PARTITION BY date
CLUSTER BY date, url, project_name;

-- Views omitted for brevity, see full file
