# LinkedIn DMA → BigQuery - Configuration Finale

## 📋 Tables BigQuery (3 tables)

### 1. `followers`
Liste des followers de la page avec consentement DMA
- `organization_id` (REQUIRED)
- `follow_id` (REQUIRED)
- `follower` (URN du follower)
- `followed_on` (date)
- `retrieved_at` (REQUIRED)

**Données actuelles** : 137 followers avec consentement DMA (sur 16k totaux)

### 2. `page_content_analytics`
Analytics détaillées par contenu/post individuel
- `organization_id` (REQUIRED)
- `content_urn`
- `impression_count`, `reaction_count`, `comment_count`, `repost_count`, `click_count`
- `demographics_breakdown`
- `retrieved_at` (REQUIRED)
- `updated_at`

**Données actuelles** : Vide (0 posts accessibles via DMA API)

### 3. `page_statistics`
Métriques globales agrégées de la page (365 derniers jours)
- `organization_id` (REQUIRED)
- **Audience** : `visitor_count`, `page_follower_count`, `new_follower_count`
- **Performance** : `impression_count`, `unique_impression_count`, `click_count`, `comment_count`, `reaction_count`, `repost_count`, `engagement_rate`, `acquired_follows`
- `retrieved_at` (REQUIRED)

**Données actuelles** : ~3M impressions, 24k visiteurs, 2k nouveaux followers/an

## 🚀 Processus de synchronisation

### Étape 1 : Créer les tables BigQuery

```bash
# Se connecter à BigQuery
bq mk --dataset ecoledesponts:linkedin_page --location=europe-west9

# Créer les tables
bq query --use_legacy_sql=false < sql/bigquery_epbs_final_schema.sql
```

Ou créer manuellement depuis la console BigQuery avec le fichier `sql/bigquery_epbs_final_schema.sql`

### Étape 2 : Récupérer les données LinkedIn

```bash
# Activer l'environnement conda
conda activate deepscouting

# Lancer la récupération
python run_epbs_final_sync.py
```

**Résultat** : Fichiers JSON créés dans `data_exports_epbs_dma/`
- `page_statistics_epbs_YYYYMMDD_HHMMSS.json`
- `followers_epbs_YYYYMMDD_HHMMSS.json`
- `page_content_analytics_epbs_YYYYMMDD_HHMMSS.json`

### Étape 3 : Upload vers BigQuery

```bash
python upload_epbs_final.py
```

## 📁 Fichiers principaux

```
linkedin/
├── config_epbs.yaml                    # Configuration (tokens, IDs)
├── run_epbs_final_sync.py              # Script de récupération
├── upload_epbs_final.py                # Script d'upload BigQuery
├── sql/
│   └── bigquery_epbs_final_schema.sql  # Schémas SQL des 3 tables
├── scripts/
│   └── linkedin_page_dma_scraper.py    # Client API (modifié)
└── data_exports_epbs_dma/              # Exports JSON
```

## ⚙️ Configuration

Le fichier `config_epbs.yaml` doit contenir :

```yaml
linkedin:
  oauth:
    access_token: "VOTRE_TOKEN"
  organization_id: "15092687"
  page_id: "15092687"
```

Le fichier `sos-linkedin-ads-library-key.json` doit contenir les credentials GCP.

## 🔄 Automatisation

Pour automatiser la synchronisation quotidienne, utiliser un cron job :

```bash
# Éditer le crontab
crontab -e

# Ajouter (exemple : tous les jours à 6h du matin)
0 6 * * * cd /path/to/linkedin && conda run -n deepscouting python run_epbs_final_sync.py && python upload_epbs_final.py
```

## 📊 Métriques disponibles

### page_statistics (Métriques sur 365 jours)
- **Audience** : 24,378 visiteurs, 2,037 nouveaux followers
- **Contenu** : 2,978,975 impressions, 19,934 clics
- **Engagement** : 2,839 réactions, 12 commentaires, 30 reposts

### followers
- 137 followers avec consentement DMA
- URNs obfusqués pour protection de la vie privée
- Dates de follow disponibles

### page_content_analytics
- Vide actuellement (0 posts accessibles)
- Prêt pour le futur si des posts deviennent accessibles

## ⚠️ Limitations connues

1. **Total followers (16k)** : Non disponible via DMA API, seulement nouveaux acquis par période
2. **Posts individuels** : 0 posts retournés (permissions ou aucun post publié)
3. **TimeRange sur posts** : Non supporté par l'endpoint dmaFeedContentsExternal
4. **Privacy DMA** : Seulement 137/16000 followers accessibles (0.85% avec consentement)

## 📈 Évolutions futures

- Ajouter d'autres tables si nécessaire (events, lead_gen_forms, content_series)
- Implémenter analytics par post quand des posts seront accessibles
- Ajouter des dimensions de segmentation (demographics_breakdown)
