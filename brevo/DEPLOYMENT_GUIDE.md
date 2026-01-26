# Guide de Déploiement - Brevo Data Sync (Cloud Run Job + Cloud Scheduler)

Ce guide explique comment déployer une synchronisation automatisée des données Brevo vers BigQuery en utilisant Google Cloud Run Jobs et Cloud Scheduler.

## Architecture

```
┌─────────────────┐
│ Cloud Scheduler │  Hebdomadaire (Lundi 3h)
└────────┬────────┘
         │ Trigger
         ▼
┌─────────────────┐
│  Cloud Run Job  │  Exécute sync_brevo_data.py
└────────┬────────┘
         │ Fetch & Upload
         ▼
┌─────────────────┐
│    BigQuery     │  Tables: campaigns, events, contacts_lists, smtp_reports
└─────────────────┘
```

## Prérequis

### 1. Outils nécessaires

- **gcloud CLI** : [Installation](https://cloud.google.com/sdk/docs/install)
- **Docker** (optionnel, pour tester localement)
- Accès au projet GCP `ecoledesponts` avec les permissions suivantes :
  - `roles/run.admin`
  - `roles/iam.serviceAccountAdmin`
  - `roles/cloudscheduler.admin`
  - `roles/secretmanager.admin`
  - `roles/bigquery.admin`

### 2. Authentification

```bash
# Se connecter à GCP
gcloud auth login

# Définir le projet par défaut
gcloud config set project ecoledesponts
```

### 3. Fichiers requis

Assurez-vous que ces fichiers existent dans le répertoire `brevo/` :
- `sync_brevo_data.py` - Script principal de synchronisation
- `config.yaml` - Configuration Brevo et BigQuery
- `requirements.txt` - Dépendances Python
- `scripts/` - Modules de fetch et upload
- `../account-key.json` - Clé de service GCP (un niveau au-dessus)

## Déploiement

### Étape 1 : Déployer le Cloud Run Job

Le script `deploy_cloud_run_job.sh` effectue automatiquement :
1. Activation des APIs nécessaires
2. Création du Service Account
3. Configuration des permissions
4. Création du secret pour les credentials
5. Build et push de l'image Docker
6. Déploiement du Cloud Run Job

```bash
cd /path/to/marketing-data-collection/brevo
./deploy_cloud_run_job.sh
```

Le script va :
- Construire l'image Docker `gcr.io/ecoledesponts/brevo-data-sync`
- Créer le Service Account `brevo-sync-sa@ecoledesponts.iam.gserviceaccount.com`
- Créer le secret `brevo-credentials` dans Secret Manager
- Déployer le job Cloud Run dans la région `europe-west9`

À la fin, le script propose de tester le job immédiatement.

### Étape 2 : Configurer le Cloud Scheduler

Le script `setup_scheduler.sh` configure l'exécution automatique :

```bash
./setup_scheduler.sh
```

Le script propose plusieurs options de planning :
1. **Hebdomadaire - Lundi à 3h** (défaut, recommandé)
2. Hebdomadaire - Dimanche à 2h
3. Bi-hebdomadaire - Lundi et Jeudi à 3h
4. Quotidien - Tous les jours à 3h
5. Personnalisé - Expression cron manuelle

Choisissez l'option 1 pour une synchronisation hebdomadaire standard.

## Configuration

### Modifier les paramètres de synchronisation

Le Cloud Run Job est configuré avec les arguments par défaut :
- `--days=7` : Récupère les événements des 7 derniers jours
- `--report-days=30` : Récupère les rapports SMTP des 30 derniers jours

Pour modifier ces paramètres, éditez le fichier `deploy_cloud_run_job.sh` ligne 144 :

```bash
--args="--days=7,--report-days=30" \
```

Puis redéployez :

```bash
./deploy_cloud_run_job.sh
```

### Modifier la fréquence d'exécution

Pour changer le planning du scheduler :

```bash
# Lister les schedulers
gcloud scheduler jobs list --location=europe-west9 --project=ecoledesponts

# Mettre à jour le planning (exemple : tous les jours à 2h)
gcloud scheduler jobs update http brevo-weekly-sync \
    --location=europe-west9 \
    --schedule="0 2 * * *" \
    --project=ecoledesponts
```

Format cron : `minute hour day month day_of_week`

Exemples :
- `0 3 * * 1` : Tous les lundis à 3h
- `0 2 * * 0` : Tous les dimanches à 2h
- `0 3 * * 1,4` : Lundis et jeudis à 3h
- `0 3 * * *` : Tous les jours à 3h
- `0 */6 * * *` : Toutes les 6 heures

## Gestion et Monitoring

### Vérifier le statut du scheduler

```bash
gcloud scheduler jobs describe brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts
```

### Déclencher manuellement une synchronisation

```bash
# Via le scheduler
gcloud scheduler jobs run brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts

# Ou directement le job
gcloud run jobs execute brevo-data-sync \
    --region=europe-west9 \
    --project=ecoledesponts \
    --wait
```

### Voir les logs

```bash
# Logs du Cloud Run Job
gcloud run jobs logs read brevo-data-sync \
    --region=europe-west9 \
    --project=ecoledesponts \
    --limit=100

# Logs en temps réel
gcloud run jobs logs tail brevo-data-sync \
    --region=europe-west9 \
    --project=ecoledesponts
```

### Historique des exécutions

```bash
# Lister les exécutions
gcloud run jobs executions list \
    --job=brevo-data-sync \
    --region=europe-west9 \
    --project=ecoledesponts

# Détails d'une exécution spécifique
gcloud run jobs executions describe EXECUTION_NAME \
    --region=europe-west9 \
    --project=ecoledesponts
```

### Vérifier les données dans BigQuery

```bash
# Lister les tables
bq ls --project_id=ecoledesponts brevo

# Compter les enregistrements
bq query --project_id=ecoledesponts \
    'SELECT COUNT(*) as total FROM `ecoledesponts.brevo.events`'

# Voir les dernières campagnes synchronisées
bq query --project_id=ecoledesponts \
    'SELECT * FROM `ecoledesponts.brevo.campaigns` ORDER BY retrieved_at DESC LIMIT 10'
```

## Maintenance

### Mettre à jour le code

Lorsque vous modifiez le code Python :

```bash
# Reconstruire et redéployer
./deploy_cloud_run_job.sh
```

Le script détectera que le job existe déjà et le mettra à jour.

### Mettre à jour les credentials

```bash
# Ajouter une nouvelle version du secret
gcloud secrets versions add brevo-credentials \
    --data-file=../account-key.json \
    --project=ecoledesponts

# Les nouvelles exécutions utiliseront automatiquement la dernière version
```

### Suspendre/Reprendre le scheduler

```bash
# Suspendre (arrêter les exécutions automatiques)
gcloud scheduler jobs pause brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts

# Reprendre
gcloud scheduler jobs resume brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts
```

### Supprimer le déploiement

```bash
# Supprimer le scheduler
gcloud scheduler jobs delete brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts

# Supprimer le Cloud Run Job
gcloud run jobs delete brevo-data-sync \
    --region=europe-west9 \
    --project=ecoledesponts

# Supprimer le secret (optionnel)
gcloud secrets delete brevo-credentials \
    --project=ecoledesponts
```

## Résolution de problèmes

### Le job échoue avec "Permission denied"

Vérifiez que le Service Account a les bonnes permissions :

```bash
# Vérifier les rôles
gcloud projects get-iam-policy ecoledesponts \
    --flatten="bindings[].members" \
    --filter="bindings.members:brevo-sync-sa@ecoledesponts.iam.gserviceaccount.com"

# Rajouter les permissions si nécessaire
gcloud projects add-iam-policy-binding ecoledesponts \
    --member="serviceAccount:brevo-sync-sa@ecoledesponts.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataEditor"
```

### Le job timeout après 30 minutes

Augmentez le timeout du job :

```bash
gcloud run jobs update brevo-data-sync \
    --region=europe-west9 \
    --task-timeout=1h \
    --project=ecoledesponts
```

### Erreur "API Key invalid" de Brevo

Mettez à jour la clé API dans [config.yaml](config.yaml:32) et redéployez :

```bash
./deploy_cloud_run_job.sh
```

### Le scheduler ne se déclenche pas

Vérifiez que :
1. Le scheduler n'est pas en pause
2. Le timezone est correct (Europe/Paris)
3. Le Service Account Scheduler a le rôle `roles/run.invoker`

```bash
# Vérifier le statut
gcloud scheduler jobs describe brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts

# Tester manuellement
gcloud scheduler jobs run brevo-weekly-sync \
    --location=europe-west9 \
    --project=ecoledesponts
```

## Coûts estimés

Pour une exécution hebdomadaire avec 1 Go de mémoire et 1 vCPU :

- **Cloud Run Jobs** : ~0,10€/mois (30 min/semaine)
- **Cloud Scheduler** : ~0,08€/mois (1 job)
- **BigQuery** : Variable selon le volume de données
- **Secret Manager** : ~0,06€/mois (1 secret actif)

**Total estimé** : ~0,25€/mois (hors BigQuery storage)

## Support

En cas de problème :

1. Consultez les logs : `gcloud run jobs logs read brevo-data-sync --region=europe-west9 --project=ecoledesponts`
2. Testez localement : `python sync_brevo_data.py --days 1`
3. Vérifiez la configuration : [config.yaml](config.yaml)
4. Consultez la documentation Brevo : https://developers.brevo.com/docs

## Ressources

- [Documentation Cloud Run Jobs](https://cloud.google.com/run/docs/create-jobs)
- [Documentation Cloud Scheduler](https://cloud.google.com/scheduler/docs)
- [Documentation Brevo API](https://developers.brevo.com/docs)
- [BigQuery Best Practices](https://cloud.google.com/bigquery/docs/best-practices)
