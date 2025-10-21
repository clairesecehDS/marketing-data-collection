-- =====================================================
-- Microsoft Clarity Schema for BigQuery
-- =====================================================
-- Dataset: microsoft_clarity
-- Following official Clarity Data Export API structure
-- =====================================================

-- =====================================================
-- Main Table: Clarity Metrics (Official Format)
-- =====================================================
CREATE TABLE IF NOT EXISTS `microsoft_clarity.clarity_metrics` (
  -- Date
  date TIMESTAMP NOT NULL,

  -- Page Information
  name STRING,
  url STRING,
  page_titles STRING,
  popular_pages STRING,
  referrer_urls STRING,

  -- Session & User Metrics
  total_sessions INT64,
  total_users INT64,
  page_views INT64,

  -- Engagement Metrics
  avg_engagement_time FLOAT64,
  scroll_depth FLOAT64,

  -- User Experience Issues
  dead_clicks INT64,
  rage_clicks INT64,
  quick_backs INT64,
  excessive_scrolling INT64,
  error_clicks INT64,

  -- Technical Issues
  script_errors INT64,

  -- Dimension Breakdowns (JSON strings)
  browser_breakdown STRING,
  device_breakdown STRING,
  os_breakdown STRING,
  user_geography STRING,

  -- Metadata
  retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(date)
CLUSTER BY url, date;

-- Views omitted for brevity, see full file
