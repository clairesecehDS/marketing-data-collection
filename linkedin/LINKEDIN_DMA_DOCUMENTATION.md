# Documentation LinkedIn Page - Schémas BigQuery

Documentation complète des schémas BigQuery pour la collecte de données LinkedIn via l'API DMA (Data Portability API).

**Date de création**: 2025-12-17
**API Version**: 202511
**Dataset BigQuery**: `linkedin_page`
**Script principal**: [`scripts/linkedin_page_dma_scraper.py`](scripts/linkedin_page_dma_scraper.py)
**Schémas BigQuery**: [`sql/bigquery_linkedin_page_schema.sql`](sql/bigquery_linkedin_page_schema.sql)

---

## 📋 Table des matières

1. [Vue d'ensemble](#vue-densemble)
2. [Configuration](#configuration)
3. [Tables Analytics](#tables-analytics)
4. [Tables Feed & Content](#tables-feed--content)
5. [Tables Followers](#tables-followers)
6. [Tables Profile](#tables-profile)
7. [Tables Lead Generation](#tables-lead-generation)
8. [Tables Events](#tables-events)
9. [Tables Publishing](#tables-publishing)
10. [Utilisation](#utilisation)

---

## 🎯 Vue d'ensemble

Le script `linkedin_page_dma_scraper.py` collecte **toutes les données disponibles** pour une page LinkedIn organisationnelle via l'API DMA (Data Portability API).

### Données collectées

Le système collecte **14 types de données** répartis en **14 tables BigQuery**:

| Catégorie | Tables | Endpoints API |
|-----------|--------|---------------|
| **Analytics** | 4 tables | Page Statistics, Edge Analytics, Content Analytics, Search Appearance |
| **Feed & Content** | 3 tables | Posts, Comments, Reactions |
| **Followers** | 1 table | Organizational Page Follows |
| **Profile** | 1 table | Page Profile |
| **Lead Gen** | 1 table | Lead Gen Forms |
| **Events** | 1 table | Events |
| **Publishing** | 2 tables | Content Series, Original Articles |

### Architecture

```
linkedin/
├── scripts/
│   └── linkedin_page_dma_scraper.py    # Script de scraping
├── bigquery_schemas/
│   └── linkedin_page_schemas.py          # Définitions des schémas
└── LINKEDIN_DMA_DOCUMENTATION.md        # Cette documentation
```

---

## ⚙️ Configuration

### Prérequis

1. **Token OAuth LinkedIn** avec la permission `r_dma_admin_pages_content`
2. **Organization ID** de votre page LinkedIn
3. **Projet Google Cloud** avec BigQuery activé
4. **Credentials GCP** (fichier JSON)

### Configuration dans `config.yaml`

```yaml
linkedin:
  oauth:
    access_token: "YOUR_ACCESS_TOKEN"
  organization_id: "12345678"  # ID numérique de votre page

google_cloud:
  project_id: "your-project-id"
  credentials_file: "path/to/credentials.json"
  datasets:
    linkedin_page: "linkedin_page"
```

---

## 📊 Tables Analytics

### 1. `page_statistics`

Statistiques globales de la page (snapshot quotidien).

**Endpoint API**: `/organizationalPageStatistics`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation (clé primaire) |
| `page_follower_count` | INTEGER | Nombre total de followers |
| `impression_count` | INTEGER | Nombre total d'impressions |
| `click_count` | INTEGER | Nombre total de clics |
| `comment_count` | INTEGER | Nombre total de commentaires |
| `reaction_count` | INTEGER | Nombre total de réactions |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Exemple de requête SQL**:
```sql
SELECT
  DATE(retrieved_at) as date,
  page_follower_count,
  impression_count,
  click_count
FROM `project.linkedin_page.page_statistics`
ORDER BY date DESC
LIMIT 30
```

---

### 2. `page_edge_analytics`

Analytics des relations followers (membres et pages).

**Endpoint API**: `/organizationalPageEdgeAnalytics`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `edge_type` | STRING | Type de relation (MEMBER_FOLLOWS / PAGE_FOLLOWS) |
| `visitor_count` | INTEGER | Nombre de visiteurs |
| `page_follower_count` | INTEGER | Nombre de followers |
| `active_follower_count` | INTEGER | Followers actifs |
| `new_follower_count` | INTEGER | Nouveaux followers |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Exemple de requête SQL**:
```sql
SELECT
  edge_type,
  new_follower_count,
  active_follower_count,
  DATE(retrieved_at) as date
FROM `project.linkedin_page.page_edge_analytics`
WHERE edge_type = 'MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE'
ORDER BY date DESC
```

---

### 3. `page_content_analytics`

Analytics détaillées par contenu publié.

**Endpoint API**: `/organizationalPageContentAnalyticsDMA`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `content_urn` | STRING | URN du contenu LinkedIn |
| `impression_count` | INTEGER | Impressions du contenu |
| `reaction_count` | INTEGER | Réactions au contenu |
| `comment_count` | INTEGER | Commentaires sur le contenu |
| `repost_count` | INTEGER | Nombre de reposts |
| `click_count` | INTEGER | Clics sur le contenu |
| `demographics_breakdown` | STRING | Données démographiques (JSON) |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Exemple de requête SQL**:
```sql
SELECT
  content_urn,
  impression_count,
  reaction_count,
  comment_count,
  ROUND(reaction_count / impression_count * 100, 2) as engagement_rate
FROM `project.linkedin_page.page_content_analytics`
WHERE impression_count > 0
ORDER BY engagement_rate DESC
LIMIT 10
```

---

### 4. `search_appearance_analytics`

Analytics des apparitions dans les résultats de recherche LinkedIn.

**Endpoint API**: `/organizationSearchAppearanceAnalytics`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `search_impressions` | INTEGER | Impressions dans les recherches |
| `search_clicks` | INTEGER | Clics depuis les recherches |
| `impression_to_click_ratio` | FLOAT | Ratio impressions/clics |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

---

## 📝 Tables Feed & Content

### 5. `posts`

Tous les posts publiés par la page.

**Endpoint API**: `/dmaPosts`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `post_id` | STRING | URN du post (clé unique) |
| `text` | STRING | Texte du post |
| `author` | STRING | URN de l'auteur |
| `visibility` | STRING | Visibilité (PUBLIC, CONNECTIONS, etc.) |
| `created_time` | TIMESTAMP | Date de création du post |
| `comment_count` | INTEGER | Nombre de commentaires |
| `reaction_count` | INTEGER | Nombre de réactions |
| `repost_count` | INTEGER | Nombre de reposts |
| `click_count` | INTEGER | Nombre de clics |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Exemple de requête SQL**:
```sql
-- Top 10 posts par engagement
SELECT
  post_id,
  LEFT(text, 100) as excerpt,
  created_time,
  reaction_count + comment_count + repost_count as total_engagement
FROM `project.linkedin_page.posts`
ORDER BY total_engagement DESC
LIMIT 10
```

---

### 6. `comments`

Tous les commentaires sur les posts de la page.

**Endpoint API**: `/dmaComments`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `comment_id` | STRING | URN du commentaire (clé unique) |
| `text` | STRING | Texte du commentaire |
| `author` | STRING | URN de l'auteur |
| `author_name` | STRING | Nom de l'auteur (si opt-in) |
| `created_time` | TIMESTAMP | Date de création |
| `reaction_count` | INTEGER | Réactions au commentaire |
| `status` | STRING | Statut du commentaire |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Note**: Les champs `author_name` ne sont disponibles que si le membre a activé le partage de données ("Page owners exporting your data").

---

### 7. `reactions`

Toutes les réactions sur les contenus de la page.

**Endpoint API**: `/dmaReactions`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `reaction_id` | STRING | URN de la réaction (clé unique) |
| `reactor` | STRING | URN de la personne ayant réagi |
| `reaction_type` | STRING | Type (LIKE, PRAISE, APPRECIATION, etc.) |
| `created_time` | TIMESTAMP | Date de la réaction |
| `content_urn` | STRING | URN du contenu réagi |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Exemple de requête SQL**:
```sql
-- Distribution des types de réactions
SELECT
  reaction_type,
  COUNT(*) as count
FROM `project.linkedin_page.reactions`
GROUP BY reaction_type
ORDER BY count DESC
```

---

## 👥 Tables Followers

### 8. `followers`

Liste complète des followers de la page.

**Endpoint API**: `/dmaOrganizationalPageFollows`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `follow_id` | STRING | URN du follow (clé unique) |
| `follower` | STRING | URN du follower |
| `followed_on` | TIMESTAMP | Date du follow |
| `follower_name` | STRING | Nom du follower (si opt-in) |
| `follower_headline` | STRING | Headline du follower (si opt-in) |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

**Exemple de requête SQL**:
```sql
-- Nouveaux followers par mois
SELECT
  DATE_TRUNC(followed_on, MONTH) as month,
  COUNT(*) as new_followers
FROM `project.linkedin_page.followers`
GROUP BY month
ORDER BY month DESC
```

---

## 🏢 Tables Profile

### 9. `page_profile`

Informations de profil de la page.

**Endpoint API**: `/organizationalPageProfilesDMA`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `page_id` | STRING | ID de la page |
| `name` | STRING | Nom de la page |
| `profile_url` | STRING | URL du profil |
| `tagline` | STRING | Tagline de la page |
| `description` | STRING | Description |
| `logo` | STRING | Logo (JSON) |
| `industry_categories` | STRING | Industries (JSON array) |
| `specialities` | STRING | Spécialités (JSON array) |
| `website` | STRING | Site web |
| `locations` | STRING | Localisations (JSON array) |
| `follower_count` | INTEGER | Nombre de followers |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

---

## 📧 Tables Lead Generation

### 10. `lead_gen_forms`

Formulaires de génération de leads.

**Endpoint API**: `/leadGenForms`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `form_id` | STRING | URN du formulaire (clé unique) |
| `form_name` | STRING | Nom du formulaire |
| `headline` | STRING | Titre du formulaire |
| `description` | STRING | Description |
| `questions` | STRING | Questions (JSON array) |
| `created_time` | TIMESTAMP | Date de création |
| `last_modified_time` | TIMESTAMP | Dernière modification |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

---

## 📅 Tables Events

### 11. `events`

Événements organisés par la page.

**Endpoint API**: `/events`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `event_id` | STRING | URN de l'événement (clé unique) |
| `title` | STRING | Titre de l'événement |
| `description` | STRING | Description |
| `start_date` | STRING | Date de début |
| `end_date` | STRING | Date de fin |
| `location` | STRING | Localisation (JSON) |
| `registration_count` | INTEGER | Nombre d'inscriptions |
| `organizer_urn` | STRING | URN de l'organisateur |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

---

## 📰 Tables Publishing

### 12. `content_series`

Séries de contenu (newsletters).

**Endpoint API**: `/contentSeries`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `series_id` | STRING | URN de la série (clé unique) |
| `name` | STRING | Nom de la série |
| `description` | STRING | Description |
| `subscriber_count` | INTEGER | Nombre d'abonnés |
| `cadence` | STRING | Fréquence de publication |
| `issue_count` | INTEGER | Nombre d'éditions |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

---

### 13. `original_articles`

Articles originaux publiés.

**Endpoint API**: `/originalArticles`

| Champ | Type | Description |
|-------|------|-------------|
| `organization_id` | STRING | ID de l'organisation |
| `article_id` | STRING | URN de l'article (clé unique) |
| `title` | STRING | Titre de l'article |
| `article_body` | STRING | Corps de l'article (HTML) |
| `cover_image` | STRING | Image de couverture (JSON) |
| `authors` | STRING | Auteurs (JSON array) |
| `published_date` | STRING | Date de publication |
| `view_count` | INTEGER | Nombre de vues |
| `like_count` | INTEGER | Nombre de likes |
| `comment_count` | INTEGER | Nombre de commentaires |
| `retrieved_at` | TIMESTAMP | Date de récupération (partition) |

---

## 🚀 Utilisation

### 1. Créer les tables BigQuery

```bash
cd linkedin/bigquery_schemas
python linkedin_page_schemas.py
```

Cela créera automatiquement:
- Le dataset `linkedin_page` (s'il n'existe pas)
- Les 14 tables avec leurs schémas
- Les partitions sur `retrieved_at` pour optimiser les coûts

### 2. Lancer le scraping

```bash
cd linkedin/scripts
python linkedin_page_dma_scraper.py
```

Le script va:
1. Collecter toutes les données depuis l'API DMA
2. Sauvegarder des exports JSON locaux dans `data_exports/`
3. Uploader automatiquement vers BigQuery

### 3. Vérifier les données

```bash
# Compter les lignes dans chaque table
bq query --use_legacy_sql=false '
SELECT
  table_name,
  row_count
FROM `project.linkedin_page.__TABLES__`
ORDER BY table_name
'
```

### 4. Requêtes d'exemple

```sql
-- Dashboard de performance globale
SELECT
  DATE(p.retrieved_at) as date,
  ps.page_follower_count,
  COUNT(DISTINCT p.post_id) as posts_published,
  SUM(p.reaction_count) as total_reactions,
  SUM(p.comment_count) as total_comments
FROM `project.linkedin_page.posts` p
LEFT JOIN `project.linkedin_page.page_statistics` ps
  ON DATE(p.retrieved_at) = DATE(ps.retrieved_at)
WHERE DATE(p.retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY date, ps.page_follower_count
ORDER BY date DESC
```

---

## 📝 Notes importantes

### Permissions LinkedIn requises

Le token OAuth doit avoir la permission:
- `r_dma_admin_pages_content` - Accès complet aux données DMA de la page

### Confidentialité des membres

Certaines données personnelles (noms, headlines) ne sont disponibles que si le membre LinkedIn a activé le paramètre **"Page owners exporting your data"** dans ses préférences de confidentialité.

**Champs concernés**:
- `followers.follower_name`
- `followers.follower_headline`
- `comments.author_name`

### Rate Limiting

L'API LinkedIn a des limites de taux. Le script inclut:
- Un délai configurable entre requêtes (par défaut 1s)
- Retry automatique en cas d'erreur 429
- Respect des headers `Retry-After`

### Partitionnement BigQuery

Toutes les tables sont partitionnées sur `retrieved_at` (jour) pour:
- Réduire les coûts de requêtage
- Optimiser les performances
- Faciliter l'archivage des données anciennes

---

## 🔧 Personnalisation

### Modifier les limites de pagination

Dans `linkedin_page_dma_scraper.py`:

```python
# Limiter le nombre de posts récupérés
all_data['posts'] = self.get_posts(max_results=500)

# Limiter les followers
all_data['followers'] = self.get_followers(max_results=5000)
```

### Ajouter des endpoints supplémentaires

1. Ajouter la méthode dans `LinkedInPageDMAClient`
2. Définir le schéma dans `linkedin_page_schemas.py`
3. Appeler la méthode dans `scrape_all()`

---

## 📚 Ressources

- [Documentation officielle LinkedIn DMA API](https://learn.microsoft.com/en-us/linkedin/dma/)
- [LinkedIn Developer Portal](https://developer.linkedin.com/)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

---

**Dernière mise à jour**: 2025-12-17
**Version**: 1.0.0
