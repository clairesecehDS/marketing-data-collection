# 📊 Marketing Data Collection Suite

Suite complète de collecte automatisée de données marketing depuis LinkedIn Ads, Microsoft Clarity et SpyFu vers Google BigQuery.

---

## 🎯 Objectif

Centraliser et historiser toutes vos données marketing dans BigQuery pour :
- ✅ Analyse unifiée multi-sources
- ✅ Reporting automatisé
- ✅ Corrélations entre sources
- ✅ Construction d'historique long terme
- ✅ Backup JSON automatique

---

## 📦 Sources de données

| Source | Données collectées | Tables | Fréquence recommandée |
|--------|-------------------|--------|------------------------|
| **LinkedIn Ads** | Campagnes, budgets, creatives, lead forms, ads library | 8 tables | Hebdomadaire |
| **Microsoft Clarity** | Comportement utilisateur, frustration, engagement | 1 table | Quotidien (obligatoire) |
| **SpyFu** | SEO/PPC concurrentiel, keywords, domaines, annonces | 11 tables | Mensuel |
| **Brevo** | Campagnes email, événements, listes contacts | 3 tables | Hebdomadaire |

---

## 🚀 Quick Start

### 1. Cloner le repository

```bash
git clone [URL_DU_REPO_GITHUB]
cd marketing-data-collection
```

### 2. Configurer

```bash
# Copier le fichier de configuration
cp config.example.yaml config.yaml

# Éditer avec vos credentials
nano config.yaml
```

### 3. Installer les dépendances

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Exécuter un script

```bash
# LinkedIn Analytics
cd linkedin/scripts
python linkedin_campaign_analytics.py

# Microsoft Clarity
cd microsoft_clarity/scripts
python clarity_analytics.py

# SpyFu Keywords
cd spyfu/scripts
python spyfu_ppc_keywords.py

# Brevo Email Marketing
cd brevo
python sync_brevo_data.py
```

---

## 📖 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Guide de configuration complet
  - Configuration Google Cloud & BigQuery
  - Obtention des tokens et API keys
  - Permissions et sécurité
  - Automatisation avec cron
  - Troubleshooting

- **[linkedin/README.md](linkedin/README.md)** - Documentation LinkedIn
  - OAuth 2.0 configuration
  - 3 scripts principaux (campaign_analytics, lead_forms, ads_library)
  - 8 tables + 10 vues BigQuery
  - Troubleshooting erreurs courantes

- **[microsoft_clarity/README.md](microsoft_clarity/README.md)** - Documentation Clarity
  - Configuration API
  - 16 métriques collectées
  - Guide d'interprétation
  - Scores de référence

- **[spyfu/README.md](spyfu/README.md)** - Documentation SpyFu
  - 10 scripts pour différents endpoints
  - 11 tables + 25 vues BigQuery
  - Configuration domaines et concurrents
  - Filtres et paramètres

- **[brevo/README.md](brevo/README.md)** - Documentation Brevo
  - Synchronisation campagnes email
  - Événements marketing (opens, clicks, bounces)
  - Listes de contacts et rapports SMTP
  - Cloud Run Job + Cloud Scheduler automatisé

---

## 🗂️ Structure du projet

```
marketing-data-collection/
├── config.example.yaml         # Template de configuration
├── config.yaml                 # Configuration (à créer, non commité)
├── config_loader.py            # Utilitaire de chargement config
├── setup_bigquery.py           # Script de setup BigQuery (avec config)
├── requirements.txt            # Dépendances Python
├── account-key.json            # Service Account GCP (à créer, non commité)
├── .gitignore                  # Fichiers à ignorer (déjà inclus)
│
├── linkedin/
│   ├── README.md
│   ├── main.py                 # Point d'entrée principal (Cloud Functions)
│   ├── main_ads_library.py     # Point d'entrée Ads Library (Cloud Functions)
│   ├── scripts/
│   │   ├── linkedin_campaign_analytics.py  # Analytics campagnes & creatives (4 tables)
│   │   ├── linkedin_budget.py              # Budgets campagnes & creatives (inclus dans campaign_analytics)
│   │   ├── linkedin_lead_forms.py          # Lead gen forms & réponses (3 tables)
│   │   ├── linkedin_ads_library.py         # Surveillance concurrence (1 table)
│   │   └── token_linkedin.py               # Génération token OAuth
│   ├── sql/
│   │   ├── bigquery_campaign_creative_schema.sql        # Schéma analytics & budgets
│   │   ├── bigquery_campaign_creative_budget_schema.sql # Schéma budgets (vues)
│   │   ├── bigquery_lead_forms_schema.sql               # Schéma lead gen (3 tables + vues)
│   │   └── bigquery_ads_library_schema.sql              # Schéma ads library (1 table)
│   ├── ads_library_weekly/     # Cloud Function Ads Library (déploiement séparé)
│   │   ├── main.py
│   │   ├── config.yaml
│   │   └── scripts/
│   └── data/                   # Backups JSON locaux
│
├── microsoft_clarity/
│   ├── README.md
│   ├── main.py                 # Point d'entrée principal (Cloud Functions)
│   ├── scripts/
│   │   └── clarity_analytics.py
│   ├── sql/
│   │   └── bigquery_clarity_schema.sql
│   └── data/
│
├── spyfu/
│   ├── README.md
│   ├── main.py                 # Point d'entrée hebdomadaire (Cloud Functions)
│   ├── main_monthly.py         # Point d'entrée mensuel
│   ├── main_quarterly.py       # Point d'entrée trimestriel
│   ├── main_on_demand.py       # Point d'entrée à la demande
│   ├── scripts/
│   │   ├── spyfu_ppc_keywords.py           # Mots-clés PPC (mensuel) → 1 table
│   │   ├── spyfu_seo_keywords.py           # Mots-clés SEO (mensuel) → 1 table
│   │   ├── spyfu_new_keywords.py           # Nouveaux mots-clés (mensuel) → 1 table
│   │   ├── spyfu_newly_ranked_keywords.py  # Nouveaux rankings (mensuel) → 1 table
│   │   ├── spyfu_top_pages.py              # Top pages SEO (mensuel) → 1 table
│   │   ├── spyfu_domain_stats.py           # Stats domaine (mensuel) → 1 table + 1 table term_domain_stats
│   │   ├── spyfu_most_valuable_keywords.py # Mots-clés précieux (mensuel) → 1 table
│   │   ├── spyfu_domain_ad_history.py      # Historique annonces (trimestriel) → 1 table
│   │   ├── spyfu_term_ad_history.py        # Historique par mot-clé (trimestriel) → 1 table
│   │   └── spyfu_related_keywords.py       # Mots-clés associés (on-demand) → 1 table
│   ├── sql/
│   │   └── bigquery_spyfu_complete_schema.sql  # Schéma complet (11 tables + 25 vues)
│   └── data/
│
├── brevo/
│   ├── README.md
│   ├── sync_brevo_data.py      # Script principal de synchronisation
│   ├── config.yaml
│   ├── scripts/
│   │   ├── fetch_campaigns.py          # Récupération campagnes → 1 table
│   │   ├── fetch_events.py             # Récupération événements → 1 table
│   │   ├── fetch_contacts_lists.py     # Récupération listes contacts → 1 table
│   │   ├── fetch_smtp_reports.py       # Récupération rapports SMTP → 1 table
│   │   └── upload_to_bigquery.py       # Upload vers BigQuery
│   ├── sql/
│   │   └── bigquery_brevo_schema.sql   # Schéma complet (4 tables)
│   └── data/
│
├── SETUP_GUIDE.md              # Guide de configuration complet
└── README.md                   # Ce fichier
```

---

## ⚙️ Configuration centralisée

Tous les paramètres sont centralisés dans `config.yaml` :

- **Credentials** - API keys, tokens, project IDs
- **Domaines et concurrents** - Liste des sites à surveiller
- **Métriques** - Sélection des métriques à collecter
- **Périodes** - Dates de collecte
- **BigQuery** - Configuration datasets et tables
- **Automatisation** - Planification des collectes

**Exemple d'utilisation dans les scripts :**

```python
from config_loader import load_config

config = load_config()
linkedin_config = config.get_linkedin_config()
spyfu_domains = config.get('spyfu.domains.all')
```

**Valider votre configuration :**

```bash
python config_loader.py
```

Voir [SETUP_GUIDE.md - Configuration détaillée](SETUP_GUIDE.md#️-configuration-détaillée) pour plus d'informations.

---

## 📊 Tables BigQuery et Métriques

### Vue d'ensemble du projet BigQuery

| Dataset | Nombre de tables | Description |
|---------|------------------|-------------|
| `GA4_EPBS` | 20 | Google Analytics 4 - Audiences, démographie, e-commerce, événements |
| `analytics_427042790` | 15 | Google Analytics classique |
| `google_Ads_EPBS` | 219 | Google Ads - Campagnes, annonces, performances |
| `google_ads_processed` | 4 | Données Google Ads traitées |
| `google_search_console_` | 3 | Google Search Console |
| `googleanalytics_` | 4 | Google Analytics |
| `searchconsole_EPBS` | 3 | Search Console EPBS |
| **`linkedin_ads_advertising`** | **10** | **LinkedIn Ads - 4 tables + 6 vues** |
| **`linkedin_ads_library`** | **1** | **LinkedIn Ads Library - 1 table** |
| **`linkedin_leadgen_form`** | **7** | **LinkedIn Lead Gen Forms - 3 tables + 4 vues** |
| **`microsoft_clarity`** | **1** | **Microsoft Clarity - 1 table** |
| **`spyfu`** | **36** | **SpyFu - 11 tables + 25 vues** |
| **`brevo`** | **3** | **Brevo Email Marketing - 3 tables** |

**Total:** 326 tables

Pour consulter le schéma détaillé de TOUTES les tables (colonnes, types, descriptions), voir **[BIGQUERY_SCHEMAS.md](BIGQUERY_SCHEMAS.md)**.

**Déploiement automatisé:**

- Cloud Run Job déployé dans `europe-west9` (Paris)
- Cloud Scheduler dans `europe-west1` (Belgique)
- Exécution hebdomadaire (lundi 2h)
- Mode APPEND pour conservation de l'historique (sauf campaigns en TRUNCATE)

---

### Résumé des tables de ce projet

**Tables de données créées par ce projet Marketing Data Collection :**

- LinkedIn Ads Advertising : 4 tables + 6 vues
- LinkedIn Ads Library : 1 table
- LinkedIn Lead Gen Forms : 3 tables + 4 vues
- Microsoft Clarity : 1 table
- SpyFu : 11 tables + 25 vues
- Brevo Email Marketing : 3 tables

**Total : 23 tables de données + 35 vues SQL = 58 objets BigQuery**

Pour voir le schéma complet de TOUTES les tables du projet BigQuery (326 tables), consultez [BIGQUERY_SCHEMAS.md](BIGQUERY_SCHEMAS.md).

---

## 🔒 Sécurité

### Fichiers sensibles (NON commités)

Ces fichiers contiennent des credentials et ne doivent **JAMAIS** être commités dans Git :

```bash
config.yaml           # Configuration avec vos credentials
account-key.json      # Service Account Google Cloud
*.log                # Logs d'exécution
data/*.json          # Backups JSON (optionnel)
```

Vérifiez que `.gitignore` contient :

```
config.yaml
account-key.json
*.log
data/
venv/
__pycache__/
```

### Bonnes pratiques

✅ Utilisez `config.example.yaml` comme template
✅ Ne partagez jamais `config.yaml` ou `account-key.json`
✅ Utilisez un Service Account GCP dédié avec permissions minimales
✅ Activez l'authentification à deux facteurs sur tous les comptes
✅ Renouvelez les tokens régulièrement
✅ Limitez les permissions BigQuery au strict nécessaire

---

## 🤖 Automatisation

### Cron jobs recommandés

```bash
# LinkedIn Analytics - Hebdomadaire (lundi à 1h)
0 1 * * 1 cd /path/to/marketing-data-collection/linkedin/scripts && python linkedin_campaign_analytics.py >> /var/log/linkedin.log 2>&1

# Microsoft Clarity - Quotidien à 3h (OBLIGATOIRE)
0 3 * * * cd /path/to/marketing-data-collection/microsoft_clarity/scripts && python clarity_analytics.py >> /var/log/clarity.log 2>&1

# SpyFu - Mensuel (1er du mois à 1h)
0 1 1 * * cd /path/to/marketing-data-collection/spyfu/scripts && python spyfu_ppc_keywords.py >> /var/log/spyfu.log 2>&1

# Brevo Email Marketing - Automatisé via Cloud Scheduler (lundi à 2h)
# Configuration: voir brevo/DEPLOYMENT_GUIDE.md
```

**Important :**

- Microsoft Clarity limite à 1-3 jours maximum, la collecte **DOIT** être quotidienne.
- Brevo utilise Cloud Run Job + Cloud Scheduler (pas de cron local nécessaire)

---

## 🔧 Prérequis

### Comptes nécessaires

- ☁️ **Google Cloud Platform** - Projet avec BigQuery activé
- 💼 **LinkedIn Marketing Developer Platform** - App approuvée
- 🔍 **Microsoft Clarity** - Projet créé
- 🎯 **SpyFu** - Abonnement actif
- 📧 **Brevo (Sendinblue)** - Compte avec API key

---

## 📝 Workflow typique

### 1. Configuration initiale

```bash
# Cloner
git clone [URL]
cd marketing-data-collection

# Configurer
cp config.example.yaml config.yaml
nano config.yaml

# Installer
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Créer les tables BigQuery
# (Exécuter les fichiers SQL depuis la console BigQuery)
```

### 2. Premier test

```bash
# Tester la configuration
python config_loader.py

# Test Clarity (plus simple, pas d'OAuth)
cd microsoft_clarity/scripts
python clarity_analytics.py

# Test SpyFu
cd spyfu/scripts
python spyfu_ppc_keywords.py
```

### 3. Configuration LinkedIn OAuth

Voir [linkedin/README.md - OAuth 2.0](linkedin/README.md#-oauth-20-configuration) pour obtenir le Refresh Token.

### 4. Automatisation

```bash
# Configurer les cron jobs
crontab -e
# (Ajouter les lignes de la section Automatisation)

# Vérifier les logs
tail -f /var/log/clarity.log
```

---

## ❓ Support et Troubleshooting

### Problèmes courants

#### Permission denied sur account-key.json
```bash
chmod 600 account-key.json
```

#### Module not found
```bash
pip install pandas-gbq google-auth pyyaml
```

#### BigQuery access denied
Vérifier les rôles du Service Account :
- BigQuery Data Editor
- BigQuery Job User

#### API rate limiting
Espacer les requêtes, attendre, vérifier les quotas.

---

## 📦 Dépendances Python

Toutes les dépendances sont listées dans [requirements.txt](requirements.txt) :

- `requests>=2.31.0` - Requêtes HTTP
- `pandas>=2.0.0` - Manipulation de données
- `numpy<2.0.0` - Calculs numériques (⚠️ version <2.0 requise)
- `google-auth>=2.23.0` - Authentification Google Cloud
- `google-cloud-bigquery>=3.11.0` - Client BigQuery
- `pandas-gbq>=0.19.0` - Intégration pandas-BigQuery
- `pyyaml>=6.0` - Lecture fichiers YAML

Installation :

```bash
pip install -r requirements.txt
```

---

## 🎓 Ressources

### Documentation API officielle

- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [Microsoft Clarity API](https://learn.microsoft.com/en-us/clarity/)
- [SpyFu API](https://www.spyfu.com/apis)
- [Google BigQuery](https://cloud.google.com/bigquery/docs)
- [Brevo API](https://developers.brevo.com/docs)

### Aide supplémentaire

- Google Cloud Console : https://console.cloud.google.com
- LinkedIn Developer Portal : https://www.linkedin.com/developers
- Microsoft Clarity : https://clarity.microsoft.com

---

## 📄 License

Ce projet est fourni tel quel pour usage interne. Respectez les conditions d'utilisation des API tierces (LinkedIn, Clarity, SpyFu).

---

## ✅ Checklist de déploiement

### Google Cloud

- [ ] Projet GCP créé
- [ ] BigQuery API activée
- [ ] Service Account créé avec permissions
- [ ] Clé JSON téléchargée (`account-key.json`)
- [ ] 6 datasets créés (linkedin_ads_advertising, linkedin_ads_library, linkedin_leadgen_form, microsoft_clarity, spyfu, brevo)
- [ ] Tables créées depuis fichiers SQL (24 tables + 35 vues)

### Configuration
- [ ] `config.yaml` créé depuis `config.example.yaml`
- [ ] Credentials Google Cloud renseignés
- [ ] LinkedIn credentials configurés
- [ ] Clarity credentials configurés
- [ ] SpyFu credentials configurés
- [ ] Liste de domaines et concurrents remplie
- [ ] Configuration validée (`python config_loader.py`)

### LinkedIn
- [ ] App LinkedIn créée
- [ ] Marketing Developer Platform approuvé
- [ ] Refresh Token généré
- [ ] Ad Account ID récupéré

### Clarity
- [ ] Projet Clarity créé
- [ ] API Token généré (JWT)
- [ ] Site web tracké

### SpyFu

- [ ] Abonnement SpyFu actif
- [ ] Secret Key récupérée

### Brevo

- [ ] Compte Brevo créé
- [ ] API Key récupérée
- [ ] Cloud Run Job déployé
- [ ] Cloud Scheduler configuré

### Tests
- [ ] Configuration validée
- [ ] Test Clarity réussi
- [ ] Test SpyFu réussi
- [ ] Test LinkedIn réussi
- [ ] Upload BigQuery vérifié

### Production
- [ ] Cron jobs configurés
- [ ] Logs configurés
- [ ] Alertes configurées (optionnel)
- [ ] Dashboard créé (optionnel)

---

**Démarrez avec le guide complet : [SETUP_GUIDE.md](SETUP_GUIDE.md)**
