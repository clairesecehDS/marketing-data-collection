# LinkedIn Marketing API Data Collection

Collection complète de scripts Python pour récupérer et analyser les données publicitaires LinkedIn (campagnes, budgets, lead forms) avec upload automatique vers BigQuery.

## 📋 Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration OAuth](#configuration-oauth)
- [Scripts disponibles](#scripts-disponibles)
- [Utilisation](#utilisation)
- [Architecture BigQuery](#architecture-bigquery)
- [Vues d'analyse](#vues-danalyse)
- [Exemples de requêtes](#exemples-de-requêtes)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Vue d'ensemble

Cette collection permet de récupérer automatiquement les données publicitaires depuis l'API LinkedIn Marketing :

| Type | Description | Script |
|------|-------------|--------|
| **Campaign Analytics** | Performances des campagnes et créatives | `linkedin_campaign_analytics.py` |
| **Budget Metrics** | Budgets, enchères, dates de campagnes | `linkedin_budget.py` |
| **Lead Forms** | Formulaires de génération de leads et réponses | `linkedin_lead_forms.py` |

### Données collectées

- **Métriques de performance** : Impressions, clics, coûts, conversions
- **Métriques vidéo** : Vues, taux de complétion, engagement
- **Budget & Enchères** : Budget total/quotidien, type et montant d'enchère
- **Lead Generation** : Réponses aux formulaires, champs personnalisés, timing

---

## 📦 Prérequis

### Comptes et accès

- **LinkedIn Marketing Developer Platform** (compte développeur)
- **LinkedIn Ad Account** avec accès API
- **Application LinkedIn** créée (pour OAuth)
- **Google Cloud Project** avec BigQuery activé
- **Service Account** GCP avec permissions BigQuery

### Permissions LinkedIn requises

Votre application LinkedIn doit avoir les scopes suivants :
- `r_ads` - Lire les données publicitaires
- `r_ads_reporting` - Accéder aux rapports
- `rw_ads` - Gérer les campagnes (optionnel)
- `r_organization_social` - Statistiques de page (non utilisé actuellement)

### Dépendances Python

```bash
pip install requests pandas pandas-gbq google-auth numpy
```

**Important :** Utiliser `numpy < 2.0.0` pour compatibilité :
```bash
pip install "numpy<2.0.0"
```

---

## ⚙️ Installation

### 1. Structure des dossiers

```
linkedin/
├── scripts/
│   ├── token_linkedin.py               # Génération OAuth token
│   ├── linkedin_campaign_analytics.py  # Analytics campagnes/créatives
│   ├── linkedin_budget.py              # Budgets et enchères
│   ├── linkedin_lead_forms.py          # Lead forms et réponses
│   └── linkedin_page_stats.py          # Stats page (non fonctionnel)
├── sql/
│   ├── bigquery_campaign_creative_schema.sql         # Tables analytics
│   ├── bigquery_campaign_creative_budget_schema.sql  # Tables budgets
│   └── bigquery_lead_forms_schema.sql                # Tables leads
├── data/                               # JSON exports (créé automatiquement)
└── README.md                           # Cette documentation
```

### 2. Créer le dataset BigQuery

```sql
CREATE SCHEMA IF NOT EXISTS `linkedin`
OPTIONS(
  location="EU"
);
```

### 3. Créer les tables et vues

Exécuter les 3 fichiers SQL :

```bash
bq query --use_legacy_sql=false < sql/bigquery_campaign_creative_schema.sql
bq query --use_legacy_sql=false < sql/bigquery_campaign_creative_budget_schema.sql
bq query --use_legacy_sql=false < sql/bigquery_lead_forms_schema.sql
```

---

## 🔐 Configuration OAuth

### Étape 1 : Créer une application LinkedIn

1. Aller sur [LinkedIn Developers](https://www.linkedin.com/developers/)
2. Cliquer sur **"Create app"**
3. Remplir les informations :
   - **App name** : "LinkedIn Data Collector"
   - **LinkedIn Page** : Sélectionner votre page entreprise
   - **App logo** : Upload un logo
4. Cliquer sur **"Create app"**

### Étape 2 : Configurer les produits

1. Dans l'onglet **"Products"**, demander l'accès à :
   - **Marketing Developer Platform**
   - **Advertising API**
2. Attendre la validation (peut prendre quelques jours)

### Étape 3 : Récupérer les credentials

1. Onglet **"Auth"**
2. Noter :
   - **Client ID**
   - **Client Secret**
3. Ajouter une **Redirect URL** :
   ```
   http://localhost:8080/callback
   ```

### Étape 4 : Obtenir le Refresh Token

Modifier `scripts/token_linkedin.py` avec vos credentials :

```python
CLIENT_ID = "VOTRE_CLIENT_ID"
CLIENT_SECRET = "VOTRE_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8080/callback"

# Scopes nécessaires
SCOPES = [
    "r_ads",
    "r_ads_reporting",
    "rw_ads",
    "r_basicprofile",
    "r_organization_social",
    "rw_organization_admin",
    "r_organization_admin"
]
```

Exécuter le script :

```bash
cd scripts
python token_linkedin.py
```

**Processus :**
1. Une URL s'affiche dans la console
2. Copier-coller l'URL dans un navigateur
3. Se connecter à LinkedIn et autoriser l'application
4. Vous serez redirigé vers `localhost:8080/callback?code=...`
5. Copier le **code** depuis l'URL
6. Le coller dans la console
7. Le script génère un **Refresh Token**

**Sauvegarder le Refresh Token** - il ne change pas et permet de générer des Access Tokens.

### Étape 5 : Configurer les scripts

Dans chaque script (`linkedin_campaign_analytics.py`, `linkedin_budget.py`, etc.), configurer :

```python
# OAuth Configuration
CLIENT_ID = "VOTRE_CLIENT_ID"
CLIENT_SECRET = "VOTRE_CLIENT_SECRET"
REFRESH_TOKEN = "VOTRE_REFRESH_TOKEN"

# Account Configuration
ACCOUNT_ID = "503061133"  # Votre Ad Account ID
```

**Trouver votre Ad Account ID :**
1. Aller sur [LinkedIn Campaign Manager](https://www.linkedin.com/campaignmanager/)
2. L'URL contient votre Account ID : `campaignmanager/accounts/XXXXXX/`

---

## 🚀 Scripts disponibles

### 1. Campaign Analytics - Performances des campagnes

**Fichier :** `scripts/linkedin_campaign_analytics.py`
**Tables BigQuery :** `campaign_analytics`, `creative_analytics`

#### Métriques collectées

**Métriques de base :**
- `impressions` - Nombre d'impressions
- `clicks` - Nombre de clics
- `cost_in_usd` - Coût total en USD
- `ctr` - Click-through rate (%)
- `average_cpc` - Coût par clic moyen

**Conversions :**
- `total_conversions` - Conversions totales
- `conversion_value_in_usd` - Valeur des conversions
- `cost_per_conversion` - Coût par conversion

**Engagement :**
- `likes` - Nombre de likes
- `comments` - Nombre de commentaires
- `shares` - Nombre de partages
- `follows` - Nouveaux abonnés
- `engagement_rate` - Taux d'engagement

**Vidéo (si applicable) :**
- `video_views` - Vues vidéo
- `video_starts` - Démarrages vidéo
- `video_completions` - Vidéos complétées
- `video_completion_rate` - Taux de complétion

#### Deux modes : CAMPAIGN vs CREATIVE

**CAMPAIGN** (agrégé) :
```python
# Données agrégées par campagne
pivot = "CAMPAIGN"
```

**CREATIVE** (détaillé) :
```python
# Données par créative individuelle
pivot = "CREATIVE"
```

#### Utilisation

```bash
cd scripts
python linkedin_campaign_analytics.py
```

Le script collecte automatiquement les deux pivots (CAMPAIGN et CREATIVE).

#### Configuration

```python
# Période de collecte
START_DATE = "2024-01-01"
END_DATE = datetime.now().strftime("%Y-%m-%d")

# Granularité
GRANULARITY = "DAILY"  # Options: DAILY, MONTHLY, YEARLY, ALL
```

---

### 2. Budget Metrics - Budgets et enchères

**Fichier :** `scripts/linkedin_budget.py`
**Tables BigQuery :** `campaign_budget`, `creative_budget`

#### Métriques collectées

**Budget :**
- `total_budget` - Budget total de la campagne
- `daily_budget` - Budget quotidien

**Enchères :**
- `bid_type` - Type d'enchère (CPM, CPC, etc.)
- `bid_amount` - Montant de l'enchère

**Dates :**
- `start_date` - Date de début
- `end_date` - Date de fin

**Statut :**
- `status` - Statut actuel (ACTIVE, PAUSED, etc.)
- `run_schedule_start` - Horaires de diffusion
- `run_schedule_end`

#### Utilisation

```bash
python linkedin_budget.py
```

---

### 3. Lead Forms - Formulaires de génération de leads

**Fichier :** `scripts/linkedin_lead_forms.py`
**Tables BigQuery :** `lead_forms`, `lead_form_responses`, `lead_form_metrics`

#### Données collectées

**Formulaires :**
- Nom, description
- Questions configurées
- Paramètres de confidentialité
- Statut du formulaire

**Réponses :**
- Email, nom, prénom
- Entreprise, poste
- Téléphone, pays
- Champs personnalisés (JSON)

**Timing (pour SLA) :**
- `submitted_at` - Moment de soumission
- `notification_received_at` - Notification reçue
- `fetched_at` - Récupéré par l'API
- Délais calculés automatiquement

**Métriques :**
- Taux de complétion
- Distribution des réponses
- Qualité des leads

#### Utilisation

```bash
python linkedin_lead_forms.py
```

#### Configuration

```python
# Période de collecte des réponses
START_DATE = "2024-01-01"
END_DATE = datetime.now().strftime("%Y-%m-%d")
```

---

### 4. Page Stats - Statistiques de page (non fonctionnel)

**Fichier :** `scripts/linkedin_page_stats.py`
**Status :** ❌ Non fonctionnel

**Problème :** Nécessite des permissions "Community Management" qui ne sont pas accessibles via l'API standard Marketing.

**Erreur :** 403 ACCESS_DENIED

Ce script est conservé pour référence mais ne peut pas être utilisé sans partenariat LinkedIn spécial.

---

## 🗄️ Architecture BigQuery

### Tables Campaign & Creative Analytics

**Tables :**
- `linkedin.campaign_analytics` - Performances agrégées par campagne
- `linkedin.creative_analytics` - Performances par creative

**Partitionnement :** `DATE(retrieved_at)`
**Clustering :** `campaign_id` / `creative_id`

#### Schéma commun

| Colonne | Type | Description |
|---------|------|-------------|
| `campaign_id` | STRING | ID de la campagne |
| `campaign_urn` | STRING | URN LinkedIn de la campagne |
| `creative_id` | STRING | ID de la creative (creative_analytics uniquement) |
| `creative_urn` | STRING | URN de la creative |
| `impressions` | INT64 | Nombre d'impressions |
| `clicks` | INT64 | Nombre de clics |
| `cost_in_usd` | FLOAT64 | Coût en USD |
| `conversions` | INT64 | Conversions totales |
| `video_views` | INT64 | Vues vidéo |
| `engagement_rate` | FLOAT64 | Taux d'engagement (%) |
| `retrieved_at` | TIMESTAMP | Date de récupération |

### Tables Budget

**Tables :**
- `linkedin.campaign_budget` - Budgets des campagnes
- `linkedin.creative_budget` - Budgets liés aux creatives

**Partitionnement :** `DATE(retrieved_at)`
**Clustering :** `campaign_id`

#### Schéma

| Colonne | Type | Description |
|---------|------|-------------|
| `campaign_id` | STRING | ID de la campagne |
| `total_budget` | FLOAT64 | Budget total |
| `daily_budget` | FLOAT64 | Budget quotidien |
| `bid_type` | STRING | Type d'enchère |
| `bid_amount` | FLOAT64 | Montant de l'enchère |
| `start_date` | DATE | Date de début |
| `end_date` | DATE | Date de fin |
| `status` | STRING | Statut |

### Tables Lead Forms

**Tables :**
- `linkedin.lead_forms` - Configuration des formulaires
- `linkedin.lead_form_responses` - Réponses aux formulaires
- `linkedin.lead_form_metrics` - Métriques agrégées

**Partitionnement :** `DATE(retrieved_at)` / `DATE(submitted_at)`
**Clustering :** `form_id` / `campaign_id`

#### Schéma lead_form_responses

| Colonne | Type | Description |
|---------|------|-------------|
| `form_id` | STRING | ID du formulaire |
| `response_id` | STRING | ID de la réponse |
| `campaign_id` | STRING | Campagne source |
| `email` | STRING | Email du lead |
| `first_name` | STRING | Prénom |
| `last_name` | STRING | Nom |
| `company` | STRING | Entreprise |
| `job_title` | STRING | Poste |
| `phone` | STRING | Téléphone |
| `country` | STRING | Pays |
| `custom_fields` | STRING | Champs personnalisés (JSON) |
| `submitted_at` | TIMESTAMP | Date de soumission |
| `fetched_at` | TIMESTAMP | Date de récupération |

---

## 📊 Vues d'analyse

### 12 vues préconfigurées

#### Campaign Analytics (4 vues)

```sql
-- Vue d'ensemble des campagnes
SELECT * FROM `linkedin.campaign_performance_overview`;

-- Top campagnes par ROI
SELECT * FROM `linkedin.campaign_roi_analysis`;

-- Analyse coût/efficacité
SELECT * FROM `linkedin.campaign_cost_efficiency`;

-- Tendances temporelles
SELECT * FROM `linkedin.campaign_trends`;
```

#### Lead Forms (4 vues)

```sql
-- Vue d'ensemble des leads
SELECT * FROM `linkedin.lead_form_overview`;

-- Qualité des leads (score)
SELECT * FROM `linkedin.lead_quality_score`;

-- SLA monitoring (délais de traitement)
SELECT * FROM `linkedin.lead_sla_monitoring`;

-- Distribution des réponses
SELECT * FROM `linkedin.lead_response_distribution`;
```

#### Budget (2 vues)

```sql
-- Suivi du budget
SELECT * FROM `linkedin.budget_tracking`;

-- Analyse des enchères
SELECT * FROM `linkedin.bid_analysis`;
```

---

## 📈 Exemples de requêtes

### Performance globale des campagnes

```sql
SELECT
  campaign_id,
  SUM(impressions) as total_impressions,
  SUM(clicks) as total_clicks,
  SUM(cost_in_usd) as total_cost,
  ROUND(SUM(clicks) / NULLIF(SUM(impressions), 0) * 100, 2) as ctr,
  ROUND(SUM(cost_in_usd) / NULLIF(SUM(clicks), 0), 2) as avg_cpc,
  SUM(total_conversions) as conversions,
  ROUND(SUM(cost_in_usd) / NULLIF(SUM(total_conversions), 0), 2) as cost_per_conversion
FROM `linkedin.campaign_analytics`
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY campaign_id
ORDER BY total_cost DESC;
```

### Analyse vidéo

```sql
SELECT
  campaign_id,
  SUM(video_views) as total_views,
  SUM(video_starts) as total_starts,
  SUM(video_completions) as total_completions,
  ROUND(SUM(video_completions) / NULLIF(SUM(video_starts), 0) * 100, 2) as completion_rate,
  SUM(cost_in_usd) as total_cost,
  ROUND(SUM(cost_in_usd) / NULLIF(SUM(video_views), 0), 2) as cost_per_view
FROM `linkedin.campaign_analytics`
WHERE video_views > 0
  AND DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY campaign_id
ORDER BY completion_rate DESC;
```

### Meilleurs creatives par engagement

```sql
SELECT
  creative_id,
  campaign_id,
  impressions,
  clicks,
  likes,
  comments,
  shares,
  ROUND((likes + comments + shares) / NULLIF(impressions, 0) * 100, 2) as engagement_rate
FROM `linkedin.creative_analytics`
WHERE DATE(retrieved_at) = CURRENT_DATE()
ORDER BY engagement_rate DESC
LIMIT 20;
```

### Budget vs dépense

```sql
-- Comparer budget prévu vs dépenses réelles
SELECT
  b.campaign_id,
  b.total_budget,
  b.daily_budget,
  b.status,
  SUM(a.cost_in_usd) as spent,
  b.total_budget - SUM(a.cost_in_usd) as remaining,
  ROUND(SUM(a.cost_in_usd) / NULLIF(b.total_budget, 0) * 100, 2) as budget_used_pct,
  DATE_DIFF(b.end_date, CURRENT_DATE(), DAY) as days_remaining
FROM `linkedin.campaign_budget` b
LEFT JOIN `linkedin.campaign_analytics` a
  ON b.campaign_id = a.campaign_id
WHERE b.status = 'ACTIVE'
  AND DATE(a.retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY b.campaign_id, b.total_budget, b.daily_budget, b.status, b.end_date
ORDER BY budget_used_pct DESC;
```

### Leads par source

```sql
SELECT
  l.campaign_id,
  COUNT(*) as total_leads,
  COUNT(DISTINCT l.email) as unique_emails,
  AVG(TIMESTAMP_DIFF(l.fetched_at, l.submitted_at, MINUTE)) as avg_fetch_delay_minutes,
  SUM(a.cost_in_usd) as total_cost,
  ROUND(SUM(a.cost_in_usd) / COUNT(*), 2) as cost_per_lead
FROM `linkedin.lead_form_responses` l
LEFT JOIN `linkedin.campaign_analytics` a
  ON l.campaign_id = a.campaign_id
WHERE DATE(l.submitted_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY l.campaign_id
ORDER BY total_leads DESC;
```

### ROI par campagne

```sql
SELECT
  campaign_id,
  SUM(cost_in_usd) as total_cost,
  SUM(conversion_value_in_usd) as total_revenue,
  SUM(conversion_value_in_usd) - SUM(cost_in_usd) as profit,
  ROUND((SUM(conversion_value_in_usd) - SUM(cost_in_usd)) / NULLIF(SUM(cost_in_usd), 0) * 100, 2) as roi_pct
FROM `linkedin.campaign_analytics`
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  AND conversion_value_in_usd > 0
GROUP BY campaign_id
ORDER BY roi_pct DESC;
```

### Évolution temporelle

```sql
SELECT
  DATE(retrieved_at) as date,
  SUM(impressions) as impressions,
  SUM(clicks) as clicks,
  SUM(cost_in_usd) as cost,
  SUM(total_conversions) as conversions,
  ROUND(SUM(clicks) / NULLIF(SUM(impressions), 0) * 100, 2) as ctr,
  ROUND(SUM(cost_in_usd) / NULLIF(SUM(total_conversions), 0), 2) as cpa
FROM `linkedin.campaign_analytics`
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY date
ORDER BY date DESC;
```

---

## 🔍 Troubleshooting

### Erreur 426 - Upgrade Required

**Problème :** Version de l'API incorrecte

**Solution :** Utiliser la version `202509` :
```python
headers = {
    "LinkedIn-Version": "202509",
    "Authorization": f"Bearer {access_token}"
}
```

---

### Erreur 400 - Invalid dateRange format

**Problème :** Format de date incorrect

**Solution :** Utiliser le format Rest.li exact :
```python
date_range = f"(start:(year:{year},month:{month},day:{day}))"
```

**Important :**
- Seulement `start`, pas de `end`
- Ordre exact : year, month, day
- Parenthèses imbriquées

---

### Erreur 403 - ACCESS_DENIED (No ad accounts)

**Problème :** Account ID incorrect ou pas d'accès

**Solutions :**
1. Vérifier l'Account ID dans Campaign Manager
2. S'assurer d'avoir les permissions sur le compte publicitaire
3. Utiliser l'ID numérique, pas l'URN complet

```python
ACCOUNT_ID = "503061133"  # ✓ Correct
ACCOUNT_ID = "urn:li:sponsoredAccount:503061133"  # ✗ Incorrect
```

---

### Erreur 400 - CREATE_IF_NOT_EXISTS invalid

**Problème :** Mauvaise disposition BigQuery

**Solution :** Utiliser `CREATE_IF_NEEDED` :
```python
job_config = bigquery.LoadJobConfig(
    create_disposition="CREATE_IF_NEEDED",  # ✓ Correct
    write_disposition="WRITE_APPEND"
)
```

---

### ImportError: numpy.core.multiarray failed to import

**Problème :** Version numpy 2.x incompatible

**Solution :**
```bash
pip install "numpy<2.0.0"
```

---

### Schema mismatch - creative_id missing

**Problème :** Colonnes creative ajoutées à la table campaign

**Cause :** Le pivot CAMPAIGN ne doit pas avoir les colonnes creative

**Solution :** Déjà corrigé dans le script. Les colonnes creative sont ajoutées uniquement pour le pivot CREATIVE.

---

### 'int' object has no attribute 'split'

**Problème :** Campaign ID est un integer au lieu d'un URN

**Solution :** Déjà corrigé avec vérification de type :
```python
if isinstance(campaign_id_raw, int):
    campaign_id = str(campaign_id_raw)
    campaign_urn = f"urn:li:sponsoredCampaign:{campaign_id}"
```

---

### Access Token expiré

**Problème :** Access token valide seulement 60 jours

**Solution :** Le script génère automatiquement un nouveau token depuis le refresh token :
```python
def get_access_token(self):
    # Génère un nouveau token à chaque exécution
    response = requests.post(
        "https://www.linkedin.com/oauth/v2/accessToken",
        data={
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
    )
    return response.json()["access_token"]
```

---

## 📅 Automatisation

### Cron job quotidien

```bash
# Ajouter au crontab
crontab -e

# Analytics tous les jours à 3h
0 3 * * * cd /path/to/linkedin/scripts && /path/to/python linkedin_campaign_analytics.py > /tmp/linkedin_analytics.log 2>&1

# Budgets toutes les semaines (lundi)
0 4 * * 1 cd /path/to/linkedin/scripts && /path/to/python linkedin_budget.py > /tmp/linkedin_budget.log 2>&1

# Leads tous les jours à 8h et 18h
0 8,18 * * * cd /path/to/linkedin/scripts && /path/to/python linkedin_lead_forms.py > /tmp/linkedin_leads.log 2>&1
```

### Script bash pour tout collecter

```bash
#!/bin/bash
# collect_all_linkedin.sh

LOG_DIR="/var/log/linkedin"
mkdir -p $LOG_DIR
DATE=$(date +%Y%m%d_%H%M%S)

cd /path/to/linkedin/scripts

echo "=== LinkedIn Collection Started ===" | tee -a "$LOG_DIR/linkedin_$DATE.log"
date | tee -a "$LOG_DIR/linkedin_$DATE.log"

echo "Collecting campaign analytics..." | tee -a "$LOG_DIR/linkedin_$DATE.log"
python linkedin_campaign_analytics.py >> "$LOG_DIR/linkedin_$DATE.log" 2>&1

echo "Collecting budget data..." | tee -a "$LOG_DIR/linkedin_$DATE.log"
python linkedin_budget.py >> "$LOG_DIR/linkedin_$DATE.log" 2>&1

echo "Collecting lead forms..." | tee -a "$LOG_DIR/linkedin_$DATE.log"
python linkedin_lead_forms.py >> "$LOG_DIR/linkedin_$DATE.log" 2>&1

echo "=== LinkedIn Collection Completed ===" | tee -a "$LOG_DIR/linkedin_$DATE.log"
date | tee -a "$LOG_DIR/linkedin_$DATE.log"

# Nettoyer les logs de plus de 30 jours
find $LOG_DIR -name "linkedin_*.log" -mtime +30 -delete
```

---

## 🎓 Best Practices

### 1. Refresh Token sécurisé

Ne **jamais** commit le refresh token dans Git :

```bash
# .gitignore
*.env
*_token.txt
credentials.json
```

Utiliser des variables d'environnement :
```python
import os
REFRESH_TOKEN = os.getenv("LINKEDIN_REFRESH_TOKEN")
```

### 2. Gestion des erreurs

```python
try:
    analytics.get_analytics()
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 429:
        print("Rate limit atteint, attendre 60 secondes...")
        time.sleep(60)
        analytics.get_analytics()
    else:
        raise
```

### 3. Monitoring

```sql
-- Vérifier la fraîcheur des données
SELECT
  MAX(DATE(retrieved_at)) as last_update,
  DATE_DIFF(CURRENT_DATE(), MAX(DATE(retrieved_at)), DAY) as days_since_update
FROM `linkedin.campaign_analytics`;

-- Alerter si pas de mise à jour depuis 2 jours
```

### 4. Optimisation des requêtes BigQuery

```sql
-- Toujours filtrer par date de partition
WHERE DATE(retrieved_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)

-- Utiliser les colonnes clusterisées
WHERE campaign_id = 'xxx'
```

### 5. Collecte incrémentale

Modifier les scripts pour ne collecter que les nouvelles données :

```python
# Récupérer la dernière date en base
last_date = get_last_date_from_bigquery()

# Collecter depuis cette date
START_DATE = (last_date + timedelta(days=1)).strftime("%Y-%m-%d")
```

---

## 📊 Dashboard recommandé

### KPIs principaux

**Vue d'ensemble :**
- Impressions, Clics, CTR
- Coût total, CPC, CPM
- Conversions, CPA, ROI

**Par campagne :**
- Performance comparative
- Budget utilisé vs remaining
- Tendance sur 30 jours

**Leads :**
- Nouveaux leads par jour
- Coût par lead
- Délai de traitement (SLA)

**Vidéo :**
- Vues, taux de complétion
- Coût par vue
- Engagement (likes, comments, shares)

### Outils de visualisation

- **Looker Studio** (Google Data Studio)
- **Tableau**
- **Power BI**
- **Metabase** (open-source)

---

## 🔗 Ressources

### Documentation officielle

- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [OAuth 2.0 LinkedIn](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication)
- [Analytics Finder](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

### Limites API

- **Rate limiting** : 100 requêtes par jour (par défaut)
- **Throttling** : 2 requêtes par seconde
- **Data retention** : 2 ans d'historique maximum

### Support LinkedIn

- [Developer Forum](https://www.linkedin.com/help/lms)
- [API Status](https://www.linkedin-apistatus.com/)

---

## 📝 Notes importantes

### Versions API

LinkedIn utilise le versioning par date :
- **Version actuelle** : `202509` (septembre 2025)
- **Anciennes versions** : dépréciation progressive

Vérifier régulièrement les [release notes](https://learn.microsoft.com/en-us/linkedin/marketing/versioning).

### Permissions et conformité

- **RGPD** : LinkedIn anonymise automatiquement certaines données
- **Données personnelles** : Les leads contiennent des PII, sécuriser l'accès BigQuery
- **Retention** : Définir une politique de rétention des données

### Limitations connues

- **Page Stats** : Nécessite Community Management API (non accessible)
- **Organic Posts** : API séparée, non couvert ici
- **Real-time** : Délai de ~24h pour certaines métriques

---

## 📞 Support

### Questions fréquentes

**Q: Comment obtenir le Marketing Developer Platform ?**
R: Demander l'accès depuis votre app LinkedIn. Validation sous quelques jours.

**Q: Le refresh token expire-t-il ?**
R: Non, sauf révocation manuelle ou non-utilisation pendant 12 mois.

**Q: Puis-je récupérer des données historiques ?**
R: Oui, jusqu'à 2 ans en arrière via l'API Analytics.

**Q: Comment gérer plusieurs comptes publicitaires ?**
R: Créer un script par compte ou boucler sur une liste d'ACCOUNT_ID.

**Q: Les coûts sont-ils en temps réel ?**
R: Non, délai de ~24h pour les métriques financières finales.

---

## 🎯 Roadmap

### Améliorations futures

- [ ] Support multi-comptes automatique
- [ ] Alertes automatiques (budget, performance)
- [ ] Dashboard Looker Studio pré-configuré
- [ ] Export vers Google Sheets
- [ ] Analyse prédictive (ML)
- [ ] Webhook pour nouveaux leads en temps réel

---

**Version:** 1.0
**Dernière mise à jour:** 2025-01-14
**Auteur:** Deep Scouting
