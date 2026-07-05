# LinkedIn Pages Data Portability API - Complete Endpoint Reference

**Base URL:** `https://api.linkedin.com/rest`

**Authentication:** OAuth 2.0 Bearer Token

**API Version:** 2025-11 (Latest)

**Headers Required:**
```
Authorization: Bearer {ACCESS_TOKEN}
LinkedIn-Version: {YYYYMM}
X-Restli-Protocol-Version: 2.0.0
Content-Type: application/json
```

---

## ANALYTICS ENDPOINTS

### Page Analytics & Statistics

#### Organization Page Statistics
```
GET /organizationalPageStatistics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  
Fields Available:
  - pageFollowerCount
  - impressionCount
  - clickCount
  - commentCount
  - reactionCount
```

#### Organization Page Edge Analytics
```
GET /organizationalPageEdgeAnalytics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - edgeType: MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE | PAGE_FOLLOWS_ORGANIZATIONAL_PAGE
  - timeInterval: (optional) specific date range

Fields Available:
  - visitorCount
  - pageFollowerCount
  - activeFollowerCount
  - newFollowerCount
```

#### Organizational Page Content Analytics DMA
```
GET /organizationalPageContentAnalyticsDMA
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - contentUrn: (optional) specific content URN

Fields Available:
  - impressionCount
  - reactionCount
  - commentCount
  - repostCount
  - clickCount
  - demographicsBreakdown
```

#### Creator Analytics
```
GET /creatorAnalytics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - contentTypes: LIST(ARTICLE, VIDEO, NEWSLETTER)

Fields Available:
  - videoAnalytics
  - articleAnalytics
  - newsletterAnalytics
  - engagementRate
  - impressions
  - clicks
```

#### Search Appearance Analytics
```
GET /organizationSearchAppearanceAnalytics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - timeInterval: (optional)

Fields Available:
  - searchImpressions
  - searchClicks
  - impressionToClickRatio
```

#### Employee Broadcast Analytics
```
GET /employeeBroadcastAnalytics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - timeInterval: (optional)

Fields Available:
  - broadcastCount
  - impressionCount
  - clickCount
  - engagementRate
```

#### Employee Broadcast Audience Demographics
```
GET /employeeBroadcastAudienceDemographics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - audienceSeniority
  - audienceFunction
  - audienceIndustry
  - audienceGeography
  - audienceCompanySize
```

#### Employee Broadcast Time Series Analytics
```
GET /employeeBroadcastTimeSeriesAnalytics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - timeInterval: (optional)

Fields Available:
  - timeSeriesImpressions
  - timeSeriesEngagement
  - timeSeriesClick
```

#### Employee Broadcast Highlights
```
GET /employeeBroadcastHighlights
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - totalEmployeeFollowers
  - totalBroadcasts
  - aggregatedImpressions
  - aggregatedEngagements
```

#### Organization Email Domain Mapping
```
GET /organizationEmailDomainMapping
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - domainMappings
  - verificationStatus
```

---

## FEED & CONTENT ENDPOINTS

### Posts
```
GET /dmaPosts
Query Parameters:
  - q: filter_type (AUTHOR | URN)
  - author: urn:li:person:{PERSON_ID} OR urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer (0-max)
  - paginationCursor: string (from previous response)

Fields Returned:
  - id (URN)
  - text
  - author
  - visibility
  - createdTime
  - commentCount
  - reactionCount
  - repostCount
  - clickCount

Sample Request:
GET https://api.linkedin.com/rest/dmaPosts?q=author&author=urn%3Ali%3AorganizationalPage%3A{ORGANIZATION_ID}&maxPaginationCount=10

Pagination:
Response includes metadata.nextPaginationCursor for fetching next page
```

### Comments
```
GET /dmaComments
Query Parameters:
  - q: CONTENT_URN | AUTHOR
  - contentUrn: urn:li:share:{SHARE_ID}
  - author: urn:li:person:{PERSON_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - text
  - author
  - authorName (if member opted-in)
  - createdTime
  - reactionCount
  - status

Sample Request:
GET https://api.linkedin.com/rest/dmaComments?q=contentUrn&contentUrn=urn%3Ali%3Ashare%3A{SHARE_ID}
```

### Reactions
```
GET /dmaReactions
Query Parameters:
  - q: CONTENT_URN | AUTHOR
  - contentUrn: urn:li:share:{SHARE_ID}
  - author: urn:li:person:{PERSON_ID}
  - reactionType: LIKE | PRAISE | APPRECIATION | EMPATHY | INTEREST | ENTERTAINMENT
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - reactor
  - reactionType
  - createdTime
  - contentUrn

Sample Request:
GET https://api.linkedin.com/rest/dmaReactions?q=contentUrn&contentUrn=urn%3Ali%3Ashare%3A{SHARE_ID}
```

### Instant Reposts
```
GET /dmaInstantReposts
Query Parameters:
  - q: CONTENT_URN | AUTHOR
  - contentUrn: urn:li:share:{SHARE_ID}
  - author: urn:li:person:{PERSON_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - reposter
  - createdTime
  - originalContentUrn
```

### Social Metadata
```
GET /dmaSocialMetadata
Query Parameters:
  - entity: urn:li:share:{SHARE_ID} OR urn:li:article:{ARTICLE_ID}

Fields Returned:
  - reactionCount
  - commentCount
  - repostCount
  - clickCount
```

### Feed Contents External
```
GET /dmaFeedContentsExternal
Query Parameters:
  - q: AUTHOR | CONTENT_URN
  - author: urn:li:organizationalPage:{ORGANIZATION_ID}
  - contentUrn: urn:li:share:{SHARE_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Returns:
  - Finder for posts
  - Finder for reactions
  - Finder for comments
  - Finder for instant reposts

Note: Can take up to 48 hours for data availability
```

### Ingested Content Summaries
```
GET /dmaIngestedContentSummaries
Query Parameters:
  - urns: urn:li:article:{ARTICLE_ID}

Fields Returned:
  - originalUrl
  - resolvedUrl
  - title
  - contentHtml
```

### Content Public URL
```
GET /dmaContentPublicUrl
Query Parameters:
  - urn: urn:li:share:{SHARE_ID}

Returns:
  - publicUrl: Publicly accessible URL for the content
```

---

## PAGES FOLLOWERS ENDPOINTS

### Organizational Page Follows
```
GET /dmaOrganizationalPageFollows
Query Parameters:
  - q: followee (required for finder)
  - followee: urn:li:organizationalPage:{ORGANIZATION_ID}
  - edgeType: MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE | PAGE_FOLLOWS_ORGANIZATIONAL_PAGE
  - maxPaginationCount: integer (0-max)
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - follower (person or page URN)
  - followedOn
  - followerName (if member opted-in)
  - followerHeadline (if member opted-in)

Sample Request:
GET https://api.linkedin.com/rest/dmaOrganizationalPageFollows?q=followee&followee=urn%3Ali%3AorganizationalPage%3A{ORGANIZATION_ID}&edgeType=MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE&maxPaginationCount=10
```

---

## PAGES PROFILES & IDENTITY ENDPOINTS

### Organizational Page Profiles DMA
```
GET /organizationalPageProfilesDMA
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - id
  - name
  - profileUrl
  - tagline
  - description
  - logo
  - industryCategories
  - specialities
  - website
  - locations
  - followerCount
```

### Organizations API
```
GET /organizations/{id}
Path Parameters:
  - id: Organization ID

Fields Available:
  - id
  - name
  - vanityName
  - organizationType
  - description
  - website
  - locations
  - industries
  - specialities
  - foundedYear
  - size
  - companySize
  - tagline
```

### Organization Lookup API
```
GET /organizationLookup
Query Parameters:
  - q: (id | vanityName | emailDomain)
  - ids: urn:li:organization:{ID} (for multiple lookups)
  - vanityName: string
  - emailDomain: string

Returns:
  - Organization names and URNs
```

### Member Profile (/me)
```
GET /me
Query Parameters:
  - projection: (optional) specific fields

Fields Returned (Self View):
  - id
  - localizedFirstName
  - localizedLastName
  - profilePicture
  - headline
  - publicProfileUrl
```

### People Profile
```
GET /people/{id}
Path Parameters:
  - id: Person ID or URN

Query Parameters:
  - ids: multiple people (URL-encoded array)
  - projection: (optional) specific fields

Fields Returned (Subject to Member Privacy Settings):
  - id
  - localizedFirstName
  - localizedLastName
  - profilePicture
  - headline
  - publicProfileUrl
```

---

## PAGES METADATA ENDPOINTS

### Organizational Page Credibility
```
GET /organizationalPageCredibility
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - credibilityHighlights (array)
  - verification
```

### Organizational Page Content Ingestion Sources
```
GET /organizationalPageContentIngestionSources
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - ingestionSources
  - sourceUrls
  - sourceStatus
```

### Organizational Page Notifications
```
GET /organizationalPageNotifications
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - notificationType (REACTION | COMMENT | MENTION)
  - actor
  - content
  - createdTime
```

---

## MESSAGING ENDPOINTS

### Page Messaging Threads
```
GET /pageMessagingThreads
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - participantUrns
  - lastMessageTime
  - unreadMessageCount
```

### Page Messaging Messages DMA
```
GET /pageMessagingMessagesDMA
Query Parameters:
  - messagingThread: urn:li:messagingThread:{THREAD_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - senderUrn
  - messageText
  - attachments
  - createdTime
  - readTime (if applicable)
```

---

## LEAD GENERATION ENDPOINTS

### Lead Gen Forms
```
GET /leadGenForms
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - formName
  - headline
  - description
  - questions (array)
  - createdTime
  - lastModifiedTime
```

### Lead Gen Form Responses
```
GET /leadGenFormResponses
Query Parameters:
  - leadGenForm: urn:li:leadGenForm:{FORM_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - respondentUrn
  - submissionTime
  - answers (map of question ID to answer)
  - leadLeadId
  - leadEmail (if opted-in)
  - leadName (if opted-in)
```

### Lead Analytics
```
GET /leadAnalytics
Query Parameters:
  - leadGenForm: urn:li:leadGenForm:{FORM_ID}
  - timeInterval: (optional)

Fields Available:
  - totalLeads
  - leads
  - conversionRate
  - submissionRate
```

---

## EVENTS ENDPOINTS

### Events
```
GET /events
Query Parameters:
  - q: (ORGANIZER)
  - organizer: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - title
  - description
  - startDate
  - endDate
  - location
  - registrationCount
  - organizerUrn
```

### Event Role Assignments
```
GET /eventRoleAssignments
Query Parameters:
  - event: urn:li:event:{EVENT_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - attendeeUrn
  - role (ORGANIZER | SPEAKER | ATTENDEE)
  - acceptedTime
```

### Live Videos
```
GET /liveVideos
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - title
  - description
  - startTime
  - endTime
  - viewerCount
  - organizerUrn
```

### Live Viewer Count Analytics
```
GET /liveViewerCountAnalytics
Query Parameters:
  - liveVideo: urn:li:liveVideo:{VIDEO_ID}

Fields Available:
  - maxViewerCount
  - averageViewerCount
  - viewerCountByTime
```

---

## PUBLISHING ENDPOINTS

### Content Series
```
GET /contentSeries
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - name
  - description
  - subscriberCount
  - cadence
  - issueCount
```

### Original Articles
```
GET /originalArticles
Query Parameters:
  - q: (OWNER)
  - owner: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - title
  - articleBody
  - coverImage
  - authors
  - publishedDate
  - viewCount
  - likeCount
  - commentCount
```

### Series Subscribers
```
GET /seriesSubscribers
Query Parameters:
  - series: urn:li:contentSeries:{SERIES_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Returned:
  - id (URN)
  - subscriberUrn
  - subscriberName (if opted-in)
  - subscriptionTime
  - lastModifiedTime
```

---

## EMPLOYER BRAND ENDPOINTS

### Organization Career Page Settings
```
GET /organizationCareerPageSettings
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - tagline
  - description
  - featuredSection
  - logo
  - bannerImage
```

### Organization Commitment
```
GET /organizationCommitments
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - commitmentType (DEI | SUSTAINABILITY | INNOVATION)
  - commitmentDescription
  - commitmentUrl
```

### Organization Content Revisions
```
GET /organizationContentRevisions
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - revisionId
  - contentType
  - revisionDate
  - author
```

### Organization Life Page Traffic Statistics
```
GET /organizationLifePageTrafficStatistics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - timeInterval: (optional)

Fields Available:
  - pageViews
  - uniqueVisitors
  - bounceRate
  - averageTimeOnPage
```

### Organization Photos
```
GET /organizationPhotos
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - photoUrl
  - title
  - description
  - uploadedDate
```

### Organization Relationship Statistics
```
GET /organizationRelationshipStatistics
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - timeInterval: (optional)

Fields Available:
  - affiliatedCompanyCount
  - subcompanyCount
  - partnerCount
```

### Organization Targeted Contents
```
GET /organizationTargetedContents
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - contentId
  - contentText
  - targetingCriteria
  - displayPosition
```

### Organization Workplace Policies
```
GET /organizationWorkplacePolicies
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - policyType
  - policyDescription
  - policyUrl
```

### Organization Talent Brand Analytic Summaries
```
GET /organizationTalentBrandAnalyticSummaries
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - timeInterval: (optional)

Fields Available:
  - totalVisitors
  - uniqueVisitors
  - jobClickCount
  - companyFollowCount
  - applicationCount
```

---

## ACCESS MANAGEMENT ENDPOINTS

### Organization Access Control
```
GET /organizationAccessControl
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - admins (array of member URNs)
  - adminEmails (if permission granted)
  - roles (array of role assignments)
  - lastModifiedTime
```

### Organization Authorizations DMA
```
GET /organizationAuthorizationsDMA
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - authorizationType
  - authorizedParty
  - permissions
  - createdTime
  - expirationTime (if applicable)
```

---

## BUSINESS MANAGER ENDPOINTS

### Business Manager Accounts
```
GET /businessManagerAccounts
Query Parameters:
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - accountName
  - accountStatus
  - owner
  - createdTime
```

### Business Manager Account Organizations
```
GET /businessManagerAccountOrganizations
Query Parameters:
  - businessManagerAccount: urn:li:businessManagerAccount:{BMA_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - id (URN)
  - organizationUrn
  - relationshipType
  - createdTime
```

---

## STANDARDIZED DATA ENDPOINTS

### Standardized Data
```
GET /standardizedData
Query Parameters:
  - q: (dataType)
  - dataType: DEGREE | FIELD_OF_STUDY | GEOGRAPHY | INDUSTRY | SENIORITY | SKILL | TITLE

Returns:
  - Array of standardized data items with IDs and names
```

---

## VERIFICATION AGENT ENDPOINTS

### Verification Agents
```
GET /dmaVerificationAgents
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}

Fields Available:
  - agentId
  - emailDomain
  - verificationStatus
  - verificationDate
```

---

## FEATURED CONTENT ENDPOINTS

### Pages Featured Content Groups
```
GET /pagesFeaturedContentGroups
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - topic: (optional) specific content topic

Fields Available:
  - groupId
  - groupName
  - contentUrns (array)
  - displayOrder
```

### Organization Products DMA
```
GET /organizationProductsDMA
Query Parameters:
  - organizationalPage: urn:li:organizationalPage:{ORGANIZATION_ID}
  - maxPaginationCount: integer
  - paginationCursor: string

Fields Available:
  - productId
  - productName
  - description
  - productUrl
  - logoUrl
  - category
  - cta
  - leadGenFormUrn
```

---

## PAGINATION REFERENCE

### Cursor-Based Pagination
All endpoints that return large datasets use cursor-based pagination:

```
Parameters:
  - maxPaginationCount: integer (0 to maximum)
  - paginationCursor: string (token from previous response)

Response Metadata:
  - metadata.nextPaginationCursor: use for next request
  - If null, end of results reached

Example Flow:
1. First request: ?maxPaginationCount=10&paginationCursor=null
2. Response includes: metadata.nextPaginationCursor = "abc123"
3. Next request: ?maxPaginationCount=10&paginationCursor=abc123
4. Continue until nextPaginationCursor is null
```

---

## MEMBER PRIVACY & OBFUSCATION

### Member Opt-In Setting
Setting Name: "Page owners exporting your data"

**When ON (Member Opted-In):**
- Full member URN returned
- Member name returned
- Member profile data included
- Member email available (if provided)

**When OFF (Default):**
- Member URN obfuscated/removed
- Member name removed
- Profile data redacted
- Email not returned

### APIs Affected by Privacy Settings
- dmaComments (author info)
- dmaReactions (reactor info)
- dmaFeedContentsExternal (author info)
- dmaOrganizationalPageFollows (follower info)
- leadGenFormResponses (respondent data)
- pageMessagingThreads (participant info)

---

## AUTHENTICATION & HEADERS

### Required Headers
```
Headers:
  Authorization: Bearer {ACCESS_TOKEN}
  LinkedIn-Version: {YYYYMM}  # e.g., 202511
  X-Restli-Protocol-Version: 2.0.0
  Content-Type: application/json
```

### OAuth 2.0 Token Acquisition
```
POST https://www.linkedin.com/oauth/v2/accessToken
Body:
  grant_type: authorization_code
  code: {AUTHORIZATION_CODE}
  client_id: {CLIENT_ID}
  client_secret: {CLIENT_SECRET}
  redirect_uri: {REDIRECT_URI}
```

---

## ERROR HANDLING

### Common Error Codes
```
400 Bad Request - Invalid query parameters
401 Unauthorized - Invalid or expired token
403 Forbidden - Insufficient permissions
404 Not Found - Resource does not exist
429 Too Many Requests - Rate limit exceeded
500 Internal Server Error - Server-side error
```

### Error Response Format
```json
{
  "code": "ERROR_CODE",
  "message": "Human-readable error message",
  "requestId": "request-id-for-tracking"
}
```

---

## PERMISSIONS REQUIRED

### Permission Scope
```
r_dma_admin_pages_content
  - Retrieve organization posts, articles, newsletters
  - Retrieve engagement data (comments, reactions)
  - Retrieve social action data
  - Retrieve lead gen forms and responses
  - Retrieve page analytics and reporting data
  - Retrieve organization follows
  - Use basic profile data
```

---

## BEST PRACTICES

1. **Use Pagination Properly**
   - Always include maxPaginationCount and paginationCursor
   - Store nextPaginationCursor for next request
   - Stop when nextPaginationCursor is null

2. **Handle Member Privacy**
   - Check member opt-in status before using personal data
   - Implement graceful handling for obfuscated fields
   - Respect member privacy preferences

3. **Data Availability**
   - Feed content (posts, reactions, comments) may take 48 hours
   - Plan for delayed data availability
   - Implement retry logic with exponential backoff

4. **Rate Limiting**
   - Implement request throttling
   - Monitor rate limit headers
   - Implement queue for bulk operations

5. **Version Management**
   - Always specify LinkedIn-Version header
   - Update API calls when new versions release
   - Test compatibility before migration

---

## EXAMPLE REQUESTS

### Get Organization Followers
```bash
curl -X GET 'https://api.linkedin.com/rest/dmaOrganizationalPageFollows?q=followee&followee=urn%3Ali%3AorganizationalPage%3A1234567&edgeType=MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE&maxPaginationCount=10' \
-H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
-H 'LinkedIn-Version: 202511' \
-H 'X-Restli-Protocol-Version: 2.0.0'
```

### Get Posts for Organization
```bash
curl -X GET 'https://api.linkedin.com/rest/dmaPosts?q=author&author=urn%3Ali%3AorganizationalPage%3A1234567&maxPaginationCount=10' \
-H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
-H 'LinkedIn-Version: 202511' \
-H 'X-Restli-Protocol-Version: 2.0.0'
```

### Get Comments on Post
```bash
curl -X GET 'https://api.linkedin.com/rest/dmaComments?q=contentUrn&contentUrn=urn%3Ali%3Ashare%3A1234567890&maxPaginationCount=10' \
-H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
-H 'LinkedIn-Version: 202511' \
-H 'X-Restli-Protocol-Version: 2.0.0'
```

### Get Page Analytics
```bash
curl -X GET 'https://api.linkedin.com/rest/organizationalPageStatistics?organizationalPage=urn%3Ali%3AorganizationalPage%3A1234567' \
-H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
-H 'LinkedIn-Version: 202511' \
-H 'X-Restli-Protocol-Version: 2.0.0'
```

---

## USEFUL RESOURCES

- **Official Documentation:** https://learn.microsoft.com/en-us/linkedin/dma/
- **Developer Portal:** https://developer.linkedin.com/
- **Terms of Service:** https://www.linkedin.com/legal/l/portability-api-terms
- **Rate Limits & Quotas:** Check developer dashboard for your account
- **Support:** https://linkedin.zendesk.com/hc/

---

*Last Updated: December 17, 2025*  
*API Version: 2025-11*
