## 📊 Schémas des Tables BigQuery

**Projet:** `ecoledesponts`


### Dataset: `GA4_EPBS`

#### Table: `ga4_Audiences_427042790`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `audienceName` | STRING | NULLABLE | - |
| `averageSessionDuration` | FLOAT | NULLABLE | - |
| `newUsers` | INTEGER | NULLABLE | - |
| `screenPageViewsPerSession` | FLOAT | NULLABLE | - |
| `sessions` | INTEGER | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `totalUsers` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_DemographicDetails_427042790`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `brandingInterest` | STRING | NULLABLE | - |
| `city` | STRING | NULLABLE | - |
| `country` | STRING | NULLABLE | - |
| `language` | STRING | NULLABLE | - |
| `region` | STRING | NULLABLE | - |
| `userAgeBracket` | STRING | NULLABLE | - |
| `userGender` | STRING | NULLABLE | - |
| `activeUsers` | INTEGER | NULLABLE | - |
| `engagedSessions` | INTEGER | NULLABLE | - |
| `engagementRate` | FLOAT | NULLABLE | - |
| `eventCount` | INTEGER | NULLABLE | - |
| `keyEvents` | FLOAT | NULLABLE | - |
| `newUsers` | INTEGER | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `userEngagementDuration` | FLOAT | NULLABLE | - |
| `userKeyEventRate` | FLOAT | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_EcommercePurchases_427042790`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `itemBrand` | STRING | NULLABLE | - |
| `itemCategory` | STRING | NULLABLE | - |
| `itemCategory2` | STRING | NULLABLE | - |
| `itemCategory3` | STRING | NULLABLE | - |
| `itemCategory4` | STRING | NULLABLE | - |
| `itemCategory5` | STRING | NULLABLE | - |
| `itemId` | STRING | NULLABLE | - |
| `itemListPosition` | STRING | NULLABLE | - |
| `itemName` | STRING | NULLABLE | - |
| `itemVariant` | STRING | NULLABLE | - |
| `itemRevenue` | FLOAT | NULLABLE | - |
| `itemsAddedToCart` | INTEGER | NULLABLE | - |
| `itemsPurchased` | INTEGER | NULLABLE | - |
| `itemsViewed` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_Events_427042790`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `eventName` | STRING | NULLABLE | - |
| `eventCount` | INTEGER | NULLABLE | - |
| `eventCountPerUser` | FLOAT | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `totalUsers` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_LandingPage_427042790`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `landingPage` | STRING | NULLABLE | - |
| `activeUsers` | INTEGER | NULLABLE | - |
| `keyEvents` | FLOAT | NULLABLE | - |
| `newUsers` | INTEGER | NULLABLE | - |
| `sessionKeyEventRate` | FLOAT | NULLABLE | - |
| `sessions` | INTEGER | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `userEngagementDurationPerSession` | FLOAT | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_PagesAndScreens_427042790`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `contentGroup` | STRING | NULLABLE | - |
| `unifiedPagePathScreen` | STRING | NULLABLE | - |
| `unifiedScreenClass` | STRING | NULLABLE | - |
| `unifiedScreenName` | STRING | NULLABLE | - |
| `activeUsers` | INTEGER | NULLABLE | - |
| `eventCount` | INTEGER | NULLABLE | - |
| `keyEvents` | FLOAT | NULLABLE | - |
| `screenPageViews` | INTEGER | NULLABLE | - |
| `screenPageViewsPerUser` | FLOAT | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `userEngagementDuration` | FLOAT | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_Promotions_427042790`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `itemListPosition` | STRING | NULLABLE | - |
| `itemPromotionCreativeName` | STRING | NULLABLE | - |
| `itemPromotionId` | STRING | NULLABLE | - |
| `itemPromotionName` | STRING | NULLABLE | - |
| `itemPromotionClickThroughRate` | FLOAT | NULLABLE | - |
| `itemRevenue` | FLOAT | NULLABLE | - |
| `itemsAddedToCart` | INTEGER | NULLABLE | - |
| `itemsCheckedOut` | INTEGER | NULLABLE | - |
| `itemsClickedInPromotion` | INTEGER | NULLABLE | - |
| `itemsPurchased` | INTEGER | NULLABLE | - |
| `itemsViewedInPromotion` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_TechDetails_427042790`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `appVersion` | STRING | NULLABLE | - |
| `browser` | STRING | NULLABLE | - |
| `deviceCategory` | STRING | NULLABLE | - |
| `operatingSystem` | STRING | NULLABLE | - |
| `operatingSystemVersion` | STRING | NULLABLE | - |
| `operatingSystemWithVersion` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `platformDeviceCategory` | STRING | NULLABLE | - |
| `screenResolution` | STRING | NULLABLE | - |
| `activeUsers` | INTEGER | NULLABLE | - |
| `engagedSessions` | INTEGER | NULLABLE | - |
| `engagementRate` | FLOAT | NULLABLE | - |
| `eventCount` | INTEGER | NULLABLE | - |
| `keyEvents` | FLOAT | NULLABLE | - |
| `newUsers` | INTEGER | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `userEngagementDuration` | FLOAT | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_TrafficAcquisition_427042790`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `sessionCampaignName` | STRING | NULLABLE | - |
| `sessionDefaultChannelGroup` | STRING | NULLABLE | - |
| `sessionMedium` | STRING | NULLABLE | - |
| `sessionPrimaryChannelGroup` | STRING | NULLABLE | - |
| `sessionSource` | STRING | NULLABLE | - |
| `sessionSourceMedium` | STRING | NULLABLE | - |
| `sessionSourcePlatform` | STRING | NULLABLE | - |
| `engagedSessions` | INTEGER | NULLABLE | - |
| `engagementRate` | FLOAT | NULLABLE | - |
| `eventCount` | INTEGER | NULLABLE | - |
| `eventsPerSession` | FLOAT | NULLABLE | - |
| `keyEvents` | FLOAT | NULLABLE | - |
| `sessionKeyEventRate` | FLOAT | NULLABLE | - |
| `sessions` | INTEGER | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `userEngagementDurationPerSession` | FLOAT | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ga4_UserAcquisition_427042790`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `firstUserCampaignName` | STRING | NULLABLE | - |
| `firstUserDefaultChannelGroup` | STRING | NULLABLE | - |
| `firstUserMedium` | STRING | NULLABLE | - |
| `firstUserPrimaryChannelGroup` | STRING | NULLABLE | - |
| `firstUserSource` | STRING | NULLABLE | - |
| `firstUserSourceMedium` | STRING | NULLABLE | - |
| `firstUserSourcePlatform` | STRING | NULLABLE | - |
| `activeUsers` | INTEGER | NULLABLE | - |
| `engagedSessions` | INTEGER | NULLABLE | - |
| `eventCount` | INTEGER | NULLABLE | - |
| `keyEvents` | FLOAT | NULLABLE | - |
| `newUsers` | INTEGER | NULLABLE | - |
| `totalRevenue` | FLOAT | NULLABLE | - |
| `totalUsers` | INTEGER | NULLABLE | - |
| `userEngagementDuration` | FLOAT | NULLABLE | - |
| `userKeyEventRate` | FLOAT | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `p_ga4_Audiences_427042790`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `audienceName` | STRING | NULLABLE | The given name of an Audience. Users are reported in the audiences to which they belonged during the report's date range. Current user behavior does not affect historical audience membership in reports. |
| `averageSessionDuration` | FLOAT | NULLABLE | The average duration (in seconds) of users` sessions. |
| `newUsers` | INTEGER | NULLABLE | The number of users who interacted with your site or launched your app for the first time (event triggered: first_open or first_visit). |
| `screenPageViewsPerSession` | FLOAT | NULLABLE | The number of app screens or web pages your users viewed per session. Repeated views of a single page or screen are counted. (screen_view + page_view events) / sessions. |
| `sessions` | INTEGER | NULLABLE | The number of sessions that began on your site or app (event triggered: session_start). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `totalUsers` | INTEGER | NULLABLE | The number of distinct users who have logged at least one event, regardless of whether the site or app was in use when that event was logged. |

#### Table: `p_ga4_DemographicDetails_427042790`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `brandingInterest` | STRING | NULLABLE | Interests demonstrated by users who are higher in the shopping funnel. Users can be counted in multiple interest categories. For example, Shoppers, Lifestyles & Hobbies/Pet Lovers, or Travel/Travel Buffs/Beachbound Travelers. |
| `city` | STRING | NULLABLE | The city from which the user activity originated. |
| `country` | STRING | NULLABLE | The country from which the user activity originated. |
| `language` | STRING | NULLABLE | The language setting of the user's browser or device. For example, English. |
| `region` | STRING | NULLABLE | The geographic region from which the user activity originated, derived from their IP address. |
| `userAgeBracket` | STRING | NULLABLE | User age brackets. |
| `userGender` | STRING | NULLABLE | User gender. |
| `activeUsers` | INTEGER | NULLABLE | The number of distinct users who visited your website or application. |
| `engagedSessions` | INTEGER | NULLABLE | The number of sessions that had an engaged event. |
| `engagementRate` | FLOAT | NULLABLE | The percentage of sessions that had an engaged event. |
| `eventCount` | INTEGER | NULLABLE | The count of events. |
| `keyEvents` | FLOAT | NULLABLE | The number of key events that occurred. |
| `newUsers` | INTEGER | NULLABLE | The number of users who interacted with your site or launched your app for the first time (event triggered: first_open or first_visit). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `userEngagementDuration` | FLOAT | NULLABLE | The total amount of time (in seconds) your website or app was in the foreground of users` devices. |
| `userKeyEventRate` | FLOAT | NULLABLE | The percentage of users who triggered any key event. |

#### Table: `p_ga4_EcommercePurchases_427042790`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `itemBrand` | STRING | NULLABLE | Brand name of the item. |
| `itemCategory` | STRING | NULLABLE | The hierarchical category in which the item is classified. For example, in Apparel/Mens/Summer/Shirts/T-shirts, Apparel is the item category. |
| `itemCategory2` | STRING | NULLABLE | The hierarchical category in which the item is classified. For example, in Apparel/Mens/Summer/Shirts/T-shirts, Mens is the item category 2. |
| `itemCategory3` | STRING | NULLABLE | The hierarchical category in which the item is classified. For example, in Apparel/Mens/Summer/Shirts/T-shirts, Summer is the item category 3. |
| `itemCategory4` | STRING | NULLABLE | The hierarchical category in which the item is classified. For example, in Apparel/Mens/Summer/Shirts/T-shirts, Shirts is the item category 4. |
| `itemCategory5` | STRING | NULLABLE | The hierarchical category in which the item is classified. For example, in Apparel/Mens/Summer/Shirts/T-shirts, T-shirts is the item category 5. |
| `itemId` | STRING | NULLABLE | The ID of the item. |
| `itemListPosition` | STRING | NULLABLE | The position of an item in a list. For example, a product you sell in a list. This dimension is populated in tagging by the index parameter in the items array. |
| `itemName` | STRING | NULLABLE | The name of the item. |
| `itemVariant` | STRING | NULLABLE | The specific variation of a product. For example, XS, S, M, or L for size; or Red, Blue, Green, or Black for color. Populated by the item_variant parameter. |
| `itemRevenue` | FLOAT | NULLABLE | The total revenue from purchases minus refunded transaction revenue from items only. Item revenue is the product of its price and quantity. Item revenue excludes tax and shipping values; tax & shipping values are specified at the event and not item level. |
| `itemsAddedToCart` | INTEGER | NULLABLE | The number of units added to cart for a single item. This metric counts the quantity of items in add_to_cart events. |
| `itemsPurchased` | INTEGER | NULLABLE | The number of units for a single item included in purchase events. This metric counts the quantity of items in purchase events. |
| `itemsViewed` | INTEGER | NULLABLE | The number of units viewed for a single item. This metric counts the quantity of items in view_item events. |

#### Table: `p_ga4_Events_427042790`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `eventName` | STRING | NULLABLE | The name of the event. |
| `eventCount` | INTEGER | NULLABLE | The count of events. |
| `eventCountPerUser` | FLOAT | NULLABLE | The average number of events per user (Event count divided by Active users). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `totalUsers` | INTEGER | NULLABLE | The number of distinct users who have logged at least one event, regardless of whether the site or app was in use when that event was logged. |

#### Table: `p_ga4_LandingPage_427042790`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `landingPage` | STRING | NULLABLE | The page path associated with the first pageview in a session. |
| `activeUsers` | INTEGER | NULLABLE | The number of distinct users who visited your website or application. |
| `keyEvents` | FLOAT | NULLABLE | The number of key events that occurred. |
| `newUsers` | INTEGER | NULLABLE | The number of users who interacted with your site or launched your app for the first time (event triggered: first_open or first_visit). |
| `sessionKeyEventRate` | FLOAT | NULLABLE | The percentage of sessions in which any key event was triggered. |
| `sessions` | INTEGER | NULLABLE | The number of sessions that began on your site or app (event triggered: session_start). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `userEngagementDurationPerSession` | FLOAT | NULLABLE | Average engagement time per session |

#### Table: `p_ga4_PagesAndScreens_427042790`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `contentGroup` | STRING | NULLABLE | A category that applies to items of published content. Populated by the event parameter content_group. |
| `unifiedPagePathScreen` | STRING | NULLABLE | The page path (web) or screen class (app) on which the event was logged. |
| `unifiedScreenClass` | STRING | NULLABLE | The page title (web) or screen class (app) on which the event was logged. |
| `unifiedScreenName` | STRING | NULLABLE | The page title (web) or screen name (app) on which the event was logged. |
| `activeUsers` | INTEGER | NULLABLE | The number of distinct users who visited your website or application. |
| `eventCount` | INTEGER | NULLABLE | The count of events. |
| `keyEvents` | FLOAT | NULLABLE | The number of key events that occurred. |
| `screenPageViews` | INTEGER | NULLABLE | The number of app screens or web pages your users viewed. Repeated views of a single page or screen are counted. (screen_view + page_view events). |
| `screenPageViewsPerUser` | FLOAT | NULLABLE | The number of app screens or web pages your users viewed per active user. Repeated views of a single page or screen are counted. (screen_view + page_view events) / active users. |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `userEngagementDuration` | FLOAT | NULLABLE | The total amount of time (in seconds) your website or app was in the foreground of users` devices. |

#### Table: `p_ga4_Promotions_427042790`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `itemListPosition` | STRING | NULLABLE | The position of an item in a list. For example, a product you sell in a list. This dimension is populated in tagging by the index parameter in the items array. |
| `itemPromotionCreativeName` | STRING | NULLABLE | The name of the item-promotion creative. |
| `itemPromotionId` | STRING | NULLABLE | The ID of the promotion. |
| `itemPromotionName` | STRING | NULLABLE | The name of the promotion for the item. |
| `itemPromotionClickThroughRate` | FLOAT | NULLABLE | The number of users who selected a promotion(s) divided by the number of users who viewed the same promotion(s). This metric is returned as a fraction; for example, 0.1382 means 13.82% of users who viewed a promotion also selected the promotion. |
| `itemRevenue` | FLOAT | NULLABLE | The total revenue from purchases minus refunded transaction revenue from items only. Item revenue is the product of its price and quantity. Item revenue excludes tax and shipping values; tax & shipping values are specified at the event and not item level. |
| `itemsAddedToCart` | INTEGER | NULLABLE | The number of units added to cart for a single item. This metric counts the quantity of items in add_to_cart events. |
| `itemsCheckedOut` | INTEGER | NULLABLE | The number of units checked out for a single item. This metric counts the quantity of items in begin_checkout events. |
| `itemsClickedInPromotion` | INTEGER | NULLABLE | The number of units clicked in promotion for a single item. This metric counts the quantity of items in select_promotion events. |
| `itemsPurchased` | INTEGER | NULLABLE | The number of units for a single item included in purchase events. This metric counts the quantity of items in purchase events. |
| `itemsViewedInPromotion` | INTEGER | NULLABLE | The number of units viewed in promotion for a single item. This metric counts the quantity of items in view_promotion events. |

#### Table: `p_ga4_TechDetails_427042790`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `appVersion` | STRING | NULLABLE | The app's versionName (Android) or short bundle version (iOS). |
| `browser` | STRING | NULLABLE | The browsers used to view your website. |
| `deviceCategory` | STRING | NULLABLE | The type of device: Desktop, Tablet, or Mobile. |
| `operatingSystem` | STRING | NULLABLE | The operating systems used by visitors to your app or website. Includes desktop and mobile operating systems such as Windows and Android. |
| `operatingSystemVersion` | STRING | NULLABLE | The operating system versions used by visitors to your website or app. For example, Android 10's version is 10, and iOS 13.5.1's version is 13.5.1. |
| `operatingSystemWithVersion` | STRING | NULLABLE | The operating system and version. For example, Android 10 or Windows 7. |
| `platform` | STRING | NULLABLE | The platform on which your app or website ran; for example, web, iOS, or Android. To determine a stream's type in a report, use both platform and streamId. |
| `platformDeviceCategory` | STRING | NULLABLE | The platform and type of device on which your website or mobile app ran. (example: Android / mobile) |
| `screenResolution` | STRING | NULLABLE | The screen resolution of the user's monitor. For example, 1920x1080. |
| `activeUsers` | INTEGER | NULLABLE | The number of distinct users who visited your website or application. |
| `engagedSessions` | INTEGER | NULLABLE | The number of sessions that lasted longer than 10 seconds, or had a key event, or had 2 or more screen views. |
| `engagementRate` | FLOAT | NULLABLE | The percentage of engaged sessions (Engaged sessions divided by Sessions). This metric is returned as a fraction; for example, 0.7239 means 72.39% of sessions were engaged sessions. |
| `eventCount` | INTEGER | NULLABLE | The count of events. |
| `keyEvents` | FLOAT | NULLABLE | The number of key events that occurred. |
| `newUsers` | INTEGER | NULLABLE | The number of users who interacted with your site or launched your app for the first time (event triggered: first_open or first_visit). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `userEngagementDuration` | FLOAT | NULLABLE | The total amount of time (in seconds) your website or app was in the foreground of users` devices. |

#### Table: `p_ga4_TrafficAcquisition_427042790`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `sessionCampaignName` | STRING | NULLABLE | The marketing campaign name for a session. Includes Google Ads Campaigns, Manual Campaigns, & other Campaigns. |
| `sessionDefaultChannelGroup` | STRING | NULLABLE | The session's default channel group is based primarily on source and medium. An enumeration which includes Direct, Organic Search, Paid Social, Organic Social, Email, Affiliates, Referral, Paid Search, Video, and Display. |
| `sessionMedium` | STRING | NULLABLE | The medium that initiated a session on your website or app. |
| `sessionPrimaryChannelGroup` | STRING | NULLABLE | The primary channel group that led to the session. Primary channel groups are the channel groups used in standard reports in Google Analytics and serve as an active record of your property's data in alignment with channel grouping over time. |
| `sessionSource` | STRING | NULLABLE | The source that initiated a session on your website or app. |
| `sessionSourceMedium` | STRING | NULLABLE | The combined values of the dimensions sessionSource and sessionMedium. |
| `sessionSourcePlatform` | STRING | NULLABLE | The source platform of the session's campaign. Don't depend on this field returning Manual for traffic that uses UTMs; this field will update from returning Manual to returning (not set) for an upcoming feature launch. |
| `engagedSessions` | INTEGER | NULLABLE | The number of sessions that lasted longer than 10 seconds, or had a key event, or had 2 or more screen views. |
| `engagementRate` | FLOAT | NULLABLE | The percentage of engaged sessions (Engaged sessions divided by Sessions). This metric is returned as a fraction; for example, 0.7239 means 72.39% of sessions were engaged sessions. |
| `eventCount` | INTEGER | NULLABLE | The count of events. |
| `eventsPerSession` | FLOAT | NULLABLE | The average number of events per session (Event count divided by Sessions). |
| `keyEvents` | FLOAT | NULLABLE | The number of key events that occurred. |
| `sessionKeyEventRate` | FLOAT | NULLABLE | The percentage of sessions in which any key event was triggered. |
| `sessions` | INTEGER | NULLABLE | The number of sessions that began on your site or app (event triggered: session_start). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `userEngagementDurationPerSession` | FLOAT | NULLABLE | Average engagement time per session |

#### Table: `p_ga4_UserAcquisition_427042790`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `firstUserCampaignName` | STRING | NULLABLE | Name of the marketing campaign that first acquired the user. Includes Google Ads Campaigns, Manual Campaigns, & other Campaigns. |
| `firstUserDefaultChannelGroup` | STRING | NULLABLE | The default channel group that first acquired the user. Default channel group is based primarily on source and medium. An enumeration which includes Direct, Organic Search, Paid Social, Organic Social, Email, Affiliates, Referral, Paid Search, Video, and Display. |
| `firstUserMedium` | STRING | NULLABLE | The medium that first acquired the user to your website or app. |
| `firstUserPrimaryChannelGroup` | STRING | NULLABLE | The primary channel group that originally acquired a user. Primary channel groups are the channel groups used in standard reports in Google Analytics and serve as an active record of your property's data in alignment with channel grouping over time. |
| `firstUserSource` | STRING | NULLABLE | The source that first acquired the user to your website or app. |
| `firstUserSourceMedium` | STRING | NULLABLE | The combined values of the dimensions firstUserSource and firstUserMedium. |
| `firstUserSourcePlatform` | STRING | NULLABLE | The source platform that first acquired the user. Don't depend on this field returning Manual for traffic that uses UTMs; this field will update from returning Manual to returning (not set) for an upcoming feature launch. |
| `activeUsers` | INTEGER | NULLABLE | The number of distinct users who visited your website or application. |
| `engagedSessions` | INTEGER | NULLABLE | The number of sessions that lasted longer than 10 seconds, or had a key event, or had 2 or more screen views. |
| `eventCount` | INTEGER | NULLABLE | The count of events. |
| `keyEvents` | FLOAT | NULLABLE | The number of key events that occurred. |
| `newUsers` | INTEGER | NULLABLE | The number of users who interacted with your site or launched your app for the first time (event triggered: first_open or first_visit). |
| `totalRevenue` | FLOAT | NULLABLE | The sum of revenue from purchases, subscriptions, and advertising (Purchase revenue plus Subscription revenue plus Ad revenue) minus refunded transaction revenue. |
| `totalUsers` | INTEGER | NULLABLE | The number of distinct users who have logged at least one event, regardless of whether the site or app was in use when that event was logged. |
| `userEngagementDuration` | FLOAT | NULLABLE | The total amount of time (in seconds) your website or app was in the foreground of users` devices. |
| `userKeyEventRate` | FLOAT | NULLABLE | The percentage of users who triggered any key event. |

---

### Dataset: `analytics_427042790`

#### Table: `events_20251209`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251210`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251211`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251212`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251213`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251214`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251215`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251216`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251217`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251218`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251219`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251220`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251221`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251222`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251223`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251224`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251225`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251226`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251227`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251228`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251229`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251230`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20251231`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260101`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260102`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260103`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260104`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260105`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260106`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260107`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260108`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260109`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260110`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260111`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260112`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260113`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260114`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260115`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260116`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260117`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260118`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260119`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260120`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260121`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260122`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260123`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260124`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_20260125`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `events_intraday_20260126`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `event_date` | STRING | NULLABLE | - |
| `event_timestamp` | INTEGER | NULLABLE | - |
| `event_name` | STRING | NULLABLE | - |
| `event_params` | RECORD | REPEATED | - |
| `event_previous_timestamp` | INTEGER | NULLABLE | - |
| `event_value_in_usd` | FLOAT | NULLABLE | - |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | - |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | - |
| `user_id` | STRING | NULLABLE | - |
| `user_pseudo_id` | STRING | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `app_info` | RECORD | NULLABLE | - |
| `traffic_source` | RECORD | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `platform` | STRING | NULLABLE | - |
| `event_dimensions` | RECORD | NULLABLE | - |
| `ecommerce` | RECORD | NULLABLE | - |
| `items` | RECORD | REPEATED | - |
| `collected_traffic_source` | RECORD | NULLABLE | - |
| `is_active_user` | BOOLEAN | NULLABLE | - |
| `batch_event_index` | INTEGER | NULLABLE | - |
| `batch_page_id` | INTEGER | NULLABLE | - |
| `batch_ordering_id` | INTEGER | NULLABLE | - |
| `session_traffic_source_last_click` | RECORD | NULLABLE | - |
| `publisher` | RECORD | NULLABLE | - |

#### Table: `pseudonymous_users_20251209`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251210`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251211`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251212`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251213`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251214`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251215`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251216`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251217`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251218`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251219`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251220`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251221`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251222`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251223`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251224`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251225`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251226`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251227`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251228`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251229`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251230`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20251231`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260101`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260102`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260103`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260104`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260105`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260106`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260107`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260108`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260109`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260110`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260111`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260112`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260113`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260114`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260115`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260116`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260117`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260118`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260119`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260120`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260121`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260122`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260123`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260124`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

#### Table: `pseudonymous_users_20260125`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `pseudo_user_id` | STRING | NULLABLE | - |
| `stream_id` | STRING | NULLABLE | - |
| `user_info` | RECORD | NULLABLE | - |
| `device` | RECORD | NULLABLE | - |
| `geo` | RECORD | NULLABLE | - |
| `audiences` | RECORD | REPEATED | - |
| `user_properties` | RECORD | REPEATED | - |
| `user_ltv` | RECORD | NULLABLE | - |
| `predictions` | RECORD | NULLABLE | - |
| `privacy_info` | RECORD | NULLABLE | - |
| `occurrence_date` | STRING | NULLABLE | - |
| `last_updated_date` | STRING | NULLABLE | - |

---

### Dataset: `brevo`

#### Table: `brevo_campaigns`

**Nombre de colonnes:** 36


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `modified_at` | TIMESTAMP | NULLABLE | - |
| `unsubscribe_rate` | FLOAT | NULLABLE | - |
| `click_rate` | FLOAT | NULLABLE | - |
| `open_rate` | FLOAT | NULLABLE | - |
| `stats_deferred` | INTEGER | NULLABLE | - |
| `stats_viewed` | INTEGER | NULLABLE | - |
| `stats_unique_views` | INTEGER | NULLABLE | - |
| `stats_hard_bounces` | INTEGER | NULLABLE | - |
| `stats_sent` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |
| `stats_trackable_views` | INTEGER | NULLABLE | - |
| `html_content` | STRING | NULLABLE | - |
| `subject_b` | STRING | NULLABLE | - |
| `stats_delivered` | INTEGER | NULLABLE | - |
| `reply_to` | STRING | NULLABLE | - |
| `stats_soft_bounces` | INTEGER | NULLABLE | - |
| `stats_complaints` | INTEGER | NULLABLE | - |
| `stats_unique_clicks` | INTEGER | NULLABLE | - |
| `subject_a` | STRING | NULLABLE | - |
| `ab_testing` | BOOLEAN | NULLABLE | - |
| `tag` | STRING | NULLABLE | - |
| `scheduled_at` | TIMESTAMP | NULLABLE | - |
| `stats_clickers` | INTEGER | NULLABLE | - |
| `type` | STRING | NULLABLE | - |
| `created_at` | TIMESTAMP | NULLABLE | - |
| `stats_unsubscriptions` | INTEGER | NULLABLE | - |
| `preview_text` | STRING | NULLABLE | - |
| `to_field` | STRING | NULLABLE | - |
| `sender_name` | STRING | NULLABLE | - |
| `status` | STRING | NULLABLE | - |
| `bounce_rate` | FLOAT | NULLABLE | - |
| `subject` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `sender_email` | STRING | NULLABLE | - |
| `sent_date` | TIMESTAMP | NULLABLE | - |
| `id` | INTEGER | NULLABLE | - |

#### Table: `brevo_contacts_lists`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `retrieved_at` | TIMESTAMP | NULLABLE | - |
| `created_at` | STRING | NULLABLE | - |
| `total_blacklisted` | INTEGER | NULLABLE | - |
| `folder_id` | INTEGER | NULLABLE | - |
| `total_subscribers` | INTEGER | NULLABLE | - |
| `folder_name` | STRING | NULLABLE | - |
| `unique_subscribers` | INTEGER | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `id` | INTEGER | NULLABLE | - |

#### Table: `brevo_events`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `date` | TIMESTAMP | NULLABLE | Date et heure de l'événement |
| `email` | STRING | NULLABLE | Adresse email du contact |
| `event` | STRING | NULLABLE | Type d'événement (spam, opened, click, hard_bounce, soft_bounce, delivered, unsubscribe, contact_deleted, contact_updated, list_addition, etc.) |
| `id` | INTEGER | NULLABLE | ID de l'événement (peut être NULL) |
| `message_id` | STRING | NULLABLE | ID du message - Identifiant principal (ex: <202302241202.77117841982@smtp-relay.mailin.fr>) |
| `reason` | STRING | NULLABLE | Raison de l'événement (ex: sent) |
| `sending_ip` | STRING | NULLABLE | IP d'envoi du message |
| `subject` | STRING | NULLABLE | Sujet de l'email |
| `tag` | STRING | NULLABLE | Tag principal associé |
| `tags` | STRING | NULLABLE | Liste de tous les tags associés au format JSON array (ex: ["tag1","tag2"]) |
| `template_id` | INTEGER | NULLABLE | ID du template utilisé |
| `ts` | TIMESTAMP | NULLABLE | Timestamp de l'événement |
| `ts_epoch` | INTEGER | NULLABLE | Timestamp epoch de l'événement |
| `ts_event` | TIMESTAMP | NULLABLE | Timestamp spécifique de l'événement |
| `x_mailin_custom` | STRING | NULLABLE | Champs personnalisés X-Mailin |
| `link` | STRING | NULLABLE | URL du lien cliqué (pour les événements de type click) |
| `s_returnpath` | BOOLEAN | NULLABLE | Indicateur de returnpath |
| `spam` | INTEGER | NULLABLE | 1 si événement spam, 0 sinon |
| `opened` | INTEGER | NULLABLE | 1 si événement opened, 0 sinon |
| `click` | INTEGER | NULLABLE | 1 si événement click, 0 sinon |
| `hard_bounce` | INTEGER | NULLABLE | 1 si événement hard_bounce, 0 sinon |
| `soft_bounce` | INTEGER | NULLABLE | 1 si événement soft_bounce, 0 sinon |
| `delivered` | INTEGER | NULLABLE | 1 si événement delivered, 0 sinon |
| `unsubscribe` | INTEGER | NULLABLE | 1 si événement unsubscribe, 0 sinon |
| `contact_deleted` | INTEGER | NULLABLE | 1 si événement contact_deleted, 0 sinon |
| `contact_updated` | INTEGER | NULLABLE | 1 si événement contact_updated, 0 sinon |
| `list_addition` | INTEGER | NULLABLE | 1 si événement list_addition, 0 sinon |
| `retrieved_at` | TIMESTAMP | REQUIRED | Date et heure de récupération des données depuis l'API Brevo |
| `updated_at` | TIMESTAMP | NULLABLE | Date de dernière mise à jour de la ligne |
| `export_process_id` | INTEGER | NULLABLE | ID du process d'export Brevo |

---

### Dataset: `google_Ads_EPBS`

#### Table: `ads_AccountBasicStats_2702575199`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AccountConversionStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AccountNonClickStats_2702575199`

**Nombre de colonnes:** 31


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_content_budget_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_content_impression_share` | FLOAT | NULLABLE | - |
| `metrics_content_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_invalid_click_rate` | FLOAT | NULLABLE | - |
| `metrics_invalid_clicks` | INTEGER | NULLABLE | - |
| `metrics_search_budget_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AccountStats_2702575199`

**Nombre de colonnes:** 34


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdBasicStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_group` | STRING | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_group` | STRING | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_group` | STRING | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdCrossDeviceStats_2702575199`

**Nombre de colonnes:** 38


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_group` | STRING | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_average_page_views` | FLOAT | NULLABLE | - |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | - |
| `metrics_bounce_rate` | FLOAT | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupAdLabel_2702575199`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `label_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_label_ad_group_ad` | STRING | NULLABLE | - |
| `ad_group_ad_label_label` | STRING | NULLABLE | - |
| `ad_group_ad_label_resource_name` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `label_name` | STRING | NULLABLE | - |
| `label_resource_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupAudienceBasicStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_campaign` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupAudienceConversionStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_campaign` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupAudienceNonClickStats_2702575199`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_campaign` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupAudienceStats_2702575199`

**Nombre de colonnes:** 44


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_campaign` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupAudience_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_campaign` | STRING | NULLABLE | - |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_keyword_text` | STRING | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | - |
| `ad_group_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_url_custom_parameters` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupBasicStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupBidModifier_2702575199`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_bid_modifier_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `ad_group_bid_modifier_ad_group` | STRING | NULLABLE | - |
| `ad_group_bid_modifier_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_bid_modifier_bid_modifier` | FLOAT | NULLABLE | - |
| `ad_group_bid_modifier_bid_modifier_source` | STRING | NULLABLE | - |
| `ad_group_bid_modifier_device_type` | STRING | NULLABLE | - |
| `ad_group_bid_modifier_resource_name` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupCriterionLabel_2702575199`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `label_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_label_ad_group_criterion` | STRING | NULLABLE | - |
| `ad_group_criterion_label_label` | STRING | NULLABLE | - |
| `ad_group_criterion_label_resource_name` | STRING | NULLABLE | - |
| `label_name` | STRING | NULLABLE | - |
| `label_resource_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupCriterion_2702575199`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_ad_group` | STRING | NULLABLE | - |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `ad_group_criterion_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_cpv_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_display_name` | STRING | NULLABLE | - |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_type` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupCrossDeviceStats_2702575199`

**Nombre de colonnes:** 51


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_average_page_views` | FLOAT | NULLABLE | - |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | - |
| `metrics_bounce_rate` | FLOAT | NULLABLE | - |
| `metrics_content_impression_share` | FLOAT | NULLABLE | - |
| `metrics_content_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | - |
| `metrics_phone_calls` | INTEGER | NULLABLE | - |
| `metrics_phone_impressions` | INTEGER | NULLABLE | - |
| `metrics_phone_through_rate` | FLOAT | NULLABLE | - |
| `metrics_relative_ctr` | FLOAT | NULLABLE | - |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupLabel_2702575199`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `label_id` | INTEGER | NULLABLE | - |
| `ad_group_label_ad_group` | STRING | NULLABLE | - |
| `ad_group_label_label` | STRING | NULLABLE | - |
| `ad_group_label_resource_name` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `label_name` | STRING | NULLABLE | - |
| `label_resource_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroupStats_2702575199`

**Nombre de colonnes:** 45


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdGroup_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_rotation_mode` | STRING | NULLABLE | - |
| `ad_group_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_cpv_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_display_custom_bid_dimension` | STRING | NULLABLE | - |
| `ad_group_effective_target_cpa_micros` | INTEGER | NULLABLE | - |
| `ad_group_effective_target_cpa_source` | STRING | NULLABLE | - |
| `ad_group_effective_target_roas` | FLOAT | NULLABLE | - |
| `ad_group_effective_target_roas_source` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `ad_group_status` | STRING | NULLABLE | - |
| `ad_group_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_type` | STRING | NULLABLE | - |
| `ad_group_url_custom_parameters` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | - |
| `campaign_manual_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | - |
| `campaign_percent_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AdStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_group` | STRING | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Ad_2702575199`

**Nombre de colonnes:** 79


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_added_by_google_ads` | BOOLEAN | NULLABLE | - |
| `ad_group_ad_ad_app_ad_descriptions` | STRING | NULLABLE | - |
| `ad_group_ad_ad_app_ad_headlines` | STRING | NULLABLE | - |
| `ad_group_ad_ad_app_ad_html5_media_bundles` | STRING | NULLABLE | - |
| `ad_group_ad_ad_app_ad_images` | STRING | NULLABLE | - |
| `ad_group_ad_ad_app_ad_mandatory_ad_text` | STRING | NULLABLE | - |
| `ad_group_ad_ad_app_ad_youtube_videos` | STRING | NULLABLE | - |
| `ad_group_ad_ad_call_ad_phone_number` | STRING | NULLABLE | - |
| `ad_group_ad_ad_device_preference` | STRING | NULLABLE | - |
| `ad_group_ad_ad_display_url` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_dynamic_search_ad_description` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_dynamic_search_ad_description2` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_description` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_description2` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_headline_part1` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_headline_part2` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_headline_part3` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_path1` | STRING | NULLABLE | - |
| `ad_group_ad_ad_expanded_text_ad_path2` | STRING | NULLABLE | - |
| `ad_group_ad_ad_final_app_urls` | STRING | NULLABLE | - |
| `ad_group_ad_ad_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_ad_ad_final_urls` | STRING | NULLABLE | - |
| `ad_group_ad_ad_group` | STRING | NULLABLE | - |
| `ad_group_ad_ad_image_ad_image_url` | STRING | NULLABLE | - |
| `ad_group_ad_ad_image_ad_mime_type` | STRING | NULLABLE | - |
| `ad_group_ad_ad_image_ad_name` | STRING | NULLABLE | - |
| `ad_group_ad_ad_image_ad_pixel_height` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_image_ad_pixel_width` | INTEGER | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_accent_color` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_allow_flexible_color` | BOOLEAN | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_business_name` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_call_to_action_text` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_description` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_format_setting` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_logo_image` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_long_headline` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_main_color` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_marketing_image` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_price_prefix` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_promo_text` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_short_headline` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_square_logo_image` | STRING | NULLABLE | - |
| `ad_group_ad_ad_legacy_responsive_display_ad_square_marketing_image` | STRING | NULLABLE | - |
| `ad_group_ad_ad_name` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_accent_color` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_business_name` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_call_to_action_text` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_descriptions` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_format_setting` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_headlines` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_logo_images` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_long_headline` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_main_color` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_marketing_images` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_price_prefix` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_promo_text` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_square_logo_images` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_square_marketing_images` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_display_ad_youtube_videos` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_search_ad_descriptions` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_search_ad_headlines` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_search_ad_path1` | STRING | NULLABLE | - |
| `ad_group_ad_ad_responsive_search_ad_path2` | STRING | NULLABLE | - |
| `ad_group_ad_ad_strength` | STRING | NULLABLE | - |
| `ad_group_ad_ad_system_managed_resource_source` | STRING | NULLABLE | - |
| `ad_group_ad_ad_text_ad_description1` | STRING | NULLABLE | - |
| `ad_group_ad_ad_text_ad_description2` | STRING | NULLABLE | - |
| `ad_group_ad_ad_text_ad_headline` | STRING | NULLABLE | - |
| `ad_group_ad_ad_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_ad_ad_type` | STRING | NULLABLE | - |
| `ad_group_ad_ad_url_custom_parameters` | STRING | NULLABLE | - |
| `ad_group_ad_policy_summary_approval_status` | STRING | NULLABLE | - |
| `ad_group_ad_status` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AgeRangeBasicStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AgeRangeConversionStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AgeRangeNonClickStats_2702575199`

**Nombre de colonnes:** 26


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AgeRangeStats_2702575199`

**Nombre de colonnes:** 48


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AgeRange_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_criterion_age_range_type` | STRING | NULLABLE | - |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | - |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AssetGroupAsset_2702575199`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_asset_asset` | STRING | NULLABLE | - |
| `asset_group_asset_asset_group` | STRING | NULLABLE | - |
| `asset_group_asset_field_type` | STRING | NULLABLE | - |
| `asset_group_asset_performance_label` | STRING | NULLABLE | - |
| `asset_group_asset_policy_summary_approval_status` | STRING | NULLABLE | - |
| `asset_group_asset_policy_summary_policy_topic_entries` | STRING | NULLABLE | - |
| `asset_group_asset_policy_summary_review_status` | STRING | NULLABLE | - |
| `asset_group_asset_source` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AssetGroupListingGroupFilter_2702575199`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_listing_group_filter_case_value_product_category_category_id` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_id` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_asset_group` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_brand_value` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_category_level` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_channel_channel` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_condition_condition` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_custom_attribute_index` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_custom_attribute_value` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_item_id_value` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_type_level` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_case_value_product_type_value` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_listing_source` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_parent_listing_group_filter` | STRING | NULLABLE | - |
| `asset_group_listing_group_filter_type` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AssetGroupProductGroupStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_product_group_view_asset_group` | STRING | NULLABLE | - |
| `asset_group_product_group_view_asset_group_listing_group_filter` | STRING | NULLABLE | - |
| `asset_group_product_group_view_resource_name` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AssetGroupSignal_2702575199`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_signal_asset_group` | STRING | NULLABLE | - |
| `asset_group_signal_audience_audience` | STRING | NULLABLE | - |
| `asset_group_signal_resource_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_AssetGroup_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_id` | STRING | NULLABLE | - |
| `asset_group_campaign` | STRING | NULLABLE | - |
| `asset_group_final_mobile_urls` | STRING | NULLABLE | - |
| `asset_group_final_urls` | STRING | NULLABLE | - |
| `asset_group_name` | STRING | NULLABLE | - |
| `asset_group_status` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Asset_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_id` | INTEGER | NULLABLE | - |
| `asset_final_urls` | STRING | NULLABLE | - |
| `asset_name` | STRING | NULLABLE | - |
| `asset_source` | STRING | NULLABLE | - |
| `asset_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Audience_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `audience_id` | STRING | NULLABLE | - |
| `audience_description` | STRING | NULLABLE | - |
| `audience_dimensions` | STRING | NULLABLE | - |
| `audience_exclusion_dimension` | STRING | NULLABLE | - |
| `audience_name` | STRING | NULLABLE | - |
| `audience_status` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_BidGoalConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `bidding_strategy_campaign_count` | INTEGER | NULLABLE | - |
| `bidding_strategy_non_removed_campaign_count` | INTEGER | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_BidGoalStats_2702575199`

**Nombre de colonnes:** 26


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `bidding_strategy_campaign_count` | INTEGER | NULLABLE | - |
| `bidding_strategy_non_removed_campaign_count` | INTEGER | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_BidGoal_2702575199`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `bidding_strategy_name` | STRING | NULLABLE | - |
| `bidding_strategy_status` | STRING | NULLABLE | - |
| `bidding_strategy_target_cpa_cpc_bid_ceiling_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_target_cpa_cpc_bid_floor_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_target_cpa_target_cpa_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_target_roas_cpc_bid_ceiling_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_target_roas_cpc_bid_floor_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_target_roas_target_roas` | FLOAT | NULLABLE | - |
| `bidding_strategy_target_spend_cpc_bid_ceiling_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_target_spend_target_spend_micros` | INTEGER | NULLABLE | - |
| `bidding_strategy_type` | STRING | NULLABLE | - |
| `customer_descriptive_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_BudgetStats_2702575199`

**Nombre de colonnes:** 40


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_budget_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_budget_recommended_budget_estimated_change_weekly_clicks` | INTEGER | NULLABLE | - |
| `campaign_budget_recommended_budget_estimated_change_weekly_cost_micros` | INTEGER | NULLABLE | - |
| `campaign_budget_recommended_budget_estimated_change_weekly_interactions` | INTEGER | NULLABLE | - |
| `campaign_budget_recommended_budget_estimated_change_weekly_views` | INTEGER | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Budget_2702575199`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_budget_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_budget_amount_micros` | INTEGER | NULLABLE | - |
| `campaign_budget_delivery_method` | STRING | NULLABLE | - |
| `campaign_budget_explicitly_shared` | BOOLEAN | NULLABLE | - |
| `campaign_budget_has_recommended_budget` | BOOLEAN | NULLABLE | - |
| `campaign_budget_name` | STRING | NULLABLE | - |
| `campaign_budget_period` | STRING | NULLABLE | - |
| `campaign_budget_recommended_budget_amount_micros` | INTEGER | NULLABLE | - |
| `campaign_budget_reference_count` | INTEGER | NULLABLE | - |
| `campaign_budget_status` | STRING | NULLABLE | - |
| `campaign_budget_total_amount_micros` | INTEGER | NULLABLE | - |
| `customer_descriptive_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignAssetStats_2702575199`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_asset_asset` | STRING | NULLABLE | - |
| `campaign_asset_campaign` | STRING | NULLABLE | - |
| `campaign_asset_field_type` | STRING | NULLABLE | - |
| `campaign_asset_resource_name` | STRING | NULLABLE | - |
| `campaign_asset_source` | STRING | NULLABLE | - |
| `campaign_asset_status` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignAudienceBasicStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignAudienceConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignAudienceNonClickStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignAudienceStats_2702575199`

**Nombre de colonnes:** 42


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignAudience_2702575199`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `campaign_criterion_bid_modifier` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignBasicStats_2702575199`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignConversionStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_conversion_attribution_event_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignCookieStats_2702575199`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignCriterion_2702575199`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `campaign_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `campaign_criterion_campaign` | STRING | NULLABLE | - |
| `campaign_criterion_device_type` | STRING | NULLABLE | - |
| `campaign_criterion_display_name` | STRING | NULLABLE | - |
| `campaign_criterion_negative` | BOOLEAN | NULLABLE | - |
| `campaign_criterion_status` | STRING | NULLABLE | - |
| `campaign_criterion_type` | STRING | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_conversion_attribution_event_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignCrossDeviceStats_2702575199`

**Nombre de colonnes:** 54


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_average_page_views` | FLOAT | NULLABLE | - |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | - |
| `metrics_bounce_rate` | FLOAT | NULLABLE | - |
| `metrics_content_budget_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_content_impression_share` | FLOAT | NULLABLE | - |
| `metrics_content_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_invalid_click_rate` | FLOAT | NULLABLE | - |
| `metrics_invalid_clicks` | INTEGER | NULLABLE | - |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | - |
| `metrics_phone_calls` | INTEGER | NULLABLE | - |
| `metrics_phone_impressions` | INTEGER | NULLABLE | - |
| `metrics_phone_through_rate` | FLOAT | NULLABLE | - |
| `metrics_relative_ctr` | FLOAT | NULLABLE | - |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_click_share` | FLOAT | NULLABLE | - |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignLabel_2702575199`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `label_id` | INTEGER | NULLABLE | - |
| `campaign_label_campaign` | STRING | NULLABLE | - |
| `campaign_label_label` | STRING | NULLABLE | - |
| `campaign_label_resource_name` | STRING | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `label_name` | STRING | NULLABLE | - |
| `label_resource_name` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignLocationTargetStats_2702575199`

**Nombre de colonnes:** 38


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_CampaignStats_2702575199`

**Nombre de colonnes:** 43


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Campaign_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `bidding_strategy_name` | STRING | NULLABLE | - |
| `campaign_advertising_channel_sub_type` | STRING | NULLABLE | - |
| `campaign_advertising_channel_type` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | - |
| `campaign_budget_amount_micros` | INTEGER | NULLABLE | - |
| `campaign_budget_explicitly_shared` | BOOLEAN | NULLABLE | - |
| `campaign_budget_has_recommended_budget` | BOOLEAN | NULLABLE | - |
| `campaign_budget_period` | STRING | NULLABLE | - |
| `campaign_budget_recommended_budget_amount_micros` | INTEGER | NULLABLE | - |
| `campaign_budget_total_amount_micros` | INTEGER | NULLABLE | - |
| `campaign_campaign_budget` | STRING | NULLABLE | - |
| `campaign_end_date` | DATE | NULLABLE | - |
| `campaign_experiment_type` | STRING | NULLABLE | - |
| `campaign_manual_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | - |
| `campaign_maximize_conversion_value_target_roas` | FLOAT | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `campaign_percent_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | - |
| `campaign_serving_status` | STRING | NULLABLE | - |
| `campaign_start_date` | DATE | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `campaign_tracking_url_template` | STRING | NULLABLE | - |
| `campaign_url_custom_parameters` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ClickStats_2702575199`

**Nombre de colonnes:** 29


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `click_view_gclid` | STRING | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_status` | STRING | NULLABLE | - |
| `click_view_ad_group_ad` | STRING | NULLABLE | - |
| `click_view_area_of_interest_city` | STRING | NULLABLE | - |
| `click_view_area_of_interest_country` | STRING | NULLABLE | - |
| `click_view_area_of_interest_metro` | STRING | NULLABLE | - |
| `click_view_area_of_interest_most_specific` | STRING | NULLABLE | - |
| `click_view_area_of_interest_region` | STRING | NULLABLE | - |
| `click_view_keyword` | STRING | NULLABLE | - |
| `click_view_keyword_info_match_type` | STRING | NULLABLE | - |
| `click_view_keyword_info_text` | STRING | NULLABLE | - |
| `click_view_location_of_presence_city` | STRING | NULLABLE | - |
| `click_view_location_of_presence_country` | STRING | NULLABLE | - |
| `click_view_location_of_presence_metro` | STRING | NULLABLE | - |
| `click_view_location_of_presence_most_specific` | STRING | NULLABLE | - |
| `click_view_location_of_presence_region` | STRING | NULLABLE | - |
| `click_view_page_number` | INTEGER | NULLABLE | - |
| `customer_descriptive_name` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Customer_2702575199`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `customer_auto_tagging_enabled` | BOOLEAN | NULLABLE | - |
| `customer_currency_code` | STRING | NULLABLE | - |
| `customer_descriptive_name` | STRING | NULLABLE | - |
| `customer_manager` | BOOLEAN | NULLABLE | - |
| `customer_test_account` | BOOLEAN | NULLABLE | - |
| `customer_time_zone` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_DisplayVideoAutomaticPlacementsStats_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `group_placement_view_placement` | STRING | NULLABLE | - |
| `group_placement_view_placement_type` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_DisplayVideoKeywordStats_2702575199`

**Nombre de colonnes:** 28


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_keyword_text` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `campaign_advertising_channel_sub_type` | STRING | NULLABLE | - |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_DisplayVideoTopicStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_topic_path` | STRING | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_GenderBasicStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_GenderConversionStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_GenderNonClickStats_2702575199`

**Nombre de colonnes:** 26


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_GenderStats_2702575199`

**Nombre de colonnes:** 48


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Gender_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_gender_type` | STRING | NULLABLE | - |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | - |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | - |
| `bidding_strategy_name` | STRING | NULLABLE | - |
| `bidding_strategy_type` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_GeoConversionStats_2702575199`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `geographic_view_country_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `ad_group_status` | STRING | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `geographic_view_location_type` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_geo_target_most_specific_location` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_GeoStats_2702575199`

**Nombre de colonnes:** 44


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `geographic_view_country_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `ad_group_status` | STRING | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `geographic_view_location_type` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_geo_target_most_specific_location` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyAccountConversionStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyAccountStats_2702575199`

**Nombre de colonnes:** 35


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyAdGroupConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyAdGroupStats_2702575199`

**Nombre de colonnes:** 39


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyBidGoalStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `bidding_strategy_campaign_count` | INTEGER | NULLABLE | - |
| `bidding_strategy_non_removed_campaign_count` | INTEGER | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyCampaignConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_HourlyCampaignStats_2702575199`

**Nombre de colonnes:** 37


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_hour` | INTEGER | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_KeywordBasicStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_KeywordConversionStats_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_slot` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_KeywordCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_KeywordCrossDeviceStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_average_page_views` | FLOAT | NULLABLE | - |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | - |
| `metrics_bounce_rate` | FLOAT | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | - |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_KeywordStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | - |
| `metrics_current_model_attributed_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Keyword_2702575199`

**Nombre de colonnes:** 34


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_approval_status` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_final_url_suffix` | STRING | NULLABLE | - |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_keyword_match_type` | STRING | NULLABLE | - |
| `ad_group_criterion_keyword_text` | STRING | NULLABLE | - |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | - |
| `ad_group_criterion_position_estimates_estimated_add_clicks_at_first_position_cpc` | INTEGER | NULLABLE | - |
| `ad_group_criterion_position_estimates_estimated_add_cost_at_first_position_cpc` | INTEGER | NULLABLE | - |
| `ad_group_criterion_position_estimates_first_page_cpc_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_position_estimates_first_position_cpc_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_position_estimates_top_of_page_cpc_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_quality_info_creative_quality_score` | STRING | NULLABLE | - |
| `ad_group_criterion_quality_info_post_click_quality_score` | STRING | NULLABLE | - |
| `ad_group_criterion_quality_info_quality_score` | INTEGER | NULLABLE | - |
| `ad_group_criterion_quality_info_search_predicted_ctr` | STRING | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_system_serving_status` | STRING | NULLABLE | - |
| `ad_group_criterion_topic_topic_constant` | STRING | NULLABLE | - |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | - |
| `campaign_manual_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | - |
| `campaign_percent_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_LandingPageStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `ad_group_status` | STRING | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `landing_page_view_unexpanded_final_url` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_mobile_friendly_clicks_percentage` | FLOAT | NULLABLE | - |
| `metrics_speed_score` | INTEGER | NULLABLE | - |
| `metrics_valid_accelerated_mobile_pages_clicks_percentage` | FLOAT | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_LocationBasedCampaignCriterion_2702575199`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `campaign_criterion_negative` | BOOLEAN | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_LocationsDistanceStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `distance_view_distance_bucket` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_LocationsUserLocationsStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `user_location_view_country_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `ad_group_status` | STRING | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_geo_target_most_specific_location` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `user_location_view_targeting_location` | BOOLEAN | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_PaidOrganicStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_combined_clicks` | INTEGER | NULLABLE | - |
| `metrics_combined_clicks_per_query` | FLOAT | NULLABLE | - |
| `metrics_combined_queries` | INTEGER | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_organic_clicks` | INTEGER | NULLABLE | - |
| `metrics_organic_clicks_per_query` | FLOAT | NULLABLE | - |
| `metrics_organic_impressions` | INTEGER | NULLABLE | - |
| `metrics_organic_impressions_per_query` | FLOAT | NULLABLE | - |
| `metrics_organic_queries` | INTEGER | NULLABLE | - |
| `paid_organic_search_term_view_search_term` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_search_engine_results_page_type` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ParentalStatusBasicStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ParentalStatusConversionStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ParentalStatusNonClickStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ParentalStatusStats_2702575199`

**Nombre de colonnes:** 48


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ParentalStatus_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | - |
| `ad_group_criterion_parental_status_type` | STRING | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | - |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_PlacementBasicStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_PlacementConversionStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_PlacementNonClickStats_2702575199`

**Nombre de colonnes:** 26


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_PlacementStats_2702575199`

**Nombre de colonnes:** 47


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | - |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | - |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | - |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | - |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | - |
| `metrics_gmail_saves` | INTEGER | NULLABLE | - |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Placement_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `ad_group_base_ad_group` | STRING | NULLABLE | - |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | - |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | - |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | - |
| `ad_group_criterion_placement_url` | STRING | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | - |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | - |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | - |
| `bidding_strategy_name` | STRING | NULLABLE | - |
| `bidding_strategy_type` | STRING | NULLABLE | - |
| `campaign_base_campaign` | STRING | NULLABLE | - |
| `campaign_bidding_strategy` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ProductGroupStats_2702575199`

**Nombre de colonnes:** 32


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_category_category_id` | STRING | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `ad_group_criterion_cpc_bid_micros` | INTEGER | NULLABLE | - |
| `ad_group_criterion_display_name` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_brand_value` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_category_level` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_channel_channel` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_channel_exclusivity_channel_exclusivity` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_condition_condition` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_custom_attribute_index` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_custom_attribute_value` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_item_id_value` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_type_level` | STRING | NULLABLE | - |
| `ad_group_criterion_listing_group_case_value_product_type_value` | STRING | NULLABLE | - |
| `ad_group_criterion_status` | STRING | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `product_group_view_resource_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_SearchQueryConversionStats_2702575199`

**Nombre de colonnes:** 29


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `search_term_view_search_term` | STRING | NULLABLE | - |
| `search_term_view_status` | STRING | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_keyword_ad_group_criterion` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_search_term_match_type` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_SearchQueryStats_2702575199`

**Nombre de colonnes:** 52


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cost` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_average_cpe` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_interaction_event_types` | STRING | NULLABLE | - |
| `metrics_interaction_rate` | FLOAT | NULLABLE | - |
| `metrics_interactions` | INTEGER | NULLABLE | - |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `search_term_view_search_term` | STRING | NULLABLE | - |
| `search_term_view_status` | STRING | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_keyword_ad_group_criterion` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_search_term_match_type` | STRING | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ShoppingProductConversionStats_2702575199`

**Nombre de colonnes:** 48


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `segments_product_aggregator_id` | INTEGER | NULLABLE | - |
| `segments_product_item_id` | STRING | NULLABLE | - |
| `segments_product_merchant_id` | INTEGER | NULLABLE | - |
| `segments_product_store_id` | STRING | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_product_brand` | STRING | NULLABLE | - |
| `segments_product_category_level1` | STRING | NULLABLE | - |
| `segments_product_category_level2` | STRING | NULLABLE | - |
| `segments_product_category_level3` | STRING | NULLABLE | - |
| `segments_product_category_level4` | STRING | NULLABLE | - |
| `segments_product_category_level5` | STRING | NULLABLE | - |
| `segments_product_channel` | STRING | NULLABLE | - |
| `segments_product_channel_exclusivity` | STRING | NULLABLE | - |
| `segments_product_condition` | STRING | NULLABLE | - |
| `segments_product_country` | STRING | NULLABLE | - |
| `segments_product_custom_attribute0` | STRING | NULLABLE | - |
| `segments_product_custom_attribute1` | STRING | NULLABLE | - |
| `segments_product_custom_attribute2` | STRING | NULLABLE | - |
| `segments_product_custom_attribute3` | STRING | NULLABLE | - |
| `segments_product_custom_attribute4` | STRING | NULLABLE | - |
| `segments_product_language` | STRING | NULLABLE | - |
| `segments_product_type_l1` | STRING | NULLABLE | - |
| `segments_product_type_l2` | STRING | NULLABLE | - |
| `segments_product_type_l3` | STRING | NULLABLE | - |
| `segments_product_type_l4` | STRING | NULLABLE | - |
| `segments_product_type_l5` | STRING | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_ShoppingProductStats_2702575199`

**Nombre de colonnes:** 57


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `segments_product_aggregator_id` | INTEGER | NULLABLE | - |
| `segments_product_item_id` | STRING | NULLABLE | - |
| `segments_product_merchant_id` | INTEGER | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpc` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | - |
| `metrics_search_click_share` | FLOAT | NULLABLE | - |
| `metrics_search_impression_share` | FLOAT | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_product_brand` | STRING | NULLABLE | - |
| `segments_product_category_level1` | STRING | NULLABLE | - |
| `segments_product_category_level2` | STRING | NULLABLE | - |
| `segments_product_category_level3` | STRING | NULLABLE | - |
| `segments_product_category_level4` | STRING | NULLABLE | - |
| `segments_product_category_level5` | STRING | NULLABLE | - |
| `segments_product_channel` | STRING | NULLABLE | - |
| `segments_product_channel_exclusivity` | STRING | NULLABLE | - |
| `segments_product_condition` | STRING | NULLABLE | - |
| `segments_product_country` | STRING | NULLABLE | - |
| `segments_product_custom_attribute0` | STRING | NULLABLE | - |
| `segments_product_custom_attribute1` | STRING | NULLABLE | - |
| `segments_product_custom_attribute2` | STRING | NULLABLE | - |
| `segments_product_custom_attribute3` | STRING | NULLABLE | - |
| `segments_product_custom_attribute4` | STRING | NULLABLE | - |
| `segments_product_language` | STRING | NULLABLE | - |
| `segments_product_type_l1` | STRING | NULLABLE | - |
| `segments_product_type_l2` | STRING | NULLABLE | - |
| `segments_product_type_l3` | STRING | NULLABLE | - |
| `segments_product_type_l4` | STRING | NULLABLE | - |
| `segments_product_type_l5` | STRING | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_VideoBasicStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `video_channel_id` | STRING | NULLABLE | - |
| `video_id` | STRING | NULLABLE | - |
| `ad_group_ad_status` | STRING | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_VideoConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `video_channel_id` | STRING | NULLABLE | - |
| `video_id` | STRING | NULLABLE | - |
| `ad_group_ad_status` | STRING | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_conversion_action` | STRING | NULLABLE | - |
| `segments_conversion_action_category` | STRING | NULLABLE | - |
| `segments_conversion_action_name` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_VideoNonClickStats_2702575199`

**Nombre de colonnes:** 32


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `video_channel_id` | STRING | NULLABLE | - |
| `video_id` | STRING | NULLABLE | - |
| `ad_group_ad_status` | STRING | NULLABLE | - |
| `metrics_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_average_cpv` | FLOAT | NULLABLE | - |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | - |
| `metrics_engagement_rate` | FLOAT | NULLABLE | - |
| `metrics_engagements` | INTEGER | NULLABLE | - |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | - |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | - |
| `metrics_video_view_rate` | FLOAT | NULLABLE | - |
| `metrics_video_views` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_VideoStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `video_channel_id` | STRING | NULLABLE | - |
| `video_id` | STRING | NULLABLE | - |
| `ad_group_ad_status` | STRING | NULLABLE | - |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | - |
| `metrics_average_cpm` | FLOAT | NULLABLE | - |
| `metrics_clicks` | INTEGER | NULLABLE | - |
| `metrics_conversions` | FLOAT | NULLABLE | - |
| `metrics_conversions_value` | FLOAT | NULLABLE | - |
| `metrics_cost_micros` | INTEGER | NULLABLE | - |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | - |
| `metrics_ctr` | FLOAT | NULLABLE | - |
| `metrics_impressions` | INTEGER | NULLABLE | - |
| `segments_ad_network_type` | STRING | NULLABLE | - |
| `segments_click_type` | STRING | NULLABLE | - |
| `segments_date` | DATE | NULLABLE | - |
| `segments_day_of_week` | STRING | NULLABLE | - |
| `segments_device` | STRING | NULLABLE | - |
| `segments_month` | DATE | NULLABLE | - |
| `segments_quarter` | DATE | NULLABLE | - |
| `segments_week` | DATE | NULLABLE | - |
| `segments_year` | INTEGER | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `ads_Video_2702575199`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `customer_id` | INTEGER | NULLABLE | - |
| `video_id` | STRING | NULLABLE | - |
| `ad_group_ad_status` | STRING | NULLABLE | - |
| `video_duration_millis` | INTEGER | NULLABLE | - |
| `video_title` | STRING | NULLABLE | - |
| `_LATEST_DATE` | DATE | NULLABLE | - |
| `_DATA_DATE` | DATE | NULLABLE | - |

#### Table: `google_Ads_EPBS`

**Nombre de colonnes:** 0


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|

#### Table: `p_ads_AccountBasicStats_2702575199`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_AccountConversionStats_2702575199`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AccountNonClickStats_2702575199`

**Nombre de colonnes:** 29


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_content_budget_lost_impression_share` | FLOAT | NULLABLE | The estimated percent of times that your ad was eligible to show on the Display Network but didn't because your budget was too low. Note: Content budget lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_content_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Display Network divided by the estimated number of impressions you were eligible to receive. Note: Content impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_content_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Display Network that your ads didn't receive due to poor Ad Rank. Note: Content rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_invalid_click_rate` | FLOAT | NULLABLE | The percentage of clicks filtered out of your total number of clicks (filtered + non-filtered clicks) during the reporting period. |
| `metrics_invalid_clicks` | INTEGER | NULLABLE | Number of clicks Google considers illegitimate and doesn't charge you for. |
| `metrics_search_budget_lost_impression_share` | FLOAT | NULLABLE | The estimated percent of times that your ad was eligible to show on the Search Network but didn't because your budget was too low. Note: Search budget lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | The impressions you've received divided by the estimated number of impressions you were eligible to receive on the Search Network for search terms that matched your keywords exactly (or were close variants of your keyword), regardless of your keyword match types. Note: Search exact match impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Search Network divided by the estimated number of impressions you were eligible to receive. Note: Search impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Search Network that your ads didn't receive due to poor Ad Rank. Note: Search rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AccountStats_2702575199`

**Nombre de colonnes:** 32


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdBasicStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | Output only. The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_ad_group` | STRING | NULLABLE | The ad group to which the ad belongs. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_AdConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | Output only. The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_ad_group` | STRING | NULLABLE | The ad group to which the ad belongs. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | Output only. The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_ad_group` | STRING | NULLABLE | The ad group to which the ad belongs. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdCrossDeviceStats_2702575199`

**Nombre de colonnes:** 36


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | Output only. The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_ad_group` | STRING | NULLABLE | The ad group to which the ad belongs. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_average_page_views` | FLOAT | NULLABLE | Average number of pages viewed per session. |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | Total duration of all sessions (in seconds) / number of sessions. Imported from Google Analytics. |
| `metrics_bounce_rate` | FLOAT | NULLABLE | Percentage of clicks where the user only visited a single page on your site. Imported from Google Analytics. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | Percentage of first-time sessions (from people who had never visited your site before). Imported from Google Analytics. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown anywhere above the organic search results. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupAdLabel_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `label_id` | INTEGER | NULLABLE | Id of the label. Read only. |
| `ad_group_ad_label_ad_group_ad` | STRING | NULLABLE | The ad group ad to which the label is attached. |
| `ad_group_ad_label_label` | STRING | NULLABLE | The label assigned to the ad group ad. |
| `ad_group_ad_label_resource_name` | STRING | NULLABLE | The resource name of the ad group ad label. Ad group ad label resource names have the form: `customers/{customer_id}/adGroupAdLabels/{ad_group_id}~{ad_id}~{label_id}` |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `label_name` | STRING | NULLABLE | The name of the label. This field is required and should not be empty when creating a new label. The length of this string should be between 1 and 80, inclusive. |
| `label_resource_name` | STRING | NULLABLE | Name of the resource. Label resource names have the form: `customers/{customer_id}/labels/{label_id}` |

#### Table: `p_ads_AdGroupAudienceBasicStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_campaign` | STRING | NULLABLE | The campaign to which the ad group belongs. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_AdGroupAudienceConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_campaign` | STRING | NULLABLE | The campaign to which the ad group belongs. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupAudienceNonClickStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_campaign` | STRING | NULLABLE | The campaign to which the ad group belongs. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupAudienceStats_2702575199`

**Nombre de colonnes:** 42


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_campaign` | STRING | NULLABLE | The campaign to which the ad group belongs. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupAudience_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_campaign` | STRING | NULLABLE | The campaign to which the ad group belongs. |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | The effective CPC (cost-per-click) bid. |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | Source of the effective CPC bid. |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | The effective CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | Source of the effective CPM bid. |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects. |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_criterion_keyword_text` | STRING | NULLABLE | The text of the keyword (at most 80 characters and 10 words). |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | The per-targeting-dimension setting to restrict the reach of your campaign or ad group. |
| `ad_group_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |

#### Table: `p_ads_AdGroupBasicStats_2702575199`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_AdGroupBidModifier_2702575199`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_bid_modifier_criterion_id` | INTEGER | NULLABLE | The ID of the criterion to bid modify. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `ad_group_bid_modifier_ad_group` | STRING | NULLABLE | The ad group to which this criterion belongs. |
| `ad_group_bid_modifier_base_ad_group` | STRING | NULLABLE | The base ad group from which this draft/trial adgroup bid modifier was created. If ad_group is a base ad group then this field will be equal to ad_group. If the ad group was created in the draft or trial and has no corresponding base ad group, then this field will be null. This field is readonly. |
| `ad_group_bid_modifier_bid_modifier` | FLOAT | NULLABLE | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. The range is 1.0 - 6.0 for PreferredContent. Use 0 to opt out of a Device type. |
| `ad_group_bid_modifier_bid_modifier_source` | STRING | NULLABLE | Bid modifier source. |
| `ad_group_bid_modifier_device_type` | STRING | NULLABLE | Type of the device. |
| `ad_group_bid_modifier_resource_name` | STRING | NULLABLE | The resource name of the ad group bid modifier. Ad group bid modifier resource names have the form: `customers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}` |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |

#### Table: `p_ads_AdGroupConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupCriterionLabel_2702575199`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `label_id` | INTEGER | NULLABLE | Id of the label. Read only. |
| `ad_group_criterion_label_ad_group_criterion` | STRING | NULLABLE | The ad group criterion to which the label is attached. |
| `ad_group_criterion_label_label` | STRING | NULLABLE | The label assigned to the ad group criterion. |
| `ad_group_criterion_label_resource_name` | STRING | NULLABLE | The resource name of the ad group criterion label. Ad group criterion label resource names have the form: `customers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{label_id}` |
| `label_name` | STRING | NULLABLE | The name of the label. This field is required and should not be empty when creating a new label. The length of this string should be between 1 and 80, inclusive. |
| `label_resource_name` | STRING | NULLABLE | Name of the resource. Label resource names have the form: `customers/{customer_id}/labels/{label_id}` |

#### Table: `p_ads_AdGroupCriterion_2702575199`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `ad_group_criterion_ad_group` | STRING | NULLABLE | The ad group to which the criterion belongs. |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. |
| `ad_group_criterion_cpc_bid_micros` | INTEGER | NULLABLE | The CPC (cost-per-click) bid. |
| `ad_group_criterion_cpm_bid_micros` | INTEGER | NULLABLE | The CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_cpv_bid_micros` | INTEGER | NULLABLE | The CPC (cost-per-view) bid. |
| `ad_group_criterion_display_name` | STRING | NULLABLE | The display name of the criterion. This field is ignored for mutates. |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_type` | STRING | NULLABLE | The type of the criterion. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |

#### Table: `p_ads_AdGroupCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupCrossDeviceStats_2702575199`

**Nombre de colonnes:** 49


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_average_page_views` | FLOAT | NULLABLE | Average number of pages viewed per session. |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | Total duration of all sessions (in seconds) / number of sessions. Imported from Google Analytics. |
| `metrics_bounce_rate` | FLOAT | NULLABLE | Percentage of clicks where the user only visited a single page on your site. Imported from Google Analytics. |
| `metrics_content_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Display Network divided by the estimated number of impressions you were eligible to receive. Note: Content impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_content_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Display Network that your ads didn't receive due to poor Ad Rank. Note: Content rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | Percentage of first-time sessions (from people who had never visited your site before). Imported from Google Analytics. |
| `metrics_phone_calls` | INTEGER | NULLABLE | Number of offline phone calls. |
| `metrics_phone_impressions` | INTEGER | NULLABLE | Number of offline phone impressions. |
| `metrics_phone_through_rate` | FLOAT | NULLABLE | Number of phone calls received (phone_calls) divided by the number of times your phone number is shown (phone_impressions). |
| `metrics_relative_ctr` | FLOAT | NULLABLE | Your clickthrough rate (Ctr) divided by the average clickthrough rate of all advertisers on the websites that show your ads. Measures how your ads perform on Display Network sites compared to other ads on the same sites. |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | The percentage of the customer's Shopping or Search ad impressions that are shown in the most prominent Shopping position. See https://support.google.com/google-ads/answer/7501826 for details. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to a low budget. Note: Search budget lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to a low budget. Note: Search budget lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | The impressions you've received divided by the estimated number of impressions you were eligible to receive on the Search Network for search terms that matched your keywords exactly (or were close variants of your keyword), regardless of your keyword match types. Note: Search exact match impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Search Network divided by the estimated number of impressions you were eligible to receive. Note: Search impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to poor Ad Rank. Note: Search rank lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Search Network that your ads didn't receive due to poor Ad Rank. Note: Search rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to poor Ad Rank. Note: Search rank lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | The impressions you've received in the top location (anywhere above the organic search results) compared to the estimated number of impressions you were eligible to receive in the top location. Note: Search top impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown anywhere above the organic search results. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroupLabel_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `label_id` | INTEGER | NULLABLE | Id of the label. Read only. |
| `ad_group_label_ad_group` | STRING | NULLABLE | The ad group to which the label is attached. |
| `ad_group_label_label` | STRING | NULLABLE | The label assigned to the ad group. |
| `ad_group_label_resource_name` | STRING | NULLABLE | The resource name of the ad group label. Ad group label resource names have the form: `customers/{customer_id}/adGroupLabels/{ad_group_id}~{label_id}` |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `label_name` | STRING | NULLABLE | The name of the label. This field is required and should not be empty when creating a new label. The length of this string should be between 1 and 80, inclusive. |
| `label_resource_name` | STRING | NULLABLE | Name of the resource. Label resource names have the form: `customers/{customer_id}/labels/{label_id}` |

#### Table: `p_ads_AdGroupStats_2702575199`

**Nombre de colonnes:** 43


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | Shows how your historic conversions data would look under the attribution model you've currently selected. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_current_model_attributed_conversions_value` | FLOAT | NULLABLE | The total value of current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The value of current model attributed conversions divided by the number of the conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AdGroup_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_rotation_mode` | STRING | NULLABLE | The ad rotation mode of the ad group. |
| `ad_group_cpc_bid_micros` | INTEGER | NULLABLE | The maximum CPC (cost-per-click) bid. |
| `ad_group_cpm_bid_micros` | INTEGER | NULLABLE | The maximum CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_cpv_bid_micros` | INTEGER | NULLABLE | The CPV (cost-per-view) bid. |
| `ad_group_display_custom_bid_dimension` | STRING | NULLABLE | Allows advertisers to specify a targeting dimension on which to place absolute bids. This is only applicable for campaigns that target only the display network and not search. |
| `ad_group_effective_target_cpa_micros` | INTEGER | NULLABLE | The effective target CPA (cost-per-acquisition). This field is read-only. |
| `ad_group_effective_target_cpa_source` | STRING | NULLABLE | Source of the effective target CPA. This field is read-only. |
| `ad_group_effective_target_roas` | FLOAT | NULLABLE | The effective target ROAS (return-on-ad-spend). This field is read-only. |
| `ad_group_effective_target_roas_source` | STRING | NULLABLE | Source of the effective target ROAS. This field is read-only. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `ad_group_status` | STRING | NULLABLE | The status of the ad group. |
| `ad_group_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_type` | STRING | NULLABLE | The type of the ad group. |
| `ad_group_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the `bidding_strategy` field to create a portfolio bidding strategy. This field is read-only. |
| `campaign_manual_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | Whether bids are to be enhanced based on conversion optimizer data. |
| `campaign_percent_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | Adjusts the bid for each auction upward or downward, depending on the likelihood of a conversion. Individual bids may exceed cpc_bid_ceiling_micros, but the average bid amount for a campaign should not. |

#### Table: `p_ads_AdStats_2702575199`

**Nombre de colonnes:** 44


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | Output only. The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_ad_group` | STRING | NULLABLE | The ad group to which the ad belongs. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | Shows how your historic conversions data would look under the attribution model you've currently selected. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The value of current model attributed conversions divided by the number of the conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_Ad_2702575199`

**Nombre de colonnes:** 77


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | Output only. The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_ad_ad_added_by_google_ads` | BOOLEAN | NULLABLE | Indicates if this ad was automatically added by Google Ads and not by a user. For example, this could happen when ads are automatically created as suggestions for new ads based on knowledge of how existing ads are performing. |
| `ad_group_ad_ad_app_ad_descriptions` | STRING | NULLABLE | List of text assets for descriptions. When the ad serves the descriptions will be selected from this list. |
| `ad_group_ad_ad_app_ad_headlines` | STRING | NULLABLE | List of text assets for headlines. When the ad serves the headlines will be selected from this list. |
| `ad_group_ad_ad_app_ad_html5_media_bundles` | STRING | NULLABLE | List of media bundle assets that may be used with the ad. |
| `ad_group_ad_ad_app_ad_images` | STRING | NULLABLE | List of image assets that may be displayed with the ad. |
| `ad_group_ad_ad_app_ad_mandatory_ad_text` | STRING | NULLABLE | An optional text asset that, if specified, must always be displayed when the ad is served. |
| `ad_group_ad_ad_app_ad_youtube_videos` | STRING | NULLABLE | List of YouTube video assets that may be displayed with the ad. |
| `ad_group_ad_ad_call_ad_phone_number` | STRING | NULLABLE | The phone number in the ad. |
| `ad_group_ad_ad_device_preference` | STRING | NULLABLE | The device preference for the ad. You can only specify a preference for mobile devices. When this preference is set the ad will be preferred over other ads when being displayed on a mobile device. The ad can still be displayed on other device types, e.g. if no other ads are available. If unspecified (no device preference), all devices are targeted. This is only supported by some ad types. |
| `ad_group_ad_ad_display_url` | STRING | NULLABLE | The URL that appears in the ad description for some ad formats. |
| `ad_group_ad_ad_expanded_dynamic_search_ad_description` | STRING | NULLABLE | The description of the ad. |
| `ad_group_ad_ad_expanded_dynamic_search_ad_description2` | STRING | NULLABLE | The second description of the ad. |
| `ad_group_ad_ad_expanded_text_ad_description` | STRING | NULLABLE | The description of the ad. |
| `ad_group_ad_ad_expanded_text_ad_description2` | STRING | NULLABLE | The second description of the ad. |
| `ad_group_ad_ad_expanded_text_ad_headline_part1` | STRING | NULLABLE | The first part of the ad's headline. |
| `ad_group_ad_ad_expanded_text_ad_headline_part2` | STRING | NULLABLE | The second part of the ad's headline. |
| `ad_group_ad_ad_expanded_text_ad_headline_part3` | STRING | NULLABLE | The third part of the ad's headline. |
| `ad_group_ad_ad_expanded_text_ad_path1` | STRING | NULLABLE | The text that can appear alongside the ad's displayed URL. |
| `ad_group_ad_ad_expanded_text_ad_path2` | STRING | NULLABLE | Additional text that can appear alongside the ad's displayed URL. |
| `ad_group_ad_ad_final_app_urls` | STRING | NULLABLE | A list of final app URLs that will be used on mobile if the user has the specific app installed. |
| `ad_group_ad_ad_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects for the ad. |
| `ad_group_ad_ad_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_ad_ad_group` | STRING | NULLABLE | The ad group to which the ad belongs. |
| `ad_group_ad_ad_image_ad_image_url` | STRING | NULLABLE | URL of the full size image. |
| `ad_group_ad_ad_image_ad_mime_type` | STRING | NULLABLE | The mime type of the image. |
| `ad_group_ad_ad_image_ad_name` | STRING | NULLABLE | The name of the image. If the image was created from a MediaFile, this is the MediaFile's name. If the image was created from bytes, this is empty. |
| `ad_group_ad_ad_image_ad_pixel_height` | INTEGER | NULLABLE | Height in pixels of the full size image. |
| `ad_group_ad_ad_image_ad_pixel_width` | INTEGER | NULLABLE | Width in pixels of the full size image. |
| `ad_group_ad_ad_legacy_responsive_display_ad_accent_color` | STRING | NULLABLE | The accent color of the ad in hexadecimal, e.g. #ffffff for white. If one of main_color and accent_color is set, the other is required as well. |
| `ad_group_ad_ad_legacy_responsive_display_ad_allow_flexible_color` | BOOLEAN | NULLABLE | Advertiser's consent to allow flexible color. When true, the ad may be served with different color if necessary. When false, the ad will be served with the specified colors or a neutral color. The default value is true. Must be true if main_color and accent_color are not set. |
| `ad_group_ad_ad_legacy_responsive_display_ad_business_name` | STRING | NULLABLE | The business name in the ad. |
| `ad_group_ad_ad_legacy_responsive_display_ad_call_to_action_text` | STRING | NULLABLE | The call-to-action text for the ad. |
| `ad_group_ad_ad_legacy_responsive_display_ad_description` | STRING | NULLABLE | The description of the ad. |
| `ad_group_ad_ad_legacy_responsive_display_ad_format_setting` | STRING | NULLABLE | Specifies which format the ad will be served in. Default is ALL_FORMATS. |
| `ad_group_ad_ad_legacy_responsive_display_ad_logo_image` | STRING | NULLABLE | The MediaFile resource name of the logo image used in the ad. |
| `ad_group_ad_ad_legacy_responsive_display_ad_long_headline` | STRING | NULLABLE | The long version of the ad's headline. |
| `ad_group_ad_ad_legacy_responsive_display_ad_main_color` | STRING | NULLABLE | The main color of the ad in hexadecimal, e.g. #ffffff for white. If one of main_color and accent_color is set, the other is required as well. |
| `ad_group_ad_ad_legacy_responsive_display_ad_marketing_image` | STRING | NULLABLE | The MediaFile resource name of the marketing image used in the ad. |
| `ad_group_ad_ad_legacy_responsive_display_ad_price_prefix` | STRING | NULLABLE | Prefix before price. E.g. 'as low as'. |
| `ad_group_ad_ad_legacy_responsive_display_ad_promo_text` | STRING | NULLABLE | Promotion text used for dynamic formats of responsive ads. For example 'Free two-day shipping'. |
| `ad_group_ad_ad_legacy_responsive_display_ad_short_headline` | STRING | NULLABLE | The short version of the ad's headline. |
| `ad_group_ad_ad_legacy_responsive_display_ad_square_logo_image` | STRING | NULLABLE | The MediaFile resource name of the square logo image used in the ad. |
| `ad_group_ad_ad_legacy_responsive_display_ad_square_marketing_image` | STRING | NULLABLE | The MediaFile resource name of the square marketing image used in the ad. |
| `ad_group_ad_ad_name` | STRING | NULLABLE | Immutable. The name of the ad. This is only used to be able to identify the ad. It does not need to be unique and does not affect the served ad. The name field is currently only supported for DisplayUploadAd, ImageAd, ShoppingComparisonListingAd and VideoAd. |
| `ad_group_ad_ad_responsive_display_ad_accent_color` | STRING | NULLABLE | The accent color of the ad in hexadecimal, e.g. #ffffff for white. If one of main_color and accent_color is set, the other is required as well. |
| `ad_group_ad_ad_responsive_display_ad_business_name` | STRING | NULLABLE | The advertiser/brand name. Maximum display width is 25. |
| `ad_group_ad_ad_responsive_display_ad_call_to_action_text` | STRING | NULLABLE | The call-to-action text for the ad. Maximum display width is 30. |
| `ad_group_ad_ad_responsive_display_ad_descriptions` | STRING | NULLABLE | Descriptive texts for the ad. The maximum length is 90 characters. At least 1 and max 5 headlines can be specified. |
| `ad_group_ad_ad_responsive_display_ad_format_setting` | STRING | NULLABLE | Specifies which format the ad will be served in. Default is ALL_FORMATS. |
| `ad_group_ad_ad_responsive_display_ad_headlines` | STRING | NULLABLE | Short format headlines for the ad. The maximum length is 30 characters. At least 1 and max 5 headlines can be specified. |
| `ad_group_ad_ad_responsive_display_ad_logo_images` | STRING | NULLABLE | Logo images to be used in the ad. Valid image types are GIF, JPEG, and PNG. The minimum size is 512x128 and the aspect ratio must be 4:1 (+-1%). Combined with square_logo_images the maximum is 5. |
| `ad_group_ad_ad_responsive_display_ad_long_headline` | STRING | NULLABLE | A required long format headline. The maximum length is 90 characters. |
| `ad_group_ad_ad_responsive_display_ad_main_color` | STRING | NULLABLE | The main color of the ad in hexadecimal, e.g. #ffffff for white. If one of main_color and accent_color is set, the other is required as well. |
| `ad_group_ad_ad_responsive_display_ad_marketing_images` | STRING | NULLABLE | Marketing images to be used in the ad. Valid image types are GIF, JPEG, and PNG. The minimum size is 600x314 and the aspect ratio must be 1.91:1 (+-1%). At least one marketing_image is required. Combined with square_marketing_images the maximum is 15. |
| `ad_group_ad_ad_responsive_display_ad_price_prefix` | STRING | NULLABLE | Prefix before price. E.g. 'as low as'. |
| `ad_group_ad_ad_responsive_display_ad_promo_text` | STRING | NULLABLE | Promotion text used for dynamic formats of responsive ads. For example 'Free two-day shipping'. |
| `ad_group_ad_ad_responsive_display_ad_square_logo_images` | STRING | NULLABLE | Square logo images to be used in the ad. Valid image types are GIF, JPEG, and PNG. The minimum size is 128x128 and the aspect ratio must be 1:1 (+-1%). Combined with square_logo_images the maximum is 5. |
| `ad_group_ad_ad_responsive_display_ad_square_marketing_images` | STRING | NULLABLE | Square marketing images to be used in the ad. Valid image types are GIF, JPEG, and PNG. The minimum size is 300x300 and the aspect ratio must be 1:1 (+-1%). At least one square marketing_image is required. Combined with marketing_images the maximum is 15. |
| `ad_group_ad_ad_responsive_display_ad_youtube_videos` | STRING | NULLABLE | Optional YouTube videos for the ad. A maximum of 5 videos can be specified. |
| `ad_group_ad_ad_responsive_search_ad_descriptions` | STRING | NULLABLE | List of text assets for descriptions. When the ad serves the descriptions will be selected from this list. |
| `ad_group_ad_ad_responsive_search_ad_headlines` | STRING | NULLABLE | List of text assets for headlines. When the ad serves the headlines will be selected from this list. |
| `ad_group_ad_ad_responsive_search_ad_path1` | STRING | NULLABLE | First part of text that may appear appended to the url displayed in the ad. |
| `ad_group_ad_ad_responsive_search_ad_path2` | STRING | NULLABLE | Second part of text that may appear appended to the url displayed in the ad. This field can only be set when path1 is also set. |
| `ad_group_ad_ad_strength` | STRING | NULLABLE | Overall ad strength for this ad group ad. |
| `ad_group_ad_ad_system_managed_resource_source` | STRING | NULLABLE | If this ad is system managed, then this field will indicate the source. This field is read-only. |
| `ad_group_ad_ad_text_ad_description1` | STRING | NULLABLE | The first line of the ad's description. |
| `ad_group_ad_ad_text_ad_description2` | STRING | NULLABLE | The second line of the ad's description. |
| `ad_group_ad_ad_text_ad_headline` | STRING | NULLABLE | The headline of the ad. |
| `ad_group_ad_ad_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_ad_ad_type` | STRING | NULLABLE | The type of ad. |
| `ad_group_ad_ad_url_custom_parameters` | STRING | NULLABLE | The list of mappings that can be used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. For mutates, please use url custom parameter operations. |
| `ad_group_ad_policy_summary_approval_status` | STRING | NULLABLE | Output only. The overall approval status of this ad, calculated based on the status of its individual policy topic entries. |
| `ad_group_ad_status` | STRING | NULLABLE | The status of the ad. |

#### Table: `p_ads_AgeRangeBasicStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |

#### Table: `p_ads_AgeRangeConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AgeRangeNonClickStats_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AgeRangeStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AgeRange_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_criterion_age_range_type` | STRING | NULLABLE | Type of the age range. |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | The effective CPC (cost-per-click) bid. |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | Source of the effective CPC bid. |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | The effective CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | Source of the effective CPM bid. |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects. |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | The per-targeting-dimension setting to restrict the reach of your campaign or ad group. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the `bidding_strategy` field to create a portfolio bidding strategy. This field is read-only. |

#### Table: `p_ads_AssetGroupAsset_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_asset_asset` | STRING | NULLABLE | The asset which this asset group asset is linking. |
| `asset_group_asset_asset_group` | STRING | NULLABLE | The asset group which this asset group asset is linking. |
| `asset_group_asset_field_type` | STRING | NULLABLE | The description of the placement of the asset within the asset group. For example: HEADLINE, YOUTUBE_VIDEO etc. |
| `asset_group_asset_performance_label` | STRING | NULLABLE | The performance of this asset group asset. |
| `asset_group_asset_policy_summary_approval_status` | STRING | NULLABLE | The overall approval status, which is calculated based on the status of its individual policy topic entries. |
| `asset_group_asset_policy_summary_policy_topic_entries` | STRING | NULLABLE | The list of policy findings. |
| `asset_group_asset_policy_summary_review_status` | STRING | NULLABLE | Where in the review process the resource is. |
| `asset_group_asset_source` | STRING | NULLABLE | Output only. Source of the asset group asset. |

#### Table: `p_ads_AssetGroupListingGroupFilter_2702575199`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_listing_group_filter_case_value_product_category_category_id` | STRING | NULLABLE | ID of the product category. This ID is equivalent to the google_product_category ID as described in this article: https://support.google.com/merchants/answer/6324436 |
| `asset_group_listing_group_filter_id` | STRING | NULLABLE | The ID of the ListingGroupFilter. |
| `asset_group_listing_group_filter_asset_group` | STRING | NULLABLE | The asset group which this asset group listing group filter is part of. |
| `asset_group_listing_group_filter_case_value_product_brand_value` | STRING | NULLABLE | String value of the product brand. |
| `asset_group_listing_group_filter_case_value_product_category_level` | STRING | NULLABLE | Indicates the level of the category in the taxonomy. |
| `asset_group_listing_group_filter_case_value_product_channel_channel` | STRING | NULLABLE | Value of the locality. |
| `asset_group_listing_group_filter_case_value_product_condition_condition` | STRING | NULLABLE | Value of the condition. |
| `asset_group_listing_group_filter_case_value_product_custom_attribute_index` | STRING | NULLABLE | Indicates the index of the custom attribute. |
| `asset_group_listing_group_filter_case_value_product_custom_attribute_value` | STRING | NULLABLE | String value of the product custom attribute. |
| `asset_group_listing_group_filter_case_value_product_item_id_value` | STRING | NULLABLE | Value of the id. |
| `asset_group_listing_group_filter_case_value_product_type_level` | STRING | NULLABLE | Level of the type. |
| `asset_group_listing_group_filter_case_value_product_type_value` | STRING | NULLABLE | Value of the type. |
| `asset_group_listing_group_filter_listing_source` | STRING | NULLABLE | The source of listings filtered by this listing group filter. |
| `asset_group_listing_group_filter_parent_listing_group_filter` | STRING | NULLABLE | Resource name of the parent listing group subdivision. Null for the root listing group filter node. |
| `asset_group_listing_group_filter_type` | STRING | NULLABLE | Type of a listing group filter node. |

#### Table: `p_ads_AssetGroupProductGroupStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_product_group_view_asset_group` | STRING | NULLABLE | The asset group associated with the listing group filter. |
| `asset_group_product_group_view_asset_group_listing_group_filter` | STRING | NULLABLE | The resource name of the asset group listing group filter. |
| `asset_group_product_group_view_resource_name` | STRING | NULLABLE | The resource name of the asset group product group view. Asset group product group view resource names have the form: customers/{customer_id}/assetGroupProductGroupViews/{asset_group_id}~{listing_group_filter_id} |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, for example, MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, for example, the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_AssetGroupSignal_2702575199`

**Nombre de colonnes:** 3


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_signal_asset_group` | STRING | NULLABLE | The asset group which this asset group signal belongs to. |
| `asset_group_signal_audience_audience` | STRING | NULLABLE | The Audience resource name. |
| `asset_group_signal_resource_name` | STRING | NULLABLE | The resource name of the asset group signal. Asset group signal resource name have the form: customers/{customer_id}/assetGroupSignals/{asset_group_id}~{signal_id} |

#### Table: `p_ads_AssetGroup_2702575199`

**Nombre de colonnes:** 6


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_id` | STRING | NULLABLE | Output only. The ID of the asset group. |
| `asset_group_campaign` | STRING | NULLABLE | Immutable. The campaign with which this asset group is associated. The asset which is linked to the asset group. |
| `asset_group_final_mobile_urls` | STRING | NULLABLE | A list of final mobile URLs after all cross domain redirects. In performance max, by default, the urls are eligible for expansion unless opted out. |
| `asset_group_final_urls` | STRING | NULLABLE | A list of final URLs after all cross domain redirects. In performance max, by default, the urls are eligible for expansion unless opted out. |
| `asset_group_name` | STRING | NULLABLE | Required. Name of the asset group. Required. It must have a minimum length of 1 and maximum length of 128. It must be unique under a campaign. |
| `asset_group_status` | STRING | NULLABLE | The status of the asset group. |

#### Table: `p_ads_Asset_2702575199`

**Nombre de colonnes:** 6


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_id` | INTEGER | NULLABLE | Output only. The ID of the asset. |
| `asset_final_urls` | STRING | NULLABLE | Output only. Type of the asset. |
| `asset_name` | STRING | NULLABLE | Optional name of the asset. |
| `asset_source` | STRING | NULLABLE | Output only. Source of the asset. |
| `asset_type` | STRING | NULLABLE | A list of possible final URLs after all cross domain redirects. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |

#### Table: `p_ads_Audience_2702575199`

**Nombre de colonnes:** 6


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `audience_id` | STRING | NULLABLE |  ID of the audience. |
| `audience_description` | STRING | NULLABLE | Description of this audience. |
| `audience_dimensions` | STRING | NULLABLE | Positive dimensions specifying the audience composition. |
| `audience_exclusion_dimension` | STRING | NULLABLE | Negative dimension specifying the audience composition. |
| `audience_name` | STRING | NULLABLE | Name of the audience. It should be unique across all audiences. It must have a minimum length of 1 and maximum length of 255. |
| `audience_status` | STRING | NULLABLE | Status of this audience. Indicates whether the audience is enabled or removed. |

#### Table: `p_ads_BidGoalConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | The ID of the bidding strategy. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `bidding_strategy_campaign_count` | INTEGER | NULLABLE | The number of campaigns attached to this bidding strategy. This field is read-only. |
| `bidding_strategy_non_removed_campaign_count` | INTEGER | NULLABLE | The number of non-removed campaigns attached to this bidding strategy. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_BidGoalStats_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | The ID of the bidding strategy. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `bidding_strategy_campaign_count` | INTEGER | NULLABLE | The number of campaigns attached to this bidding strategy. This field is read-only. |
| `bidding_strategy_non_removed_campaign_count` | INTEGER | NULLABLE | The number of non-removed campaigns attached to this bidding strategy. This field is read-only. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_BidGoal_2702575199`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | The ID of the bidding strategy. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `bidding_strategy_name` | STRING | NULLABLE | The name of the bidding strategy. All bidding strategies within an account must be named distinctly. The length of this string should be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed). |
| `bidding_strategy_status` | STRING | NULLABLE | The status of the bidding strategy. This field is read-only. |
| `bidding_strategy_target_cpa_cpc_bid_ceiling_micros` | INTEGER | NULLABLE | Maximum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. |
| `bidding_strategy_target_cpa_cpc_bid_floor_micros` | INTEGER | NULLABLE | Minimum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. |
| `bidding_strategy_target_cpa_target_cpa_micros` | INTEGER | NULLABLE | Average CPA target. This target should be greater than or equal to minimum billable unit based on the currency for the account. |
| `bidding_strategy_target_roas_cpc_bid_ceiling_micros` | INTEGER | NULLABLE | Maximum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. |
| `bidding_strategy_target_roas_cpc_bid_floor_micros` | INTEGER | NULLABLE | Minimum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. |
| `bidding_strategy_target_roas_target_roas` | FLOAT | NULLABLE | Required. The desired revenue (based on conversion data) per unit of spend. Value must be between 0.01 and 1000.0, inclusive. |
| `bidding_strategy_target_spend_cpc_bid_ceiling_micros` | INTEGER | NULLABLE | Maximum bid limit that can be set by the bid strategy. The limit applies to all keywords managed by the strategy. |
| `bidding_strategy_target_spend_target_spend_micros` | INTEGER | NULLABLE | The spend target under which to maximize clicks. A TargetSpend bidder will attempt to spend the smaller of this value or the natural throttling spend amount. If not specified, the budget is used as the spend target. |
| `bidding_strategy_type` | STRING | NULLABLE | The type of the bidding strategy. Create a bidding strategy by setting the bidding scheme. This field is read-only. |
| `customer_descriptive_name` | STRING | NULLABLE | Optional, non-unique descriptive name of the customer. |

#### Table: `p_ads_BudgetStats_2702575199`

**Nombre de colonnes:** 38


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_budget_id` | INTEGER | NULLABLE | The ID of the campaign budget. A campaign budget is created using the CampaignBudgetService create operation and is assigned a budget ID. A budget ID can be shared across different campaigns; the system will then allocate the campaign budget among different campaigns to get optimum results. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_budget_recommended_budget_estimated_change_weekly_clicks` | INTEGER | NULLABLE | The estimated change in weekly clicks if the recommended budget is applied. This field is read-only. |
| `campaign_budget_recommended_budget_estimated_change_weekly_cost_micros` | INTEGER | NULLABLE | The estimated change in weekly cost in micros if the recommended budget is applied. One million is equivalent to one currency unit. This field is read-only. |
| `campaign_budget_recommended_budget_estimated_change_weekly_interactions` | INTEGER | NULLABLE | The estimated change in weekly interactions if the recommended budget is applied. This field is read-only. |
| `campaign_budget_recommended_budget_estimated_change_weekly_views` | INTEGER | NULLABLE | The estimated change in weekly views if the recommended budget is applied. This field is read-only. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |

#### Table: `p_ads_Budget_2702575199`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_budget_id` | INTEGER | NULLABLE | The ID of the campaign budget. A campaign budget is created using the CampaignBudgetService create operation and is assigned a budget ID. A budget ID can be shared across different campaigns; the system will then allocate the campaign budget among different campaigns to get optimum results. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_budget_amount_micros` | INTEGER | NULLABLE | The amount of the budget, in the local currency for the account. Amount is specified in micros, where one million is equivalent to one currency unit. Monthly spend is capped at 30.4 times this amount. |
| `campaign_budget_delivery_method` | STRING | NULLABLE | The delivery method that determines the rate at which the campaign budget is spent. Defaults to STANDARD if unspecified in a create operation. |
| `campaign_budget_explicitly_shared` | BOOLEAN | NULLABLE | Specifies whether the budget is explicitly shared. Defaults to true if unspecified in a create operation. If true, the budget was created with the purpose of sharing across one or more campaigns. If false, the budget was created with the intention of only being used with a single campaign. The budget's name and status will stay in sync with the campaign's name and status. Attempting to share the budget with a second campaign will result in an error. A non-shared budget can become an explicitly shared. The same operation must also assign the budget a name. A shared campaign budget can never become non-shared. |
| `campaign_budget_has_recommended_budget` | BOOLEAN | NULLABLE | Indicates whether there is a recommended budget for this campaign budget. This field is read-only. |
| `campaign_budget_name` | STRING | NULLABLE | The name of the campaign budget. When creating a campaign budget through CampaignBudgetService, every explicitly shared campaign budget must have a non-null, non-empty name. Campaign budgets that are not explicitly shared derive their name from the attached campaign's name. The length of this string must be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed). |
| `campaign_budget_period` | STRING | NULLABLE | Period over which to spend the budget. Defaults to DAILY if not specified. |
| `campaign_budget_recommended_budget_amount_micros` | INTEGER | NULLABLE | The recommended budget amount. If no recommendation is available, this will be set to the budget amount. Amount is specified in micros, where one million is equivalent to one currency unit. This field is read-only. |
| `campaign_budget_reference_count` | INTEGER | NULLABLE | The number of campaigns actively using the budget. This field is read-only. |
| `campaign_budget_status` | STRING | NULLABLE | The status of this campaign budget. This field is read-only. |
| `campaign_budget_total_amount_micros` | INTEGER | NULLABLE | The lifetime amount of the budget, in the local currency for the account. Amount is specified in micros, where one million is equivalent to one currency unit. |
| `customer_descriptive_name` | STRING | NULLABLE | Optional, non-unique descriptive name of the customer. |

#### Table: `p_ads_CampaignAssetStats_2702575199`

**Nombre de colonnes:** 28


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_asset_asset` | STRING | NULLABLE | The asset which is linked to the campaign. |
| `campaign_asset_campaign` | STRING | NULLABLE | The campaign to which the asset is linked. |
| `campaign_asset_field_type` | STRING | NULLABLE | Role that the asset takes under the linked campaign. |
| `campaign_asset_resource_name` | STRING | NULLABLE | The resource name of the campaign asset. CampaignAsset resource names have the form: customers/{customer_id}/campaignAssets/{campaign_id}~{asset_id}~{field_type} |
| `campaign_asset_source` | STRING | NULLABLE | Source of the campaign asset link. |
| `campaign_asset_status` | STRING | NULLABLE | Status of the campaign asset. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. If you use conversion-based bidding, your bid strategies will optimize for these conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, for example, MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, for example, the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignAudienceBasicStats_2702575199`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | Output only. The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_CampaignAudienceConversionStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | Output only. The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignAudienceNonClickStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | Output only. The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignAudienceStats_2702575199`

**Nombre de colonnes:** 40


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | Output only. The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignAudience_2702575199`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | STRING | NULLABLE | Output only. The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `campaign_criterion_bid_modifier` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |

#### Table: `p_ads_CampaignBasicStats_2702575199`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_CampaignConversionStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_conversion_attribution_event_type` | STRING | NULLABLE | Conversion attribution event type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignCookieStats_2702575199`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to a low budget. Note: Search budget lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to a low budget. Note: Search budget lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to poor Ad Rank. Note: Search rank lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to poor Ad Rank. Note: Search rank lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | The impressions you've received in the top location (anywhere above the organic search results) compared to the estimated number of impressions you were eligible to receive in the top location. Note: Search top impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown anywhere above the organic search results. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |

#### Table: `p_ads_CampaignCriterion_2702575199`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `campaign_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bids when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. Use 0 to opt out of a Device type. |
| `campaign_criterion_campaign` | STRING | NULLABLE | The campaign to which the criterion belongs. |
| `campaign_criterion_device_type` | STRING | NULLABLE | Type of the device. |
| `campaign_criterion_display_name` | STRING | NULLABLE | The display name of the criterion. This field is ignored for mutates. |
| `campaign_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. |
| `campaign_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `campaign_criterion_type` | STRING | NULLABLE | The type of the criterion. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |

#### Table: `p_ads_CampaignCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_conversion_attribution_event_type` | STRING | NULLABLE | Conversion attribution event type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignCrossDeviceStats_2702575199`

**Nombre de colonnes:** 52


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_average_page_views` | FLOAT | NULLABLE | Average number of pages viewed per session. |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | Total duration of all sessions (in seconds) / number of sessions. Imported from Google Analytics. |
| `metrics_bounce_rate` | FLOAT | NULLABLE | Percentage of clicks where the user only visited a single page on your site. Imported from Google Analytics. |
| `metrics_content_budget_lost_impression_share` | FLOAT | NULLABLE | The estimated percent of times that your ad was eligible to show on the Display Network but didn't because your budget was too low. Note: Content budget lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_content_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Display Network divided by the estimated number of impressions you were eligible to receive. Note: Content impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_content_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Display Network that your ads didn't receive due to poor Ad Rank. Note: Content rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_invalid_click_rate` | FLOAT | NULLABLE | The percentage of clicks filtered out of your total number of clicks (filtered + non-filtered clicks) during the reporting period. |
| `metrics_invalid_clicks` | INTEGER | NULLABLE | Number of clicks Google considers illegitimate and doesn't charge you for. |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | Percentage of first-time sessions (from people who had never visited your site before). Imported from Google Analytics. |
| `metrics_phone_calls` | INTEGER | NULLABLE | Number of offline phone calls. |
| `metrics_phone_impressions` | INTEGER | NULLABLE | Number of offline phone impressions. |
| `metrics_phone_through_rate` | FLOAT | NULLABLE | Number of phone calls received (phone_calls) divided by the number of times your phone number is shown (phone_impressions). |
| `metrics_relative_ctr` | FLOAT | NULLABLE | Your clickthrough rate (Ctr) divided by the average clickthrough rate of all advertisers on the websites that show your ads. Measures how your ads perform on Display Network sites compared to other ads on the same sites. |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | The percentage of the customer's Shopping or Search ad impressions that are shown in the most prominent Shopping position. See https://support.google.com/google-ads/answer/7501826 for details. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to a low budget. Note: Search budget lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_budget_lost_impression_share` | FLOAT | NULLABLE | The estimated percent of times that your ad was eligible to show on the Search Network but didn't because your budget was too low. Note: Search budget lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to a low budget. Note: Search budget lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_click_share` | FLOAT | NULLABLE | The number of clicks you've received on the Search Network divided by the estimated number of clicks you were eligible to receive. Note: Search click share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | The impressions you've received divided by the estimated number of impressions you were eligible to receive on the Search Network for search terms that matched your keywords exactly (or were close variants of your keyword), regardless of your keyword match types. Note: Search exact match impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Search Network divided by the estimated number of impressions you were eligible to receive. Note: Search impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to poor Ad Rank. Note: Search rank lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Search Network that your ads didn't receive due to poor Ad Rank. Note: Search rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to poor Ad Rank. Note: Search rank lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | The impressions you've received in the top location (anywhere above the organic search results) compared to the estimated number of impressions you were eligible to receive in the top location. Note: Search top impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown anywhere above the organic search results. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignLabel_2702575199`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `label_id` | INTEGER | NULLABLE | Id of the label. Read only. |
| `campaign_label_campaign` | STRING | NULLABLE | The campaign to which the label is attached. |
| `campaign_label_label` | STRING | NULLABLE | The label assigned to the campaign. |
| `campaign_label_resource_name` | STRING | NULLABLE | Name of the resource. Campaign label resource names have the form: `customers/{customer_id}/campaignLabels/{campaign_id}~{label_id}` |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `label_name` | STRING | NULLABLE | The name of the label. This field is required and should not be empty when creating a new label. The length of this string should be between 1 and 80, inclusive. |
| `label_resource_name` | STRING | NULLABLE | Name of the resource. Label resource names have the form: `customers/{customer_id}/labels/{label_id}` |

#### Table: `p_ads_CampaignLocationTargetStats_2702575199`

**Nombre de colonnes:** 36


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_CampaignStats_2702575199`

**Nombre de colonnes:** 41


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | Shows how your historic conversions data would look under the attribution model you've currently selected. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_current_model_attributed_conversions_value` | FLOAT | NULLABLE | The total value of current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The value of current model attributed conversions divided by the number of the conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_Campaign_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `bidding_strategy_name` | STRING | NULLABLE | The name of the bidding strategy. All bidding strategies within an account must be named distinctly. The length of this string should be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed). |
| `campaign_advertising_channel_sub_type` | STRING | NULLABLE | Optional refinement to `advertising_channel_type`. Must be a valid sub-type of the parent channel type. Can be set only when creating campaigns. After campaign is created, the field can not be changed. |
| `campaign_advertising_channel_type` | STRING | NULLABLE | The primary serving target for ads within the campaign. The targeting options can be refined in `network_settings`. This field is required and should not be empty when creating new campaigns. Can be set only when creating campaigns. After the campaign is created, the field can not be changed. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the `bidding_strategy` field to create a portfolio bidding strategy. This field is read-only. |
| `campaign_budget_amount_micros` | INTEGER | NULLABLE | The amount of the budget, in the local currency for the account. Amount is specified in micros, where one million is equivalent to one currency unit. Monthly spend is capped at 30.4 times this amount. |
| `campaign_budget_explicitly_shared` | BOOLEAN | NULLABLE | Specifies whether the budget is explicitly shared. Defaults to true if unspecified in a create operation. If true, the budget was created with the purpose of sharing across one or more campaigns. If false, the budget was created with the intention of only being used with a single campaign. The budget's name and status will stay in sync with the campaign's name and status. Attempting to share the budget with a second campaign will result in an error. A non-shared budget can become an explicitly shared. The same operation must also assign the budget a name. A shared campaign budget can never become non-shared. |
| `campaign_budget_has_recommended_budget` | BOOLEAN | NULLABLE | Indicates whether there is a recommended budget for this campaign budget. This field is read-only. |
| `campaign_budget_period` | STRING | NULLABLE | Period over which to spend the budget. Defaults to DAILY if not specified. |
| `campaign_budget_recommended_budget_amount_micros` | INTEGER | NULLABLE | The recommended budget amount. If no recommendation is available, this will be set to the budget amount. Amount is specified in micros, where one million is equivalent to one currency unit. This field is read-only. |
| `campaign_budget_total_amount_micros` | INTEGER | NULLABLE | The lifetime amount of the budget, in the local currency for the account. Amount is specified in micros, where one million is equivalent to one currency unit. |
| `campaign_campaign_budget` | STRING | NULLABLE | The budget of the campaign. |
| `campaign_end_date` | DATE | NULLABLE | The date when campaign ended. This field must not be used in WHERE clauses. |
| `campaign_experiment_type` | STRING | NULLABLE | The type of campaign: normal, draft, or experiment. |
| `campaign_manual_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | Whether bids are to be enhanced based on conversion optimizer data. |
| `campaign_maximize_conversion_value_target_roas` | FLOAT | NULLABLE | The target return on ad spend (ROAS) option. If set, the bid strategy will maximize revenue while averaging the target return on ad spend. If the target ROAS is high, the bid strategy may not be able to spend the full budget. If the target ROAS is not set, the bid strategy will aim to achieve the highest possible ROAS for the budget. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `campaign_percent_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | Adjusts the bid for each auction upward or downward, depending on the likelihood of a conversion. Individual bids may exceed cpc_bid_ceiling_micros, but the average bid amount for a campaign should not. |
| `campaign_serving_status` | STRING | NULLABLE | The ad serving status of the campaign. |
| `campaign_start_date` | DATE | NULLABLE | The date when campaign started. This field must not be used in WHERE clauses. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `campaign_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `campaign_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |

#### Table: `p_ads_ClickStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `click_view_gclid` | STRING | NULLABLE | The Google Click ID. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_status` | STRING | NULLABLE | The status of the ad group. |
| `click_view_ad_group_ad` | STRING | NULLABLE | The associated ad. |
| `click_view_area_of_interest_city` | STRING | NULLABLE | The city location criterion associated with the impression. |
| `click_view_area_of_interest_country` | STRING | NULLABLE | The country location criterion associated with the impression. |
| `click_view_area_of_interest_metro` | STRING | NULLABLE | The metro location criterion associated with the impression. |
| `click_view_area_of_interest_most_specific` | STRING | NULLABLE | The most specific location criterion associated with the impression. |
| `click_view_area_of_interest_region` | STRING | NULLABLE | The region location criterion associated with the impression. |
| `click_view_keyword` | STRING | NULLABLE | The associated keyword, if one exists and the click corresponds to the SEARCH channel. |
| `click_view_keyword_info_match_type` | STRING | NULLABLE | The match type of the keyword. |
| `click_view_keyword_info_text` | STRING | NULLABLE | The text of the keyword (at most 80 characters and 10 words). |
| `click_view_location_of_presence_city` | STRING | NULLABLE | The city location criterion associated with the impression. |
| `click_view_location_of_presence_country` | STRING | NULLABLE | The country location criterion associated with the impression. |
| `click_view_location_of_presence_metro` | STRING | NULLABLE | The metro location criterion associated with the impression. |
| `click_view_location_of_presence_most_specific` | STRING | NULLABLE | The most specific location criterion associated with the impression. |
| `click_view_location_of_presence_region` | STRING | NULLABLE | The region location criterion associated with the impression. |
| `click_view_page_number` | INTEGER | NULLABLE | Page number in search results where the ad was shown. |
| `customer_descriptive_name` | STRING | NULLABLE | Optional, non-unique descriptive name of the customer. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_Customer_2702575199`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `customer_auto_tagging_enabled` | BOOLEAN | NULLABLE | Whether auto-tagging is enabled for the customer. |
| `customer_currency_code` | STRING | NULLABLE | The currency in which the account operates. A subset of the currency codes from the ISO 4217 standard is supported. |
| `customer_descriptive_name` | STRING | NULLABLE | Optional, non-unique descriptive name of the customer. |
| `customer_manager` | BOOLEAN | NULLABLE | Whether the customer is a manager. |
| `customer_test_account` | BOOLEAN | NULLABLE | Whether the customer is a test account. |
| `customer_time_zone` | STRING | NULLABLE | The local timezone ID of the customer. |

#### Table: `p_ads_DisplayVideoAutomaticPlacementsStats_2702575199`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `group_placement_view_placement` | STRING | NULLABLE | The automatic placement string at group level, e. g. web domain, mobile app ID, or a YouTube channel ID. |
| `group_placement_view_placement_type` | STRING | NULLABLE | Type of the placement, e.g. Website, YouTube Channel, Mobile Application. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_DisplayVideoKeywordStats_2702575199`

**Nombre de colonnes:** 26


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_criterion_keyword_text` | STRING | NULLABLE | The text of the keyword (at most 80 characters and 10 words). |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `campaign_advertising_channel_sub_type` | STRING | NULLABLE | Optional refinement to `advertising_channel_type`. Must be a valid sub-type of the parent channel type. Can be set only when creating campaigns. After campaign is created, the field can not be changed. |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the `bidding_strategy` field to create a portfolio bidding strategy. This field is read-only. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_DisplayVideoTopicStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_topic_path` | STRING | NULLABLE | The category to target or exclude. Each subsequent element in the array describes a more specific sub-category. For example, \"Pets & Animals\", \"Pets\", \"Dogs\" represents the \"Pets & Animals/Pets/Dogs\" category. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_GenderBasicStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |

#### Table: `p_ads_GenderConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_GenderNonClickStats_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_GenderStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_Gender_2702575199`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | The effective CPC (cost-per-click) bid. |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | Source of the effective CPC bid. |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | The effective CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | Source of the effective CPM bid. |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects. |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_criterion_gender_type` | STRING | NULLABLE | Type of the gender. |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | The per-targeting-dimension setting to restrict the reach of your campaign or ad group. |
| `bidding_strategy_name` | STRING | NULLABLE | The name of the bidding strategy. All bidding strategies within an account must be named distinctly. The length of this string should be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed). |
| `bidding_strategy_type` | STRING | NULLABLE | The type of the bidding strategy. Create a bidding strategy by setting the bidding scheme. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |

#### Table: `p_ads_GeoConversionStats_2702575199`

**Nombre de colonnes:** 28


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `geographic_view_country_criterion_id` | INTEGER | NULLABLE | Criterion Id for the country. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `ad_group_status` | STRING | NULLABLE | The status of the ad group. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `geographic_view_location_type` | STRING | NULLABLE | Type of the geo targeting of the campaign. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_geo_target_most_specific_location` | STRING | NULLABLE | Resource name of the geo target constant that represents the most specific location. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_GeoStats_2702575199`

**Nombre de colonnes:** 42


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `geographic_view_country_criterion_id` | INTEGER | NULLABLE | Criterion Id for the country. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `ad_group_status` | STRING | NULLABLE | The status of the ad group. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `geographic_view_location_type` | STRING | NULLABLE | Type of the geo targeting of the campaign. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_geo_target_most_specific_location` | STRING | NULLABLE | Resource name of the geo target constant that represents the most specific location. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyAccountConversionStats_2702575199`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyAccountStats_2702575199`

**Nombre de colonnes:** 33


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyAdGroupConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyAdGroupStats_2702575199`

**Nombre de colonnes:** 37


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyBidGoalStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `bidding_strategy_id` | INTEGER | NULLABLE | The ID of the bidding strategy. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `bidding_strategy_campaign_count` | INTEGER | NULLABLE | The number of campaigns attached to this bidding strategy. This field is read-only. |
| `bidding_strategy_non_removed_campaign_count` | INTEGER | NULLABLE | The number of non-removed campaigns attached to this bidding strategy. This field is read-only. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyCampaignConversionStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_HourlyCampaignStats_2702575199`

**Nombre de colonnes:** 35


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_hour` | INTEGER | NULLABLE | Hour of day as a number between 0 and 23, inclusive. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_KeywordBasicStats_2702575199`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |

#### Table: `p_ads_KeywordConversionStats_2702575199`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_slot` | STRING | NULLABLE | Position of the ad. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_KeywordCrossDeviceConversionStats_2702575199`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_KeywordCrossDeviceStats_2702575199`

**Nombre de colonnes:** 44


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_average_page_views` | FLOAT | NULLABLE | Average number of pages viewed per session. |
| `metrics_average_time_on_site` | FLOAT | NULLABLE | Total duration of all sessions (in seconds) / number of sessions. Imported from Google Analytics. |
| `metrics_bounce_rate` | FLOAT | NULLABLE | Percentage of clicks where the user only visited a single page on your site. Imported from Google Analytics. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_percent_new_visitors` | FLOAT | NULLABLE | Percentage of first-time sessions (from people who had never visited your site before). Imported from Google Analytics. |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | The percentage of the customer's Shopping or Search ad impressions that are shown in the most prominent Shopping position. See https://support.google.com/google-ads/answer/7501826 for details. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_budget_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to a low budget. Note: Search budget lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_budget_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to a low budget. Note: Search budget lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_exact_match_impression_share` | FLOAT | NULLABLE | The impressions you've received divided by the estimated number of impressions you were eligible to receive on the Search Network for search terms that matched your keywords exactly (or were close variants of your keyword), regardless of your keyword match types. Note: Search exact match impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Search Network divided by the estimated number of impressions you were eligible to receive. Note: Search impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_rank_lost_absolute_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad wasn't the very first ad above the organic search results due to poor Ad Rank. Note: Search rank lost absolute top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_impression_share` | FLOAT | NULLABLE | The estimated percentage of impressions on the Search Network that your ads didn't receive due to poor Ad Rank. Note: Search rank lost impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_rank_lost_top_impression_share` | FLOAT | NULLABLE | The number estimating how often your ad didn't show anywhere above the organic search results due to poor Ad Rank. Note: Search rank lost top impression share is reported in the range of 0 to 0.9. Any value above 0.9 is reported as 0.9001. |
| `metrics_search_top_impression_share` | FLOAT | NULLABLE | The impressions you've received in the top location (anywhere above the organic search results) compared to the estimated number of impressions you were eligible to receive in the top location. Note: Search top impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown anywhere above the organic search results. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_KeywordStats_2702575199`

**Nombre de colonnes:** 44


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_current_model_attributed_conversions` | FLOAT | NULLABLE | Shows how your historic conversions data would look under the attribution model you've currently selected. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_current_model_attributed_conversions_value` | FLOAT | NULLABLE | The total value of current model attributed conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_current_model_attributed_conversion` | FLOAT | NULLABLE | The value of current model attributed conversions divided by the number of the conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_Keyword_2702575199`

**Nombre de colonnes:** 32


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_criterion_approval_status` | STRING | NULLABLE | Approval status of the criterion. |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | The effective CPC (cost-per-click) bid. |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | Source of the effective CPC bid. |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | The effective CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects. |
| `ad_group_criterion_final_url_suffix` | STRING | NULLABLE | URL template for appending params to final URL. |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_criterion_keyword_match_type` | STRING | NULLABLE | The match type of the keyword. |
| `ad_group_criterion_keyword_text` | STRING | NULLABLE | The text of the keyword (at most 80 characters and 10 words). |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. |
| `ad_group_criterion_position_estimates_estimated_add_clicks_at_first_position_cpc` | INTEGER | NULLABLE | Estimate of how many clicks per week you might get by changing your keyword bid to the value in first_position_cpc_micros. |
| `ad_group_criterion_position_estimates_estimated_add_cost_at_first_position_cpc` | INTEGER | NULLABLE | Estimate of how your cost per week might change when changing your keyword bid to the value in first_position_cpc_micros. |
| `ad_group_criterion_position_estimates_first_page_cpc_micros` | INTEGER | NULLABLE | The estimate of the CPC bid required for ad to be shown on first page of search results. |
| `ad_group_criterion_position_estimates_first_position_cpc_micros` | INTEGER | NULLABLE | The estimate of the CPC bid required for ad to be displayed in first position, at the top of the first page of search results. |
| `ad_group_criterion_position_estimates_top_of_page_cpc_micros` | INTEGER | NULLABLE | The estimate of the CPC bid required for ad to be displayed at the top of the first page of search results. |
| `ad_group_criterion_quality_info_creative_quality_score` | STRING | NULLABLE | The performance of the ad compared to other advertisers. |
| `ad_group_criterion_quality_info_post_click_quality_score` | STRING | NULLABLE | The quality score of the landing page. |
| `ad_group_criterion_quality_info_quality_score` | INTEGER | NULLABLE | The quality score. This field may not be populated if Google does not have enough information to determine a value. |
| `ad_group_criterion_quality_info_search_predicted_ctr` | STRING | NULLABLE | The click-through rate compared to that of other advertisers. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_system_serving_status` | STRING | NULLABLE | Serving status of the criterion. |
| `ad_group_criterion_topic_topic_constant` | STRING | NULLABLE | The Topic Constant resource name. |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the `bidding_strategy` field to create a portfolio bidding strategy. This field is read-only. |
| `campaign_manual_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | Whether bids are to be enhanced based on conversion optimizer data. |
| `campaign_percent_cpc_enhanced_cpc_enabled` | BOOLEAN | NULLABLE | Adjusts the bid for each auction upward or downward, depending on the likelihood of a conversion. Individual bids may exceed cpc_bid_ceiling_micros, but the average bid amount for a campaign should not. |

#### Table: `p_ads_LandingPageStats_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `ad_group_status` | STRING | NULLABLE | The status of the ad group. |
| `campaign_name` | STRING | NULLABLE | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `landing_page_view_unexpanded_final_url` | STRING | NULLABLE | The advertiser-specified final URL. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_mobile_friendly_clicks_percentage` | FLOAT | NULLABLE | The percentage of mobile clicks that go to a mobile-friendly page. |
| `metrics_speed_score` | INTEGER | NULLABLE | A measure of how quickly your page loads after clicks on your mobile ads. The score is a range from 1 to 10, 10 being the fastest. |
| `metrics_valid_accelerated_mobile_pages_clicks_percentage` | FLOAT | NULLABLE | The percentage of ad clicks to Accelerated Mobile Pages (AMP) landing pages that reach a valid AMP page. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_LocationBasedCampaignCriterion_2702575199`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored during mutate. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `campaign_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bids when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. Use 0 to opt out of a Device type. |
| `campaign_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. |

#### Table: `p_ads_LocationsDistanceStats_2702575199`

**Nombre de colonnes:** 17


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `distance_view_distance_bucket` | STRING | NULLABLE | Grouping of user distance from location extensions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_LocationsUserLocationsStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `user_location_view_country_criterion_id` | INTEGER | NULLABLE | Criterion Id for the country. |
| `ad_group_name` | STRING | NULLABLE | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |
| `ad_group_status` | STRING | NULLABLE | The status of the ad group. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_geo_target_most_specific_location` | STRING | NULLABLE | Resource name of the geo target constant that represents the most specific location. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |
| `user_location_view_targeting_location` | BOOLEAN | NULLABLE | Target location. |

#### Table: `p_ads_PaidOrganicStats_2702575199`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_combined_clicks` | INTEGER | NULLABLE | The number of times your ad or your site's listing in the unpaid results was clicked. See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_combined_clicks_per_query` | FLOAT | NULLABLE | The number of times your ad or your site's listing in the unpaid results was clicked (combined_clicks) divided by combined_queries. See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_combined_queries` | INTEGER | NULLABLE | The number of searches that returned pages from your site in the unpaid results or showed one of your text ads. See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_organic_clicks` | INTEGER | NULLABLE | The number of times someone clicked your site's listing in the unpaid results for a particular query. See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_organic_clicks_per_query` | FLOAT | NULLABLE | The number of times someone clicked your site's listing in the unpaid results (organic_clicks) divided by the total number of searches that returned pages from your site (organic_queries). See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_organic_impressions` | INTEGER | NULLABLE | The number of listings for your site in the unpaid search results. See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_organic_impressions_per_query` | FLOAT | NULLABLE | The number of times a page from your site was listed in the unpaid search results (organic_impressions) divided by the number of searches returning your site's listing in the unpaid results (organic_queries). See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `metrics_organic_queries` | INTEGER | NULLABLE | The total number of searches that returned your site's listing in the unpaid results. See the help page at https://support.google.com/google-ads/answer/3097241 for details. |
| `paid_organic_search_term_view_search_term` | STRING | NULLABLE | The search term. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_search_engine_results_page_type` | STRING | NULLABLE | Type of the search engine results page. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_ParentalStatusBasicStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |

#### Table: `p_ads_ParentalStatusConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_ParentalStatusNonClickStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_ParentalStatusStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_ParentalStatus_2702575199`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | The effective CPC (cost-per-click) bid. |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | Source of the effective CPC bid. |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | The effective CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | Source of the effective CPM bid. |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects. |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. |
| `ad_group_criterion_parental_status_type` | STRING | NULLABLE | Type of the parental status. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | The per-targeting-dimension setting to restrict the reach of your campaign or ad group. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |

#### Table: `p_ads_PlacementBasicStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |

#### Table: `p_ads_PlacementConversionStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_PlacementNonClickStats_2702575199`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_PlacementStats_2702575199`

**Nombre de colonnes:** 45


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `metrics_active_view_cpm` | FLOAT | NULLABLE | Average cost of viewable impressions (`active_view_impressions`). |
| `metrics_active_view_ctr` | FLOAT | NULLABLE | Active view measurable clicks divided by active view viewable impressions. This metric is reported only for display network. |
| `metrics_active_view_impressions` | INTEGER | NULLABLE | A measurement of how often your ad has become viewable on a Display Network site. |
| `metrics_active_view_measurability` | FLOAT | NULLABLE | The ratio of impressions that could be measured by Active View over the number of served impressions. |
| `metrics_active_view_measurable_cost_micros` | INTEGER | NULLABLE | The cost of the impressions you received that were measurable by Active View. |
| `metrics_active_view_measurable_impressions` | INTEGER | NULLABLE | The number of times your ads are appearing on placements in positions where they can be seen. |
| `metrics_active_view_viewability` | FLOAT | NULLABLE | The percentage of time when your ad appeared on an Active View enabled site (measurable impressions) and was viewable (viewable impressions). |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_gmail_forwards` | INTEGER | NULLABLE | The number of times the ad was forwarded to someone else as a message. |
| `metrics_gmail_saves` | INTEGER | NULLABLE | The number of times someone has saved your Gmail ad to their inbox as a message. |
| `metrics_gmail_secondary_clicks` | INTEGER | NULLABLE | The number of clicks to the landing page on the expanded state of Gmail ads. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_Placement_2702575199`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `ad_group_base_ad_group` | STRING | NULLABLE | For draft or experiment ad groups, this field is the resource name of the base ad group from which this ad group was created. If a draft or experiment ad group does not have a base ad group, then this field is null. For base ad groups, this field equals the ad group resource name. This field is read-only. |
| `ad_group_criterion_bid_modifier` | FLOAT | NULLABLE | The modifier for the bid when the criterion matches. The modifier must be in the range: 0.1 - 10.0. Most targetable criteria types support modifiers. |
| `ad_group_criterion_effective_cpc_bid_micros` | INTEGER | NULLABLE | The effective CPC (cost-per-click) bid. |
| `ad_group_criterion_effective_cpc_bid_source` | STRING | NULLABLE | Source of the effective CPC bid. |
| `ad_group_criterion_effective_cpm_bid_micros` | INTEGER | NULLABLE | The effective CPM (cost-per-thousand viewable impressions) bid. |
| `ad_group_criterion_effective_cpm_bid_source` | STRING | NULLABLE | Source of the effective CPM bid. |
| `ad_group_criterion_final_mobile_urls` | STRING | NULLABLE | The list of possible final mobile URLs after all cross-domain redirects. |
| `ad_group_criterion_final_urls` | STRING | NULLABLE | The list of possible final URLs after all cross-domain redirects for the ad. |
| `ad_group_criterion_negative` | BOOLEAN | NULLABLE | Whether to target (`false`) or exclude (`true`) the criterion. This field is immutable. To switch a criterion from positive to negative, remove then re-add it. |
| `ad_group_criterion_placement_url` | STRING | NULLABLE | URL of the placement. For example, \"http://www.domain.com\". |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `ad_group_criterion_tracking_url_template` | STRING | NULLABLE | The URL template for constructing a tracking URL. |
| `ad_group_criterion_url_custom_parameters` | STRING | NULLABLE | The list of mappings used to substitute custom parameter tags in a `tracking_url_template`, `final_urls`, or `mobile_final_urls`. |
| `ad_group_targeting_setting_target_restrictions` | STRING | NULLABLE | The per-targeting-dimension setting to restrict the reach of your campaign or ad group. |
| `bidding_strategy_name` | STRING | NULLABLE | The name of the bidding strategy. All bidding strategies within an account must be named distinctly. The length of this string should be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed). |
| `bidding_strategy_type` | STRING | NULLABLE | The type of the bidding strategy. Create a bidding strategy by setting the bidding scheme. This field is read-only. |
| `campaign_base_campaign` | STRING | NULLABLE | The resource name of the base campaign of a draft or experiment campaign. For base campaigns, this is equal to `resource_name`. This field is read-only. |
| `campaign_bidding_strategy` | STRING | NULLABLE | Portfolio bidding strategy used by campaign. |

#### Table: `p_ads_ProductGroupStats_2702575199`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_criterion_criterion_id` | INTEGER | NULLABLE | The ID of the criterion. This field is ignored for mutates. |
| `ad_group_criterion_listing_group_case_value_product_category_category_id` | STRING | NULLABLE | ID of the product category. This ID is equivalent to the google_product_category ID as described in this article: https://support.google.com/merchants/answer/6324436 |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `ad_group_criterion_cpc_bid_micros` | INTEGER | NULLABLE | The CPC (cost-per-click) bid. |
| `ad_group_criterion_display_name` | STRING | NULLABLE | The display name of the criterion. This field is ignored for mutates. |
| `ad_group_criterion_listing_group_case_value_product_brand_value` | STRING | NULLABLE | String value of the product brand. |
| `ad_group_criterion_listing_group_case_value_product_category_level` | STRING | NULLABLE | Level of the product category. |
| `ad_group_criterion_listing_group_case_value_product_channel_channel` | STRING | NULLABLE | Value of the locality. |
| `ad_group_criterion_listing_group_case_value_product_channel_exclusivity_channel_exclusivity` | STRING | NULLABLE | Value of the availability. |
| `ad_group_criterion_listing_group_case_value_product_condition_condition` | STRING | NULLABLE | Value of the condition. |
| `ad_group_criterion_listing_group_case_value_product_custom_attribute_index` | STRING | NULLABLE | Indicates the index of the custom attribute. |
| `ad_group_criterion_listing_group_case_value_product_custom_attribute_value` | STRING | NULLABLE | String value of the product custom attribute. |
| `ad_group_criterion_listing_group_case_value_product_item_id_value` | STRING | NULLABLE | Value of the id. |
| `ad_group_criterion_listing_group_case_value_product_type_level` | STRING | NULLABLE | Level of the type. |
| `ad_group_criterion_listing_group_case_value_product_type_value` | STRING | NULLABLE | Value of the type. |
| `ad_group_criterion_status` | STRING | NULLABLE | The status of the criterion. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `product_group_view_resource_name` | STRING | NULLABLE | The resource name of the product group view. Product group view resource names have the form: customers/{customer_id}/productGroupViews/{ad_group_id}~{criterion_id} |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_SearchQueryConversionStats_2702575199`

**Nombre de colonnes:** 27


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `search_term_view_search_term` | STRING | NULLABLE | The search term. |
| `search_term_view_status` | STRING | NULLABLE | Indicates whether the search term is currently one of your targeted or excluded keywords. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_keyword_ad_group_criterion` | STRING | NULLABLE | The AdGroupCriterion resource name. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_search_term_match_type` | STRING | NULLABLE | Match type of the keyword that triggered the ad, including variants. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_SearchQueryStats_2702575199`

**Nombre de colonnes:** 50


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `metrics_absolute_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown as the very first ad above the organic search results. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cost` | FLOAT | NULLABLE | The average amount you pay per interaction. This amount is the total cost of your ads divided by the total number of interactions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_average_cpe` | FLOAT | NULLABLE | The average amount that you've been charged for an ad engagement. This amount is the total cost of all ad engagements divided by the total number of ad engagements. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_interaction_event_types` | STRING | NULLABLE | The types of payable and free interactions. |
| `metrics_interaction_rate` | FLOAT | NULLABLE | How often people interact with your ad after it is shown to them. This is the number of interactions divided by the number of times your ad is shown. |
| `metrics_interactions` | INTEGER | NULLABLE | The number of interactions. An interaction is the main user action associated with an ad format-clicks for text and shopping ads, views for video ads, and so on. |
| `metrics_top_impression_percentage` | FLOAT | NULLABLE | The percent of your ad impressions that are shown anywhere above the organic search results. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `search_term_view_search_term` | STRING | NULLABLE | The search term. |
| `search_term_view_status` | STRING | NULLABLE | Indicates whether the search term is currently one of your targeted or excluded keywords. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_keyword_ad_group_criterion` | STRING | NULLABLE | The AdGroupCriterion resource name. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_search_term_match_type` | STRING | NULLABLE | Match type of the keyword that triggered the ad, including variants. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_ShoppingProductConversionStats_2702575199`

**Nombre de colonnes:** 46


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `segments_product_aggregator_id` | INTEGER | NULLABLE | Aggregator ID of the product. |
| `segments_product_item_id` | STRING | NULLABLE | Item ID of the product. |
| `segments_product_merchant_id` | INTEGER | NULLABLE | Merchant ID of the product. |
| `segments_product_store_id` | STRING | NULLABLE | Store ID of the product. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_product_brand` | STRING | NULLABLE | Brand of the product. |
| `segments_product_category_level1` | STRING | NULLABLE | Category (level 1) of the product. |
| `segments_product_category_level2` | STRING | NULLABLE | Category (level 2) of the product. |
| `segments_product_category_level3` | STRING | NULLABLE | Category (level 3) of the product. |
| `segments_product_category_level4` | STRING | NULLABLE | Category (level 4) of the product. |
| `segments_product_category_level5` | STRING | NULLABLE | Category (level 5) of the product. |
| `segments_product_channel` | STRING | NULLABLE | Channel of the product. |
| `segments_product_channel_exclusivity` | STRING | NULLABLE | Channel exclusivity of the product. |
| `segments_product_condition` | STRING | NULLABLE | Condition of the product. |
| `segments_product_country` | STRING | NULLABLE | Resource name of the geo target constant for the country of sale of the product. |
| `segments_product_custom_attribute0` | STRING | NULLABLE | Custom attribute 0 of the product. |
| `segments_product_custom_attribute1` | STRING | NULLABLE | Custom attribute 1 of the product. |
| `segments_product_custom_attribute2` | STRING | NULLABLE | Custom attribute 2 of the product. |
| `segments_product_custom_attribute3` | STRING | NULLABLE | Custom attribute 3 of the product. |
| `segments_product_custom_attribute4` | STRING | NULLABLE | Custom attribute 4 of the product. |
| `segments_product_language` | STRING | NULLABLE | Resource name of the language constant for the language of the product. |
| `segments_product_type_l1` | STRING | NULLABLE | Type (level 1) of the product. |
| `segments_product_type_l2` | STRING | NULLABLE | Type (level 2) of the product. |
| `segments_product_type_l3` | STRING | NULLABLE | Type (level 3) of the product. |
| `segments_product_type_l4` | STRING | NULLABLE | Type (level 4) of the product. |
| `segments_product_type_l5` | STRING | NULLABLE | Type (level 5) of the product. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_ShoppingProductStats_2702575199`

**Nombre de colonnes:** 55


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `segments_product_aggregator_id` | INTEGER | NULLABLE | Aggregator ID of the product. |
| `segments_product_item_id` | STRING | NULLABLE | Item ID of the product. |
| `segments_product_merchant_id` | INTEGER | NULLABLE | Merchant ID of the product. |
| `campaign_status` | STRING | NULLABLE | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpc` | FLOAT | NULLABLE | The total cost of all clicks divided by the total number of clicks received. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_from_interactions_rate` | FLOAT | NULLABLE | Conversions from interactions divided by the number of ad interactions (such as clicks for text ads or views for video ads). This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_search_absolute_top_impression_share` | FLOAT | NULLABLE | The percentage of the customer's Shopping or Search ad impressions that are shown in the most prominent Shopping position. See https://support.google.com/google-ads/answer/7501826 for details. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_click_share` | FLOAT | NULLABLE | The number of clicks you've received on the Search Network divided by the estimated number of clicks you were eligible to receive. Note: Search click share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_search_impression_share` | FLOAT | NULLABLE | The impressions you've received on the Search Network divided by the estimated number of impressions you were eligible to receive. Note: Search impression share is reported in the range of 0.1 to 1. Any value below 0.1 is reported as 0.0999. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_value_per_conversion` | FLOAT | NULLABLE | The value of conversions divided by the number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_product_brand` | STRING | NULLABLE | Brand of the product. |
| `segments_product_category_level1` | STRING | NULLABLE | Category (level 1) of the product. |
| `segments_product_category_level2` | STRING | NULLABLE | Category (level 2) of the product. |
| `segments_product_category_level3` | STRING | NULLABLE | Category (level 3) of the product. |
| `segments_product_category_level4` | STRING | NULLABLE | Category (level 4) of the product. |
| `segments_product_category_level5` | STRING | NULLABLE | Category (level 5) of the product. |
| `segments_product_channel` | STRING | NULLABLE | Channel of the product. |
| `segments_product_channel_exclusivity` | STRING | NULLABLE | Channel exclusivity of the product. |
| `segments_product_condition` | STRING | NULLABLE | Condition of the product. |
| `segments_product_country` | STRING | NULLABLE | Resource name of the geo target constant for the country of sale of the product. |
| `segments_product_custom_attribute0` | STRING | NULLABLE | Custom attribute 0 of the product. |
| `segments_product_custom_attribute1` | STRING | NULLABLE | Custom attribute 1 of the product. |
| `segments_product_custom_attribute2` | STRING | NULLABLE | Custom attribute 2 of the product. |
| `segments_product_custom_attribute3` | STRING | NULLABLE | Custom attribute 3 of the product. |
| `segments_product_custom_attribute4` | STRING | NULLABLE | Custom attribute 4 of the product. |
| `segments_product_language` | STRING | NULLABLE | Resource name of the language constant for the language of the product. |
| `segments_product_type_l1` | STRING | NULLABLE | Type (level 1) of the product. |
| `segments_product_type_l2` | STRING | NULLABLE | Type (level 2) of the product. |
| `segments_product_type_l3` | STRING | NULLABLE | Type (level 3) of the product. |
| `segments_product_type_l4` | STRING | NULLABLE | Type (level 4) of the product. |
| `segments_product_type_l5` | STRING | NULLABLE | Type (level 5) of the product. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_VideoBasicStats_2702575199`

**Nombre de colonnes:** 16


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `video_channel_id` | STRING | NULLABLE | The owner channel id of the video. |
| `video_id` | STRING | NULLABLE | The ID of the video. |
| `ad_group_ad_status` | STRING | NULLABLE | The status of the ad. |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `metrics_view_through_conversions` | INTEGER | NULLABLE | The total number of view-through conversions. These happen when a customer sees an image or rich media ad, then later completes a conversion on your site without interacting with (e.g., clicking on) another ad. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |

#### Table: `p_ads_VideoConversionStats_2702575199`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `video_channel_id` | STRING | NULLABLE | The owner channel id of the video. |
| `video_id` | STRING | NULLABLE | The ID of the video. |
| `ad_group_ad_status` | STRING | NULLABLE | The status of the ad. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_conversion_action` | STRING | NULLABLE | Resource name of the conversion action. |
| `segments_conversion_action_category` | STRING | NULLABLE | Conversion action category. |
| `segments_conversion_action_name` | STRING | NULLABLE | Conversion action name. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_VideoNonClickStats_2702575199`

**Nombre de colonnes:** 30


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `video_channel_id` | STRING | NULLABLE | The owner channel id of the video. |
| `video_id` | STRING | NULLABLE | The ID of the video. |
| `ad_group_ad_status` | STRING | NULLABLE | The status of the ad. |
| `metrics_all_conversions` | FLOAT | NULLABLE | The total number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_all_conversions_value` | FLOAT | NULLABLE | The total value of all conversions. |
| `metrics_average_cpv` | FLOAT | NULLABLE | The average amount you pay each time someone views your ad. The average CPV is defined by the total cost of all ad views divided by the number of views. |
| `metrics_cost_per_all_conversions` | FLOAT | NULLABLE | The cost of ad interactions divided by all conversions. |
| `metrics_cross_device_conversions` | FLOAT | NULLABLE | Conversions from when a customer clicks on a Google Ads ad on one device, then converts on a different device or browser. Cross-device conversions are already included in all_conversions. |
| `metrics_engagement_rate` | FLOAT | NULLABLE | How often people engage with your ad after it's shown to them. This is the number of ad expansions divided by the number of times your ad is shown. |
| `metrics_engagements` | INTEGER | NULLABLE | The number of engagements. An engagement occurs when a viewer expands your Lightbox ad. Also, in the future, other ad types may support engagement metrics. |
| `metrics_value_per_all_conversions` | FLOAT | NULLABLE | The value of all conversions divided by the number of all conversions. |
| `metrics_video_quartile_p100_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched all of your video. |
| `metrics_video_quartile_p25_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 25% of your video. |
| `metrics_video_quartile_p50_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 50% of your video. |
| `metrics_video_quartile_p75_rate` | FLOAT | NULLABLE | Percentage of impressions where the viewer watched 75% of your video. |
| `metrics_video_view_rate` | FLOAT | NULLABLE | The number of views your TrueView video ad receives divided by its number of impressions, including thumbnail impressions for TrueView in-display ads. |
| `metrics_video_views` | INTEGER | NULLABLE | The number of times your video ads were viewed. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_VideoStats_2702575199`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_ad_ad_id` | INTEGER | NULLABLE | The ID of the ad. |
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `video_channel_id` | STRING | NULLABLE | The owner channel id of the video. |
| `video_id` | STRING | NULLABLE | The ID of the video. |
| `ad_group_ad_status` | STRING | NULLABLE | The status of the ad. |
| `metrics_all_conversions_from_interactions_rate` | FLOAT | NULLABLE | All conversions from interactions (as oppose to view through conversions) divided by the number of ad interactions. |
| `metrics_average_cpm` | FLOAT | NULLABLE | Average cost-per-thousand impressions (CPM). |
| `metrics_clicks` | INTEGER | NULLABLE | The number of clicks. |
| `metrics_conversions` | FLOAT | NULLABLE | The number of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_conversions_value` | FLOAT | NULLABLE | The total value of conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_cost_micros` | INTEGER | NULLABLE | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. |
| `metrics_cost_per_conversion` | FLOAT | NULLABLE | The cost of ad interactions divided by conversions. This only includes conversion actions which include_in_conversions_metric attribute is set to true. |
| `metrics_ctr` | FLOAT | NULLABLE | The number of clicks your ad receives (Clicks) divided by the number of times your ad is shown (Impressions). |
| `metrics_impressions` | INTEGER | NULLABLE | Count of how often your ad has appeared on a search results page or website on the Google Network. |
| `segments_ad_network_type` | STRING | NULLABLE | Ad network type. |
| `segments_click_type` | STRING | NULLABLE | Click type. |
| `segments_date` | DATE | NULLABLE | Date to which metrics apply. yyyy-MM-dd format, e.g., 2018-04-17. |
| `segments_day_of_week` | STRING | NULLABLE | Day of the week, e.g., MONDAY. |
| `segments_device` | STRING | NULLABLE | Device to which metrics apply. |
| `segments_month` | DATE | NULLABLE | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. |
| `segments_quarter` | DATE | NULLABLE | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, e.g., the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. |
| `segments_week` | DATE | NULLABLE | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. |
| `segments_year` | INTEGER | NULLABLE | Year, formatted as yyyy. |

#### Table: `p_ads_Video_2702575199`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `ad_group_id` | INTEGER | NULLABLE | The ID of the ad group. |
| `campaign_id` | INTEGER | NULLABLE | The ID of the campaign. |
| `customer_id` | INTEGER | NULLABLE | The ID of the customer. |
| `video_id` | STRING | NULLABLE | The ID of the video. |
| `ad_group_ad_status` | STRING | NULLABLE | The status of the ad. |
| `video_duration_millis` | INTEGER | NULLABLE | The duration of the video in milliseconds. |
| `video_title` | STRING | NULLABLE | The title of the video. |

---

### Dataset: `google_ads_processed`

#### Table: `v_adgroup_daily`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `campaign_advertising_channel_type` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `device` | STRING | NULLABLE | - |
| `ad_network_type` | STRING | NULLABLE | - |
| `cost` | FLOAT | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `conversions` | FLOAT | NULLABLE | - |
| `conversions_value` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `conversion_rate` | FLOAT | NULLABLE | - |
| `cost_per_conversion` | FLOAT | NULLABLE | - |
| `roas` | FLOAT | NULLABLE | - |

#### Table: `v_asset_group_daily`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `asset_group_product_group_view_asset_group` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `device` | STRING | NULLABLE | - |
| `ad_network_type` | STRING | NULLABLE | - |
| `cost` | FLOAT | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `conversions` | FLOAT | NULLABLE | - |
| `conversions_value` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `roas` | FLOAT | NULLABLE | - |

#### Table: `v_campaign_daily`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `campaign_status` | STRING | NULLABLE | - |
| `campaign_advertising_channel_type` | STRING | NULLABLE | - |
| `campaign_bidding_strategy_type` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `week` | DATE | NULLABLE | - |
| `month` | DATE | NULLABLE | - |
| `device` | STRING | NULLABLE | - |
| `ad_network_type` | STRING | NULLABLE | - |
| `slot` | STRING | NULLABLE | - |
| `cost` | FLOAT | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `interactions` | INTEGER | NULLABLE | - |
| `conversions` | FLOAT | NULLABLE | - |
| `conversions_value` | FLOAT | NULLABLE | - |
| `view_through_conversions` | INTEGER | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `interaction_rate` | FLOAT | NULLABLE | - |
| `conversion_rate` | FLOAT | NULLABLE | - |
| `cost_per_conversion` | FLOAT | NULLABLE | - |
| `roas` | FLOAT | NULLABLE | - |
| `cpc` | FLOAT | NULLABLE | - |

#### Table: `v_search_term_daily`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `customer_id` | INTEGER | NULLABLE | - |
| `campaign_id` | INTEGER | NULLABLE | - |
| `campaign_name` | STRING | NULLABLE | - |
| `ad_group_id` | INTEGER | NULLABLE | - |
| `ad_group_name` | STRING | NULLABLE | - |
| `search_term` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `cost` | FLOAT | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `conversions` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `cpc` | FLOAT | NULLABLE | - |

---

### Dataset: `google_search_console_`

#### Table: `google_search_console_best_keywords`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `position` | FLOAT | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |

#### Table: `google_search_console_keyword_performance`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `page` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `brand_type` | STRING | NULLABLE | - |
| `device_type` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `position` | FLOAT | NULLABLE | - |
| `country` | STRING | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |

#### Table: `google_search_console_sitemap_performance`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `date` | DATE | NULLABLE | - |
| `site_url` | STRING | NULLABLE | - |
| `page_url` | STRING | NULLABLE | - |
| `query` | STRING | NULLABLE | - |
| `is_amp` | BOOLEAN | NULLABLE | - |
| `country` | STRING | NULLABLE | - |
| `search_type` | STRING | NULLABLE | - |
| `device` | STRING | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `sum_top_position` | FLOAT | NULLABLE | - |

---

### Dataset: `googleanalytics_`

#### Table: `google_analytics_device_sessions_breakdown`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `page_location` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `sessions` | INTEGER | NULLABLE | - |
| `property_name` | STRING | NULLABLE | - |

#### Table: `google_analytics_event_metrics`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `event_value` | FLOAT | NULLABLE | - |
| `sessions` | INTEGER | NULLABLE | - |
| `bounce_rate` | FLOAT | NULLABLE | - |
| `event_count` | INTEGER | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `user_engagement_duration` | INTEGER | NULLABLE | - |
| `total_users` | INTEGER | NULLABLE | - |
| `average_session_duration` | FLOAT | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `events_per_session` | FLOAT | NULLABLE | - |
| `new_users` | INTEGER | NULLABLE | - |
| `property_name` | STRING | NULLABLE | - |

#### Table: `google_analytics_geo_channel`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `total_users` | INTEGER | NULLABLE | - |
| `session_primary_channel_group` | STRING | NULLABLE | - |
| `date` | STRING | NULLABLE | - |
| `property_name` | STRING | NULLABLE | - |

#### Table: `google_analytics_user_engagement`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `event_value` | FLOAT | NULLABLE | - |
| `sessions` | INTEGER | NULLABLE | - |
| `bounce_rate` | FLOAT | NULLABLE | - |
| `event_count` | INTEGER | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `user_engagement_duration` | INTEGER | NULLABLE | - |
| `total_users` | INTEGER | NULLABLE | - |
| `average_session_duration` | FLOAT | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `events_per_session` | FLOAT | NULLABLE | - |
| `new_users` | INTEGER | NULLABLE | - |
| `property_name` | STRING | NULLABLE | - |

---

### Dataset: `linkedin_ads_advertising`

#### Table: `campaign_analytics`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `cost_in_usd` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `cpc` | FLOAT | NULLABLE | - |
| `cpm` | FLOAT | NULLABLE | - |
| `reactions` | INTEGER | NULLABLE | - |
| `comments` | INTEGER | NULLABLE | - |
| `shares` | INTEGER | NULLABLE | - |
| `total_engagements` | INTEGER | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `landing_page_clicks` | INTEGER | NULLABLE | - |
| `one_click_leads` | INTEGER | NULLABLE | - |
| `external_website_conversions` | INTEGER | NULLABLE | - |
| `external_website_post_click_conversions` | INTEGER | NULLABLE | - |
| `external_website_post_view_conversions` | INTEGER | NULLABLE | - |
| `video_views` | INTEGER | NULLABLE | - |
| `video_starts` | INTEGER | NULLABLE | - |
| `video_completions` | INTEGER | NULLABLE | - |
| `campaign_urn` | STRING | NULLABLE | - |
| `campaign_id` | STRING | NULLABLE | - |
| `retrieved_at` | DATETIME | NULLABLE | - |
| `date_range_start` | DATE | NULLABLE | - |
| `date_range_end` | DATE | NULLABLE | - |

#### Table: `campaign_budget`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `campaign_urn` | STRING | NULLABLE | - |
| `total_budget` | FLOAT | NULLABLE | - |
| `daily_budget` | INTEGER | NULLABLE | - |
| `lifetime_budget` | FLOAT | NULLABLE | - |
| `budget_remaining` | FLOAT | NULLABLE | - |
| `budget_spent` | FLOAT | NULLABLE | - |
| `billing_currency` | STRING | NULLABLE | - |
| `bid_type` | STRING | NULLABLE | - |
| `bid_amount` | FLOAT | NULLABLE | - |
| `bid_multiplier` | FLOAT | NULLABLE | - |
| `bid_adjustment_type` | STRING | NULLABLE | - |
| `min_bid` | FLOAT | NULLABLE | - |
| `max_bid` | FLOAT | NULLABLE | - |
| `pacing_type` | STRING | NULLABLE | - |
| `pacing_rate` | FLOAT | NULLABLE | - |
| `start_date` | DATE | NULLABLE | - |
| `end_date` | DATE | NULLABLE | - |
| `retrieved_at` | DATETIME | NULLABLE | - |

#### Table: `creative_analytics`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `cost_in_usd` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `cpc` | FLOAT | NULLABLE | - |
| `cpm` | FLOAT | NULLABLE | - |
| `reactions` | INTEGER | NULLABLE | - |
| `comments` | INTEGER | NULLABLE | - |
| `shares` | INTEGER | NULLABLE | - |
| `total_engagements` | INTEGER | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `landing_page_clicks` | INTEGER | NULLABLE | - |
| `one_click_leads` | INTEGER | NULLABLE | - |
| `external_website_conversions` | INTEGER | NULLABLE | - |
| `external_website_post_click_conversions` | INTEGER | NULLABLE | - |
| `external_website_post_view_conversions` | INTEGER | NULLABLE | - |
| `video_views` | INTEGER | NULLABLE | - |
| `video_starts` | INTEGER | NULLABLE | - |
| `video_completions` | INTEGER | NULLABLE | - |
| `creative_urn` | STRING | NULLABLE | - |
| `creative_id` | STRING | NULLABLE | - |
| `retrieved_at` | DATETIME | NULLABLE | - |
| `date_range_start` | DATE | NULLABLE | - |
| `date_range_end` | DATE | NULLABLE | - |

#### Table: `creative_budget`

**Nombre de colonnes:** 21


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `campaign_urn` | STRING | NULLABLE | - |
| `creative_id` | STRING | NULLABLE | - |
| `creative_urn` | STRING | NULLABLE | - |
| `total_budget` | FLOAT | NULLABLE | - |
| `daily_budget` | INTEGER | NULLABLE | - |
| `lifetime_budget` | FLOAT | NULLABLE | - |
| `budget_remaining` | FLOAT | NULLABLE | - |
| `budget_spent` | FLOAT | NULLABLE | - |
| `billing_currency` | STRING | NULLABLE | - |
| `bid_type` | STRING | NULLABLE | - |
| `bid_amount` | FLOAT | NULLABLE | - |
| `bid_multiplier` | FLOAT | NULLABLE | - |
| `bid_adjustment_type` | STRING | NULLABLE | - |
| `min_bid` | FLOAT | NULLABLE | - |
| `max_bid` | FLOAT | NULLABLE | - |
| `pacing_type` | STRING | NULLABLE | - |
| `pacing_rate` | FLOAT | NULLABLE | - |
| `start_date` | DATE | NULLABLE | - |
| `end_date` | DATE | NULLABLE | - |
| `retrieved_at` | DATETIME | NULLABLE | - |

#### Table: `v_active_campaign_budgets`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `campaign_urn` | STRING | NULLABLE | - |
| `daily_budget` | FLOAT | NULLABLE | - |
| `lifetime_budget` | FLOAT | NULLABLE | - |
| `budget_spent` | FLOAT | NULLABLE | - |
| `budget_remaining` | FLOAT | NULLABLE | - |
| `budget_utilization_pct` | FLOAT | NULLABLE | - |
| `billing_currency` | STRING | NULLABLE | - |
| `bid_type` | STRING | NULLABLE | - |
| `bid_amount` | FLOAT | NULLABLE | - |
| `start_date` | DATE | NULLABLE | - |
| `end_date` | DATE | NULLABLE | - |
| `is_currently_active` | BOOLEAN | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `v_campaign_budget_summary`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `data_points` | INTEGER | NULLABLE | - |
| `first_seen` | TIMESTAMP | NULLABLE | - |
| `last_seen` | TIMESTAMP | NULLABLE | - |
| `current_budget_spent` | FLOAT | NULLABLE | - |
| `current_budget_remaining` | FLOAT | NULLABLE | - |
| `lifetime_budget` | FLOAT | NULLABLE | - |
| `avg_daily_budget` | FLOAT | NULLABLE | - |
| `current_bid_amount` | FLOAT | NULLABLE | - |

#### Table: `v_campaign_creative_reconciliation`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `campaign_impressions` | INTEGER | NULLABLE | - |
| `creative_impressions_sum` | INTEGER | NULLABLE | - |
| `campaign_clicks` | INTEGER | NULLABLE | - |
| `creative_clicks_sum` | INTEGER | NULLABLE | - |
| `campaign_cost` | FLOAT | NULLABLE | - |
| `creative_cost_sum` | FLOAT | NULLABLE | - |
| `num_creatives` | INTEGER | NULLABLE | - |
| `avg_impressions_per_creative` | FLOAT | NULLABLE | - |
| `avg_cost_per_creative` | FLOAT | NULLABLE | - |
| `impressions_diff` | INTEGER | NULLABLE | - |
| `cost_diff` | FLOAT | NULLABLE | - |

#### Table: `v_latest_campaign_metrics`

**Nombre de colonnes:** 18


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `campaign_urn` | STRING | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `cost_in_usd` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `cpc` | FLOAT | NULLABLE | - |
| `cpm` | FLOAT | NULLABLE | - |
| `total_engagements` | INTEGER | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `one_click_leads` | INTEGER | NULLABLE | - |
| `external_website_conversions` | INTEGER | NULLABLE | - |
| `video_views` | INTEGER | NULLABLE | - |
| `video_completions` | INTEGER | NULLABLE | - |
| `approximate_member_reach` | INTEGER | NULLABLE | - |
| `date_range_start` | DATE | NULLABLE | - |
| `date_range_end` | DATE | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `v_overall_performance`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `report_date` | DATE | NULLABLE | - |
| `num_campaigns` | INTEGER | NULLABLE | - |
| `total_impressions` | INTEGER | NULLABLE | - |
| `total_clicks` | INTEGER | NULLABLE | - |
| `total_cost` | FLOAT | NULLABLE | - |
| `overall_ctr` | FLOAT | NULLABLE | - |
| `overall_cpc` | FLOAT | NULLABLE | - |
| `overall_cpm` | FLOAT | NULLABLE | - |
| `total_engagements` | INTEGER | NULLABLE | - |
| `overall_engagement_rate` | FLOAT | NULLABLE | - |
| `total_leads` | INTEGER | NULLABLE | - |
| `total_conversions` | INTEGER | NULLABLE | - |

#### Table: `v_top_creatives_by_campaign`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `creative_id` | STRING | NULLABLE | - |
| `creative_urn` | STRING | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `cost_in_usd` | FLOAT | NULLABLE | - |
| `ctr` | FLOAT | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `total_engagements` | INTEGER | NULLABLE | - |
| `rank_in_campaign` | INTEGER | NULLABLE | - |

---

### Dataset: `linkedin_ads_library`

#### Table: `ads_library`

**Nombre de colonnes:** 22


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `Keyword` | STRING | NULLABLE | - |
| `Countries` | STRING | NULLABLE | - |
| `Advertiser` | STRING | NULLABLE | - |
| `Date_Range` | STRING | NULLABLE | - |
| `Paging_Context` | STRING | NULLABLE | - |
| `Ad_URL` | STRING | NULLABLE | - |
| `Is_Restricted` | BOOLEAN | NULLABLE | - |
| `Restriction_Details` | STRING | NULLABLE | - |
| `Advertiser_Name` | STRING | NULLABLE | - |
| `Advertiser_URL` | STRING | NULLABLE | - |
| `Ad_Payer` | STRING | NULLABLE | - |
| `Facet_Name` | STRING | NULLABLE | - |
| `Is_Inclusive` | STRING | NULLABLE | - |
| `Inclusive_Segments` | STRING | NULLABLE | - |
| `Is_Exclusive` | STRING | NULLABLE | - |
| `Exclusive_Segments` | STRING | NULLABLE | - |
| `First_Impression_Date` | DATE | NULLABLE | - |
| `Latest_Impression_Date` | DATE | NULLABLE | - |
| `Total_Impressions_Range` | STRING | NULLABLE | - |
| `Impressions_Distribution_by_Country` | STRING | NULLABLE | - |
| `Ad_Type` | STRING | NULLABLE | - |
| `Retrieved_At` | TIMESTAMP | NULLABLE | - |

---

### Dataset: `linkedin_leadgen_form`

#### Table: `lead_form_metrics`

**Nombre de colonnes:** 23


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `form_id` | STRING | REQUIRED | - |
| `campaign_id` | STRING | NULLABLE | - |
| `date` | DATE | REQUIRED | - |
| `total_leads` | INTEGER | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `ad_spend` | FLOAT | NULLABLE | - |
| `submission_rate` | FLOAT | NULLABLE | - |
| `conversion_rate` | FLOAT | NULLABLE | - |
| `cost_per_lead` | FLOAT | NULLABLE | - |
| `avg_time_to_first_notification` | FLOAT | NULLABLE | - |
| `avg_time_to_full_fetch` | FLOAT | NULLABLE | - |
| `field_completion_rate` | FLOAT | NULLABLE | - |
| `consent_opt_in_rate` | FLOAT | NULLABLE | - |
| `email_validity_rate` | FLOAT | NULLABLE | - |
| `lead_quality_score` | FLOAT | NULLABLE | - |
| `lead_to_opportunity_count` | INTEGER | NULLABLE | - |
| `lead_to_opportunity_rate` | FLOAT | NULLABLE | - |
| `sla_breach_count` | INTEGER | NULLABLE | - |
| `anomaly_detected` | BOOLEAN | NULLABLE | - |
| `anomaly_description` | STRING | NULLABLE | - |
| `calculated_at` | TIMESTAMP | REQUIRED | - |
| `updated_at` | TIMESTAMP | NULLABLE | - |

#### Table: `lead_form_responses`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `lead_response_id` | STRING | REQUIRED | - |
| `form_id` | STRING | REQUIRED | - |
| `organization_id` | STRING | NULLABLE | - |
| `ad_account_id` | STRING | NULLABLE | - |
| `lead_type` | STRING | NULLABLE | - |
| `submitted_at` | TIMESTAMP | NULLABLE | - |
| `notification_received_at` | TIMESTAMP | NULLABLE | - |
| `fetched_at` | TIMESTAMP | NULLABLE | - |
| `first_name` | STRING | NULLABLE | - |
| `last_name` | STRING | NULLABLE | - |
| `email_address` | STRING | NULLABLE | - |
| `phone_number` | STRING | NULLABLE | - |
| `company_name` | STRING | NULLABLE | - |
| `job_title` | STRING | NULLABLE | - |
| `country` | STRING | NULLABLE | - |
| `campaign_id` | STRING | NULLABLE | - |
| `campaign_group_id` | STRING | NULLABLE | - |
| `creative_id` | STRING | NULLABLE | - |
| `device_type` | STRING | NULLABLE | - |
| `custom_fields` | JSON | NULLABLE | - |
| `consent_granted` | BOOLEAN | NULLABLE | - |
| `form_data` | JSON | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |
| `updated_at` | TIMESTAMP | NULLABLE | - |

#### Table: `lead_forms`

**Nombre de colonnes:** 15


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `form_id` | STRING | REQUIRED | - |
| `lead_form_urn` | STRING | NULLABLE | - |
| `organization_id` | STRING | NULLABLE | - |
| `ad_account_id` | STRING | NULLABLE | - |
| `name` | STRING | NULLABLE | - |
| `locale` | STRING | NULLABLE | - |
| `status` | STRING | NULLABLE | - |
| `lead_type` | STRING | NULLABLE | - |
| `privacy_policy_url` | STRING | NULLABLE | - |
| `custom_disclaimer` | STRING | NULLABLE | - |
| `confirmation_message` | STRING | NULLABLE | - |
| `created_at` | TIMESTAMP | NULLABLE | - |
| `last_modified_at` | TIMESTAMP | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |
| `updated_at` | TIMESTAMP | NULLABLE | - |

#### Table: `v_lead_performance_by_campaign`

**Nombre de colonnes:** 13


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `campaign_id` | STRING | NULLABLE | - |
| `form_id` | STRING | NULLABLE | - |
| `form_name` | STRING | NULLABLE | - |
| `total_leads` | INTEGER | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `ad_spend` | FLOAT | NULLABLE | - |
| `submission_rate` | FLOAT | NULLABLE | - |
| `conversion_rate` | FLOAT | NULLABLE | - |
| `cost_per_lead` | FLOAT | NULLABLE | - |
| `active_days` | INTEGER | NULLABLE | - |
| `first_lead` | TIMESTAMP | NULLABLE | - |
| `last_lead` | TIMESTAMP | NULLABLE | - |

#### Table: `v_lead_quality_dashboard`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `form_id` | STRING | NULLABLE | - |
| `form_name` | STRING | NULLABLE | - |
| `status` | STRING | NULLABLE | - |
| `total_leads` | INTEGER | NULLABLE | - |
| `field_completion_rate` | FLOAT | NULLABLE | - |
| `email_validity_rate` | FLOAT | NULLABLE | - |
| `consent_opt_in_rate` | FLOAT | NULLABLE | - |
| `lead_quality_score` | FLOAT | NULLABLE | - |
| `avg_notification_time_seconds` | FLOAT | NULLABLE | - |
| `avg_fetch_time_seconds` | FLOAT | NULLABLE | - |

#### Table: `v_lead_sla_monitoring`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `form_id` | STRING | NULLABLE | - |
| `lead_response_id` | STRING | NULLABLE | - |
| `submitted_at` | TIMESTAMP | NULLABLE | - |
| `notification_received_at` | TIMESTAMP | NULLABLE | - |
| `fetched_at` | TIMESTAMP | NULLABLE | - |
| `notification_latency_seconds` | INTEGER | NULLABLE | - |
| `fetch_latency_seconds` | INTEGER | NULLABLE | - |
| `sla_breached` | BOOLEAN | NULLABLE | - |

#### Table: `v_lead_volume_anomalies`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `form_id` | STRING | NULLABLE | - |
| `form_name` | STRING | NULLABLE | - |
| `date` | DATE | NULLABLE | - |
| `daily_leads` | INTEGER | NULLABLE | - |
| `rolling_7day_avg` | FLOAT | NULLABLE | - |
| `pct_change` | FLOAT | NULLABLE | - |
| `anomaly_detected` | BOOLEAN | NULLABLE | - |
| `anomaly_type` | STRING | NULLABLE | - |

---

### Dataset: `linkedin_page`

#### Table: `content_statistics`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `organization_id` | STRING | REQUIRED | - |
| `time_start` | DATE | REQUIRED | - |
| `time_end` | DATE | REQUIRED | - |
| `unique_impressions_count` | INTEGER | NULLABLE | - |
| `impression_count` | INTEGER | NULLABLE | - |
| `click_count` | INTEGER | NULLABLE | - |
| `like_count` | INTEGER | NULLABLE | - |
| `comment_count` | INTEGER | NULLABLE | - |
| `share_count` | INTEGER | NULLABLE | - |
| `engagement_rate` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |

#### Table: `followers`

**Nombre de colonnes:** 6


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `organization_id` | STRING | REQUIRED | - |
| `dimension_type` | STRING | REQUIRED | - |
| `dimension_value` | STRING | REQUIRED | - |
| `organic_follower_count` | INTEGER | NULLABLE | - |
| `paid_follower_count` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |

#### Table: `followers_timeseries`

**Nombre de colonnes:** 6


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `organization_id` | STRING | REQUIRED | - |
| `time_start` | DATE | REQUIRED | - |
| `time_end` | DATE | REQUIRED | - |
| `organic_follower_gain` | INTEGER | NULLABLE | - |
| `paid_follower_gain` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |

#### Table: `page_statistics`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `organization_id` | STRING | REQUIRED | - |
| `dimension_type` | STRING | REQUIRED | - |
| `dimension_value` | STRING | NULLABLE | - |
| `page_views` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |

#### Table: `page_statistics_timeseries`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `organization_id` | STRING | REQUIRED | - |
| `time_start` | DATE | REQUIRED | - |
| `time_end` | DATE | REQUIRED | - |
| `page_views` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | REQUIRED | - |

---

### Dataset: `microsoft_clarity`

#### Table: `clarity_metrics`

**Nombre de colonnes:** 20


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `date` | DATE | REQUIRED | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `visits_count` | INTEGER | NULLABLE | - |
| `scroll_depth` | RECORD | NULLABLE | - |
| `engagement_time` | RECORD | NULLABLE | - |
| `traffic` | RECORD | NULLABLE | - |
| `browser` | RECORD | REPEATED | - |
| `device` | RECORD | REPEATED | - |
| `os` | RECORD | REPEATED | - |
| `country` | RECORD | REPEATED | - |
| `page_title` | RECORD | REPEATED | - |
| `referrer_url` | RECORD | REPEATED | - |
| `dead_clicks` | RECORD | NULLABLE | - |
| `excessive_scroll` | RECORD | NULLABLE | - |
| `rage_clicks` | RECORD | NULLABLE | - |
| `quickback_clicks` | RECORD | NULLABLE | - |
| `script_errors` | RECORD | NULLABLE | - |
| `error_clicks` | RECORD | NULLABLE | - |
| `project_name` | STRING | NULLABLE | - |

---

### Dataset: `searchconsole_EPBS`

#### Table: `ExportLog`

**Nombre de colonnes:** 5


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `agenda` | STRING | NULLABLE | - |
| `namespace` | STRING | NULLABLE | - |
| `data_date` | DATE | NULLABLE | - |
| `epoch_version` | INTEGER | NULLABLE | - |
| `publish_time` | TIMESTAMP | NULLABLE | - |

#### Table: `searchdata_site_impression`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `data_date` | DATE | NULLABLE | - |
| `site_url` | STRING | NULLABLE | - |
| `query` | STRING | NULLABLE | - |
| `is_anonymized_query` | BOOLEAN | NULLABLE | - |
| `country` | STRING | NULLABLE | - |
| `search_type` | STRING | NULLABLE | - |
| `device` | STRING | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `sum_top_position` | INTEGER | NULLABLE | - |

#### Table: `searchdata_url_impression`

**Nombre de colonnes:** 42


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `data_date` | DATE | NULLABLE | - |
| `site_url` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `query` | STRING | NULLABLE | - |
| `is_anonymized_query` | BOOLEAN | NULLABLE | - |
| `is_anonymized_discover` | BOOLEAN | NULLABLE | - |
| `country` | STRING | NULLABLE | - |
| `search_type` | STRING | NULLABLE | - |
| `device` | STRING | NULLABLE | - |
| `is_amp_top_stories` | BOOLEAN | NULLABLE | - |
| `is_amp_blue_link` | BOOLEAN | NULLABLE | - |
| `is_job_listing` | BOOLEAN | NULLABLE | - |
| `is_job_details` | BOOLEAN | NULLABLE | - |
| `is_tpf_qa` | BOOLEAN | NULLABLE | - |
| `is_tpf_faq` | BOOLEAN | NULLABLE | - |
| `is_tpf_howto` | BOOLEAN | NULLABLE | - |
| `is_weblite` | BOOLEAN | NULLABLE | - |
| `is_action` | BOOLEAN | NULLABLE | - |
| `is_events_listing` | BOOLEAN | NULLABLE | - |
| `is_events_details` | BOOLEAN | NULLABLE | - |
| `is_forums` | BOOLEAN | NULLABLE | - |
| `is_search_appearance_android_app` | BOOLEAN | NULLABLE | - |
| `is_amp_story` | BOOLEAN | NULLABLE | - |
| `is_amp_image_result` | BOOLEAN | NULLABLE | - |
| `is_video` | BOOLEAN | NULLABLE | - |
| `is_organic_shopping` | BOOLEAN | NULLABLE | - |
| `is_review_snippet` | BOOLEAN | NULLABLE | - |
| `is_special_announcement` | BOOLEAN | NULLABLE | - |
| `is_recipe_feature` | BOOLEAN | NULLABLE | - |
| `is_recipe_rich_snippet` | BOOLEAN | NULLABLE | - |
| `is_subscribed_content` | BOOLEAN | NULLABLE | - |
| `is_page_experience` | BOOLEAN | NULLABLE | - |
| `is_practice_problems` | BOOLEAN | NULLABLE | - |
| `is_math_solvers` | BOOLEAN | NULLABLE | - |
| `is_translated_result` | BOOLEAN | NULLABLE | - |
| `is_edu_q_and_a` | BOOLEAN | NULLABLE | - |
| `is_product_snippets` | BOOLEAN | NULLABLE | - |
| `is_merchant_listings` | BOOLEAN | NULLABLE | - |
| `is_learning_videos` | BOOLEAN | NULLABLE | - |
| `impressions` | INTEGER | NULLABLE | - |
| `clicks` | INTEGER | NULLABLE | - |
| `sum_position` | INTEGER | NULLABLE | - |

---

### Dataset: `spyfu`

#### Table: `active_ads_analysis`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `total_ads` | INTEGER | NULLABLE | - |
| `total_keywords` | INTEGER | NULLABLE | - |
| `avg_cpc` | FLOAT | NULLABLE | - |
| `total_monthly_spend` | FLOAT | NULLABLE | - |
| `avg_days_active` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `ads_by_keyword`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `keyword` | STRING | NULLABLE | - |
| `advertisers_count` | INTEGER | NULLABLE | - |
| `total_ads` | INTEGER | NULLABLE | - |
| `avg_cpc` | FLOAT | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `competing_domains` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `best_ad_headlines_by_keyword`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `keyword` | STRING | NULLABLE | - |
| `domain` | STRING | NULLABLE | - |
| `headline` | STRING | NULLABLE | - |
| `description` | STRING | NULLABLE | - |
| `days_seen` | INTEGER | NULLABLE | - |
| `cost_per_click` | FLOAT | NULLABLE | - |
| `position` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `cpc_analysis`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `phrase_monthly_cost` | FLOAT | NULLABLE | - |
| `exact_monthly_cost` | FLOAT | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_ad_history`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `ad_id` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `headline` | STRING | NULLABLE | - |
| `description` | STRING | NULLABLE | - |
| `display_url` | STRING | NULLABLE | - |
| `destination_url` | STRING | NULLABLE | - |
| `first_seen_date` | DATE | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `cost_per_click` | FLOAT | NULLABLE | - |
| `monthly_cost` | FLOAT | NULLABLE | - |
| `position` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_page_performance`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `total_pages` | INTEGER | NULLABLE | - |
| `total_keywords` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `avg_clicks_per_page` | FLOAT | NULLABLE | - |
| `avg_keywords_per_page` | FLOAT | NULLABLE | - |
| `top_page_clicks` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_performance_overview`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `total_ad_keywords` | INTEGER | NULLABLE | - |
| `total_seo_keywords` | INTEGER | NULLABLE | - |
| `total_organic_traffic` | INTEGER | NULLABLE | - |
| `total_ad_budget` | FLOAT | NULLABLE | - |
| `domain_rank` | INTEGER | NULLABLE | - |
| `domain_authority` | FLOAT | NULLABLE | - |
| `ppc_keywords_tracked` | INTEGER | NULLABLE | - |
| `seo_keywords_tracked` | INTEGER | NULLABLE | - |
| `active_ads` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_spend_by_keyword`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `keyword` | STRING | NULLABLE | - |
| `domain_name` | STRING | NULLABLE | - |
| `budget` | FLOAT | NULLABLE | - |
| `total_ads_purchased` | INTEGER | NULLABLE | - |
| `ad_count` | INTEGER | NULLABLE | - |
| `coverage` | INTEGER | NULLABLE | - |
| `percentage_leaderboard` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_stats`

**Nombre de colonnes:** 14


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `country_code` | STRING | NULLABLE | - |
| `total_ad_keywords` | INTEGER | NULLABLE | - |
| `total_ad_budget` | FLOAT | NULLABLE | - |
| `total_ad_clicks` | INTEGER | NULLABLE | - |
| `ad_history_months` | INTEGER | NULLABLE | - |
| `total_seo_keywords` | INTEGER | NULLABLE | - |
| `total_organic_keywords` | INTEGER | NULLABLE | - |
| `total_organic_traffic` | INTEGER | NULLABLE | - |
| `total_organic_value` | FLOAT | NULLABLE | - |
| `domain_rank` | INTEGER | NULLABLE | - |
| `domain_authority` | FLOAT | NULLABLE | - |
| `raw_stats` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_stats_comparison`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `total_ad_keywords` | INTEGER | NULLABLE | - |
| `total_seo_keywords` | INTEGER | NULLABLE | - |
| `total_organic_traffic` | INTEGER | NULLABLE | - |
| `total_organic_value` | FLOAT | NULLABLE | - |
| `total_ad_budget` | FLOAT | NULLABLE | - |
| `domain_rank` | INTEGER | NULLABLE | - |
| `domain_authority` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `domain_stats_evolution`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `total_ad_keywords` | INTEGER | NULLABLE | - |
| `total_seo_keywords` | INTEGER | NULLABLE | - |
| `total_organic_traffic` | INTEGER | NULLABLE | - |
| `total_ad_budget` | FLOAT | NULLABLE | - |
| `domain_rank` | INTEGER | NULLABLE | - |
| `domain_authority` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `estimated_roi_analysis`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `tracked_keywords` | INTEGER | NULLABLE | - |
| `total_search_volume` | INTEGER | NULLABLE | - |
| `avg_cpc` | FLOAT | NULLABLE | - |
| `estimated_monthly_ppc_spend` | FLOAT | NULLABLE | - |
| `active_ads` | INTEGER | NULLABLE | - |
| `actual_monthly_ad_spend` | FLOAT | NULLABLE | - |
| `total_organic_clicks` | INTEGER | NULLABLE | - |
| `estimated_organic_value` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `keyword_clusters`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `source_keyword` | STRING | NULLABLE | - |
| `related_count` | INTEGER | NULLABLE | - |
| `avg_related_volume` | FLOAT | NULLABLE | - |
| `avg_difficulty` | FLOAT | NULLABLE | - |
| `avg_cpc` | FLOAT | NULLABLE | - |
| `total_potential_volume` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `keyword_expansion_opportunities`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `source_keyword` | STRING | NULLABLE | - |
| `related_keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `opportunity_score` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `keyword_opportunities`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `keyword_rich_pages`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `title` | STRING | NULLABLE | - |
| `keyword_count` | INTEGER | NULLABLE | - |
| `est_monthly_seo_clicks` | INTEGER | NULLABLE | - |
| `top_keyword` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `most_valuable_keywords`

**Nombre de colonnes:** 25


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `keyword` | STRING | NULLABLE | - |
| `top_ranked_url` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `rank_change` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `seo_clicks_change` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `percent_mobile_searches` | FLOAT | NULLABLE | - |
| `percent_desktop_searches` | FLOAT | NULLABLE | - |
| `percent_not_clicked` | FLOAT | NULLABLE | - |
| `percent_paid_clicks` | FLOAT | NULLABLE | - |
| `percent_organic_clicks` | FLOAT | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `phrase_monthly_cost` | FLOAT | NULLABLE | - |
| `exact_monthly_cost` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `ranking_homepages` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `most_valuable_pages`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `url` | STRING | NULLABLE | - |
| `title` | STRING | NULLABLE | - |
| `est_monthly_seo_clicks` | INTEGER | NULLABLE | - |
| `keyword_count` | INTEGER | NULLABLE | - |
| `top_keyword` | STRING | NULLABLE | - |
| `top_keyword_position` | INTEGER | NULLABLE | - |
| `top_keyword_search_volume` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `most_valuable_seo_keywords`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `rank_change` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `seo_clicks_change` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `top_ranked_url` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `new_keyword_opportunities`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `is_question` | BOOLEAN | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `new_keywords`

**Nombre de colonnes:** 29


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `live_search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `percent_mobile_searches` | FLOAT | NULLABLE | - |
| `percent_desktop_searches` | FLOAT | NULLABLE | - |
| `percent_searches_not_clicked` | FLOAT | NULLABLE | - |
| `percent_paid_clicks` | FLOAT | NULLABLE | - |
| `percent_organic_clicks` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `broad_monthly_clicks` | INTEGER | NULLABLE | - |
| `phrase_monthly_clicks` | INTEGER | NULLABLE | - |
| `exact_monthly_clicks` | INTEGER | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `phrase_monthly_cost` | FLOAT | NULLABLE | - |
| `exact_monthly_cost` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `distinct_competitors` | STRING | NULLABLE | - |
| `ranking_homepages` | INTEGER | NULLABLE | - |
| `serp_features_csv` | STRING | NULLABLE | - |
| `serp_first_result` | STRING | NULLABLE | - |
| `is_question` | BOOLEAN | NULLABLE | - |
| `is_not_safe_for_work` | BOOLEAN | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `new_keywords_by_domain`

**Nombre de colonnes:** 8


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `newly_ranked_keywords`

**Nombre de colonnes:** 24


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `keyword` | STRING | NULLABLE | - |
| `top_ranked_url` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `seo_clicks_change` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `percent_mobile_searches` | FLOAT | NULLABLE | - |
| `percent_desktop_searches` | FLOAT | NULLABLE | - |
| `percent_not_clicked` | FLOAT | NULLABLE | - |
| `percent_paid_clicks` | FLOAT | NULLABLE | - |
| `percent_organic_clicks` | FLOAT | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `phrase_monthly_cost` | FLOAT | NULLABLE | - |
| `exact_monthly_cost` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `ranking_homepages` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `newly_ranked_top_keywords`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `estimated_value` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `ppc_keywords`

**Nombre de colonnes:** 29


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `live_search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `percent_mobile_searches` | FLOAT | NULLABLE | - |
| `percent_desktop_searches` | FLOAT | NULLABLE | - |
| `percent_searches_not_clicked` | FLOAT | NULLABLE | - |
| `percent_paid_clicks` | FLOAT | NULLABLE | - |
| `percent_organic_clicks` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `broad_monthly_clicks` | INTEGER | NULLABLE | - |
| `phrase_monthly_clicks` | INTEGER | NULLABLE | - |
| `exact_monthly_clicks` | INTEGER | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `phrase_monthly_cost` | FLOAT | NULLABLE | - |
| `exact_monthly_cost` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `distinct_competitors` | STRING | NULLABLE | - |
| `ranking_homepages` | INTEGER | NULLABLE | - |
| `serp_features_csv` | STRING | NULLABLE | - |
| `serp_first_result` | STRING | NULLABLE | - |
| `is_question` | BOOLEAN | NULLABLE | - |
| `is_not_safe_for_work` | BOOLEAN | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `related_keywords`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `source_keyword` | STRING | REQUIRED | - |
| `related_keyword` | STRING | REQUIRED | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `seo_keywords`

**Nombre de colonnes:** 26


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `keyword` | STRING | NULLABLE | - |
| `search_type` | STRING | NULLABLE | - |
| `top_ranked_url` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `rank_change` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `phrase_cost_per_click` | FLOAT | NULLABLE | - |
| `exact_cost_per_click` | FLOAT | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `seo_clicks_change` | INTEGER | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `percent_mobile_searches` | FLOAT | NULLABLE | - |
| `percent_desktop_searches` | FLOAT | NULLABLE | - |
| `percent_not_clicked` | FLOAT | NULLABLE | - |
| `percent_paid_clicks` | FLOAT | NULLABLE | - |
| `percent_organic_clicks` | FLOAT | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `phrase_monthly_cost` | FLOAT | NULLABLE | - |
| `exact_monthly_cost` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `ranking_homepages` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `seo_opportunities`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `seo_rankings`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `rank_change` | INTEGER | NULLABLE | - |
| `top_ranked_url` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `term_ad_history`

**Nombre de colonnes:** 19


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `keyword` | STRING | REQUIRED | - |
| `ad_id` | INTEGER | NULLABLE | - |
| `domain_name` | STRING | NULLABLE | - |
| `title` | STRING | NULLABLE | - |
| `body` | STRING | NULLABLE | - |
| `full_url` | STRING | NULLABLE | - |
| `term` | STRING | NULLABLE | - |
| `search_date_id` | INTEGER | NULLABLE | - |
| `average_position` | FLOAT | NULLABLE | - |
| `position` | INTEGER | NULLABLE | - |
| `average_ad_count` | FLOAT | NULLABLE | - |
| `ad_count` | INTEGER | NULLABLE | - |
| `leaderboard_count` | INTEGER | NULLABLE | - |
| `percentage_leaderboard` | FLOAT | NULLABLE | - |
| `percentage_ads_served` | FLOAT | NULLABLE | - |
| `is_leaderboard_ad` | BOOLEAN | NULLABLE | - |
| `source` | STRING | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `term_domain_stats`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `keyword` | STRING | NULLABLE | - |
| `domain_name` | STRING | NULLABLE | - |
| `budget` | FLOAT | NULLABLE | - |
| `coverage` | INTEGER | NULLABLE | - |
| `percentage_leaderboard` | INTEGER | NULLABLE | - |
| `total_ads_purchased` | INTEGER | NULLABLE | - |
| `ad_count` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `top_10_most_valuable`

**Nombre de colonnes:** 9


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `rank` | INTEGER | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `seo_clicks` | INTEGER | NULLABLE | - |
| `keyword_difficulty` | FLOAT | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `estimated_value` | FLOAT | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `top_keywords_by_volume`

**Nombre de colonnes:** 10


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `live_search_volume` | INTEGER | NULLABLE | - |
| `ranking_difficulty` | FLOAT | NULLABLE | - |
| `total_monthly_clicks` | INTEGER | NULLABLE | - |
| `broad_cost_per_click` | FLOAT | NULLABLE | - |
| `broad_monthly_cost` | FLOAT | NULLABLE | - |
| `paid_competitors` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `top_pages`

**Nombre de colonnes:** 11


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | REQUIRED | - |
| `url` | STRING | REQUIRED | - |
| `title` | STRING | NULLABLE | - |
| `keyword_count` | INTEGER | NULLABLE | - |
| `est_monthly_seo_clicks` | INTEGER | NULLABLE | - |
| `top_keyword` | STRING | NULLABLE | - |
| `top_keyword_position` | INTEGER | NULLABLE | - |
| `top_keyword_search_volume` | INTEGER | NULLABLE | - |
| `top_keyword_clicks` | INTEGER | NULLABLE | - |
| `country_code` | STRING | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `top_performing_ads`

**Nombre de colonnes:** 12


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `domain` | STRING | NULLABLE | - |
| `headline` | STRING | NULLABLE | - |
| `description` | STRING | NULLABLE | - |
| `keyword` | STRING | NULLABLE | - |
| `search_volume` | INTEGER | NULLABLE | - |
| `cost_per_click` | FLOAT | NULLABLE | - |
| `monthly_cost` | FLOAT | NULLABLE | - |
| `days_seen` | INTEGER | NULLABLE | - |
| `position` | INTEGER | NULLABLE | - |
| `first_seen_date` | DATE | NULLABLE | - |
| `last_seen_date` | DATE | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

#### Table: `top_spenders_by_keyword`

**Nombre de colonnes:** 7


| Colonne | Type | Mode | Description |
|---------|------|------|-------------|
| `keyword` | STRING | NULLABLE | - |
| `competing_domains` | INTEGER | NULLABLE | - |
| `total_keyword_budget` | FLOAT | NULLABLE | - |
| `avg_domain_budget` | FLOAT | NULLABLE | - |
| `top_spender_budget` | FLOAT | NULLABLE | - |
| `total_ads` | INTEGER | NULLABLE | - |
| `retrieved_at` | TIMESTAMP | NULLABLE | - |

---
