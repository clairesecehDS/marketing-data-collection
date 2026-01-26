# Brevo Marketing Events Collection

Ce dossier contient les scripts et schémas pour collecter les événements marketing hebdomadaires de Brevo (anciennement Sendinblue).

## 📋 Vue d'ensemble

Le système collecte les événements marketing de Brevo via l'API **Weekly Event Exports** :
- Spam (marqué comme spam)
- Opened (ouvertures d'email)
- Click (clics sur liens)
- Hard Bounce (rebonds définitifs)
- Soft Bounce (rebonds temporaires)
- Delivered (emails délivrés)
- Unsubscribe (désabonnements)
- Contact Deleted (contacts supprimés)
- Contact Updated (contacts mis à jour)
- List Addition (ajouts à des listes)

## 🗂️ Structure

```
brevo/
├── scripts/
│   └── brevo_weekly_events.py    # Script principal de collecte
├── sql/
│   └── bigquery_brevo_schema.sql # Schéma BigQuery
├── config.yaml                    # Configuration
└── README.md                      # Cette documentation
```

## 📊 Architecture BigQuery

### Dataset et Table
- **Dataset**: `brevo`
- **Table**: `brevo`
- **Partitionnement**: Par date (colonne `date`)
- **Clustering**: Par `event` et `email`

### Colonnes principales
- `date`: Date et heure de l'événement
- `email`: Adresse email du contact
- `event`: Type d'événement (spam, opened, click, etc.)
- `message_id`: Identifiant unique du message
- `subject`: Sujet de l'email
- `template_id`: ID du template utilisé
- `link`: URL cliquée (pour événements click)
- Compteurs booléens pour chaque type d'événement

## 🚀 Installation

### 1. Prérequis
```bash
pip install requests pyyaml google-cloud-bigquery
```

### 2. Configuration

Le fichier `config.yaml` contient tous les paramètres nécessaires :

```yaml
google_cloud:
  project_id: "votre-projet-gcp"
  credentials_file: "../account-key.json"
  datasets:
    brevo: "brevo"

brevo:
  api_key: "xkeysib-..."
  collection:
    event_type: "allEvents"
    days: 7
```

### 3. Créer le dataset et la table BigQuery

```bash
# Depuis le dossier marketing-data-collection
python setup_bigquery.py
```

Ou manuellement :

```bash
# Créer le dataset
bq mk --dataset --location=europe-west9 ecoledesponts:brevo

# Créer la table
bq mk --table ecoledesponts:brevo.brevo brevo/sql/bigquery_brevo_schema.sql
```

## 💻 Utilisation

### Exécution manuelle

```bash
cd brevo/scripts
python brevo_weekly_events.py
```

Le script va :
1. Demander un export d'événements à l'API Brevo
2. Attendre que l'export soit prêt (polling)
3. Télécharger le fichier CSV (ou ZIP)
4. Parser les données
5. Uploader vers BigQuery

### Automatisation

Pour une exécution hebdomadaire automatique, utiliser **Google Cloud Scheduler** :

```bash
# Créer un job Cloud Scheduler (à adapter)
gcloud scheduler jobs create http brevo-weekly-export \
  --schedule="0 3 * * 1" \
  --uri="https://YOUR_CLOUD_FUNCTION_URL" \
  --http-method=POST \
  --time-zone="Europe/Paris" \
  --location="europe-west1"
```

## 📝 API Brevo

### Endpoint utilisé
```
POST https://api.brevo.com/v3/webhooks/export
```

### Paramètres
```json
{
  "event": "allEvents",
  "type": "marketing",
  "days": 7
}
```

### Workflow
1. **Demande d'export** → Retourne un `processId`
2. **Polling du statut** → `GET /v3/processes/{processId}`
3. **Statut completed** → Télécharge depuis `export_url`
4. **Parse CSV** → Upload vers BigQuery

### Limitations
- Maximum **20 exports** sur 7 jours
- Données disponibles **7 jours** après génération
- Export peut prendre plusieurs minutes selon le volume
- Fichiers compressés (ZIP) si volume important

## 📊 Requêtes utiles

### Taux d'ouverture par campagne
```sql
SELECT 
  subject,
  COUNTIF(event = 'delivered') as delivered,
  COUNTIF(event = 'opened') as opened,
  SAFE_DIVIDE(COUNTIF(event = 'opened'), COUNTIF(event = 'delivered')) * 100 as open_rate
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY subject
HAVING delivered > 0
ORDER BY open_rate DESC;
```

### Taux de clic (CTR)
```sql
SELECT 
  subject,
  COUNTIF(event = 'opened') as opened,
  COUNTIF(event = 'click') as clicks,
  SAFE_DIVIDE(COUNTIF(event = 'click'), COUNTIF(event = 'opened')) * 100 as ctr
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY subject
HAVING opened > 0
ORDER BY ctr DESC;
```

### Analyse des bounces
```sql
SELECT 
  email,
  COUNTIF(event = 'hard_bounce') as hard_bounces,
  COUNTIF(event = 'soft_bounce') as soft_bounces,
  COUNTIF(event = 'delivered') as delivered
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY email
HAVING hard_bounces > 0 OR soft_bounces > 0
ORDER BY hard_bounces DESC;
```

### Événements par jour
```sql
SELECT 
  DATE(date) as event_date,
  event,
  COUNT(*) as count
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY event_date, event
ORDER BY event_date DESC, count DESC;
```

### Top templates performants
```sql
SELECT 
  template_id,
  subject,
  COUNTIF(event = 'delivered') as delivered,
  COUNTIF(event = 'opened') as opened,
  COUNTIF(event = 'click') as clicks,
  SAFE_DIVIDE(COUNTIF(event = 'opened'), COUNTIF(event = 'delivered')) * 100 as open_rate,
  SAFE_DIVIDE(COUNTIF(event = 'click'), COUNTIF(event = 'opened')) * 100 as ctr
FROM `ecoledesponts.brevo.brevo`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND template_id IS NOT NULL
GROUP BY template_id, subject
HAVING delivered > 100
ORDER BY open_rate DESC
LIMIT 20;
```

## 🔍 Debugging

### Vérifier les logs
```bash
# Logs du script
tail -f logs/brevo_collection.log
```

### Mode debug
Modifier `config.yaml` :
```yaml
development:
  debug_mode: true
  verbose: true
  test_days: 1  # Tester avec 1 jour seulement
```

### Dry run (sans upload BigQuery)
```yaml
development:
  dry_run: true
```

## 📚 Documentation

- [API Brevo - Weekly Event Exports](https://developers.brevo.com/docs/fetch-all-your-weekly-marketing-events)
- [Brevo API Reference](https://developers.brevo.com/reference)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

## 🔐 Sécurité

⚠️ **Important** :
- Ne JAMAIS commiter `config.yaml` avec les clés API
- Utiliser des Service Accounts GCP avec permissions minimales
- Rotation régulière des clés API
- Logs ne doivent pas contenir d'informations sensibles

## 📞 Support

Pour toute question ou problème :
1. Vérifier les logs
2. Consulter la documentation API Brevo
3. Vérifier les quotas API (max 20 exports/7 jours)
4. Contacter l'administrateur système

## 📅 Maintenance

### Tâches régulières
- [ ] Vérifier les exports hebdomadaires
- [ ] Surveiller les taux de bounce
- [ ] Nettoyer les anciennes sauvegardes locales
- [ ] Analyser les performances des campagnes
- [ ] Vérifier les quotas API Brevo

### Évolutions futures
- [ ] Webhook pour notifications en temps réel
- [ ] Dashboard Looker Studio
- [ ] Alertes automatiques (bounce rate élevé, etc.)
- [ ] Segmentation avancée des contacts
- [ ] A/B testing analysis

---

*Dernière mise à jour: Décembre 2024*
