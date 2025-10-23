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
git clone https://github.com/clairesecehDS/marketing-data-collection.git

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

Voir section [Configuration détaillée](#-configuration-détaillée) pour remplir chaque partie.

---

### Étape 3 : Installer les dépendances Python

```bash
# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Mettre à jour pip
pip install --upgrade pip

# Installer toutes les dépendances depuis requirements.txt
pip install -r requirements.txt
```

**Dépendances installées :**

- `requests` - Requêtes HTTP vers les APIs
- `pandas` - Manipulation de données
- `numpy<2.0.0` - Calculs numériques (version <2.0 requise)
- `google-auth` - Authentification Google Cloud
- `google-cloud-bigquery` - Client BigQuery
- `pandas-gbq` - Intégration pandas-BigQuery
- `pyyaml` - Lecture fichiers YAML (config)

---

### Étape 4 : Vérifier l'installation

```bash
# Vérifier que les modules sont installés
python -c "import requests, pandas, pandas_gbq, google.auth, yaml; print('✓ Toutes les dépendances sont installées')"
```

---

## 🔧 Configuration Google Cloud & BigQuery

### Étape 1 : Créer ou sélectionner un projet Google Cloud

1. Aller sur [Google Cloud Console](https://console.cloud.google.com/)
2. Cliquer sur le **sélecteur de projet** en haut (à côté du logo Google Cloud)

**Option A : Utiliser un projet existant**
- Sélectionner votre projet existant dans la liste
- **Noter le Project ID** (visible sous le nom du projet)
- Passer à l'Étape 2

**Option B : Créer un nouveau projet**
1. Cliquer sur **"Nouveau projet"**
2. Renseigner :
   - **Nom du projet** : `deepscouting-marketing` (ou autre nom descriptif)
   - **Organisation** : Sélectionner si applicable (optionnel)
3. Cliquer sur **"Créer"**
4. **Noter le Project ID** (ex: `clean-avatar-466709-a0`)
   - ⚠️ Le Project ID est différent du nom ! Notez bien l'ID qui est généré.

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

1. Menu latéral → **"BigQuery"** → **"Studio"** (ou "SQL Workspace" dans les anciennes versions)
2. Dans l'explorateur à gauche, cliquer sur votre projet
3. Cliquer sur les **trois points** (⋮) à côté du nom du projet → **"Create dataset"**

**Créer 6 datasets :**

#### Datasets LinkedIn (4 datasets)

**Dataset 1 : LinkedIn Ads Advertising**
- **Dataset ID** : `linkedin_ads_advertising`
- **Data location** : `europe-west9` (Paris) ou autre selon votre région

**Dataset 2 : LinkedIn Ads Library**
- **Dataset ID** : `linkedin_ads_library`
- **Data location** : `europe-west9` (Paris) ou autre selon votre région

**Dataset 3 : LinkedIn Lead Gen Forms**
- **Dataset ID** : `linkedin_leadgen_form`
- **Data location** : `europe-west9` (Paris) ou autre selon votre région

**Dataset 4 : LinkedIn Page Statistics**
- **Dataset ID** : `linkedin_page`
- **Data location** : `europe-west9` (Paris) ou autre selon votre région

#### Dataset 5 : Microsoft Clarity
- **Dataset ID** : `microsoft_clarity`
- **Data location** : `europe-west9` (Paris) ou autre selon votre région

#### Dataset 6 : SpyFu
- **Dataset ID** : `spyfu`
- **Data location** : `europe-west9` (Paris) ou autre selon votre région

---

### Étape 6 : Créer les tables et vues

Les fichiers SQL contiennent des Project IDs hardcodés. Le script `setup_bigquery.py` les remplace automatiquement par votre Project ID depuis `config.yaml`.

#### Option A : Script automatique (recommandé) ✨

```bash
# Exécuter le script de setup
python setup_bigquery.py
```

Le script va :
1. ✅ Lire votre Project ID depuis `config.yaml`
2. ✅ Générer les fichiers SQL avec le bon Project ID dans `generated_sql/`
3. ✅ Vous proposer d'exécuter automatiquement via `bq` CLI ou manuellement

Pour l'exécution automatique, il faudra au préalable vous **authentifier** avec `gcloud auth login` puis sélectionner le projet avec `gcloud config set project votre-project-id`.

Pour l'exécution automatique, il faudra au préalable vous **authentifier** avec `gcloud auth login` puis sélectionner le projet avec `gcloud config set project votre-project-id`.

**Fichiers SQL traités (7 fichiers) :**
- `linkedin/sql/bigquery_campaign_creative_schema.sql`
- `linkedin/sql/bigquery_campaign_creative_budget_schema.sql`
- `linkedin/sql/bigquery_lead_forms_schema.sql`
- `linkedin/sql/bigquery_linkedin_page_schema.sql`
- `linkedin/sql/bigquery_ads_library_schema.sql`
- `microsoft_clarity/sql/bigquery_clarity_schema.sql`
- `spyfu/sql/bigquery_spyfu_schema.sql`

---

#### Option B : Exécution manuelle

Si vous préférez exécuter manuellement :

**Via bq CLI :**

```bash
# 1. Générer les fichiers SQL
python setup_bigquery.py
# Choisir option [2] pour affichage manuel

# 2. Exécuter les commandes affichées
```

**Via Console BigQuery Studio :**

1. Exécuter `python setup_bigquery.py` et choisir option [2]
2. Aller sur https://console.cloud.google.com/bigquery
3. Cliquer sur **"Studio"** → **"+"** (nouvelle requête)
4. Pour chaque fichier dans `generated_sql/` :
   - Copier le contenu du fichier
   - Coller dans l'éditeur
   - Cliquer sur **"Run"**

⚠️ **Important :** Les fichiers dans `generated_sql/` utilisent votre Project ID. N'utilisez PAS directement les fichiers SQL originaux qui contiennent des IDs hardcodés !

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

---

#### 7.4 - Résumé des datasets créés

Après configuration, vous aurez ces datasets dans BigQuery :

```
votre-project-id
├── linkedin_ads_advertising    # Scripts Python (campagnes, budgets, creatives)
├── linkedin_ads_library        # Scripts Python (surveillance concurrence)
├── linkedin_leadgen_form       # Scripts Python (formulaires leads)
├── linkedin_page               # Scripts Python (statistiques page)
├── microsoft_clarity           # Scripts Python (comportement utilisateur)
├── spyfu                       # Scripts Python (SEO/PPC concurrentiel)
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

⚠️ **Important :** Tous les credentials collectés dans cette section devront être renseignés dans le fichier `config.yaml` (voir Étape 6). Les scripts lisent automatiquement leurs configurations depuis ce fichier centralisé.

⚠️ **Important :** Tous les credentials collectés dans cette section devront être renseignés dans le fichier `config.yaml` (voir Étape 6). Les scripts lisent automatiquement leurs configurations depuis ce fichier centralisé.

**Flux OAuth :**
```
1. Créer une App LinkedIn
2. Obtenir Client ID + Client Secret
3. Générer un Authorization Code (via navigateur)
4. Échanger le code contre un Refresh Token
5. Renseigner tous les credentials dans config.yaml
5. Renseigner tous les credentials dans config.yaml
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

### Étape 5 : Configurer config.yaml avec Client ID et Client Secret

⚠️ **Important :** Avant de générer le Refresh Token, vous devez d'abord renseigner le Client ID et le Client Secret dans `config.yaml`.

1. **Ouvrir** `config.yaml` (ou créer depuis `config.example.yaml`)

   ```bash
   cd /home/cseceh/Deep_Scouting/admin/Projet_Ads/code
   nano config.yaml
   ```

2. **Remplir la section LinkedIn OAuth** avec les informations de l'Étape 3 :

   ```yaml
   linkedin:
     oauth:
       client_id: "78xxxxxxxxxxxxxxxx"      # Client ID de l'Étape 3
       client_secret: "WPxxxxxxxxxxxxxxxx"  # Client Secret de l'Étape 3
       refresh_token: ""                    # Sera rempli après l'Étape 6
       redirect_uri: "http://localhost:8080/callback"  # Doit correspondre à l'Étape 3
       scopes:  # Scopes par défaut (peut être modifié si nécessaire)
         - "r_ads"
         - "rw_ads"
         - "r_ads_reporting"
         - "r_ads_leadgen_automation"
   
     account_id: "503061133"  # Ad Account ID de l'Étape 4
   
     collection:
       start_date: "2024-01-01"
       end_date: null  # null = aujourd'hui
       granularity: "DAILY"
       api_version: "202509"
   
     analytics:
       pivots:
         - "CAMPAIGN"
         - "CREATIVE"
   ```

3. **Sauvegarder** le fichier

4. **Sécuriser** le fichier

   ```bash
   chmod 600 config.yaml
   ```

⚠️ **Laissez `refresh_token` vide pour le moment** - Il sera généré à l'étape suivante.

---

### Étape 6 : Générer le Refresh Token

Le Refresh Token est un token permanent qui permet aux scripts de générer automatiquement des Access Tokens.

⚠️ **Prérequis :** Le fichier `config.yaml` doit être configuré avec `client_id` et `client_secret` (Étape 5).

**Processus :**

1. **Exécuter le script de génération de token**

   Le script `token_linkedin.py` lit automatiquement les credentials depuis `config.yaml` :

   ```bash
   cd linkedin/scripts
   python token_linkedin.py
   ```

2. **Autoriser dans le navigateur**
   - Une page LinkedIn s'ouvre automatiquement
   - Se connecter avec votre compte LinkedIn
   - Cliquer sur **"Autoriser"** pour donner les permissions

3. **Le script récupère automatiquement le code**
   - Si `redirect_uri` est `localhost` : le code est capturé automatiquement
   - Sinon : copier le code depuis l'URL de redirection

4. **Le Refresh Token est affiché dans le terminal**

   ```
   ╔════════════════════════════════════════════════════════════════════╗
   ║               ✓ ACCESS TOKEN GÉNÉRÉ AVEC SUCCÈS!                  ║
   ╔════════════════════════════════════════════════════════════════════╝
   
   Access Token:
   AQV...xxxxxxxxxxxxxxxxxx...
   
   Refresh Token:
   AQV...yyyyyyyyyyyyyyyyyy...
   ```

5. **Copier le Refresh Token affiché** (la longue chaîne commençant par `AQV`)

---

### Étape 7 : Ajouter le Refresh Token dans config.yaml

1. **Rouvrir** `config.yaml`

   ```bash
   nano config.yaml
   ```

2. **Ajouter le Refresh Token** dans la section LinkedIn OAuth :

   ```yaml
   linkedin:
     oauth:
       client_id: "78xxxxxxxxxxxxxxxx"
       client_secret: "WPxxxxxxxxxxxxxxxx"
       refresh_token: "AQVxxxxxxxxxxxxxxxx"  # ← COLLER LE REFRESH TOKEN ICI
       redirect_uri: "http://localhost:8080/callback"
   ```

3. **Sauvegarder** le fichier

✅ **Configuration terminée !** Les scripts LinkedIn liront automatiquement tous les credentials depuis `config.yaml`.

**Voir aussi :** Documentation complète dans [linkedin/README.md](linkedin/README.md) section "Configuration OAuth".
### Étape 5 : Configurer config.yaml avec Client ID et Client Secret

⚠️ **Important :** Avant de générer le Refresh Token, vous devez d'abord renseigner le Client ID et le Client Secret dans `config.yaml`.

1. **Ouvrir** `config.yaml` (ou créer depuis `config.example.yaml`)

   ```bash
   cd /home/cseceh/Deep_Scouting/admin/Projet_Ads/code
   nano config.yaml
   ```

2. **Remplir la section LinkedIn OAuth** avec les informations de l'Étape 3 :

   ```yaml
   linkedin:
     oauth:
       client_id: "78xxxxxxxxxxxxxxxx"      # Client ID de l'Étape 3
       client_secret: "WPxxxxxxxxxxxxxxxx"  # Client Secret de l'Étape 3
       refresh_token: ""                    # Sera rempli après l'Étape 6
       redirect_uri: "http://localhost:8080/callback"  # Doit correspondre à l'Étape 3
       scopes:  # Scopes par défaut (peut être modifié si nécessaire)
         - "r_ads"
         - "rw_ads"
         - "r_ads_reporting"
         - "r_ads_leadgen_automation"
   
     account_id: "503061133"  # Ad Account ID de l'Étape 4
   
     collection:
       start_date: "2024-01-01"
       end_date: null  # null = aujourd'hui
       granularity: "DAILY"
       api_version: "202509"
   
     analytics:
       pivots:
         - "CAMPAIGN"
         - "CREATIVE"
   ```

3. **Sauvegarder** le fichier

4. **Sécuriser** le fichier

   ```bash
   chmod 600 config.yaml
   ```

⚠️ **Laissez `refresh_token` vide pour le moment** - Il sera généré à l'étape suivante.

---

### Étape 6 : Générer le Refresh Token

Le Refresh Token est un token permanent qui permet aux scripts de générer automatiquement des Access Tokens.

⚠️ **Prérequis :** Le fichier `config.yaml` doit être configuré avec `client_id` et `client_secret` (Étape 5).

**Processus :**

1. **Exécuter le script de génération de token**

   Le script `token_linkedin.py` lit automatiquement les credentials depuis `config.yaml` :

   ```bash
   cd linkedin/scripts
   python token_linkedin.py
   ```

2. **Autoriser dans le navigateur**
   - Une page LinkedIn s'ouvre automatiquement
   - Se connecter avec votre compte LinkedIn
   - Cliquer sur **"Autoriser"** pour donner les permissions

3. **Le script récupère automatiquement le code**
   - Si `redirect_uri` est `localhost` : le code est capturé automatiquement
   - Sinon : copier le code depuis l'URL de redirection

4. **Le Refresh Token est affiché dans le terminal**

   ```
   ╔════════════════════════════════════════════════════════════════════╗
   ║               ✓ ACCESS TOKEN GÉNÉRÉ AVEC SUCCÈS!                  ║
   ╔════════════════════════════════════════════════════════════════════╝
   
   Access Token:
   AQV...xxxxxxxxxxxxxxxxxx...
   
   Refresh Token:
   AQV...yyyyyyyyyyyyyyyyyy...
   ```

5. **Copier le Refresh Token affiché** (la longue chaîne commençant par `AQV`)

---

### Étape 7 : Ajouter le Refresh Token dans config.yaml

1. **Rouvrir** `config.yaml`

   ```bash
   nano config.yaml
   ```

2. **Ajouter le Refresh Token** dans la section LinkedIn OAuth :

   ```yaml
   linkedin:
     oauth:
       client_id: "78xxxxxxxxxxxxxxxx"
       client_secret: "WPxxxxxxxxxxxxxxxx"
       refresh_token: "AQVxxxxxxxxxxxxxxxx"  # ← COLLER LE REFRESH TOKEN ICI
       redirect_uri: "http://localhost:8080/callback"
   ```

3. **Sauvegarder** le fichier

✅ **Configuration terminée !** Les scripts LinkedIn liront automatiquement tous les credentials depuis `config.yaml`.

**Voir aussi :** Documentation complète dans [linkedin/README.md](linkedin/README.md) section "Configuration OAuth".

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
│   ├── scripts/                  # 5 scripts Python
│   ├── sql/                      # 5 fichiers SQL
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
python linkedin_page_stats.py
python linkedin_ads_library.py

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
# Fichiers de configuration sensibles
config.yaml              # ⚠️ Contient tous les credentials (LinkedIn, Clarity, SpyFu)
account-key.json         # Service Account Google Cloud
# Fichiers de configuration sensibles
config.yaml              # ⚠️ Contient tous les credentials (LinkedIn, Clarity, SpyFu)
account-key.json         # Service Account Google Cloud

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

⚠️ **Fichiers à ne JAMAIS commiter :**
- `config.yaml` - Contient tous vos credentials (LinkedIn OAuth, API keys, etc.)
- `account-key.json` - Clé du Service Account Google Cloud

⚠️ **Fichiers à ne JAMAIS commiter :**
- `config.yaml` - Contient tous vos credentials (LinkedIn OAuth, API keys, etc.)
- `account-key.json` - Clé du Service Account Google Cloud

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
| LinkedIn | ads_library | Quotidien/Hebdomadaire | Surveillance concurrence |
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

# LinkedIn Ads Library - Quotidien (4h) pour surveillance concurrence
0 4 * * * cd $REPO_DIR/linkedin/scripts && $PYTHON linkedin_ads_library.py >> /var/log/linkedin_ads_library.log 2>&1

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

⚠️ **Important :** Les credentials OAuth LinkedIn (Client ID, Client Secret, Refresh Token) doivent être renseignés dans ce fichier `config.yaml`. Les scripts lisent automatiquement ces informations depuis ce fichier.

⚠️ **Important :** Les credentials OAuth LinkedIn (Client ID, Client Secret, Refresh Token) doivent être renseignés dans ce fichier `config.yaml`. Les scripts lisent automatiquement ces informations depuis ce fichier.

```yaml
linkedin:
  oauth:
    client_id: "78xxxxxxxxxxxxxxxx"  # Client ID depuis LinkedIn App (Étape 3)
    client_secret: "WPxxxxxxxxxxxxxxxx"  # Client Secret depuis LinkedIn App (Étape 3)
    refresh_token: "AQVxxxxxxxxxxxxxxxx"  # Refresh Token généré via token_linkedin.py (Étape 5)
    access_token: "AQWxxxxxxxxxxxxxxxx"  # Access Token (généré automatiquement ou manuellement)

  account_id: "503061133"  # Votre Ad Account ID (Étape 4)
  organization_id: "5509810"  # Organization ID pour page stats et lead forms

  collection:
    start_date: "2024-01-01"  # Date de début de collecte
    end_date: null  # null = aujourd'hui
    granularity: "DAILY"  # DAILY, MONTHLY, YEARLY, ALL
    api_version: "202509"  # Version API LinkedIn

  analytics:
    pivots:
      - "CAMPAIGN"  # Données par campagne
      - "CREATIVE"  # Données par creative

  # Ads Library - Surveillance des publicités concurrentes
  ads_library:
    # Mots-clés à rechercher dans les publicités
    # Utilisez des termes liés à votre secteur d'activité
    keywords:
      - "marketing digital"
      - "formation"
      - "intelligence artificielle"
      - "data science"

    # Annonceurs spécifiques à surveiller (noms EXACTS)
    # IMPORTANT: Utilisez le nom exact tel qu'il apparaît sur LinkedIn
    # Pour trouver le nom exact :
    #   1. Cherchez la page LinkedIn de votre concurrent
    #   2. Le nom exact est affiché en haut de la page
    advertisers:
      - "HEC Paris"
      - "ESSEC Business School"
      - "ESCP Business School"
      - "emlyon business school"

    # Pays à cibler (codes ISO à 2 lettres en MINUSCULES)
    countries:
      - "fr"  # France
      - "us"  # États-Unis
      # - "gb"  # Royaume-Uni
      # - "de"  # Allemagne
      # - "es"  # Espagne
      # - "it"  # Italie

    # Maximum de résultats par recherche
    # L'API LinkedIn retourne 25 résultats par page
    # Cette valeur définit le nombre total maximum à récupérer
    max_results_per_search: 500

    # Délai entre les requêtes API (en secondes)
    # IMPORTANT: Ne pas descendre en dessous de 2.0 pour éviter les erreurs 429
    # L'API LinkedIn limite à environ 30 requêtes par minute
    request_delay: 2.0
```

**Notes sur la configuration Ads Library :**

1. **Keywords vs Advertisers** :
   - Vous pouvez utiliser uniquement `keywords`, uniquement `advertisers`, ou les deux
   - Au moins l'un des deux doit être renseigné (non vide)
   - `keywords` : Recherche large dans toutes les publicités contenant ces mots
   - `advertisers` : Recherche ciblée sur des annonceurs spécifiques

2. **Nom exact des annonceurs** :
   - Le nom doit correspondre EXACTEMENT au nom de la page LinkedIn
   - Sensible à la casse (majuscules/minuscules)
   - Sensible aux espaces et caractères spéciaux
   - Astuce : Recherchez "SKEMA BUSINESS SCHOOL" si c'est le nom exact sur LinkedIn

3. **Codes pays** :
   - Utilisez les codes ISO 3166-1 alpha-2 (2 lettres)
   - Toujours en **minuscules** : `"fr"` et non `"FR"`
   - Liste complète : https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

4. **Rate limiting** :
   - L'API limite à ~30 requêtes par minute
   - Le paramètre `request_delay: 2.0` ajoute 2 secondes entre chaque requête
   - En cas d'erreur 429 (trop de requêtes), le script attend automatiquement
   - Augmentez `request_delay` à 3.0 ou 5.0 si vous avez beaucoup d'erreurs 429

5. **Données collectées** :
   - URL de la publicité
   - Nom de l'annonceur
   - Type de publicité (SPONSORED_VIDEO, SPONSORED_CONTENT, etc.)
   - Dates de première et dernière impression
   - Fourchette d'impressions
   - Distribution par pays
   - Informations de ciblage (segments)

**Exemple de configuration complète :**

```yaml
linkedin:
  ads_library:
    # Recherche par mots-clés dans le secteur éducation
    keywords:
      - "MBA"
      - "Executive Education"
      - "Business School"
      - "Formation continue"
      - "Grande École"

    # Surveillance de 5 concurrents directs
    advertisers:
      - "HEC Paris"
      - "INSEAD"
      - "ESSEC Business School"
      - "ESCP Business School"
      - "emlyon business school"

    # Ciblage France uniquement
    countries:
      - "fr"

    # Limite à 250 pubs par recherche (économiser les appels API)
    max_results_per_search: 250

    # Délai de 3 secondes pour être plus prudent
    request_delay: 3.0
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

### Configuration initiale

- [ ] Repository cloné depuis GitHub
- [ ] Fichier `config.yaml` créé depuis `config.example.yaml`
- [ ] Dépendances Python installées (`requirements.txt`)

### Configuration initiale

- [ ] Repository cloné depuis GitHub
- [ ] Fichier `config.yaml` créé depuis `config.example.yaml`
- [ ] Dépendances Python installées (`requirements.txt`)

### Google Cloud

- [ ] Projet GCP créé
- [ ] BigQuery API activée
- [ ] Service Account créé avec permissions
- [ ] Clé JSON téléchargée et renommée `account-key.json`
- [ ] `account-key.json` sécurisé (chmod 600)
- [ ] Project ID ajouté dans `config.yaml`
- [ ] 6 datasets créés (linkedin x4, clarity, spyfu)
- [ ] Tables créées depuis SQL (via `setup_bigquery.py`)
- [ ] Clé JSON téléchargée et renommée `account-key.json`
- [ ] `account-key.json` sécurisé (chmod 600)
- [ ] Project ID ajouté dans `config.yaml`
- [ ] 6 datasets créés (linkedin x4, clarity, spyfu)
- [ ] Tables créées depuis SQL (via `setup_bigquery.py`)

### LinkedIn

- [ ] App LinkedIn créée
- [ ] Marketing Developer Platform approuvé
- [ ] Client ID et Client Secret récupérés (Étape 3)
- [ ] Redirect URL configuré : `http://localhost:8080/callback` (Étape 3)
- [ ] Ad Account ID récupéré (Étape 4)
- [ ] **Client ID et Client Secret ajoutés dans `config.yaml`** (Étape 5)
- [ ] Refresh Token généré via `token_linkedin.py` (Étape 6)
- [ ] **Refresh Token ajouté dans `config.yaml`** (Étape 7)
- [ ] Client ID et Client Secret récupérés (Étape 3)
- [ ] Redirect URL configuré : `http://localhost:8080/callback` (Étape 3)
- [ ] Ad Account ID récupéré (Étape 4)
- [ ] **Client ID et Client Secret ajoutés dans `config.yaml`** (Étape 5)
- [ ] Refresh Token généré via `token_linkedin.py` (Étape 6)
- [ ] **Refresh Token ajouté dans `config.yaml`** (Étape 7)

### Clarity

- [ ] Projet Clarity créé
- [ ] Tracking code installé sur le site
- [ ] Project ID récupéré
- [ ] API Key (JWT) récupérée
- [ ] **Credentials ajoutés dans `config.yaml`** (project_id, api_key)
- [ ] Tracking code installé sur le site
- [ ] Project ID récupéré
- [ ] API Key (JWT) récupérée
- [ ] **Credentials ajoutés dans `config.yaml`** (project_id, api_key)

### SpyFu

- [ ] API Secret Key récupérée depuis compte SpyFu
- [ ] Domaines à surveiller définis
- [ ] Concurrents identifiés
- [ ] **Credentials et domaines ajoutés dans `config.yaml`** (api_key, domains, competitors)
- [ ] API Secret Key récupérée depuis compte SpyFu
- [ ] Domaines à surveiller définis
- [ ] Concurrents identifiés
- [ ] **Credentials et domaines ajoutés dans `config.yaml`** (api_key, domains, competitors)

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
