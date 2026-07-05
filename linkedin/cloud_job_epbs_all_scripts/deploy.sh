#!/bin/bash

# Script de déploiement complet pour LinkedIn Data Collection EPBS
# Ce script déploie le Cloud Run Job et configure le Cloud Scheduler

set -e

# Configuration
PROJECT_ID="ecoledesponts"
REGION="europe-west1"
JOB_NAME="linkedin-epbs-all-scripts"
SCHEDULER_NAME="linkedin-epbs-all-weekly"
SERVICE_ACCOUNT="linkedin-epbs-all@${PROJECT_ID}.iam.gserviceaccount.com"
ARTIFACT_REGISTRY_REPO="linkedin-jobs"

# Couleurs pour les logs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "Déploiement LinkedIn Data Collection EPBS"
echo "=========================================="
echo ""
echo "Projet: ${PROJECT_ID}"
echo "Région: ${REGION}"
echo "Job: ${JOB_NAME}"
echo ""

# Vérifier que gcloud est installé
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ gcloud CLI n'est pas installé${NC}"
    exit 1
fi

# Vérifier le projet actuel
CURRENT_PROJECT=$(gcloud config get-value project 2>/dev/null)
if [ "$CURRENT_PROJECT" != "$PROJECT_ID" ]; then
    echo -e "${YELLOW}⚠️  Changement de projet: $CURRENT_PROJECT → $PROJECT_ID${NC}"
    gcloud config set project $PROJECT_ID
fi

echo ""
echo "→ Étape 1/7: Préparation des fichiers"
echo "======================================"
./prepare_deploy.sh

echo ""
echo "→ Étape 2/7: Activation des APIs nécessaires"
echo "============================================="
echo "Activation de Cloud Run API..."
gcloud services enable run.googleapis.com --project=$PROJECT_ID

echo "Activation de Cloud Build API..."
gcloud services enable cloudbuild.googleapis.com --project=$PROJECT_ID

echo "Activation de Cloud Scheduler API..."
gcloud services enable cloudscheduler.googleapis.com --project=$PROJECT_ID

echo "Activation de Artifact Registry API..."
gcloud services enable artifactregistry.googleapis.com --project=$PROJECT_ID

echo -e "${GREEN}✅ APIs activées${NC}"

echo ""
echo "→ Étape 3/7: Création du repository Artifact Registry"
echo "====================================================="
if gcloud artifacts repositories describe $ARTIFACT_REGISTRY_REPO \
    --location=$REGION \
    --project=$PROJECT_ID &>/dev/null; then
    echo "Repository existant: $ARTIFACT_REGISTRY_REPO"
else
    echo "Création du repository..."
    gcloud artifacts repositories create $ARTIFACT_REGISTRY_REPO \
        --repository-format=docker \
        --location=$REGION \
        --description="Repository pour les jobs LinkedIn" \
        --project=$PROJECT_ID
    echo -e "${GREEN}✅ Repository créé${NC}"
fi

echo ""
echo "→ Étape 4/7: Vérification/Création du Service Account"
echo "====================================================="
if gcloud iam service-accounts describe $SERVICE_ACCOUNT \
    --project=$PROJECT_ID &>/dev/null; then
    echo "Service account existant: $SERVICE_ACCOUNT"
else
    echo "Création du service account..."
    gcloud iam service-accounts create linkedin-epbs-all \
        --display-name="LinkedIn EPBS All Scripts Job" \
        --description="Service account pour le job Cloud Run LinkedIn EPBS complet" \
        --project=$PROJECT_ID

    echo "Attente de la propagation (10 secondes)..."
    sleep 10
    echo -e "${GREEN}✅ Service account créé${NC}"
fi

echo ""
echo "Attribution des permissions..."

# Permission BigQuery Data Editor
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT" \
    --role="roles/bigquery.dataEditor" \
    --condition=None \
    2>/dev/null || echo "  BigQuery Data Editor déjà attribué"

# Permission BigQuery Job User
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT" \
    --role="roles/bigquery.jobUser" \
    --condition=None \
    2>/dev/null || echo "  BigQuery Job User déjà attribué"

# Permission Cloud Run Invoker (pour le scheduler)
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT" \
    --role="roles/run.invoker" \
    --condition=None \
    2>/dev/null || echo "  Cloud Run Invoker déjà attribué"

echo -e "${GREEN}✅ Permissions configurées${NC}"

echo ""
echo "→ Étape 5/7: Build et Push de l'image Docker"
echo "============================================"
gcloud builds submit \
    --config=cloudbuild.yaml \
    --project=$PROJECT_ID \
    --region=$REGION

echo -e "${GREEN}✅ Image construite et poussée${NC}"

echo ""
echo "→ Étape 6/7: Création/Mise à jour du Cloud Run Job"
echo "=================================================="

# Vérifier si le job existe
if gcloud run jobs describe $JOB_NAME \
    --region=$REGION \
    --project=$PROJECT_ID &>/dev/null; then
    echo "Job existant - mise à jour..."
    gcloud run jobs update $JOB_NAME \
        --image=europe-west1-docker.pkg.dev/$PROJECT_ID/$ARTIFACT_REGISTRY_REPO/linkedin-epbs-all:latest \
        --region=$REGION \
        --max-retries=2 \
        --task-timeout=1h \
        --memory=2Gi \
        --cpu=2 \
        --service-account=$SERVICE_ACCOUNT \
        --set-env-vars=GOOGLE_CLOUD_PROJECT=$PROJECT_ID \
        --project=$PROJECT_ID
else
    echo "Création du job..."
    gcloud run jobs create $JOB_NAME \
        --image=europe-west1-docker.pkg.dev/$PROJECT_ID/$ARTIFACT_REGISTRY_REPO/linkedin-epbs-all:latest \
        --region=$REGION \
        --max-retries=2 \
        --task-timeout=1h \
        --memory=2Gi \
        --cpu=2 \
        --service-account=$SERVICE_ACCOUNT \
        --set-env-vars=GOOGLE_CLOUD_PROJECT=$PROJECT_ID \
        --project=$PROJECT_ID
fi

echo -e "${GREEN}✅ Cloud Run Job configuré${NC}"

echo ""
echo "→ Étape 7/7: Configuration du Cloud Scheduler"
echo "============================================="

# Supprimer l'ancien scheduler s'il existe
if gcloud scheduler jobs describe $SCHEDULER_NAME \
    --location=$REGION \
    --project=$PROJECT_ID &>/dev/null; then
    echo "Suppression de l'ancien scheduler..."
    gcloud scheduler jobs delete $SCHEDULER_NAME \
        --location=$REGION \
        --project=$PROJECT_ID \
        --quiet
fi

# Créer le nouveau scheduler
echo "Création du scheduler (tous les lundis à 1h du matin)..."
gcloud scheduler jobs create http $SCHEDULER_NAME \
    --location=$REGION \
    --schedule="0 1 * * 1" \
    --time-zone="Europe/Paris" \
    --uri="https://$REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT_ID/jobs/$JOB_NAME:run" \
    --http-method=POST \
    --oauth-service-account-email=$SERVICE_ACCOUNT \
    --project=$PROJECT_ID

echo -e "${GREEN}✅ Cloud Scheduler configuré${NC}"

echo ""
echo "=========================================="
echo -e "${GREEN}✅ Déploiement terminé avec succès!${NC}"
echo "=========================================="
echo ""
echo "📋 Informations:"
echo "  • Job Cloud Run: $JOB_NAME"
echo "  • Scheduler: $SCHEDULER_NAME"
echo "  • Planification: Tous les lundis à 1h du matin (Europe/Paris)"
echo "  • Service Account: $SERVICE_ACCOUNT"
echo "  • Ressources: 2Gi RAM, 2 CPUs, timeout 1h"
echo ""
echo "Scripts exécutés:"
echo "  1. LinkedIn Ads Library → dataset: linkedin_ads_library"
echo "  2. LinkedIn Budget → dataset: linkedin_ads_advertising"
echo "  3. LinkedIn Campaign Analytics → dataset: linkedin_ads_advertising"
echo "  4. LinkedIn Lead Forms → dataset: linkedin_leadgen_form"
echo "  5. LinkedIn Page Stats → dataset: linkedin_page"
echo ""
echo "🧪 Pour tester immédiatement:"
echo "  gcloud run jobs execute $JOB_NAME --region=$REGION --project=$PROJECT_ID"
echo ""
echo "📅 Pour déclencher le scheduler manuellement:"
echo "  gcloud scheduler jobs run $SCHEDULER_NAME --location=$REGION --project=$PROJECT_ID"
echo ""
echo "📊 Pour voir les logs du job:"
echo "  gcloud logging read \"resource.type=cloud_run_job AND resource.labels.job_name=$JOB_NAME\" --limit=50 --project=$PROJECT_ID"
echo ""
echo "📋 Pour lister les exécutions:"
echo "  gcloud run jobs executions list --job=$JOB_NAME --region=$REGION --project=$PROJECT_ID"
echo ""
