0. Preconditions (Do This Once)
Access & Auth
LinkedIn Marketing Developer access approved.


OAuth2 token with:


r_organization_social


r_organization_admin


Org ID resolved → ORG_ID


Global Headers (all calls)
Authorization: Bearer {TOKEN}


X-Restli-Protocol-Version: 2.0.0


LinkedIn-Version: 202501


Content-Type: application/json


Time Rules
Granularity: DAY or MONTH only.


Lookback: max 12 months.


Data latency: T+2 days.


Time format: epoch milliseconds (UTC).



1. Followers Growth & Demographics
Purpose
Track follower growth trends and audience composition.
Endpoint
GET /rest/organizationalEntityFollowerStatistics

Call Structure
q=organizationalEntity
organizationalEntity=urn:li:organization:{ORG_ID}
timeIntervals.timeGranularityType=DAY | MONTH
timeIntervals.timeRange.start
timeIntervals.timeRange.end

Metrics to Extract
Time Series
followerGains.organicFollowerGain


followerGains.paidFollowerGain


followerCounts.totalFollowerCount


Demographics (lifetime / snapshot)
By function


By seniority


By industry


By geography (country + region)


By company size


Employee vs non-employee


Notes
No daily demographic deltas.


Demographics come aggregated in response fields.


Store demographics as slowly changing dimensions.



2. Content Impressions & Engagement (Organic Only)
Purpose
Measure how organic content performs over time.
Endpoint
GET /rest/organizationalEntityShareStatistics

Call Structure
q=organizationalEntity
organizationalEntity=urn:li:organization:{ORG_ID}
timeIntervals.timeGranularityType=DAY | MONTH
timeIntervals.timeRange.start
timeIntervals.timeRange.end

Metrics to Extract
impressionCount


uniqueImpressionsCount


clickCount


likeCount


commentCount


shareCount


Derived Metric
engagement_rate =
(clickCount + likeCount + commentCount + shareCount) / impressionCount

Notes
Organic only.


No guaranteed pagination.


If post-level analysis is needed, request specific post URNs.


Paid metrics live in Ad Analytics API (out of scope here).



3. Page Traffic & Visitors
Purpose
Understand page usage and visitor behavior.
Endpoint
GET /rest/organizationPageStatistics

Call Structure
q=organization
organization=urn:li:organization:{ORG_ID}
timeIntervals.timeGranularityType=DAY | MONTH
timeIntervals.timeRange.start
timeIntervals.timeRange.end

Metrics to Extract
Traffic
allPageViews


allDesktopPageViews


allMobilePageViews


overviewPageViews


careersPageViews


CTA Interactions
desktopCustomButtonClickCounts


mobileCustomButtonClickCounts


Demographics (Parsed from Response Fields)
pageStatisticsByFunction


pageStatisticsBySeniority


pageStatisticsByIndustry


pageStatisticsByGeoCountry


pageStatisticsByGeo


pageStatisticsByStaffCountRange


Notes
No pivot query params.


Demographics are nested response objects.


Parse and normalize downstream.






5. Data Model (Recommended)
Fact Tables
linkedin_followers_timeseries


linkedin_page_engagement_timeseries


linkedin_page_views_timeseries


Dimension Tables
linkedin_org_metadata


linkedin_follower_demographics


linkedin_page_visitor_demographics


Keys
organization_urn


date


granularity



6. Scheduling Strategy
Daily Jobs
Share statistics (DAY)


Page statistics (DAY)


Monthly Jobs
Followers (MONTH)


Demographics snapshots


Org metadata refresh


Reporting Rule
Always report up to T-2.



7. Known Hard Limits (Do Not Fight These)
No WEEK granularity.


No historical data beyond 12 months.


No daily demographic attribution.


No paid metrics in these endpoints.


No guaranteed pagination on shares.


Design around them.

8. Minimal cURL Templates (For Validation)
Followers
GET https://api.linkedin.com/rest/organizationalEntityFollowerStatistics

Engagement
GET https://api.linkedin.com/rest/organizationalEntityShareStatistics

Page Stats
GET https://api.linkedin.com/rest/organizationPageStatistics

(Parameters as defined above.)

