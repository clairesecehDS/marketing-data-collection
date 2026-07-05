#!/bin/bash
set -e
PROJECT_ID="verbus-480211"
REGION="europe-west1"
JOB_NAME="spyfu-monthly-voyages"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${JOB_NAME}"
# Configuration SpyFu pour Voyages
# Utilise config_verbus_voyages.yaml
CONFIG_FILE="config_verbus_voyages.yaml"

echo "Déploiement Cloud Run Job - Verbus Voyages"
gcloud config set project $PROJECT_ID
gcloud services enable cloudbuild.googleapis.com run.googleapis.com cloudscheduler.googleapis.com appengine.googleapis.com --project=$PROJECT_ID

# Initialiser App Engine si nécessaire (requis pour Cloud Scheduler)
echo "🔧 Vérification App Engine..."
if ! gcloud app describe --project=$PROJECT_ID &>/dev/null; then
    echo "📱 Création de l'application App Engine..."
    gcloud app create --region=europe-west --project=$PROJECT_ID || true
fi
cd "$(dirname "$0")/.."
gcloud builds submit --config=cloud_job_spyfu_monthly/cloudbuild.yaml --substitutions=_IMAGE_NAME=$IMAGE_NAME --project=$PROJECT_ID .
gcloud run jobs create $JOB_NAME --image $IMAGE_NAME --region $REGION --project $PROJECT_ID --max-retries 2 --task-timeout 3600 --memory 2Gi --cpu 1 --set-env-vars "SPYFU_CONFIG_FILE=${CONFIG_FILE},GCP_PROJECT_ID=${PROJECT_ID}" || gcloud run jobs update $JOB_NAME --image $IMAGE_NAME --region $REGION --project $PROJECT_ID --max-retries 2 --task-timeout 3600 --memory 2Gi --cpu 1 --set-env-vars "SPYFU_CONFIG_FILE=${CONFIG_FILE},GCP_PROJECT_ID=${PROJECT_ID}"
gcloud scheduler jobs create http ${JOB_NAME}-scheduler --location $REGION --schedule "40 0 1 * *" --time-zone "UTC" --uri "https://${REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${PROJECT_ID}/jobs/${JOB_NAME}:run" --http-method POST --oauth-service-account-email "${PROJECT_ID}@appspot.gserviceaccount.com" --project $PROJECT_ID || gcloud scheduler jobs update http ${JOB_NAME}-scheduler --location $REGION --schedule "40 0 1 * *" --time-zone "UTC" --uri "https://${REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${PROJECT_ID}/jobs/${JOB_NAME}:run" --http-method POST --oauth-service-account-email "${PROJECT_ID}@appspot.gserviceaccount.com" --project $PROJECT_ID
echo "✅ Déploiement terminé! Schedule: 1er de chaque mois à 1h40 (heure de Paris)"
