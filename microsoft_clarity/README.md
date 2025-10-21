# Microsoft Clarity Data Collection

Script Python pour récupérer et analyser les métriques d'interaction utilisateur depuis Microsoft Clarity avec upload automatique vers BigQuery.

## 📋 Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Architecture BigQuery](#architecture-bigquery)
- [Métriques collectées](#métriques-collectées)
- [Exemples de requêtes](#exemples-de-requêtes)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Vue d'ensemble

Microsoft Clarity est un outil gratuit d'analyse comportementale qui enregistre les interactions des utilisateurs sur votre site web (clics, scrolling, rage clicks, etc.).

Ce script permet de :
- ✅ Récupérer automatiquement les métriques Clarity via l'API
- ✅ Parser les données dans un format structuré
- ✅ Uploader vers BigQuery pour analyse
- ✅ Sauvegarder en JSON pour backup

### Données collectées

| Catégorie | Métriques |
|-----------|-----------|
| **Trafic** | Sessions totales, utilisateurs uniques |
| **Engagement** | Temps d'engagement moyen, profondeur de scroll |
| **Frustration** | Dead clicks, rage clicks, quick backs, scrolling excessif |
| **Erreurs** | Error clicks, erreurs JavaScript |
| **Dimensions** | Navigateurs, devices, OS, géographie |

---

## 📦 Prérequis

### Comptes et accès

- **Microsoft Clarity Project** configuré sur votre site
- **Clarity API Credentials** (récupérables depuis votre tableau de bord Clarity)
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
microsoft_clarity/
├── scripts/
│   └── clarity_analytics.py    # Script principal
├── sql/
│   └── bigquery_clarity_schema.sql  # Schéma BigQuery
├── data/                        # JSON exports (créé automatiquement)
└── README.md                    # Cette documentation
```

### 2. Créer le dataset BigQuery

```sql
CREATE SCHEMA IF NOT EXISTS `microsoft_clarity`
OPTIONS(
  location="EU"
);
```

### 3. Créer la table

Exécuter le fichier SQL :

```bash
bq query --use_legacy_sql=false < sql/bigquery_clarity_schema.sql
```

Ou depuis la console BigQuery, copier-coller le contenu de `sql/bigquery_clarity_schema.sql`.

---

## 🔧 Configuration

### Configuration de l'API Clarity

#### 1. Récupérer vos credentials Clarity

1. Connectez-vous à [Microsoft Clarity](https://clarity.microsoft.com/)
2. Sélectionnez votre projet
3. Allez dans **Settings** → **API Access**
4. Notez votre **Project ID** et **API Key**

#### 2. Configurer le script

Ouvrir `scripts/clarity_analytics.py` et modifier :

```python
class ClarityAnalytics:
    # Configuration Clarity
    BASE_URL = "https://www.clarity.ms/api/project-live-insights"
    PROJECT_ID = "VOTRE_PROJECT_ID"
    API_KEY = "VOTRE_API_KEY"

    # Configuration collecte
    NUM_OF_DAYS = 1  # IMPORTANT: Limité à 1, 2 ou 3 jours maximum
```

#### 3. Configurer BigQuery

```python
# Configuration BigQuery
PROJECT_ID = "votre-project-id"
DATASET_ID = "microsoft_clarity"
TABLE_ID = "clarity_metrics"
CREDENTIALS_PATH = "../../../account-key.json"
```

---

## 🚀 Utilisation

### Exécution simple

```bash
cd scripts
python clarity_analytics.py
```

### Workflow du script

1. **Appel API Clarity** - Récupère les métriques des derniers jours
2. **Parsing des données** - Format structuré pour BigQuery
3. **Export JSON** - Sauvegarde automatique dans `data/`
4. **Upload BigQuery** - Insertion dans la table

### Sortie typique

```
============================================================
Microsoft Clarity Analytics Collection
============================================================
📊 Récupération des métriques Clarity...
✓ Données récupérées avec succès

✓ 1 enregistrements parsés
✓ Données exportées: ../data/clarity_metrics_20250114_151230.json

📤 Upload de 1 lignes vers deepscouting.microsoft_clarity.clarity_metrics...
✓ Upload réussi vers BigQuery

✓ Collection terminée
```

---

## 🗄️ Architecture BigQuery

### Table unique : `clarity_metrics`

**Partitionnement :** `DATE(date)`
**Clustering :** `url, date`

#### Schéma

| Colonne | Type | Description |
|---------|------|-------------|
| `date` | TIMESTAMP | Date de collecte |
| `name` | STRING | Nom du projet Clarity |
| `url` | STRING | URL du site |
| `total_sessions` | INT64 | Nombre total de sessions |
| `total_users` | INT64 | Nombre d'utilisateurs uniques |
| `avg_engagement_time` | FLOAT64 | Temps d'engagement moyen (secondes) |
| `scroll_depth` | FLOAT64 | Profondeur moyenne de scroll (%) |
| `dead_clicks` | INT64 | Clics sur éléments non-cliquables |
| `rage_clicks` | INT64 | Clics répétés rapides (frustration) |
| `quick_backs` | INT64 | Retours arrière rapides |
| `excessive_scrolling` | INT64 | Scrolling excessif |
| `error_clicks` | INT64 | Clics provoquant des erreurs |
| `script_errors` | INT64 | Erreurs JavaScript détectées |
| `browser_breakdown` | STRING | Répartition navigateurs (JSON) |
| `device_breakdown` | STRING | Répartition devices (JSON) |
| `os_breakdown` | STRING | Répartition OS (JSON) |
| `user_geography` | STRING | Répartition géographique (JSON) |
| `retrieved_at` | TIMESTAMP | Horodatage de récupération |

### Optimisations

- **Partitionnement par date** : Requêtes rapides sur périodes récentes
- **Clustering** : Filtrage efficace par URL et date
- **Colonnes JSON** : Dimensions détaillées sans exploser le nombre de colonnes

---

## 📊 Métriques collectées

### 1. Métriques de trafic

**`total_sessions`** - Nombre total de sessions
- Utile pour : Mesurer l'audience globale

**`total_users`** - Utilisateurs uniques
- Utile pour : Calculer les sessions par utilisateur

### 2. Métriques d'engagement

**`avg_engagement_time`** - Temps moyen passé (secondes)
- Utile pour : Identifier les pages captivantes
- Bon score : > 60 secondes

**`scroll_depth`** - Profondeur moyenne de scroll (%)
- Utile pour : Évaluer si le contenu est lu
- Bon score : > 50%

### 3. Métriques de frustration

**`dead_clicks`** - Clics sur éléments non-cliquables
- Signification : Utilisateurs qui cliquent sur du texte/images pensant que c'est un lien
- Action : Ajouter des liens ou clarifier les CTA

**`rage_clicks`** - Clics répétés rapides
- Signification : Frustration extrême (bouton qui ne répond pas)
- Action : Vérifier la réactivité des éléments cliquables

**`quick_backs`** - Retours arrière rapides
- Signification : Page ne correspond pas aux attentes
- Action : Revoir le titre/meta description ou le contenu

**`excessive_scrolling`** - Scrolling excessif
- Signification : Utilisateur cherche quelque chose sans le trouver
- Action : Améliorer la navigation et la hiérarchie

### 4. Métriques d'erreur

**`error_clicks`** - Clics provoquant des erreurs
- Signification : Éléments cassés (liens 404, formulaires bugués)
- Action : Corriger les éléments défectueux

**`script_errors`** - Erreurs JavaScript
- Signification : Code JavaScript planté
- Action : Débugger les scripts côté client

### 5. Dimensions (JSON)

**`browser_breakdown`** - Répartition des navigateurs
```json
[
  {"name": "Chrome", "sessions": 450, "percentage": 65.2},
  {"name": "Safari", "sessions": 180, "percentage": 26.1},
  {"name": "Firefox", "sessions": 60, "percentage": 8.7}
]
```

**`device_breakdown`** - Répartition des devices
```json
[
  {"name": "Desktop", "sessions": 420, "percentage": 60.9},
  {"name": "Mobile", "sessions": 250, "percentage": 36.2},
  {"name": "Tablet", "sessions": 20, "percentage": 2.9}
]
```

**`os_breakdown`** - Répartition des OS
```json
[
  {"name": "Windows", "sessions": 380, "percentage": 55.1},
  {"name": "macOS", "sessions": 150, "percentage": 21.7},
  {"name": "iOS", "sessions": 100, "percentage": 14.5},
  {"name": "Android", "sessions": 60, "percentage": 8.7}
]
```

**`user_geography`** - Répartition géographique
```json
[
  {"country": "France", "sessions": 500, "percentage": 72.5},
  {"country": "Belgium", "sessions": 100, "percentage": 14.5},
  {"country": "Switzerland", "sessions": 90, "percentage": 13.0}
]
```

---

## 📈 Exemples de requêtes

### Vue d'ensemble des performances

```sql
SELECT
  DATE(date) as jour,
  total_sessions,
  total_users,
  ROUND(total_sessions / total_users, 2) as sessions_par_user,
  ROUND(avg_engagement_time, 2) as engagement_seconds,
  ROUND(scroll_depth, 2) as scroll_pct,
  dead_clicks,
  rage_clicks,
  quick_backs
FROM `microsoft_clarity.clarity_metrics`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
ORDER BY jour DESC;
```

### Score de frustration

```sql
-- Calculer un score de frustration global
SELECT
  DATE(date) as jour,
  total_sessions,
  (dead_clicks + rage_clicks + quick_backs + excessive_scrolling) as total_frustrations,
  ROUND((dead_clicks + rage_clicks + quick_backs + excessive_scrolling) / total_sessions * 100, 2)
    as frustration_rate_pct
FROM `microsoft_clarity.clarity_metrics`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
ORDER BY frustration_rate_pct DESC;
```

### Analyse des navigateurs

```sql
-- Parser le JSON des navigateurs
SELECT
  DATE(date) as jour,
  JSON_EXTRACT_SCALAR(browser, '$.name') as navigateur,
  CAST(JSON_EXTRACT_SCALAR(browser, '$.sessions') AS INT64) as sessions,
  CAST(JSON_EXTRACT_SCALAR(browser, '$.percentage') AS FLOAT64) as pourcentage
FROM `microsoft_clarity.clarity_metrics`,
  UNNEST(JSON_EXTRACT_ARRAY(browser_breakdown)) as browser
WHERE DATE(date) = CURRENT_DATE()
ORDER BY sessions DESC;
```

### Analyse des devices

```sql
-- Comparer engagement mobile vs desktop
SELECT
  JSON_EXTRACT_SCALAR(device, '$.name') as type_device,
  AVG(avg_engagement_time) as engagement_moyen,
  AVG(scroll_depth) as scroll_moyen,
  SUM(CAST(JSON_EXTRACT_SCALAR(device, '$.sessions') AS INT64)) as total_sessions
FROM `microsoft_clarity.clarity_metrics`,
  UNNEST(JSON_EXTRACT_ARRAY(device_breakdown)) as device
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY type_device
ORDER BY total_sessions DESC;
```

### Détection des pages problématiques

```sql
-- Pages avec le plus de frustration
SELECT
  url,
  DATE(date) as jour,
  total_sessions,
  dead_clicks,
  rage_clicks,
  quick_backs,
  ROUND((dead_clicks + rage_clicks + quick_backs) / total_sessions * 100, 2) as frustration_pct
FROM `microsoft_clarity.clarity_metrics`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
  AND total_sessions > 10
ORDER BY frustration_pct DESC
LIMIT 20;
```

### Évolution temporelle

```sql
-- Tendance sur 30 jours
SELECT
  DATE(date) as jour,
  total_sessions,
  avg_engagement_time,
  scroll_depth,
  (dead_clicks + rage_clicks) as frustration_clicks,
  script_errors
FROM `microsoft_clarity.clarity_metrics`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
ORDER BY jour ASC;
```

### Analyse géographique

```sql
-- Top pays par engagement
SELECT
  JSON_EXTRACT_SCALAR(geo, '$.country') as pays,
  SUM(CAST(JSON_EXTRACT_SCALAR(geo, '$.sessions') AS INT64)) as sessions,
  AVG(avg_engagement_time) as engagement_moyen,
  AVG(scroll_depth) as scroll_moyen
FROM `microsoft_clarity.clarity_metrics`,
  UNNEST(JSON_EXTRACT_ARRAY(user_geography)) as geo
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY pays
ORDER BY sessions DESC;
```

### Dashboard KPI

```sql
-- Métriques clés pour un dashboard
WITH latest_data AS (
  SELECT *
  FROM `microsoft_clarity.clarity_metrics`
  WHERE DATE(date) = CURRENT_DATE()
),
previous_data AS (
  SELECT *
  FROM `microsoft_clarity.clarity_metrics`
  WHERE DATE(date) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
)
SELECT
  l.total_sessions as sessions_today,
  p.total_sessions as sessions_yesterday,
  ROUND((l.total_sessions - p.total_sessions) / p.total_sessions * 100, 2) as sessions_change_pct,

  ROUND(l.avg_engagement_time, 2) as engagement_today,
  ROUND(p.avg_engagement_time, 2) as engagement_yesterday,
  ROUND(l.avg_engagement_time - p.avg_engagement_time, 2) as engagement_change_sec,

  l.dead_clicks + l.rage_clicks + l.quick_backs as frustration_today,
  p.dead_clicks + p.rage_clicks + p.quick_backs as frustration_yesterday,

  l.script_errors as errors_today,
  p.script_errors as errors_yesterday
FROM latest_data l, previous_data p;
```

---

## 🔍 Troubleshooting

### Erreur 400 - Bad Request (numOfDays)

**Problème :** `numOfDays doit être 1, 2 ou 3`

**Solution :** L'API Clarity limite la récupération à 3 jours maximum.

```python
NUM_OF_DAYS = 1  # Valeurs acceptées: 1, 2, 3
```

Pour construire un historique, il faut collecter quotidiennement.

---

### Toutes les métriques sont NULL

**Problème :** Le parsing ne fonctionne pas

**Cause :** L'API Clarity retourne une structure `metricName` / `information`

**Vérification :** Le script actuel gère correctement cette structure. Si le problème persiste :

```python
# Debug: afficher la réponse brute
print(json.dumps(data, indent=2))
```

---

### Erreur d'authentification API

**Problème :** 401 Unauthorized

**Solutions :**
1. Vérifier le **PROJECT_ID**
2. Vérifier l'**API_KEY**
3. S'assurer que l'API est activée dans les settings Clarity

---

### Type not found: FLOAT

**Problème :** BigQuery n'accepte pas le type FLOAT

**Solution :** Déjà corrigé dans le schéma. Utiliser `FLOAT64` et `INT64`.

---

### CLUSTER BY clause error

**Problème :** `DATE(date)` dans CLUSTER BY

**Solution :** Déjà corrigé. Ne pas utiliser de fonctions dans CLUSTER BY :

```sql
CLUSTER BY url, date  -- ✓ Correct
CLUSTER BY url, DATE(date)  -- ✗ Incorrect
```

---

### Upload BigQuery échoue

**Solution :** Les données sont sauvegardées en JSON dans `data/`

Vous pouvez ré-uploader manuellement :

```python
from clarity_analytics import ClarityAnalytics
import json

collector = ClarityAnalytics()

# Charger le JSON
with open('../data/clarity_metrics_20250114_151230.json', 'r') as f:
    data = json.load(f)

# Uploader
collector.upload_to_bigquery(data, project_id="votre-project-id")
```

---

## 📅 Automatisation

### Limitation importante

⚠️ **L'API Clarity ne permet de récupérer que 1 à 3 jours de données**

Pour construire un historique, il **faut collecter quotidiennement**.

### Cron job quotidien

```bash
# Ajouter au crontab
crontab -e

# Exécuter tous les jours à 2h du matin
0 2 * * * cd /path/to/microsoft_clarity/scripts && /path/to/python clarity_analytics.py > /tmp/clarity.log 2>&1
```

### Script bash avec rotation des logs

```bash
#!/bin/bash
# collect_clarity.sh

LOG_DIR="/var/log/clarity"
mkdir -p $LOG_DIR

DATE=$(date +%Y%m%d)
LOG_FILE="$LOG_DIR/clarity_$DATE.log"

cd /path/to/microsoft_clarity/scripts

echo "=== Clarity Collection Started ===" >> $LOG_FILE
date >> $LOG_FILE

python clarity_analytics.py >> $LOG_FILE 2>&1

if [ $? -eq 0 ]; then
  echo "✓ Collection successful" >> $LOG_FILE
else
  echo "✗ Collection failed" >> $LOG_FILE
  # Envoyer une alerte email
  # mail -s "Clarity Collection Failed" admin@example.com < $LOG_FILE
fi

echo "=== Clarity Collection Completed ===" >> $LOG_FILE
date >> $LOG_FILE

# Nettoyer les logs de plus de 30 jours
find $LOG_DIR -name "clarity_*.log" -mtime +30 -delete
```

---

## 🎓 Best Practices

### 1. Collecte quotidienne obligatoire

Étant donné la limitation de l'API (1-3 jours), configurez une collecte automatique quotidienne.

### 2. Monitoring des erreurs

```sql
-- Alerter si le nombre d'erreurs augmente significativement
SELECT
  DATE(date) as jour,
  script_errors,
  error_clicks,
  LAG(script_errors) OVER (ORDER BY date) as errors_yesterday
FROM `microsoft_clarity.clarity_metrics`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
ORDER BY jour DESC;
```

### 3. Dashboard Looker Studio / Data Studio

Créer un dashboard avec :
- **Sessions / Utilisateurs** (tendance)
- **Engagement moyen** (gauge)
- **Score de frustration** (KPI)
- **Top devices** (pie chart)
- **Top navigateurs** (bar chart)
- **Géographie** (map)

### 4. Alertes automatiques

Configurer des alertes si :
- **Frustration rate** > 20%
- **Script errors** > 50 par jour
- **Avg engagement time** < 30 secondes
- **Scroll depth** < 30%

### 5. Corrélation avec d'autres données

Joindre avec Google Analytics ou d'autres sources :

```sql
SELECT
  c.date,
  c.total_sessions as clarity_sessions,
  g.sessions as ga_sessions,
  c.avg_engagement_time,
  c.dead_clicks,
  g.bounce_rate
FROM `microsoft_clarity.clarity_metrics` c
LEFT JOIN `google_analytics.sessions` g
  ON DATE(c.date) = DATE(g.date)
WHERE DATE(c.date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY);
```

---

## 📊 Interprétation des métriques

### Scores de référence

| Métrique | Excellent | Bon | Moyen | Mauvais |
|----------|-----------|-----|-------|---------|
| **Avg Engagement Time** | > 120s | 60-120s | 30-60s | < 30s |
| **Scroll Depth** | > 70% | 50-70% | 30-50% | < 30% |
| **Frustration Rate** | < 5% | 5-10% | 10-20% | > 20% |
| **Script Errors** | 0 | 1-5 | 5-20 | > 20 |

### Actions correctives

**Si Engagement faible :**
- Améliorer la pertinence du contenu
- Réduire les distractions
- Améliorer la lisibilité

**Si Scroll Depth faible :**
- Rendre le contenu plus captivant en début de page
- Améliorer la structure (H1, H2, H3)
- Ajouter des visuels

**Si Dead Clicks élevés :**
- Transformer les éléments en vrais liens/boutons
- Clarifier les CTA (Call-to-Action)
- Améliorer le design (affordance)

**Si Rage Clicks élevés :**
- Vérifier la réactivité des boutons
- Corriger les bugs JavaScript
- Améliorer les temps de chargement

**Si Quick Backs élevés :**
- Améliorer le SEO (titre/description)
- Aligner le contenu avec les attentes
- Réduire les pop-ups agressifs

**Si Script Errors élevés :**
- Débugger le JavaScript
- Vérifier la compatibilité navigateurs
- Minifier et optimiser les scripts

---

## 🔗 Ressources

### Documentation officielle

- [Microsoft Clarity](https://clarity.microsoft.com/)
- [Clarity API Documentation](https://docs.microsoft.com/en-us/clarity/)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

### Outils complémentaires

- **Session Recordings** : Regarder les enregistrements Clarity pour comprendre le comportement
- **Heatmaps** : Analyser les zones chaudes de clics
- **Funnel Analysis** : Analyser les parcours utilisateurs

---

## 📝 Notes importantes

### Données personnelles (RGPD)

Microsoft Clarity **anonymise automatiquement** les données sensibles :
- Masquage des informations personnelles dans les formulaires
- Anonymisation des adresses IP
- Pas de tracking cross-site

Clarity est conforme RGPD par défaut.

### Limitations

- **Historique limité** : 1-3 jours via API
- **Temps réel** : Délai de ~15 minutes pour les nouvelles données
- **Granularité** : Agrégation quotidienne, pas de données par heure

### Recommandations

- Collecter **quotidiennement** pour historique complet
- Combiner avec **Google Analytics** pour vue 360°
- Utiliser les **session recordings** pour investigations approfondies

---

## 📞 Support

### Questions fréquentes

**Q: Les données sont-elles en temps réel ?**
R: Non, délai de ~15 minutes. Collectez quotidiennement.

**Q: Puis-je récupérer plus de 3 jours ?**
R: Non, limitation API. Il faut collecter régulièrement pour construire un historique.

**Q: Clarity est-il gratuit ?**
R: Oui, totalement gratuit et sans limitation de trafic.

**Q: Comment voir les enregistrements de sessions ?**
R: Directement dans le dashboard Clarity (non disponible via API).

**Q: Les données sont-elles conformes RGPD ?**
R: Oui, Clarity anonymise automatiquement les données sensibles.

---

## 🎯 Roadmap

### Améliorations futures

- [ ] Support de plusieurs projets Clarity
- [ ] Alertes automatiques par email
- [ ] Dashboard Looker Studio pré-configuré
- [ ] Analyse des tendances avec ML
- [ ] Export vers autres formats (CSV, Parquet)

---

**Version:** 1.0
**Dernière mise à jour:** 2025-01-14
**Auteur:** Deep Scouting
