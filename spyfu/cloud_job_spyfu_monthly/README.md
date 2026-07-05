# Cloud Run Jobs - SpyFu Monthly Collection

Automatisation mensuelle de la collecte SpyFu via Cloud Run Jobs, avec déclenchement automatique via Cloud Scheduler.

## 📋 Architecture

- **1 Cloud Run Job par projet/dataset**
- **Cloud Scheduler** : Déclenchement automatique le 1er de chaque mois
- **Docker** : Image contenant tous les scripts Python SpyFu
- **Variables d'environnement** : Configuration dynamique par projet

## 🗂️ Structure

```
cloud_job_spyfu_monthly/
├── Dockerfile                      # Image Docker pour tous les jobs
├── entrypoint.sh                   # Script d'exécution principal
├── config_template.yaml            # Template de configuration
├── deploy_ecoledesponts.sh         # Déploiement ecoledesponts
├── deploy_international_sos.sh     # Déploiement international-sos-479209
├── deploy_verbus_events.sh         # Déploiement verbus - events
├── deploy_verbus_scolaires.sh      # Déploiement verbus - scolaires
├── deploy_verbus_transport.sh      # Déploiement verbus - transport
├── deploy_verbus_voyages.sh        # Déploiement verbus - voyages
└── README.md                       # Ce fichier
```

## 🚀 Déploiement

### Prérequis

1. **gcloud CLI** installé et configuré
2. **Docker** (pour le build local optionnel)
3. **Permissions GCP** :
   - Cloud Run Admin
   - Cloud Scheduler Admin
   - Cloud Build Editor
   - Storage Admin (pour GCR)

### Étape 1 : Configuration des clés API

Éditez chaque script `deploy_*.sh` et remplacez :

```bash
SPYFU_API_KEY="YOUR_SPYFU_API_KEY"  # Votre clé API SpyFu
DOMAINS="domain1.com,domain2.com"    # Liste de vos domaines
```

### Étape 2 : Déploiement par projet

#### Pour ecoledesponts

```bash
cd cloud_job_spyfu_monthly
./deploy_ecoledesponts.sh
```

#### Pour international-sos-479209

```bash
./deploy_international_sos.sh
```

#### Pour verbus-480211 (4 jobs)

```bash
./deploy_verbus_events.sh       # Dataset: spyfu_events
./deploy_verbus_scolaires.sh    # Dataset: spyfu_scolaires
./deploy_verbus_transport.sh    # Dataset: spyfu_transport
./deploy_verbus_voyages.sh      # Dataset: spyfu_voyages
```

## ⏰ Planification

Tous les jobs sont configurés pour s'exécuter **le 1er de chaque mois à partir de 1h du matin (heure de Paris)**, avec des horaires décalés de 10 minutes :

| Job | Horaire UTC | Horaire Paris | Projet | Dataset |
|-----|-------------|---------------|--------|---------|
| spyfu-monthly-collection | 0h00 | 1h00 | ecoledesponts | spyfu |
| spyfu-monthly-collection | 0h00 | 1h00 | international-sos-479209 | spyfu |
| spyfu-monthly-events | 0h10 | 1h10 | verbus-480211 | spyfu_events |
| spyfu-monthly-scolaires | 0h20 | 1h20 | verbus-480211 | spyfu_scolaires |
| spyfu-monthly-transport | 0h30 | 1h30 | verbus-480211 | spyfu_transport |
| spyfu-monthly-voyages | 0h40 | 1h40 | verbus-480211 | spyfu_voyages |

> **Note** : Les horaires sont en UTC dans Cloud Scheduler. Paris = UTC+1 en hiver, UTC+2 en été.

## 🧪 Test manuel

Pour tester un job sans attendre le scheduler :

```bash
# ecoledesponts
gcloud run jobs execute spyfu-monthly-collection \
    --region europe-west1 \
    --project ecoledesponts

# international-sos
gcloud run jobs execute spyfu-monthly-collection \
    --region europe-west1 \
    --project international-sos-479209

# verbus - events
gcloud run jobs execute spyfu-monthly-events \
    --region europe-west1 \
    --project verbus-480211

# ... etc pour les autres
```

## 📊 Tables collectées

Chaque job exécute les 10 scripts mensuels et remplit les tables suivantes :

1. **domain_ad_history** - Historique des annonces par domaine
2. **domain_stats** - Statistiques de domaine
3. **most_valuable_keywords** - Keywords les plus rentables
4. **new_keywords** - Nouveaux mots-clés
5. **newly_ranked_keywords** - Keywords nouvellement classés
6. **ppc_keywords** - Keywords PPC
7. **related_keywords** - Keywords associés
8. **seo_keywords** - Keywords SEO
9. **term_ad_history** - Historique des annonces par keyword
10. **top_pages** - Pages les plus performantes

## 🔧 Configuration

### Variables d'environnement

Chaque job utilise ces variables d'environnement :

- `SPYFU_API_KEY` : Clé API SpyFu
- `SPYFU_COUNTRY_CODE` : Code pays (US, FR, etc.)
- `GCP_PROJECT_ID` : ID du projet GCP
- `SPYFU_DATASET` : Dataset BigQuery cible
- `SPYFU_DOMAINS` : Liste des domaines (séparés par virgules)
- `SPYFU_CONFIG_FILE` : Fichier de config (config.yaml)

### Ressources

- **CPU** : 1 vCPU
- **Mémoire** : 2 GB
- **Timeout** : 3600 secondes (1 heure)
- **Retries** : 2 tentatives max

## 📝 Logs

Pour consulter les logs d'exécution :

```bash
# Via Console GCP
https://console.cloud.google.com/run/jobs

# Via gcloud
gcloud logging read "resource.type=cloud_run_job AND resource.labels.job_name=spyfu-monthly-collection" \
    --project ecoledesponts \
    --limit 50 \
    --format json
```

## 🔄 Mise à jour

Pour mettre à jour un job existant :

1. Modifiez les scripts Python dans `/spyfu/scripts/`
2. Réexécutez le script de déploiement correspondant
3. Le nouveau code sera automatiquement déployé

```bash
# Exemple pour ecoledesponts
./deploy_ecoledesponts.sh
```

## ⚠️ Troubleshooting

### Job échoue lors de l'exécution

```bash
# Vérifier les logs
gcloud logging read "resource.type=cloud_run_job" \
    --project YOUR_PROJECT_ID \
    --limit 100

# Tester localement avec Docker
docker build -t spyfu-test .
docker run -e SPYFU_API_KEY=xxx ... spyfu-test
```

### Scheduler ne déclenche pas le job

```bash
# Vérifier le scheduler
gcloud scheduler jobs describe spyfu-monthly-collection-scheduler \
    --location europe-west1 \
    --project YOUR_PROJECT_ID

# Tester le scheduler manuellement
gcloud scheduler jobs run spyfu-monthly-collection-scheduler \
    --location europe-west1 \
    --project YOUR_PROJECT_ID
```

### Erreur de permissions

Assurez-vous que le service account a les permissions :
- `roles/run.invoker`
- `roles/bigquery.dataEditor`
- `roles/bigquery.jobUser`

## 📚 Documentation

- [Cloud Run Jobs](https://cloud.google.com/run/docs/create-jobs)
- [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
- [SpyFu API Documentation](https://www.spyfu.com/apis)
