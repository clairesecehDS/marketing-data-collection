#!/bin/bash
#
# Déploiement Cloud Run Job pour Ecole des Ponts (EPBS)
# Collection SpyFu mensuelle
#

set -e

PROJECT_ID="ecoledesponts"
REGION="europe-west1"
JOB_NAME="spyfu-epbs-collection"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${JOB_NAME}"

# Configuration SpyFu pour Ecole des Ponts
CONFIG_FILE="config_epbs.yaml"

echo "============================================================"
echo "  Déploiement Cloud Run Job - Ecole des Ponts (EPBS)"
echo "============================================================"
echo "📦 Project: $PROJECT_ID"
echo "🌍 Region: $REGION"
echo "🏷️  Job Name: $JOB_NAME"
echo ""

# 1. Définir le projet GCP
echo "🔧 Configuration du projet GCP..."
gcloud config set project $PROJECT_ID

# 2. Activer les APIs nécessaires
echo "🔧 Activation des APIs..."
gcloud services enable \
    cloudbuild.googleapis.com \
    run.googleapis.com \
    cloudscheduler.googleapis.com \
    appengine.googleapis.com \
    --project=$PROJECT_ID

# 2b. Initialiser App Engine si nécessaire (requis pour Cloud Scheduler)
echo "🔧 Vérification App Engine..."
if ! gcloud app describe --project=$PROJECT_ID &>/dev/null; then
    echo "📱 Création de l'application App Engine..."
    gcloud app create --region=europe-west --project=$PROJECT_ID || true
fi

# 3. Build de l'image Docker
echo "🐳 Build de l'image Docker..."
cd "$(dirname "$0")/.."
gcloud builds submit \
    --config=cloud_job_epbs/cloudbuild.yaml \
    --substitutions=_IMAGE_NAME=$IMAGE_NAME \
    --project=$PROJECT_ID \
    .

# 4. Créer/Mettre à jour le Cloud Run Job
echo "☁️  Déploiement du Cloud Run Job..."
gcloud run jobs create $JOB_NAME \
    --image $IMAGE_NAME \
    --region $REGION \
    --project $PROJECT_ID \
    --max-retries 2 \
    --task-timeout 3600 \
    --memory 2Gi \
    --cpu 1 \
    --set-env-vars "SPYFU_CONFIG_FILE=${CONFIG_FILE}" \
    --set-env-vars "GCP_PROJECT_ID=${PROJECT_ID}" \
    || gcloud run jobs update $JOB_NAME \
        --image $IMAGE_NAME \
        --region $REGION \
        --project $PROJECT_ID \
        --max-retries 2 \
        --task-timeout 3600 \
        --memory 2Gi \
        --cpu 1 \
        --set-env-vars "SPYFU_CONFIG_FILE=${CONFIG_FILE}" \
        --set-env-vars "GCP_PROJECT_ID=${PROJECT_ID}"

# 5. Créer le Cloud Scheduler (1er du mois à minuit UTC)
echo "⏰ Configuration du Cloud Scheduler..."
gcloud scheduler jobs create http spyfu-epbs-scheduler \
    --location $REGION \
    --schedule "0 0 1 * *" \
    --time-zone "UTC" \
    --uri "https://${REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${PROJECT_ID}/jobs/${JOB_NAME}:run" \
    --http-method POST \
    --oauth-service-account-email "spyfu-runner@${PROJECT_ID}.iam.gserviceaccount.com" \
    --project $PROJECT_ID \
    || gcloud scheduler jobs update http spyfu-epbs-scheduler \
        --location $REGION \
        --schedule "0 0 1 * *" \
        --time-zone "UTC" \
        --uri "https://${REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${PROJECT_ID}/jobs/${JOB_NAME}:run" \
        --http-method POST \
        --oauth-service-account-email "spyfu-runner@${PROJECT_ID}.iam.gserviceaccount.com" \
        --project $PROJECT_ID

echo ""
echo "============================================================"
echo "✅ Déploiement terminé!"
echo "============================================================"
echo "📦 Image: $IMAGE_NAME"
echo "☁️  Job: $JOB_NAME"
echo "⏰ Schedule: 1er de chaque mois à minuit UTC"
echo ""
echo "Pour tester manuellement:"
echo "  gcloud run jobs execute $JOB_NAME --region $REGION --project $PROJECT_ID"
echo ""
