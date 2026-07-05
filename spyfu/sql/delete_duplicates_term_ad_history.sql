-- ============================================================
-- Supprimer les doublons dans term_ad_history
-- ============================================================
-- Cette requête supprime UNIQUEMENT les doublons créés aujourd'hui
-- en gardant les anciennes données intactes
-- ============================================================

-- ÉTAPE 1: Voir combien de lignes par retrieved_at
SELECT 
  DATE(retrieved_at) as date_retrieved,
  COUNT(*) as count
FROM `verbus-480211.spyfu_transport.term_ad_history`
GROUP BY date_retrieved
ORDER BY date_retrieved DESC;

-- ÉTAPE 2: Identifier les doublons créés AUJOURD'HUI uniquement
-- (à exécuter pour vérifier avant suppression)
/*
SELECT 
  keyword,
  domain_name,
  title,
  search_date_id,
  position,
  COUNT(*) as count,
  ARRAY_AGG(retrieved_at ORDER BY retrieved_at DESC) as retrieved_dates
FROM `verbus-480211.spyfu_transport.term_ad_history`
WHERE DATE(retrieved_at) = CURRENT_DATE('Europe/Paris')
GROUP BY keyword, domain_name, title, search_date_id, position
HAVING COUNT(*) > 1
ORDER BY count DESC;
*/

-- ÉTAPE 3: Supprimer UNIQUEMENT les doublons d'aujourd'hui (garder 1 par groupe)
-- Cette requête garde:
-- - TOUTES les lignes anciennes (retrieved_at != aujourd'hui)
-- - UNE SEULE ligne par groupe pour aujourd'hui (la plus récente)
CREATE OR REPLACE TABLE `verbus-480211.spyfu_transport.term_ad_history` AS
SELECT * EXCEPT(row_num)
FROM (
  SELECT 
    *,
    CASE 
      -- Pour les lignes d'aujourd'hui, numéroter les doublons
      WHEN DATE(retrieved_at) = CURRENT_DATE('Europe/Paris') THEN
        ROW_NUMBER() OVER (
          PARTITION BY keyword, domain_name, title, search_date_id, position
          ORDER BY retrieved_at DESC
        )
      -- Pour les anciennes lignes, toujours 1 (= à garder)
      ELSE 1
    END as row_num
  FROM `verbus-480211.spyfu_transport.term_ad_history`
)
WHERE row_num = 1;

-- Note: Adaptez le nom du dataset selon votre config:
-- - spyfu_transport (transport)
-- - spyfu_scolaires (scolaires)  
-- - spyfu_events (events)
-- - spyfu_voyages (voyages)
