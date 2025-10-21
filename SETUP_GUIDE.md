# Marketing Data Collection Suite - Setup Guide

Documentation complète pour la configuration et l'utilisation de la suite de collecte de données marketing (LinkedIn, Microsoft Clarity, SpyFu).

## 📋 Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Architecture globale](#architecture-globale)
- [Prérequis techniques](#prérequis-techniques)
- [Configuration Google Cloud & BigQuery](#configuration-google-cloud--bigquery)
- [Configuration LinkedIn](#configuration-linkedin)
- [Configuration Microsoft Clarity](#configuration-microsoft-clarity)
- [Configuration SpyFu](#configuration-spyfu)
- [Déploiement et exécution](#déploiement-et-exécution)
- [Sécurité et bonnes pratiques](#sécurité-et-bonnes-pratiques)
- [Automatisation](#automatisation)
- [Troubleshooting global](#troubleshooting-global)
- [Checklist de déploiement](#checklist-de-déploiement)

---

## 🎯 Vue d'ensemble

Cette suite permet de collecter automatiquement des données marketing depuis 3 sources :

| Source | Type de données | Fréquence recommandée |
|--------|-----------------|----------------------|
| **LinkedIn** | Campagnes publicitaires, budgets, leads | Quotidien |
| **Microsoft Clarity** | Comportement utilisateur, UX metrics | Quotidien (obligatoire) |
| **SpyFu** | SEO/PPC concurrentiel, keywords | Hebdomadaire |

**Objectif :** Centraliser toutes les données dans BigQuery pour analyse et reporting unifiés.

### Bénéfices

✅ **Centralisation** - Toutes les données au même endroit
✅ **Historisation** - Construction d'un historique long terme
✅ **Analyse croisée** - Corrélations entre sources
✅ **Automatisation** - Collecte sans intervention manuelle
✅ **Backup** - Sauvegarde JSON avant upload

---

## 🏗️ Architecture globale

```
┌─────────────────────────────────────────────────────────────┐
│                      Sources de données                     │
├─────────────────┬───────────────────┬───────────────────────┤
│   LinkedIn Ads  │ Microsoft Clarity │      SpyFu API        │
│   - Campaigns   │   - User behavior │   - SEO keywords      │
│   - Budgets     │   - Frustration   │   - PPC keywords      │
│   - Lead forms  │   - Engagement    │   - Competitors       │
└────────┬────────┴──────────┬────────┴─────────┬─────────────┘
         │                   │                  │
         │ OAuth 2.0         │ API Key          │ API Key
         │                   │                  │
         v                   v                  v
┌─────────────────────────────────────────────────────────────┐
│              Scripts Python (ce repository)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  linkedin/   │  │  microsoft_  │  │   spyfu/     │       │
│  │  scripts/    │  │  clarity/    │  │   scripts/   │       │
│  │              │  │  scripts/    │  │              │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
│         │                 │                 │               │
│         └─────────────────┴─────────────────┘               │
│                           │                                 │
│                  JSON Backup (data/)                        │
│                           │                                 │
└───────────────────────────┼─────────────────────────────────┘
                            │
                            │ Service Account
                            │
                            v
                    ┌─────────────────┐
                    │   BigQuery      │
                    │   (Google Cloud)│
                    │                 │
                    │  - linkedin     │
                    │  - clarity      │
                    │  - spyfu        │
                    └────────┬────────┘
                             │
                             v
                    ┌─────────────────┐
                    │  Visualization  │
                    │  - Looker       │
                    │  - Tableau      │
                    │  - Custom SQL   │
                    └─────────────────┘
```

---

## 📦 Prérequis techniques

### Comptes nécessaires

| Service | Type | Coût |
|---------|------|------|
| Google Cloud Platform | Cloud provider | Gratuit pour petits volumes, puis facturation usage |
| LinkedIn Developer | Marketing API | Gratuit (nécessite Ad Account actif) |
| Microsoft Clarity | Analytics | Totalement gratuit |
| SpyFu | SEO/PPC Intelligence | Payant - selon abonnement |

### Logiciels requis

```bash
# Python 3.8+
python --version

# Pip
pip --version

# Git (pour cloner le repository)
git --version
```

---

## 📥 Installation du code

### Étape 1 : Cloner le repository GitHub

```bash
# Cloner le repository
git clone [URL_DU_REPO_GITHUB]

# Se déplacer dans le dossier
cd marketing-data-collection

# Structure attendue après clonage :
# marketing-data-collection/
# ├── linkedin/
# ├── microsoft_clarity/
# ├── spyfu/
# ├── SETUP_GUIDE.md
# └── README.md
```

⚠️ **Important :** Le fichier `account-key.json` n'est PAS dans le repository (pour des raisons de sécurité). Vous devrez le créer comme expliqué dans la section "Configuration Google Cloud".

---

### Étape 2 : Configurer le fichier de configuration

```bash
# Copier le fichier d'exemple
cp config.example.yaml config.yaml

# Éditer avec vos paramètres
nano config.yaml  # ou vim, code, etc.
```

**Ce fichier centralise TOUTE la configuration :**
- Credentials (API keys, tokens, project IDs)
- Liste des domaines et concurrents à analyser
- Métriques à collecter
- Périodes de collecte
- Paramètres BigQuery
- Planification de l'automatisation

📸 **TODO: Screenshot du fichier config.yaml ouvert dans un éditeur**

Voir section [Configuration détaillée](#-configuration-détaillée) pour remplir chaque partie.

---

### Étape 3 : Installer les dépendances Python

```bash
# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install requests pandas pandas-gbq google-auth google-cloud-bigquery "numpy<2.0.0"
```

---

### Étape 3 : Vérifier l'installation

```bash
# Vérifier que les modules sont installés
python -c "import requests, pandas, pandas_gbq, google.auth; print('✓ Toutes les dépendances sont installées')"
```

---

## 🔧 Configuration Google Cloud & BigQuery

### Étape 1 : Créer un projet Google Cloud

1. Aller sur [Google Cloud Console](https://console.cloud.google.com/)
2. Cliquer sur le sélecteur de projet en haut
3. Cliquer sur **"Nouveau projet"**
4. Renseigner :
   - **Nom du projet** : `deepscouting-marketing` (ou autre)
   - **Organisation** : Sélectionner si applicable
5. Cliquer sur **"Créer"**
6. **Noter le Project ID** (ex: `clean-avatar-466709-a0`)

---

### Étape 2 : Activer l'API BigQuery

1. Dans la console GCP, menu latéral → **"APIs & Services"** → **"Library"**
2. Rechercher **"BigQuery API"**
3. Cliquer sur **"Enable"**

---

### Étape 3 : Créer un Service Account

Un Service Account permet aux scripts d'accéder à BigQuery de manière sécurisée.

1. Menu latéral → **"IAM & Admin"** → **"Service Accounts"**
2. Cliquer sur **"Create Service Account"**
3. Renseigner :
   - **Service account name** : `marketing-data-collector`
   - **Description** : "Service account for automated data collection"
4. Cliquer sur **"Create and Continue"**

5. **Accorder les permissions** :
   - Rôle : **"BigQuery Data Editor"**
   - Rôle : **"BigQuery Job User"**
   - Cliquer sur **"Continue"**

6. Cliquer sur **"Done"**

---

### Étape 4 : Générer une clé JSON

1. Dans la liste des Service Accounts, cliquer sur le service account créé
2. Onglet **"Keys"**
3. Cliquer sur **"Add Key"** → **"Create new key"**
4. Sélectionner **JSON**
5. Cliquer sur **"Create"**
6. Un fichier JSON se télécharge automatiquement

⚠️ **Important :** Ce fichier contient des credentials sensibles !

7. **Renommer le fichier** en `account-key.json`
8. **Placer le fichier** à la racine du repository cloné :
   ```bash
   # Si vous avez cloné dans /home/user/marketing-data-collection/
   mv ~/Downloads/account-key-xxx.json /home/user/marketing-data-collection/account-key.json
   ```

9. **Sécuriser le fichier** :
   ```bash
   chmod 600 account-key.json
   ```

⚠️ **Ne jamais commiter ce fichier dans Git !** Il est déjà dans le `.gitignore`.

---

### Étape 5 : Créer les datasets BigQuery

1. Menu latéral → **"BigQuery"** → **"SQL Workspace"**
2. Cliquer sur votre projet
3. Cliquer sur les trois points → **"Create dataset"**

**Créer 3 datasets :**

#### Dataset 1 : LinkedIn
- **Dataset ID** : `linkedin`
- **Data location** : `EU` (ou US selon votre région)
- **Default table expiration** : Never
- Cliquer sur **"Create dataset"**

#### Dataset 2 : Microsoft Clarity
- **Dataset ID** : `microsoft_clarity`
- **Data location** : `EU`
- **Default table expiration** : Never

#### Dataset 3 : SpyFu
- **Dataset ID** : `spyfu`
- **Data location** : `EU`
- **Default table expiration** : Never

---

### Étape 6 : Créer les tables et vues

Pour chaque source, exécuter les fichiers SQL :

#### Via bq CLI (recommandé)

```bash
# Installer gcloud CLI si nécessaire
# https://cloud.google.com/sdk/docs/install

# Authentification
gcloud auth login
gcloud config set project VOTRE_PROJECT_ID

# Créer les tables LinkedIn
bq query --use_legacy_sql=false < linkedin/sql/bigquery_campaign_creative_schema.sql
bq query --use_legacy_sql=false < linkedin/sql/bigquery_campaign_creative_budget_schema.sql
bq query --use_legacy_sql=false < linkedin/sql/bigquery_lead_forms_schema.sql

# Créer la table Clarity
bq query --use_legacy_sql=false < microsoft_clarity/sql/bigquery_clarity_schema.sql

# Créer les tables SpyFu
bq query --use_legacy_sql=false < spyfu/sql/bigquery_spyfu_schema.sql
```

#### Via Console BigQuery

1. Aller dans BigQuery SQL Workspace
2. Cliquer sur **"Compose new query"**
3. Copier-coller le contenu d'un fichier SQL
4. Cliquer sur **"Run"**
5. Répéter pour chaque fichier SQL

---

### Étape 7 : Connecter Google Search Console, Google Analytics et Google Ads (NATIF)

BigQuery peut se connecter **directement** aux services Google sans code ni script ! Les données sont synchronisées automatiquement.

---

#### 7.1 - Google Search Console → BigQuery

**Export NATIF des données Search Console vers BigQuery**

1. Aller sur [Google Search Console](https://search.google.com/search-console)
2. Sélectionner votre propriété (site web)
3. Menu latéral → **"Paramètres"** (⚙️)
4. Section **"Exportations de données"** → Cliquer sur **"BigQuery"**
5. Cliquer sur **"Exporter vers BigQuery"**
6. Configurer :
   - **Projet Google Cloud** : Sélectionner votre projet GCP
   - **Dataset** : Créer un nouveau dataset `google_search_console` ou utiliser existant
   - **Fréquence** : Quotidienne (automatique)
   - **Données historiques** : Cocher si vous voulez les 16 derniers mois
7. Cliquer sur **"Exporter"**


**Résultat :**
- Table créée automatiquement : `searchdata_site_impression`
- Mise à jour quotidienne automatique
- Colonnes : url, query, impressions, clicks, position, country, device, etc.

**Exemple de requête :**

```sql
SELECT
  data_date,
  query,
  SUM(impressions) as total_impressions,
  SUM(clicks) as total_clicks,
  AVG(sum_position / impressions) as avg_position
FROM `votre-project-id.google_search_console.searchdata_site_impression`
WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY data_date, query
ORDER BY total_clicks DESC
LIMIT 100;
```

---

#### 7.2 - Google Analytics 4 → BigQuery

**Export NATIF GA4 vers BigQuery (gratuit jusqu'à 1M événements/jour)**

1. Aller dans [Google Analytics 4](https://analytics.google.com/)
2. Menu **"Admin"** (⚙️ en bas à gauche)
3. Colonne **"Propriété"** → **"BigQuery Linking"** ou **"Lien BigQuery"**
4. Cliquer sur **"Link"** ou **"Associer"**
5. Sélectionner votre projet Google Cloud
6. Configurer :
   - **Dataset location** : Choisir `EU` ou `US`
   - **Nom du dataset** : `analytics_XXXXXXXXX` (auto-généré)
   - **Fréquence d'export** :
     - ✅ **Quotidien** (Daily) - Export tous les jours à ~14h
     - ✅ **Streaming** (si besoin temps réel, payant au-delà de 1M événements/jour)
   - **Inclure les données publicitaires** : Cocher si applicable
7. Cliquer sur **"Suivant"** → **"Envoyer"**

**Résultat :**
- Tables créées automatiquement : `events_YYYYMMDD` (une par jour)
- Table intraday : `events_intraday_YYYYMMDD` (si streaming activé)
- Schéma nested avec événements, paramètres, user properties

**Exemple de requête - Sessions et utilisateurs :**

```sql
SELECT
  PARSE_DATE('%Y%m%d', event_date) as date,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNT(DISTINCT CONCAT(user_pseudo_id,
    (SELECT value.int_value FROM UNNEST(event_params)
     WHERE key = 'ga_session_id'))) as sessions
FROM `votre-project-id.analytics_XXXXXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20250101' AND '20251231'
GROUP BY date
ORDER BY date DESC;
```

**Exemple de requête - Top pages :**

```sql
SELECT
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') as page_url,
  COUNT(*) as page_views,
  COUNT(DISTINCT user_pseudo_id) as unique_users
FROM `votre-project-id.analytics_XXXXXXXXX.events_*`
WHERE event_name = 'page_view'
  AND _TABLE_SUFFIX BETWEEN '20250101' AND '20251231'
GROUP BY page_url
ORDER BY page_views DESC
LIMIT 20;
```

---

#### 7.3 - Google Ads → BigQuery

**Export NATIF Google Ads vers BigQuery**

⚠️ **Prérequis :** Compte Google Ads avec droits administrateur

1. Se connecter à [Google Ads](https://ads.google.com/)
2. Menu **"Outils et paramètres"** (🔧) → **"Configuration"** → **"Exports BigQuery"**
3. Cliquer sur le bouton **+** (Nouvel export)
4. Configurer :
   - **Projet Google Cloud** : Sélectionner votre projet
   - **Dataset** : Créer `google_ads` ou utiliser existant
   - **Emplacement des données** : `EU` ou `US`
   - **Tables à exporter** : Sélectionner les tables nécessaires
     - ✅ Campaign (campagnes)
     - ✅ Ad Group (groupes d'annonces)
     - ✅ Ad (annonces)
     - ✅ Keyword (mots-clés)
     - ✅ Search Term (termes de recherche)
     - ✅ Geo (géographie)
     - ✅ Click (clics)
     - Etc.
   - **Fréquence** : Quotidienne (automatique chaque nuit)
5. Cliquer sur **"Créer"**

**Résultat :**
- Tables créées : `Campaign_XXXXXXXX`, `AdGroup_XXXXXXXX`, etc.
- Mise à jour quotidienne automatique
- Historique : jusqu'à 13 mois de données

**Exemple de requête - Performances campagnes :**

```sql
SELECT
  c.campaign_name,
  SUM(c.impressions) as total_impressions,
  SUM(c.clicks) as total_clicks,
  SUM(c.conversions) as total_conversions,
  SUM(c.cost_micros) / 1000000 as total_cost_usd,
  SAFE_DIVIDE(SUM(c.clicks), SUM(c.impressions)) * 100 as ctr,
  SAFE_DIVIDE(SUM(c.cost_micros) / 1000000, SUM(c.clicks)) as cpc
FROM `votre-project-id.google_ads.Campaign_XXXXXXXX` c
WHERE c.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND c.campaign_status = 'ENABLED'
GROUP BY c.campaign_name
ORDER BY total_cost_usd DESC;
```

**Exemple de requête - Performance mots-clés :**

```sql
SELECT
  k.ad_group_criterion_keyword_text as keyword,
  k.segments_date as date,
  SUM(k.impressions) as impressions,
  SUM(k.clicks) as clicks,
  SUM(k.cost_micros) / 1000000 as cost_usd,
  SAFE_DIVIDE(SUM(k.clicks), SUM(k.impressions)) * 100 as ctr
FROM `votre-project-id.google_ads.Keyword_XXXXXXXX` k
WHERE k.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY keyword, date
ORDER BY cost_usd DESC
LIMIT 50;
```

---

#### 7.4 - Résumé des datasets créés

Après configuration, vous aurez ces datasets dans BigQuery :

```
votre-project-id
├── linkedin                    # Scripts Python (ce projet)
├── microsoft_clarity           # Scripts Python (ce projet)
├── spyfu                       # Scripts Python (ce projet)
├── google_search_console       # 🔗 Connexion native GSC
├── analytics_XXXXXXXXX         # 🔗 Connexion native GA4
└── google_ads                  # 🔗 Connexion native Google Ads
```

**Avantages des connexions natives :**
- ✅ Aucun code à écrire
- ✅ Synchronisation automatique quotidienne
- ✅ Gratuit (sauf streaming GA4 au-delà de 1M événements)
- ✅ Données historiques disponibles
- ✅ Schéma maintenu par Google
- ✅ Pas de gestion d'API keys

**Analyse combinée possible :**

```sql
-- Corrélation Google Ads + LinkedIn Ads
SELECT
  ga.segments_date as date,
  'Google Ads' as source,
  SUM(ga.impressions) as impressions,
  SUM(ga.clicks) as clicks,
  SUM(ga.cost_micros) / 1000000 as cost
FROM `votre-project-id.google_ads.Campaign_XXXXXXXX` ga
WHERE ga.segments_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY date, source

UNION ALL

SELECT
  DATE(l.date) as date,
  'LinkedIn Ads' as source,
  SUM(l.impressions) as impressions,
  SUM(l.clicks) as clicks,
  SUM(l.costInUsd) as cost
FROM `votre-project-id.linkedin.campaign_analytics` l
WHERE DATE(l.date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY date, source

ORDER BY date DESC, source;
```

---

### Étape 8 : Vérifier la configuration

```sql
-- Vérifier que les datasets existent
SELECT schema_name
FROM INFORMATION_SCHEMA.SCHEMATA;

-- Vérifier les tables LinkedIn
SELECT table_name
FROM `linkedin.INFORMATION_SCHEMA.TABLES`;

-- Vérifier les tables Clarity
SELECT table_name
FROM `microsoft_clarity.INFORMATION_SCHEMA.TABLES`;

-- Vérifier les tables SpyFu
SELECT table_name
FROM `spyfu.INFORMATION_SCHEMA.TABLES`;
```

---

## 🔐 Configuration LinkedIn

### Vue d'ensemble OAuth 2.0

LinkedIn utilise OAuth 2.0 avec un **Refresh Token** qui ne change pas et permet de générer des **Access Tokens** temporaires (60 jours).

**Flux OAuth :**
```
1. Créer une App LinkedIn
2. Obtenir Client ID + Client Secret
3. Générer un Authorization Code (via navigateur)
4. Échanger le code contre un Refresh Token
5. Utiliser le Refresh Token dans les scripts
   → Les scripts génèrent automatiquement les Access Tokens
```

---

### Étape 1 : Créer une application LinkedIn

1. Aller sur [LinkedIn Developers](https://www.linkedin.com/developers/)
2. Se connecter avec votre compte LinkedIn
3. Cliquer sur **"Create app"**

4. Remplir le formulaire :
   - **App name** : `Marketing Data Collector`
   - **LinkedIn Page** : Sélectionner votre page entreprise
     - ⚠️ **Vous devez être admin de la page**
     - Si pas de page : créer une page entreprise d'abord
   - **Privacy policy URL** : URL de votre politique de confidentialité
   - **App logo** : Upload un logo (256x256px minimum)
   - **Legal agreement** : Cocher la case

5. Cliquer sur **"Create app"**

---

### Étape 2 : Demander l'accès aux produits

1. Dans votre app, onglet **"Products"**
2. Demander l'accès à :
   - ✅ **Marketing Developer Platform**
   - ✅ **Advertising API**

3. Pour chaque produit :
   - Cliquer sur **"Request access"**
   - Remplir le formulaire de demande
   - Expliquer l'usage : "Automated data collection for internal marketing analytics"

⏱️ **Délai d'approbation :** 1-7 jours ouvrés

📧 **Notification :** Email de confirmation une fois approuvé

---

### Étape 3 : Configurer OAuth 2.0

1. Onglet **"Auth"**
2. **Redirect URLs** → Cliquer sur le crayon pour éditer
3. Ajouter :
   ```
   http://localhost:8080/callback
   ```
4. Cliquer sur **"Update"**

5. **Noter vos credentials** :
   - **Client ID** : `78...` (long string)
   - **Client Secret** : `WP...` (long string)

⚠️ **Ne jamais partager** ces credentials !

---

### Étape 4 : Obtenir l'Ad Account ID

1. Aller sur [LinkedIn Campaign Manager](https://www.linkedin.com/campaignmanager/)
2. L'URL contient votre Account ID :
   ```
   https://www.linkedin.com/campaignmanager/accounts/503061133/
                                                    ^^^^^^^^^^
                                                    Account ID
   ```
3. **Noter cet ID**

---

### Étape 5 : Générer le Refresh Token

Voir la documentation complète dans [linkedin/README.md](linkedin/README.md) section "Configuration OAuth".

**Résumé :**
1. Configurer `token_linkedin.py` avec Client ID/Secret
2. Exécuter le script
3. Autoriser dans le navigateur
4. Copier le code de l'URL
5. Obtenir le Refresh Token

---

## 🔍 Configuration Microsoft Clarity

### Étape 1-3 : Configuration du projet

Voir [microsoft_clarity/README.md](microsoft_clarity/README.md) pour les étapes détaillées :
1. Créer un projet Clarity
2. Installer le tracking code
3. Obtenir Project ID et API Key

---

## 🎯 Configuration SpyFu

### Obtenir l'API Key

Voir [spyfu/README.md](spyfu/README.md) pour les étapes détaillées.

**Résumé :**
1. Se connecter à SpyFu (abonnement requis)
2. Account Settings → API
3. Copier la **Secret Key**

---

## 🚀 Déploiement et exécution

### Structure de fichiers finale

```
marketing-data-collection/        # Repository cloné depuis GitHub
├── account-key.json              # À créer (Service Account GCP - NE PAS COMMIT)
├── linkedin/
│   ├── scripts/                  # 4 scripts Python
│   ├── sql/                      # 3 fichiers SQL
│   ├── data/                     # JSON backups (créé automatiquement)
│   └── README.md
├── microsoft_clarity/
│   ├── scripts/                  # 1 script Python
│   ├── sql/                      # 1 fichier SQL
│   ├── data/                     # JSON backups (créé automatiquement)
│   └── README.md
├── spyfu/
│   ├── scripts/                  # 8 scripts Python
│   ├── sql/                      # 1 fichier SQL
│   ├── data/                     # JSON backups (créé automatiquement)
│   └── README.md
├── SETUP_GUIDE.md                # Ce fichier
├── README.md                     # Documentation principale
└── .gitignore                    # Protège les credentials
```

---

### Exécution manuelle

```bash
# Se placer dans le dossier du repository cloné
cd marketing-data-collection

# LinkedIn
cd linkedin/scripts
python linkedin_campaign_analytics.py
python linkedin_budget.py
python linkedin_lead_forms.py

# Clarity
cd ../../microsoft_clarity/scripts
python clarity_analytics.py

# SpyFu
cd ../../spyfu/scripts
python spyfu_ppc_keywords.py
python spyfu_seo_keywords.py
# ... autres scripts
```

---

## 🔒 Sécurité et bonnes pratiques

### .gitignore (déjà inclus dans le repository)

Le repository contient déjà un `.gitignore` qui protège automatiquement :

```gitignore
# Credentials Google Cloud
account-key.json
*.json

# Tokens
*_token.txt
.env

# Data exports (JSON backups)
linkedin/data/*.json
microsoft_clarity/data/*.json
spyfu/data/*.json

# Python
__pycache__/
*.pyc
venv/
.venv/

# Logs
*.log
```

⚠️ **Ne jamais modifier le .gitignore pour éviter de commit des credentials !**

---

### Permissions fichiers

```bash
# Sécuriser le Service Account key
chmod 600 account-key.json

# Scripts exécutables
chmod 755 linkedin/scripts/*.py
chmod 755 microsoft_clarity/scripts/*.py
chmod 755 spyfu/scripts/*.py
```

---

## ⏰ Automatisation

### Fréquences recommandées

| Source | Script | Fréquence | Raison |
|--------|--------|-----------|--------|
| Clarity | clarity_analytics | **Quotidien (2h)** | **API limitée à 3 jours** |
| LinkedIn | campaign_analytics | Quotidien (3h) | Métriques jour J-1 |
| LinkedIn | lead_forms | 2x/jour (8h, 18h) | Réactivité sur leads |
| SpyFu | ppc/seo_keywords | Hebdomadaire | Économiser API calls |

### Cron jobs

```bash
crontab -e
```

Ajouter :

```bash
# Variables (adapter selon votre installation)
REPO_DIR=/home/user/marketing-data-collection
PYTHON=/usr/bin/python3  # ou le chemin vers votre venv

# Clarity - QUOTIDIEN OBLIGATOIRE
0 2 * * * cd $REPO_DIR/microsoft_clarity/scripts && $PYTHON clarity_analytics.py >> /var/log/clarity.log 2>&1

# LinkedIn Analytics - Quotidien
0 3 * * * cd $REPO_DIR/linkedin/scripts && $PYTHON linkedin_campaign_analytics.py >> /var/log/linkedin.log 2>&1

# LinkedIn Leads - 2x/jour
0 8,18 * * * cd $REPO_DIR/linkedin/scripts && $PYTHON linkedin_lead_forms.py >> /var/log/linkedin_leads.log 2>&1

# SpyFu - Hebdomadaire (dimanche)
0 5 * * 0 cd $REPO_DIR/spyfu/scripts && $PYTHON spyfu_ppc_keywords.py >> /var/log/spyfu.log 2>&1
```

---

## ⚙️ Configuration détaillée

### Fichier config.yaml

Le fichier `config.yaml` centralise tous les paramètres du projet. Voici comment le remplir section par section :

#### 1. Google Cloud & BigQuery

```yaml
google_cloud:
  project_id: "votre-project-id"  # ID de votre projet GCP
  credentials_file: "./account-key.json"  # Chemin vers le Service Account

  datasets:
    linkedin: "linkedin"  # Nom du dataset pour LinkedIn
    clarity: "microsoft_clarity"  # Nom du dataset pour Clarity
    spyfu: "spyfu"  # Nom du dataset pour SpyFu

  location: "EU"  # EU, US, ou autre région
```

#### 2. LinkedIn

```yaml
linkedin:
  oauth:
    client_id: "VOTRE_CLIENT_ID"  # Depuis LinkedIn App
    client_secret: "VOTRE_CLIENT_SECRET"
    refresh_token: "VOTRE_REFRESH_TOKEN"  # Token permanent

  account_id: "503061133"  # Votre Ad Account ID

  collection:
    start_date: "2024-01-01"  # Date de début de collecte
    end_date: null  # null = aujourd'hui
    granularity: "DAILY"  # DAILY, MONTHLY, YEARLY, ALL
    api_version: "202509"  # Version API LinkedIn

  analytics:
    pivots:
      - "CAMPAIGN"  # Données par campagne
      - "CREATIVE"  # Données par creative
```

#### 3. Microsoft Clarity

```yaml
microsoft_clarity:
  project_id: "neutnvggsv"  # Project ID Clarity
  api_key: "VOTRE_API_KEY"  # Token JWT depuis Clarity

  api:
    base_url: "https://www.clarity.ms/api/project-live-insights"
    num_of_days: 1  # 1, 2 ou 3 maximum (limitation API)
```

⚠️ **Important:** L'API Clarity limite à 3 jours maximum. Collecte quotidienne OBLIGATOIRE.

#### 4. SpyFu

```yaml
spyfu:
  api_key: "VOTRE_SECRET_KEY"  # Secret Key (pas l'ID !)

  global:
    country_code: "FR"  # FR, US, DE, GB, etc.
    page_size: 1000  # Nombre de résultats par requête

  domains:
    primary: "votre-domaine.com"  # Votre domaine principal

    competitors:  # Liste de concurrents à surveiller
      - "concurrent1.com"
      - "concurrent2.com"
      - "concurrent3.com"

  comparisons:  # Comparaisons SEO (outrank_comparison)
    - domain: "votre-domaine.com"
      compare_domain: "concurrent1.com"

    - domain: "votre-domaine.com"
      compare_domain: "concurrent2.com"

  filters:  # Filtres globaux
    min_search_volume: 100  # Volume de recherche minimum
    max_keyword_difficulty: 80  # Difficulté maximum
    max_cost_per_click: 50.0  # CPC maximum

  # Configuration par endpoint
  ppc_keywords:
    enabled: true
    sort_by: "SearchVolume"
    filters:
      min_search_volume: 100

  seo_keywords:
    enabled: true
    search_type: "MostValuable"  # MostValuable, GainedClicks, etc.
    filters:
      min_search_volume: 100
      min_seo_clicks: 10
```

**Endpoints disponibles:**
- `ppc_keywords` - Mots-clés PPC
- `new_keywords` - Nouveaux mots-clés
- `paid_serps` - SERPs payants
- `seo_keywords` - Mots-clés SEO
- `newly_ranked` - Nouveaux rankings
- `outrank_comparison` - Comparaisons de ranking
- `top_pages` - Pages les plus performantes
- `ppc_competitors` - Concurrents PPC

#### 5. Automatisation

```yaml
automation:
  schedules:
    linkedin:
      campaign_analytics: "daily"  # Quotidien à 3h
      budget: "weekly"  # Hebdomadaire
      lead_forms: "twice_daily"  # 2x/jour

    clarity:
      analytics: "daily"  # OBLIGATOIRE quotidien

    spyfu:
      ppc_keywords: "weekly"  # Hebdomadaire
      seo_keywords: "weekly"
      other: "monthly"  # Autres endpoints
```

#### 6. Développement & Debug

```yaml
development:
  debug_mode: false  # Mode debug (verbose)
  dry_run: false  # Test sans upload BigQuery
  limit_results: null  # Limiter résultats (ex: 10 pour tests)
  verbose: false  # Logging détaillé
```

### Utilisation dans les scripts

Les scripts chargent automatiquement la configuration :

```python
from config_loader import load_config

# Charger la config
config = load_config()

# Accéder aux valeurs
linkedin_config = config.get_linkedin_config()
spyfu_config = config.get_spyfu_config()

# Ou accès direct par chemin
project_id = config.get('google_cloud.project_id')
domains = config.get('spyfu.domains.all')
```

### Validation de la configuration

```bash
# Tester la configuration
python config_loader.py

# Affiche :
# ✓ Configuration chargée depuis config.yaml
# Configuration Summary
# ======================================
# Google Cloud: clean-avatar-466709-a0
# LinkedIn: 503061133
# SpyFu: votre-domaine.com (3 competitors)
# ...
```

---

## 🔧 Troubleshooting global

### Problèmes courants

#### Permission denied

```bash
chmod 600 account-key.json
```

#### Module not found

```bash
pip install pandas-gbq google-auth
```

#### BigQuery access denied

Vérifier les rôles du Service Account :
- BigQuery Data Editor
- BigQuery Job User

#### API rate limiting

Attendre et espacer les requêtes.

---

## ✅ Checklist de déploiement

### Google Cloud

- [ ] Projet GCP créé
- [ ] BigQuery API activée
- [ ] Service Account créé avec permissions
- [ ] Clé JSON téléchargée et sécurisée
- [ ] 3 datasets créés
- [ ] Tables créées depuis SQL

### LinkedIn

- [ ] App LinkedIn créée
- [ ] Marketing Developer Platform approuvé
- [ ] Refresh Token généré
- [ ] Ad Account ID récupéré
- [ ] Scripts configurés

### Clarity

- [ ] Projet Clarity créé
- [ ] Tracking code installé
- [ ] API Key récupérée
- [ ] Script configuré

### SpyFu

- [ ] API Secret Key récupérée
- [ ] Domaines définis
- [ ] Scripts configurés

### Tests

- [ ] Test LinkedIn analytics
- [ ] Test Clarity analytics
- [ ] Test SpyFu keywords
- [ ] Vérification données BigQuery
- [ ] Vérification JSON backups

### Automatisation

- [ ] Cron jobs configurés
- [ ] Logs directory créé
- [ ] Monitoring mis en place

### Sécurité

- [ ] .gitignore configuré
- [ ] Permissions fichiers correctes
- [ ] Credentials non commités

---

## 📚 Documentation détaillée

Pour plus de détails sur chaque source :

- **[LinkedIn README](linkedin/README.md)** - Configuration OAuth complète, 3 scripts, 7 tables
- **[Microsoft Clarity README](microsoft_clarity/README.md)** - Métriques UX, interprétation, scores
- **[SpyFu README](spyfu/README.md)** - 8 endpoints, analyse SEO/PPC, 26 vues

---

### Documentation API

- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [Microsoft Clarity API](https://docs.microsoft.com/en-us/clarity/)
- [SpyFu API](https://www.spyfu.com/api)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

---

**Version:** 1.0
**Dernière mise à jour:** 2025-10-21
**Auteur:** Deep Scouting
