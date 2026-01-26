# Guide Complet : Brevo Data Collection → BigQuery

Système complet de collecte et synchronisation des données Brevo vers BigQuery via les API REST (sans webhooks ni Brevo+).

## 📊 Données collectées

Ce système récupère **4 types de données** depuis l'API Brevo :

| Table BigQuery | Données | API Endpoint | Fréquence |
|---|---|---|---|
| `brevo.brevo` | Événements email (opens, clicks, bounces) | `/v3/smtp/statistics/events` | Quotidien |
| `brevo.brevo_campaigns` | Campagnes avec stats | `/v3/emailCampaigns` | Quotidien |
| `brevo.brevo_contacts_lists` | Listes de contacts | `/v3/contacts/lists` | Hebdomadaire |
| `brevo.brevo_smtp_reports` | Rapports agrégés par jour | `/v3/smtp/statistics/aggregatedReport` | Quotidien |

## 🚀 Installation

### 1. Prérequis

```bash
pip install requests PyYAML google-cloud-bigquery
```

### 2. Configuration

Votre [config.yaml](config.yaml) est déjà configuré avec :
- ✅ Projet GCP : `ecoledesponts`
- ✅ Dataset : `brevo`
- ✅ API Key Brevo

### 3. Créer les tables BigQuery

```bash
cd /home/cseceh/Deep_Scouting/admin/Projet_Ads/marketing-data-collection/brevo

# Créer toutes les tables
bq query --use_legacy_sql=false < sql/bigquery_brevo_schema.sql
bq query --use_legacy_sql=false < sql/bigquery_campaigns_schema.sql
bq query --use_legacy_sql=false < sql/bigquery_contacts_lists_schema.sql
bq query --use_legacy_sql=false < sql/bigquery_smtp_reports_schema.sql
```

## 📖 Utilisation

### Synchronisation complète (recommandé)

```bash
python sync_brevo_data.py
```

Résultat :
```
✅ SYNCHRONISATION TERMINÉE AVEC SUCCÈS
  📧 Campagnes: 42
  📨 Événements: 1,523
  📋 Listes: 8
  📊 Rapports: 30
  ⏱️  Durée: 12.3s
```

### Synchronisations partielles

```bash
# Seulement les événements (30 derniers jours)
python sync_brevo_data.py --events-only --days 30

# Seulement les campagnes
python sync_brevo_data.py --campaigns-only

# Seulement les listes de contacts
python sync_brevo_data.py --lists-only

# Seulement les rapports SMTP (60 derniers jours)
python sync_brevo_data.py --reports-only --report-days 60
```

### Tester individuellement

```bash
cd scripts

# Tester chaque collecteur
python fetch_campaigns.py
python fetch_events.py
python fetch_contacts_lists.py
python fetch_smtp_reports.py

# Tester BigQuery
python upload_to_bigquery.py
```

## 📁 Structure du projet

```
brevo/
├── sync_brevo_data.py              # 🎯 Script principal
├── config.yaml                      # ⚙️  Configuration
├── GUIDE_COMPLET.md                # 📖 Ce fichier
│
├── scripts/
│   ├── fetch_campaigns.py          # Récupère les campagnes
│   ├── fetch_events.py             # Récupère les événements
│   ├── fetch_contacts_lists.py     # Récupère les listes
│   ├── fetch_smtp_reports.py       # Récupère les rapports
│   └── upload_to_bigquery.py       # Upload vers BigQuery
│
└── sql/
    ├── bigquery_brevo_schema.sql           # Table événements
    ├── bigquery_campaigns_schema.sql       # Table campagnes
    ├── bigquery_contacts_lists_schema.sql  # Table listes
    └── bigquery_smtp_reports_schema.sql    # Table rapports
```

## 📊 Exemples de requêtes BigQuery

### 1. Performance des campagnes (30 derniers jours)

```sql
SELECT
  name,
  subject,
  sent_date,
  stats_sent,
  stats_delivered,
  stats_unique_views,
  open_rate,
  click_rate,
  bounce_rate
FROM `ecoledesponts.brevo.brevo_campaigns`
WHERE sent_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND status = 'sent'
ORDER BY open_rate DESC
LIMIT 10;
```

### 2. Événements détaillés par jour

```sql
SELECT
  DATE(date) as jour,
  event,
  COUNT(*) as nombre
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY jour, event
ORDER BY jour DESC, nombre DESC;
```

### 3. Top emails cliqués

```sql
SELECT
  subject,
  link,
  COUNT(*) as clics
FROM `ecoledesponts.brevo.brevo`
WHERE event = 'click'
  AND DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY subject, link
ORDER BY clics DESC
LIMIT 20;
```

### 4. Statistiques des listes de contacts

```sql
SELECT
  name,
  total_subscribers,
  total_blacklisted,
  ROUND(total_blacklisted / NULLIF(total_subscribers, 0) * 100, 2) as blacklist_rate,
  created_at
FROM `ecoledesponts.brevo.brevo_contacts_lists`
ORDER BY total_subscribers DESC;
```

### 5. Évolution des taux sur 30 jours

```sql
SELECT
  report_date,
  delivered,
  unique_opens,
  unique_clicks,
  open_rate,
  click_rate,
  bounce_rate,
  unsubscribe_rate
FROM `ecoledesponts.brevo.brevo_smtp_reports`
WHERE report_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
ORDER BY report_date DESC;
```

### 6. Analyse des bounces par email

```sql
SELECT
  email,
  COUNTIF(event = 'hardbounce') as hard_bounces,
  COUNTIF(event = 'softbounce') as soft_bounces,
  COUNTIF(event = 'delivered') as delivered
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY email
HAVING hard_bounces > 0 OR soft_bounces > 0
ORDER BY hard_bounces DESC, soft_bounces DESC
LIMIT 100;
```

## 🔄 Automatisation

### Option 1 : Cron (serveur Linux)

```bash
# Éditer le crontab
crontab -e

# Ajouter cette ligne pour sync quotidienne à 3h
0 3 * * * cd /home/cseceh/Deep_Scouting/admin/Projet_Ads/marketing-data-collection/brevo && python sync_brevo_data.py >> logs/sync.log 2>&1
```

### Option 2 : Google Cloud Scheduler (recommandé)

```bash
# Créer un Cloud Scheduler
gcloud scheduler jobs create http brevo-daily-sync \
  --schedule="0 3 * * *" \
  --uri="https://europe-west9-run.app/brevo-sync" \
  --http-method=POST \
  --location="europe-west9" \
  --time-zone="Europe/Paris"
```

## 🔧 Dépannage

### Erreur : "Unauthorized" (401)

```
❌ Erreur 401: Unauthorized
```

**Solution** : Vérifiez votre clé API dans [config.yaml](config.yaml:32).

### Erreur : "Credentials not found"

```
❌ Fichier de credentials introuvable
```

**Solution** : Vérifiez le chemin vers `account-key.json` :
```bash
ls -la /home/cseceh/Deep_Scouting/admin/Projet_Ads/account-key.json
```

### Aucune donnée récupérée

```
⚠️  Aucun événement à synchroniser
```

**Solution** : Augmentez le nombre de jours :
```bash
python sync_brevo_data.py --days 30
```

### Erreur de quota API

```
❌ Too Many Requests (429)
```

**Solution** : L'API Brevo a des limites. Espacez vos appels ou contactez Brevo.

## 📈 Métriques calculées automatiquement

Le système calcule ces métriques pour vous :

| Métrique | Formule | Disponible dans |
|---|---|---|
| **Taux d'ouverture** | `unique_opens / delivered * 100` | Campagnes, Rapports |
| **Taux de clic** | `unique_clicks / delivered * 100` | Campagnes, Rapports |
| **Taux de bounce** | `(hard_bounces + soft_bounces) / sent * 100` | Campagnes, Rapports |
| **Taux de désabo** | `unsubscribed / delivered * 100` | Campagnes, Rapports |
| **CTR** | `clicks / opens * 100` | À calculer dans vos requêtes |

## 🎯 Cas d'usage

### 1. Dashboard de performance email

Créez un dashboard Looker Studio avec :
- Évolution du taux d'ouverture
- Top campagnes performantes
- Tendances de désabonnement
- Analyse des bounces

### 2. Alertes automatiques

Configurez des alertes si :
- Taux de bounce > 10%
- Taux d'ouverture < 15%
- Augmentation des désabonnements

### 3. Segmentation avancée

Identifiez :
- Les contacts les plus engagés (nombreux clics)
- Les contacts inactifs (pas d'ouverture depuis 90 jours)
- Les hard bounces à supprimer

## 🔐 Sécurité

⚠️ **Important** :
- ❌ Ne JAMAIS commiter `config.yaml` avec les clés API
- ✅ Utiliser des Service Accounts GCP avec permissions minimales
- ✅ Rotation régulière des clés API Brevo
- ✅ Logs ne contiennent pas d'informations sensibles

## 📞 Support

En cas de problème :

1. **Vérifier les logs** :
   ```bash
   tail -f logs/sync.log
   ```

2. **Tester individuellement** :
   ```bash
   python scripts/fetch_campaigns.py
   ```

3. **Consulter la doc API** :
   - https://developers.brevo.com/reference

## 📚 Documentation des APIs utilisées

| API | Documentation |
|---|---|
| Email Campaigns | https://developers.brevo.com/reference/get-email-campaigns |
| Email Events | https://developers.brevo.com/reference/get-email-event-report |
| Contacts Lists | https://developers.brevo.com/reference/get-lists |
| SMTP Reports | https://developers.brevo.com/reference/get-aggregated-smtp-report |

## ✅ Checklist de déploiement

- [ ] Tables BigQuery créées
- [ ] Configuration `config.yaml` validée
- [ ] Test manuel réussi : `python sync_brevo_data.py`
- [ ] Données visibles dans BigQuery
- [ ] Automatisation configurée (cron ou Cloud Scheduler)
- [ ] Dashboard/requêtes créés pour le client

## 🎉 Prêt à l'emploi !

Votre système est maintenant opérationnel. Lancez simplement :

```bash
python sync_brevo_data.py
```

Et vos données Brevo seront dans BigQuery ! 🚀

---

*Dernière mise à jour: Décembre 2024*
