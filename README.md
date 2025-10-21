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

| Source | Données collectées | Fréquence recommandée |
|--------|-------------------|-----------------------|
| **LinkedIn Ads** | Campagnes, budgets, lead forms | Quotidien |
| **Microsoft Clarity** | Comportement utilisateur, frustration | Quotidien (obligatoire) |
| **SpyFu** | SEO/PPC concurrentiel, keywords | Hebdomadaire |

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
pip install requests pandas pandas-gbq google-auth google-cloud-bigquery "numpy<2.0.0" pyyaml
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
  - 3 scripts (analytics, budget, lead forms)
  - 7 tables + 12 vues BigQuery
  - Troubleshooting erreurs courantes

- **[microsoft_clarity/README.md](microsoft_clarity/README.md)** - Documentation Clarity
  - Configuration API
  - 16 métriques collectées
  - Guide d'interprétation
  - Scores de référence

- **[spyfu/README.md](spyfu/README.md)** - Documentation SpyFu
  - 8 endpoints différents
  - 8 tables + 26 vues BigQuery
  - Configuration concurrents
  - Filtres et paramètres

---

## 🗂️ Structure du projet

```
marketing-data-collection/
├── config.example.yaml         # Template de configuration
├── config.yaml                 # Configuration (à créer, non commité)
├── config_loader.py            # Utilitaire de chargement config
├── account-key.json            # Service Account GCP (à créer, non commité)
│
├── linkedin/
│   ├── README.md
│   ├── scripts/
│   │   ├── linkedin_campaign_analytics.py
│   │   ├── linkedin_budget.py
│   │   ├── linkedin_lead_forms.py
│   │   └── token_linkedin.py
│   ├── sql/
│   │   └── bigquery_linkedin_schema.sql
│   └── data/                   # Backups JSON
│
├── microsoft_clarity/
│   ├── README.md
│   ├── scripts/
│   │   └── clarity_analytics.py
│   ├── sql/
│   │   └── bigquery_clarity_schema.sql
│   └── data/
│
├── spyfu/
│   ├── README.md
│   ├── scripts/
│   │   ├── spyfu_ppc_keywords.py
│   │   ├── spyfu_seo_keywords.py
│   │   ├── spyfu_new_keywords.py
│   │   ├── spyfu_newly_ranked.py
│   │   ├── spyfu_paid_serps.py
│   │   ├── spyfu_top_pages.py
│   │   ├── spyfu_outrank_comparison.py
│   │   └── spyfu_ppc_competitors.py
│   ├── sql/
│   │   └── bigquery_spyfu_schema.sql
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

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Sources de données                        │
├──────────────┬──────────────────┬──────────────────────────┤
│ LinkedIn Ads │ Microsoft Clarity│      SpyFu API           │
│  OAuth 2.0   │    API Key       │      API Key             │
└──────┬───────┴────────┬─────────┴──────────┬───────────────┘
       │                │                    │
       v                v                    v
┌─────────────────────────────────────────────────────────────┐
│              Scripts Python (ce repository)                 │
│     ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│     │  linkedin/  │  │  clarity/   │  │   spyfu/    │      │
│     │  scripts/   │  │  scripts/   │  │   scripts/  │      │
│     └─────────────┘  └─────────────┘  └─────────────┘      │
│                           │                                 │
│                    JSON Backup (data/)                      │
└───────────────────────────┼─────────────────────────────────┘
                            │ Service Account
                            v
                    ┌─────────────────┐
                    │   BigQuery      │
                    │ (Google Cloud)  │
                    │                 │
                    │  ┌───────────┐  │
                    │  │ linkedin  │  │
                    │  ├───────────┤  │
                    │  │ clarity   │  │
                    │  ├───────────┤  │
                    │  │ spyfu     │  │
                    │  └───────────┘  │
                    └─────────────────┘
                            │
                            v
                    ┌─────────────────┐
                    │  Looker Studio  │
                    │  Data Studio    │
                    │  Tableau, etc.  │
                    └─────────────────┘
```

---

## 📊 Tables BigQuery

### LinkedIn (7 tables)
- `campaign_analytics` - Métriques par campagne
- `creative_analytics` - Métriques par creative
- `campaign_metadata` - Informations campagnes
- `creative_metadata` - Informations creatives
- `budget_data` - Budgets et enchères
- `lead_form_responses` - Réponses lead forms
- `lead_form_questions` - Questions des formulaires

### Microsoft Clarity (1 table)
- `clarity_metrics` - Toutes les métriques (traffic, engagement, frustration, errors)

### SpyFu (8 tables)
- `ppc_keywords` - Mots-clés PPC
- `new_keywords` - Nouveaux mots-clés
- `paid_serps` - SERPs payants
- `seo_keywords` - Mots-clés SEO
- `newly_ranked` - Nouveaux rankings
- `outrank_comparison` - Comparaisons
- `top_pages` - Pages performantes
- `ppc_competitors` - Concurrents PPC

**+ 38 vues SQL** pour faciliter l'analyse

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
# LinkedIn Analytics - Quotidien à 3h
0 3 * * * cd /path/to/marketing-data-collection/linkedin/scripts && python linkedin_campaign_analytics.py >> /var/log/linkedin.log 2>&1

# Microsoft Clarity - Quotidien à 2h (OBLIGATOIRE)
0 2 * * * cd /path/to/marketing-data-collection/microsoft_clarity/scripts && python clarity_analytics.py >> /var/log/clarity.log 2>&1

# SpyFu PPC Keywords - Hebdomadaire (dimanche à 5h)
0 5 * * 0 cd /path/to/marketing-data-collection/spyfu/scripts && python spyfu_ppc_keywords.py >> /var/log/spyfu.log 2>&1

# SpyFu SEO Keywords - Hebdomadaire (dimanche à 6h)
0 6 * * 0 cd /path/to/marketing-data-collection/spyfu/scripts && python spyfu_seo_keywords.py >> /var/log/spyfu.log 2>&1
```

**Important :** Microsoft Clarity limite à 1-3 jours maximum, la collecte **DOIT** être quotidienne.

---

## 🔧 Prérequis

### Comptes nécessaires

- ☁️ **Google Cloud Platform** - Projet avec BigQuery activé
- 💼 **LinkedIn Marketing Developer Platform** - App approuvée
- 🔍 **Microsoft Clarity** - Projet créé
- 🎯 **SpyFu** - Abonnement actif

### Logiciels

- Python 3.8+
- Git
- Connexion internet

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
pip install requests pandas pandas-gbq google-auth google-cloud-bigquery "numpy<2.0.0" pyyaml

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

### Documentation détaillée

- 📖 [SETUP_GUIDE.md](SETUP_GUIDE.md) - Guide complet avec screenshots
- 🔵 [linkedin/README.md](linkedin/README.md) - Troubleshooting LinkedIn
- 🟣 [microsoft_clarity/README.md](microsoft_clarity/README.md) - Guide Clarity
- 🟢 [spyfu/README.md](spyfu/README.md) - Configuration SpyFu

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

```
requests
pandas
pandas-gbq
google-auth
google-cloud-bigquery
pyyaml
numpy<2.0.0
```

Installation :

```bash
pip install requests pandas pandas-gbq google-auth google-cloud-bigquery "numpy<2.0.0" pyyaml
```

---

## 🎓 Ressources

### Documentation API officielle

- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [Microsoft Clarity API](https://learn.microsoft.com/en-us/clarity/)
- [SpyFu API](https://www.spyfu.com/apis)
- [Google BigQuery](https://cloud.google.com/bigquery/docs)

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
- [ ] 3 datasets créés (linkedin, microsoft_clarity, spyfu)
- [ ] Tables créées depuis fichiers SQL

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
