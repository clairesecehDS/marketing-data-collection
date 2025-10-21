# SpyFu Data Collection

Collection complète de scripts Python pour récupérer et analyser les données SpyFu (SEO et PPC) avec upload automatique vers BigQuery.

## 📋 Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Scripts disponibles](#scripts-disponibles)
- [Utilisation](#utilisation)
- [Architecture BigQuery](#architecture-bigquery)
- [Vues d'analyse](#vues-danalyse)
- [Exemples de requêtes](#exemples-de-requêtes)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Vue d'ensemble

Cette collection permet de récupérer automatiquement 8 types de données depuis l'API SpyFu :

| Type | Description | Script |
|------|-------------|--------|
| **PPC Keywords** | Mots-clés PPC les plus performants | `spyfu_ppc_keywords.py` |
| **New Keywords** | Nouveaux mots-clés PPC détectés | `spyfu_new_keywords.py` |
| **Paid SERPs** | Annonces payantes affichées | `spyfu_paid_serps.py` |
| **SEO Keywords** | Mots-clés organiques | `spyfu_seo_keywords.py` |
| **Newly Ranked** | Mots-clés nouvellement classés | `spyfu_newly_ranked.py` |
| **Outrank Comparison** | Comparaison vs concurrents | `spyfu_outrank_comparison.py` |
| **Top Pages** | Pages les plus performantes | `spyfu_top_pages.py` |
| **PPC Competitors** | Principaux concurrents PPC | `spyfu_ppc_competitors.py` |

---

## 📦 Prérequis

### Comptes et accès

- **SpyFu API Key** (Secret Key)
- **Google Cloud Project** avec BigQuery activé
- **Service Account** GCP avec permissions BigQuery

### Dépendances Python

```bash
pip install requests pandas pandas-gbq google-auth
```

---

## ⚙️ Installation

### 1. Structure des dossiers

```
spyfu/
├── scripts/          # Scripts Python de collecte
├── sql/             # Schémas BigQuery
├── data/            # JSON exports (créé automatiquement)
└── README.md        # Cette documentation
```

### 2. Créer le dataset BigQuery

```sql
CREATE SCHEMA IF NOT EXISTS `spyfu`
OPTIONS(
  location="EU"
);
```

### 3. Créer les tables et vues

Exécuter le fichier SQL :

```bash
bq query --use_legacy_sql=false < sql/bigquery_spyfu_schema.sql
```

Ou depuis la console BigQuery, copier-coller le contenu de `sql/bigquery_spyfu_schema.sql`.

---

## 🔧 Configuration

### Paramètres à personnaliser dans chaque script

#### 1. API Key SpyFu

```python
API_KEY = "VOTRE_SECRET_KEY_ICI"
```

#### 2. Project ID Google Cloud

```python
PROJECT_ID = "votre-project-id"
```

#### 3. Domaines à analyser

```python
DOMAINS = [
    "votre-domaine.com",
    "concurrent1.com",
    "concurrent2.com"
]
```

#### 4. Pays de recherche

```python
country_code = "FR"  # FR, US, DE, GB, etc.
```

#### 5. Filtres optionnels

```python
min_search_volume = 100      # Volume de recherche minimum
min_seo_clicks = 50          # Clics SEO minimum
min_ad_count = 3             # Nombre d'annonces minimum
```

---

## 🚀 Scripts disponibles

### 1. PPC Keywords - Top mots-clés payants

**Fichier :** `scripts/spyfu_ppc_keywords.py`
**Endpoint :** `/apis/keyword_api/v2/ppc/getMostSuccessful`
**Table BigQuery :** `spyfu.ppc_keywords`

**Métriques collectées :**
- Volume de recherche, difficulté, CPC
- Clics et coûts mensuels (Broad, Phrase, Exact)
- Pourcentages mobile/desktop
- Nombre de concurrents

**Utilisation :**
```bash
cd scripts
python spyfu_ppc_keywords.py
```

**Personnalisation :**
```python
DOMAINS = ["votre-domaine.com"]
country_code = "FR"
min_search_volume = 100
```

---

### 2. New Keywords - Nouveaux mots-clés PPC

**Fichier :** `scripts/spyfu_new_keywords.py`
**Endpoint :** `/apis/keyword_api/v2/ppc/getNewKeywords`
**Table BigQuery :** `spyfu.new_keywords`

**Utilisation :**
```bash
python spyfu_new_keywords.py
```

**Métriques identiques à PPC Keywords** avec focus sur les nouvelles opportunités.

---

### 3. Paid SERPs - Annonces payantes

**Fichier :** `scripts/spyfu_paid_serps.py`
**Endpoint :** `/apis/serp_api/v2/ppc/getPaidSerps`
**Table BigQuery :** `spyfu.paid_serps`

**Métriques collectées :**
- Position de l'annonce
- Titre et contenu (HTML)
- Domaine de l'annonceur
- Date de recherche
- Volume et difficulté du mot-clé

**Utilisation :**
```bash
python spyfu_paid_serps.py
```

---

### 4. SEO Keywords - Mots-clés organiques

**Fichier :** `scripts/spyfu_seo_keywords.py`
**Endpoint :** `/apis/serp_api/v2/seo/getSeoKeywords`
**Table BigQuery :** `spyfu.seo_keywords`

**Types de recherche disponibles :**
- `MostValuable` - Mots-clés les plus précieux
- `GainedClicks` - Clics gagnés récemment
- `LostClicks` - Clics perdus
- `JustMadeIt` - Nouvellement classés
- `JustLostIt` - Récemment perdus
- `All` - Tous les keywords

**Métriques collectées :**
- Ranking et changement de position
- URL classée
- Clics SEO et évolution
- Volume, difficulté, CPC

**Utilisation :**
```bash
python spyfu_seo_keywords.py
```

**Personnalisation du type de recherche :**
```python
SEARCH_TYPE = "MostValuable"  # Modifier selon besoin
```

---

### 5. Newly Ranked - Keywords nouvellement classés

**Fichier :** `scripts/spyfu_newly_ranked.py`
**Endpoint :** `/apis/serp_api/v2/seo/getNewlyRankedKeywords`
**Table BigQuery :** `spyfu.newly_ranked_keywords`

**Focus :** Mots-clés qui viennent d'apparaître dans les résultats organiques.

**Utilisation :**
```bash
python spyfu_newly_ranked.py
```

---

### 6. Outrank Comparison - Analyse compétitive

**Fichier :** `scripts/spyfu_outrank_comparison.py`
**Endpoint :** `/apis/seo_api/v2/seo/getWhereOutRankYou`
**Table BigQuery :** `spyfu.outrank_comparison`

**Objectif :** Identifier où les concurrents vous surclassent.

**Configuration des comparaisons :**
```python
COMPARISONS = [
    {"domain": "votre-domaine.com", "compare_domain": "concurrent1.com"},
    {"domain": "votre-domaine.com", "compare_domain": "concurrent2.com"},
]
```

**Métriques collectées :**
- Votre ranking vs ranking concurrent
- Écart de position
- Clics SEO du concurrent
- Volume et difficulté

**Utilisation :**
```bash
python spyfu_outrank_comparison.py
```

---

### 7. Top Pages - Pages les plus performantes

**Fichier :** `scripts/spyfu_top_pages.py`
**Endpoint :** `/apis/seo_api/v2/seo/getTopPages`
**Table BigQuery :** `spyfu.top_pages`

**Métriques collectées :**
- URL et titre de la page
- Nombre de mots-clés positionnés
- Clics SEO mensuels estimés
- Top keyword de la page (position, volume, clics)

**Utilisation :**
```bash
python spyfu_top_pages.py
```

**Filtrage :**
```python
min_seo_clicks = 50  # Pages avec minimum 50 clics/mois
```

---

### 8. PPC Competitors - Concurrents payants

**Fichier :** `scripts/spyfu_ppc_competitors.py`
**Endpoint :** `/apis/competitors_api/v2/ppc/getTopCompetitors`
**Table BigQuery :** `spyfu.ppc_competitors`

**Métriques collectées :**
- Domaine concurrent
- Nombre de mots-clés communs
- Rang du concurrent

**Utilisation :**
```bash
python spyfu_ppc_competitors.py
```

---

## 💾 Mode d'upload depuis JSON

Tous les scripts sauvegardent automatiquement les données en JSON **avant** l'upload BigQuery.

### En cas d'échec BigQuery

Si l'upload BigQuery échoue, vous pouvez ré-uploader depuis le JSON sans refaire l'appel API :

```bash
python spyfu_ppc_keywords.py upload spyfu_ppc_keywords_20250114_123456.json
```

### Avantages

- **Économie d'appels API** (API payante)
- **Backup des données**
- **Réessai facilité** en cas d'erreur BigQuery

---

## 🗄️ Architecture BigQuery

### 8 Tables créées

| Table | Partitionnement | Clustering | Description |
|-------|-----------------|------------|-------------|
| `ppc_keywords` | DATE(retrieved_at) | domain, keyword | Top keywords PPC |
| `new_keywords` | DATE(retrieved_at) | domain, keyword | Nouveaux keywords PPC |
| `paid_serps` | DATE(retrieved_at) | domain, keyword | Annonces PPC |
| `seo_keywords` | DATE(retrieved_at) | domain, keyword | Keywords SEO |
| `newly_ranked_keywords` | DATE(retrieved_at) | domain, keyword | Keywords nouvellement classés |
| `outrank_comparison` | DATE(retrieved_at) | domain, compare_domain, keyword | Comparaisons compétitives |
| `top_pages` | DATE(retrieved_at) | domain, url | Pages performantes |
| `ppc_competitors` | DATE(retrieved_at) | domain, competitor_domain | Concurrents PPC |

### Optimisations

- **Partitionnement par date** : Requêtes rapides sur périodes récentes
- **Clustering** : Filtrage efficace par domaine/keyword
- **Types optimisés** : INT64, FLOAT64, TIMESTAMP

---

## 📊 Vues d'analyse

### 26 vues préconfigurées pour l'analyse

#### PPC Keywords (4 vues)

```sql
-- Top keywords par volume
SELECT * FROM `spyfu.top_keywords_by_volume` WHERE domain = 'votre-domaine.com';

-- Analyse CPC
SELECT * FROM `spyfu.cpc_analysis` WHERE domain = 'votre-domaine.com';

-- Mobile vs Desktop
SELECT * FROM `spyfu.mobile_vs_desktop` WHERE domain = 'votre-domaine.com';

-- Opportunités (faible difficulté, haut volume)
SELECT * FROM `spyfu.keyword_opportunities` WHERE domain = 'votre-domaine.com';
```

#### SEO Keywords (4 vues)

```sql
-- Keywords les plus précieux
SELECT * FROM `spyfu.most_valuable_seo_keywords` WHERE domain = 'votre-domaine.com';

-- Gains/pertes de trafic
SELECT * FROM `spyfu.seo_traffic_changes` WHERE domain = 'votre-domaine.com';

-- Positions SEO (top 20)
SELECT * FROM `spyfu.seo_rankings` WHERE domain = 'votre-domaine.com';

-- Opportunités SEO
SELECT * FROM `spyfu.seo_opportunities` WHERE domain = 'votre-domaine.com';
```

#### Newly Ranked (3 vues)

```sql
-- Nouveaux keywords par volume
SELECT * FROM `spyfu.newly_ranked_by_volume` WHERE domain = 'votre-domaine.com';

-- Nouveaux keywords bien positionnés (top 10)
SELECT * FROM `spyfu.newly_ranked_top_positions` WHERE domain = 'votre-domaine.com';

-- Opportunités parmi les nouveaux
SELECT * FROM `spyfu.newly_ranked_opportunities` WHERE domain = 'votre-domaine.com';
```

#### Paid SERPs (3 vues)

```sql
-- Annonces par position
SELECT * FROM `spyfu.serps_by_position` WHERE domain = 'votre-domaine.com';

-- Analyse de la compétition publicitaire
SELECT * FROM `spyfu.ad_competition_analysis`;

-- Meilleurs titres d'annonces
SELECT * FROM `spyfu.top_ad_titles` WHERE domain = 'votre-domaine.com';
```

#### Outrank Comparison (3 vues)

```sql
-- Gaps SEO (vous n'êtes pas classé)
SELECT * FROM `spyfu.seo_gaps` WHERE domain = 'votre-domaine.com';

-- Opportunités de rattrapage
SELECT * FROM `spyfu.catch_up_opportunities` WHERE domain = 'votre-domaine.com';

-- Analyse par concurrent
SELECT * FROM `spyfu.competitor_advantage_analysis` WHERE domain = 'votre-domaine.com';
```

#### Top Pages (3 vues)

```sql
-- Pages les plus performantes
SELECT * FROM `spyfu.most_valuable_pages` WHERE domain = 'votre-domaine.com';

-- Pages riches en keywords
SELECT * FROM `spyfu.keyword_rich_pages` WHERE domain = 'votre-domaine.com';

-- Performance globale par domaine
SELECT * FROM `spyfu.domain_page_performance` WHERE domain = 'votre-domaine.com';
```

#### PPC Competitors (3 vues)

```sql
-- Top concurrents PPC
SELECT * FROM `spyfu.top_ppc_competitors` WHERE domain = 'votre-domaine.com';

-- Intensité de la concurrence
SELECT * FROM `spyfu.ppc_competition_intensity` WHERE domain = 'votre-domaine.com';

-- Concurrents communs entre domaines
SELECT * FROM `spyfu.shared_ppc_competitors`;
```

#### New Keywords (3 vues)

```sql
-- Nouveaux keywords par domaine
SELECT * FROM `spyfu.new_keywords_by_domain` WHERE domain = 'votre-domaine.com';

-- Nouvelles opportunités
SELECT * FROM `spyfu.new_keyword_opportunities` WHERE domain = 'votre-domaine.com';
```

---

## 📈 Exemples de requêtes

### Analyse complète d'un domaine

```sql
-- Vue d'ensemble des performances
SELECT
  'PPC Keywords' as type,
  COUNT(*) as total,
  SUM(search_volume) as total_volume
FROM `spyfu.ppc_keywords`
WHERE domain = 'essca.eu'
  AND DATE(retrieved_at) = CURRENT_DATE()

UNION ALL

SELECT
  'SEO Keywords' as type,
  COUNT(*) as total,
  SUM(search_volume) as total_volume
FROM `spyfu.seo_keywords`
WHERE domain = 'essca.eu'
  AND DATE(retrieved_at) = CURRENT_DATE();
```

### Top opportunités combinées (SEO + PPC)

```sql
-- Keywords avec fort potentiel (bon volume, faible difficulté, CPC intéressant)
WITH seo_opps AS (
  SELECT
    keyword,
    search_volume,
    keyword_difficulty,
    broad_cost_per_click,
    'SEO' as source
  FROM `spyfu.seo_opportunities`
  WHERE domain = 'essca.eu'
),
ppc_opps AS (
  SELECT
    keyword,
    search_volume,
    ranking_difficulty as keyword_difficulty,
    broad_cost_per_click,
    'PPC' as source
  FROM `spyfu.keyword_opportunities`
  WHERE domain = 'essca.eu'
)
SELECT * FROM seo_opps
UNION ALL
SELECT * FROM ppc_opps
ORDER BY search_volume DESC, keyword_difficulty ASC
LIMIT 50;
```

### Comparaison avec concurrents

```sql
-- Où perdez-vous face à vos concurrents ?
SELECT
  compare_domain as concurrent,
  COUNT(*) as keywords_ou_ils_gagnent,
  SUM(search_volume) as volume_total_perdu,
  AVG(rank) as leur_position_moyenne,
  AVG(your_rank) as votre_position_moyenne,
  AVG(your_rank - rank) as ecart_moyen
FROM `spyfu.outrank_comparison`
WHERE domain = 'essca.eu'
  AND DATE(retrieved_at) = CURRENT_DATE()
GROUP BY compare_domain
ORDER BY keywords_ou_ils_gagnent DESC;
```

### ROI potentiel des opportunités

```sql
-- Estimer le ROI potentiel (clics SEO vs coût PPC)
SELECT
  keyword,
  search_volume,
  seo_clicks,
  broad_cost_per_click,
  (seo_clicks * broad_cost_per_click) as valeur_mensuelle_estimee,
  keyword_difficulty
FROM `spyfu.seo_keywords`
WHERE domain = 'essca.eu'
  AND search_type = 'MostValuable'
  AND seo_clicks > 10
  AND broad_cost_per_click > 1
ORDER BY valeur_mensuelle_estimee DESC
LIMIT 100;
```

### Évolution temporelle

```sql
-- Évolution du nombre de keywords SEO dans le temps
SELECT
  DATE(retrieved_at) as date,
  COUNT(DISTINCT keyword) as total_keywords,
  SUM(seo_clicks) as total_clicks
FROM `spyfu.seo_keywords`
WHERE domain = 'essca.eu'
  AND DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY DATE(retrieved_at)
ORDER BY date DESC;
```

---

## 🔍 Troubleshooting

### Erreur 400 - Bad Request

**Problème :** `StartingRow must be between 1 and 10000`

**Solution :** SpyFu commence à 1, pas 0. Déjà corrigé dans les scripts.

---

### Erreur 500 - Internal Server Error

**Causes possibles :**
1. **API Key invalide** - Vérifier la Secret Key
2. **Domaine sans données** - Essayer un domaine US connu (ex: harvard.edu)
3. **Country code incompatible** - Certains domaines n'ont pas de données pour tous les pays

**Solution :**
```python
# Tester avec un domaine US
DOMAINS = ["harvard.edu"]
country_code = "US"
```

---

### Erreur BigQuery - Schema mismatch

**Problème :** Colonnes manquantes ou types incompatibles

**Solution :**
1. Supprimer la table existante :
```sql
DROP TABLE `spyfu.nom_table`;
```

2. Recréer depuis le schéma :
```bash
bq query --use_legacy_sql=false < sql/bigquery_spyfu_schema.sql
```

---

### Aucune donnée collectée

**Vérifications :**
1. **API Key correcte** dans le script
2. **Domaine valide** et avec données dans le pays spécifié
3. **Filtres pas trop restrictifs** (ex: min_search_volume trop élevé)

**Debug :**
```python
# Réduire les filtres
min_search_volume = 10  # Au lieu de 100
page_size = 100  # Au lieu de 1000
```

---

### Timeout lors de l'appel API

**Solution :** Augmenter le timeout :
```python
response = self.session.get(endpoint, params=params, headers=headers, timeout=120)
```

---

### Upload BigQuery échoue

**Solution :** Utiliser le mode upload depuis JSON

1. Les données sont déjà sauvegardées dans `data/`
2. Corriger le problème BigQuery
3. Ré-uploader :

```bash
python spyfu_ppc_keywords.py upload spyfu_ppc_keywords_20250114_123456.json
```

---

## 📅 Automatisation

### Cron job quotidien

```bash
# Ajouter au crontab
crontab -e

# Exécuter tous les jours à 3h du matin
0 3 * * * cd /path/to/spyfu/scripts && /path/to/python spyfu_ppc_keywords.py > /tmp/spyfu_ppc.log 2>&1
0 4 * * * cd /path/to/spyfu/scripts && /path/to/python spyfu_seo_keywords.py > /tmp/spyfu_seo.log 2>&1
```

### Script bash pour tout collecter

```bash
#!/bin/bash
# collect_all_spyfu.sh

cd /path/to/spyfu/scripts

echo "=== SpyFu Collection Started ==="
date

python spyfu_ppc_keywords.py
python spyfu_new_keywords.py
python spyfu_paid_serps.py
python spyfu_seo_keywords.py
python spyfu_newly_ranked.py
python spyfu_top_pages.py
python spyfu_ppc_competitors.py

echo "=== SpyFu Collection Completed ==="
date
```

---

## 📞 Support

### Documentation API SpyFu

- https://www.spyfu.com/api

### Questions fréquentes

**Q: L'API est-elle payante ?**
R: Oui, selon votre plan SpyFu. Attention aux quotas.

**Q: Puis-je récupérer des données historiques ?**
R: Non, l'API retourne les données actuelles. Il faut collecter régulièrement pour construire un historique.

**Q: Quelle fréquence de collecte recommandez-vous ?**
R:
- **PPC/SEO Keywords** : 1x/semaine
- **Paid SERPs** : 2-3x/semaine
- **Newly Ranked** : 1x/jour
- **Competitors** : 1x/mois

**Q: Comment gérer plusieurs domaines ?**
R: Modifier la liste `DOMAINS` dans chaque script. Tous les domaines sont collectés en une seule exécution.

---

## 🎓 Best Practices

### 1. Économiser les appels API

- Utiliser des **filtres appropriés** (min_search_volume)
- **Sauvegarder les JSON** avant de tester BigQuery
- Ne pas relancer si les données du jour existent déjà

### 2. Optimiser BigQuery

- **Partitionner les requêtes** par date :
```sql
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
```

- **Utiliser les vues** plutôt que réécrire les requêtes

### 3. Monitoring

- Logger les résultats dans des fichiers
- Alerter si aucune donnée collectée
- Vérifier les quotas API régulièrement

---

## 📝 Licence

Usage interne uniquement. Respecter les conditions d'utilisation de l'API SpyFu.

---

**Version:** 1.0
**Dernière mise à jour:** 2025-01-14
**Auteur:** Deep Scouting
