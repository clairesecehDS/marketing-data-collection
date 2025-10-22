-- Schéma BigQuery pour la table ads_library
-- Exécutez cette commande pour créer la table dans BigQuery

CREATE TABLE `project-id.linkedin_ads_library.ads_library` (
  Keyword STRING,
  Countries STRING,
  Advertiser STRING,
  Date_Range STRING,
  Paging_Context STRING,
  Ad_URL STRING,
  Is_Restricted BOOLEAN,
  Restriction_Details STRING,
  Advertiser_Name STRING,
  Advertiser_URL STRING,
  Ad_Payer STRING,
  Facet_Name STRING,
  Is_Inclusive STRING,
  Inclusive_Segments STRING,
  Is_Exclusive STRING,
  Exclusive_Segments STRING,
  First_Impression_Date DATE,
  Latest_Impression_Date DATE,
  Total_Impressions_Range STRING,
  Impressions_Distribution_by_Country STRING,
  Ad_Type STRING,
  Retrieved_At TIMESTAMP
)
PARTITION BY First_Impression_Date
CLUSTER BY Advertiser_Name, Ad_Type;
