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
| **LinkedIn Ads** | Campagnes, budgets, creatives, lead forms, ads library | 8 tables | Quotidien/Hebdomadaire |
| **Microsoft Clarity** | Comportement utilisateur, frustration, engagement | 1 table | Quotidien (obligatoire) |
| **SpyFu** | SEO/PPC concurrentiel, keywords, domaines, annonces | 11 tables | Mensuel/Trimestriel |

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
├── spyfu-monthly/              # Cloud Function SpyFu mensuel (déploiement séparé)
│   ├── main.py
│   ├── config.yaml
│   └── scripts/
│
├── spyfu-quarterly/            # Cloud Function SpyFu trimestriel (déploiement séparé)
│   ├── main.py
│   ├── config.yaml
│   └── scripts/
│
├── spyfu-on-demand/            # Cloud Function SpyFu on-demand (déploiement séparé)
│   ├── main.py
│   ├── config.yaml
│   └── scripts/
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

## 📊 Tables BigQuery et Métriques

### Vue d'ensemble du projet BigQuery

**Projet:** `ecoledesponts`

Le projet contient **323 tables** réparties sur **12 datasets** :

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

**Total:** 323 tables

Pour consulter le schéma détaillé de TOUTES les tables (colonnes, types, descriptions), voir **[BIGQUERY_SCHEMAS.md](BIGQUERY_SCHEMAS.md)**.

Les sections ci-dessous détaillent uniquement les tables créées par ce projet (LinkedIn, Clarity, SpyFu).

---

### LinkedIn Ads Advertising (4 tables + 6 vues)

#### Table `campaign_analytics`
**Script:** [linkedin_campaign_analytics.py](linkedin/scripts/linkedin_campaign_analytics.py)
**Métriques collectées (25 colonnes):**
- **Identifiants:** campaign_id, campaign_urn
- **Période:** date_range_start, date_range_end
- **Métriques de base:** impressions, clicks, cost_in_usd
- **Performance:** ctr, cpc, cpm
- **Engagement:** reactions, comments, shares, total_engagements, engagement_rate
- **Conversions:** landing_page_clicks, one_click_leads, external_website_conversions, external_website_post_click_conversions, external_website_post_view_conversions
- **Vidéo:** video_views, video_starts, video_completions
- **Reach:** approximate_member_reach
- **Métadonnées:** retrieved_at, updated_at

#### Table `creative_analytics`
**Script:** [linkedin_campaign_analytics.py](linkedin/scripts/linkedin_campaign_analytics.py)
**Métriques collectées (25 colonnes):**
- **Identifiants:** creative_id, creative_urn
- **Période:** date_range_start, date_range_end
- **Métriques de base:** impressions, clicks, cost_in_usd
- **Performance:** ctr, cpc, cpm
- **Engagement:** reactions, comments, shares, total_engagements, engagement_rate
- **Conversions:** landing_page_clicks, one_click_leads, external_website_conversions, external_website_post_click_conversions, external_website_post_view_conversions
- **Vidéo:** video_views, video_starts, video_completions
- **Reach:** approximate_member_reach
- **Métadonnées:** retrieved_at, updated_at

#### Table `campaign_budget`
**Script:** [linkedin_budget.py](linkedin/scripts/linkedin_budget.py)
**Métriques collectées (21 colonnes):**
- **Identifiants:** campaign_id, campaign_urn
- **Budget:** total_budget, daily_budget, lifetime_budget, budget_remaining, budget_spent, billing_currency
- **Bid:** bid_type, bid_amount, bid_multiplier, bid_adjustment_type, min_bid, max_bid
- **Pacing:** pacing_type, pacing_rate
- **Dates:** start_date, end_date
- **Métadonnées:** retrieved_at, updated_at

#### Table `creative_budget`
**Script:** [linkedin_budget.py](linkedin/scripts/linkedin_budget.py)
**Métriques collectées (23 colonnes):**
- **Identifiants:** creative_id, creative_urn, campaign_id, campaign_urn
- **Budget:** total_budget, daily_budget, lifetime_budget, budget_remaining, budget_spent, billing_currency
- **Bid:** bid_type, bid_amount, bid_multiplier, bid_adjustment_type, min_bid, max_bid
- **Pacing:** pacing_type, pacing_rate
- **Dates:** start_date, end_date
- **Métadonnées:** retrieved_at, updated_at

**Vues (6) :** v_active_campaign_budgets, v_campaign_budget_summary, v_campaign_creative_reconciliation, v_latest_campaign_metrics, v_overall_performance, v_top_creatives_by_campaign

---

### LinkedIn Ads Library (1 table)

#### Table `ads_library`
**Script:** [linkedin_ads_library.py](linkedin/scripts/linkedin_ads_library.py)
**Métriques collectées (26 colonnes):**
- **Recherche:** Keyword, Countries, Date_Range, Paging_Context
- **Annonceur:** Advertiser, Advertiser_Name, Advertiser_URL, Ad_Payer
- **Publicité:** Ad_URL, Ad_Type
- **Restrictions:** Is_Restricted, Restriction_Details
- **Ciblage:** Facet_Name, Is_Inclusive, Inclusive_Segments, Is_Exclusive, Exclusive_Segments
- **Impressions:** First_Impression_Date, Latest_Impression_Date, Total_Impressions_Range, Impressions_Distribution_by_Country
- **Métadonnées:** Retrieved_At

---

### LinkedIn Lead Gen Forms (3 tables + 4 vues)

#### Table `lead_forms`
**Script:** [linkedin_lead_forms.py](linkedin/scripts/linkedin_lead_forms.py)
**Métriques collectées (14 colonnes):**
- **Identifiants:** form_id, lead_form_urn, organization_id, ad_account_id
- **Information:** name, locale, status, lead_type
- **Configuration:** privacy_policy_url, custom_disclaimer, confirmation_message
- **Métadonnées:** created_at, last_modified_at, retrieved_at, updated_at

#### Table `lead_form_responses`
**Script:** [linkedin_lead_forms.py](linkedin/scripts/linkedin_lead_forms.py)
**Métriques collectées (22 colonnes):**
- **Identifiants:** lead_response_id, form_id, organization_id, ad_account_id, lead_type
- **Timing:** submitted_at, notification_received_at, fetched_at
- **Lead Info:** first_name, last_name, email_address, phone_number, company_name, job_title, country
- **Attribution:** campaign_id, campaign_group_id, creative_id, device_type
- **Custom:** custom_fields (JSON), consent_granted, form_data (JSON)
- **Métadonnées:** retrieved_at, updated_at

#### Table `lead_form_metrics`
**Script:** [linkedin_lead_forms.py](linkedin/scripts/linkedin_lead_forms.py)
**Métriques collectées (20 colonnes):**
- **Identifiants:** form_id, campaign_id, date
- **Volume:** total_leads, impressions, clicks, ad_spend
- **Performance:** submission_rate, conversion_rate, cost_per_lead
- **Timing:** avg_time_to_first_notification, avg_time_to_full_fetch
- **Qualité:** field_completion_rate, consent_opt_in_rate, email_validity_rate, lead_quality_score
- **Conversion:** lead_to_opportunity_count, lead_to_opportunity_rate
- **SLA:** sla_breach_count, anomaly_detected, anomaly_description
- **Métadonnées:** calculated_at, updated_at

**Vues (4) :** v_lead_quality_dashboard, v_lead_performance_by_campaign, v_lead_sla_monitoring, v_lead_volume_anomalies

---

### Microsoft Clarity (1 table)

#### Table `clarity_metrics`
**Script:** [clarity_analytics.py](microsoft_clarity/scripts/clarity_analytics.py)
**Métriques collectées (structures RECORD/STRUCT):**
- **Base:** date, retrieved_at, url, visits_count
- **Scroll Depth:** percentage_0_10, percentage_11_25, percentage_26_50, percentage_51_75, percentage_76_100, average_scroll_depth
- **Engagement Time:** total_time, active_time
- **Traffic:** total_session_count, total_bot_session_count, distinct_user_count, pages_per_session
- **Dimensions (ARRAY):** browser, device, os, country, page_title, referrer_url
- **Frustration Signals:** dead_clicks, excessive_scroll, rage_clicks, quick_backs
- **JavaScript Errors:** error_clicks, javascript_errors

---

### SpyFu (11 tables + 25 vues)

#### Table `ppc_keywords`
**Script:** [spyfu_ppc_keywords.py](spyfu/scripts/spyfu_ppc_keywords.py) - **Mensuel**
**Métriques collectées (32 colonnes):**
- **Identifiants:** domain, keyword
- **Recherche:** search_volume, live_search_volume, ranking_difficulty, total_monthly_clicks
- **Pourcentages:** percent_mobile_searches, percent_desktop_searches, percent_searches_not_clicked, percent_paid_clicks, percent_organic_clicks
- **CPC:** broad_cost_per_click, phrase_cost_per_click, exact_cost_per_click
- **Clics mensuels:** broad_monthly_clicks, phrase_monthly_clicks, exact_monthly_clicks
- **Coûts mensuels:** broad_monthly_cost, phrase_monthly_cost, exact_monthly_cost
- **Compétition:** paid_competitors, distinct_competitors, ranking_homepages
- **SERP:** serp_features_csv, serp_first_result
- **Flags:** is_question, is_not_safe_for_work
- **Métadonnées:** country_code, retrieved_at

#### Table `new_keywords`
**Script:** [spyfu_new_keywords.py](spyfu/scripts/spyfu_new_keywords.py) - **Mensuel**
**Métriques collectées (32 colonnes):** Identiques à ppc_keywords

#### Table `related_keywords`
**Script:** [spyfu_related_keywords.py](spyfu/scripts/spyfu_related_keywords.py) - **À la demande**
**Métriques collectées :** Mots-clés associés et suggestions pour un keyword donné

#### Table `term_domain_stats`
**Métriques collectées :** Statistiques de domaine pour des termes spécifiques

#### Table `seo_keywords`
**Script:** [spyfu_seo_keywords.py](spyfu/scripts/spyfu_seo_keywords.py) - **Mensuel**
**Métriques collectées (30 colonnes):**
- **Identifiants:** domain, keyword, search_type
- **Ranking:** top_ranked_url, rank, rank_change
- **Recherche:** search_volume, keyword_difficulty
- **CPC:** broad_cost_per_click, phrase_cost_per_click, exact_cost_per_click
- **SEO:** seo_clicks, seo_clicks_change, total_monthly_clicks
- **Pourcentages:** percent_mobile_searches, percent_desktop_searches, percent_not_clicked, percent_paid_clicks, percent_organic_clicks
- **Coûts:** broad_monthly_cost, phrase_monthly_cost, exact_monthly_cost
- **Compétition:** paid_competitors, ranking_homepages
- **Métadonnées:** country_code, retrieved_at

#### Table `most_valuable_keywords`
**Script:** [spyfu_most_valuable_keywords.py](spyfu/scripts/spyfu_most_valuable_keywords.py) - **Mensuel**
**Métriques collectées (29 colonnes):**
- **Identifiants:** domain, keyword
- **Ranking:** top_ranked_url, rank, rank_change
- **Recherche:** search_volume, keyword_difficulty
- **CPC:** broad_cost_per_click, phrase_cost_per_click, exact_cost_per_click
- **SEO:** seo_clicks, seo_clicks_change, total_monthly_clicks
- **Pourcentages:** percent_mobile_searches, percent_desktop_searches, percent_not_clicked, percent_paid_clicks, percent_organic_clicks
- **Coûts:** broad_monthly_cost, phrase_monthly_cost, exact_monthly_cost
- **Compétition:** paid_competitors, ranking_homepages
- **Métadonnées:** country_code, retrieved_at

#### Table `newly_ranked_keywords`
**Script:** [spyfu_newly_ranked_keywords.py](spyfu/scripts/spyfu_newly_ranked_keywords.py) - **Mensuel**
**Métriques collectées (28 colonnes):**
- **Identifiants:** domain, keyword
- **Ranking:** top_ranked_url, rank
- **Recherche:** search_volume, keyword_difficulty
- **CPC:** broad_cost_per_click, phrase_cost_per_click, exact_cost_per_click
- **SEO:** seo_clicks, seo_clicks_change, total_monthly_clicks
- **Pourcentages:** percent_mobile_searches, percent_desktop_searches, percent_not_clicked, percent_paid_clicks, percent_organic_clicks
- **Coûts:** broad_monthly_cost, phrase_monthly_cost, exact_monthly_cost
- **Compétition:** paid_competitors, ranking_homepages
- **Métadonnées:** country_code, retrieved_at

#### Table `top_pages`
**Script:** [spyfu_top_pages.py](spyfu/scripts/spyfu_top_pages.py) - **Mensuel**
**Métriques collectées (11 colonnes):**
- **Identifiants:** domain, url, title
- **Métriques:** keyword_count, est_monthly_seo_clicks
- **Top keyword:** top_keyword, top_keyword_position, top_keyword_search_volume, top_keyword_clicks
- **Métadonnées:** country_code, retrieved_at

#### Table `domain_stats`
**Script:** [spyfu_domain_stats.py](spyfu/scripts/spyfu_domain_stats.py) - **Mensuel**
**Métriques collectées (15 colonnes):**
- **Identifiants:** domain, country_code
- **PPC:** total_ad_keywords, total_ad_budget, total_ad_clicks, ad_history_months
- **SEO:** total_seo_keywords, total_organic_keywords, total_organic_traffic, total_organic_value
- **Domaine:** domain_rank, domain_authority
- **Raw:** raw_stats (JSON)
- **Métadonnées:** retrieved_at

#### Table `domain_ad_history`
**Script:** [spyfu_domain_ad_history.py](spyfu/scripts/spyfu_domain_ad_history.py) - **Trimestriel**
**Métriques collectées (16 colonnes):**
- **Identifiants:** domain, ad_id, keyword
- **Contenu:** headline, description, display_url, destination_url
- **Temporel:** first_seen_date, last_seen_date, days_seen
- **Performance:** search_volume, cost_per_click, monthly_cost, position
- **Métadonnées:** country_code, retrieved_at

#### Table `term_ad_history`
**Script:** [spyfu_term_ad_history.py](spyfu/scripts/spyfu_term_ad_history.py) - **Trimestriel**
**Métriques collectées (19 colonnes):**
- **Identifiants:** keyword, ad_id, domain_name
- **Contenu:** title, body, full_url, term
- **Temporel:** search_date_id
- **Position:** average_position, position
- **Volume:** average_ad_count, ad_count, leaderboard_count
- **Pourcentages:** percentage_leaderboard, percentage_ads_served
- **Flags:** is_leaderboard_ad
- **Métadonnées:** source, country_code, retrieved_at

**Vues (25) :** top_keywords_by_volume, cpc_analysis, keyword_opportunities, most_valuable_seo_keywords, seo_rankings, most_valuable_pages, domain_stats_evolution, active_ads_analysis, ads_by_keyword, best_ad_headlines_by_keyword, domain_page_performance, domain_performance_overview, domain_spend_by_keyword, domain_stats_comparison, estimated_roi_analysis, keyword_clusters, keyword_expansion_opportunities, new_keyword_opportunities, new_keywords_by_domain, newly_ranked_top_keywords, seo_opportunities, top_10_most_valuable, top_performing_ads, top_spenders_by_keyword, keyword_rich_pages

---

### Résumé des tables de ce projet

**Tables de données créées par ce projet Marketing Data Collection :**
- LinkedIn Ads Advertising : 4 tables + 6 vues
- LinkedIn Ads Library : 1 table
- LinkedIn Lead Gen Forms : 3 tables + 4 vues
- Microsoft Clarity : 1 table
- SpyFu : 11 tables + 25 vues

**Total : 20 tables de données + 35 vues SQL = 55 objets BigQuery**

Pour voir le schéma complet de TOUTES les tables du projet BigQuery (323 tables), consultez [BIGQUERY_SCHEMAS.md](BIGQUERY_SCHEMAS.md).

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
- [ ] 5 datasets créés (linkedin_ads_advertising, linkedin_ads_library, linkedin_leadgen_form, microsoft_clarity, spyfu)
- [ ] Tables créées depuis fichiers SQL (20 tables + 35 vues)

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
