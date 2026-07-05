#!/bin/bash

# =============================================================================
# Script de déploiement Cloud Run Job pour Brevo Data Sync
# =============================================================================
#
# Ce script déploie un Cloud Run Job qui synchronise les données Brevo vers BigQuery
# et configure un Cloud Scheduler pour l'exécuter de manière hebdomadaire
#
# Usage:
#   ./deploy_cloud_run_job.sh
#
# Prérequis:
#   - gcloud CLI installé et authentifié
#   - Permissions nécessaires sur le projet GCP
#   - Docker installé localement (pour tester le build)
# =============================================================================

set -e  # Arrêter en cas d'erreur

# =============================================================================
# CONFIGURATION
# =============================================================================

PROJECT_ID="ecoledesponts"
REGION="europe-west9"
JOB_NAME="brevo-data-sync"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${JOB_NAME}"
SERVICE_ACCOUNT="brevo-sync-sa@${PROJECT_ID}.iam.gserviceaccount.com"
SECRET_NAME="brevo-credentials"
DATASET="brevo"

# Couleurs pour les logs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# =============================================================================
# FONCTIONS
# =============================================================================

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# =============================================================================
# VÉRIFICATIONS PRÉALABLES
# =============================================================================

log_info "Vérification des prérequis..."

# Vérifier que gcloud est installé
if ! command -v gcloud &> /dev/null; then
    log_error "gcloud CLI n'est pas installé"
    exit 1
fi

# Vérifier que nous sommes dans le bon répertoire
if [ ! -f "sync_brevo_data.py" ]; then
    log_error "Le fichier sync_brevo_data.py n'existe pas. Êtes-vous dans le bon répertoire?"
    exit 1
fi

# Définir le projet
log_info "Configuration du projet GCP: ${PROJECT_ID}"
gcloud config set project ${PROJECT_ID}

# =============================================================================
# ÉTAPE 1: Activer les APIs nécessaires
# =============================================================================

log_info "Activation des APIs Google Cloud..."
gcloud services enable \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    cloudscheduler.googleapis.com \
    secretmanager.googleapis.com \
    bigquery.googleapis.com \
    --project=${PROJECT_ID}

log_success "APIs activées"

# =============================================================================
# ÉTAPE 2: Créer le Service Account (si nécessaire)
# =============================================================================

log_info "Vérification du Service Account: ${SERVICE_ACCOUNT}"

if gcloud iam service-accounts describe ${SERVICE_ACCOUNT} --project=${PROJECT_ID} &> /dev/null; then
    log_warning "Le Service Account existe déjà"
else
    log_info "Création du Service Account..."
    gcloud iam service-accounts create brevo-sync-sa \
        --display-name="Brevo Data Sync Service Account" \
        --project=${PROJECT_ID}
    log_success "Service Account créé"
    
    # Attendre la propagation du Service Account dans IAM
    log_info "Attente de la propagation du Service Account (30 secondes)..."
    sleep 30
fi

# =============================================================================
# ÉTAPE 3: Accorder les permissions au Service Account
# =============================================================================

log_info "Attribution des rôles au Service Account..."

# Rôles nécessaires
ROLES=(
    "roles/bigquery.dataEditor"
    "roles/bigquery.jobUser"
    "roles/secretmanager.secretAccessor"
)

for ROLE in "${ROLES[@]}"; do
    log_info "Attribution du rôle: ${ROLE}"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${SERVICE_ACCOUNT}" \
        --role="${ROLE}" \
        --condition=None \
        --quiet
done

log_success "Permissions accordées"

# =============================================================================
# ÉTAPE 4: Créer/Vérifier le Secret Manager pour les credentials
# =============================================================================

log_info "Vérification du secret pour les credentials..."

if gcloud secrets describe ${SECRET_NAME} --project=${PROJECT_ID} &> /dev/null; then
    log_warning "Le secret ${SECRET_NAME} existe déjà"
    log_info "Si vous voulez le mettre à jour, exécutez:"
    log_info "  gcloud secrets versions add ${SECRET_NAME} --data-file=../account-key.json --project=${PROJECT_ID}"
else
    log_info "Création du secret..."
    if [ -f "../account-key.json" ]; then
        gcloud secrets create ${SECRET_NAME} \
            --data-file=../account-key.json \
            --replication-policy="automatic" \
            --project=${PROJECT_ID}
        log_success "Secret créé avec le fichier ../account-key.json"
    else
        log_error "Le fichier ../account-key.json n'existe pas"
        log_info "Veuillez créer le secret manuellement avec:"
        log_info "  gcloud secrets create ${SECRET_NAME} --data-file=PATH_TO_KEY --project=${PROJECT_ID}"
        exit 1
    fi
fi

# Donner accès au secret au Service Account
log_info "Attribution de l'accès au secret..."
gcloud secrets add-iam-policy-binding ${SECRET_NAME} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="roles/secretmanager.secretAccessor" \
    --project=${PROJECT_ID}

log_success "Accès au secret configuré"

# =============================================================================
# ÉTAPE 5: Build et Push de l'image Docker
# =============================================================================

log_info "Build de l'image Docker..."
log_info "Image: ${IMAGE_NAME}"

gcloud builds submit \
    --tag ${IMAGE_NAME} \
    --project=${PROJECT_ID} \
    --region=${REGION} \
    .

log_success "Image Docker construite et poussée vers GCR"

# =============================================================================
# ÉTAPE 6: Créer le dataset BigQuery (si nécessaire)
# =============================================================================

log_info "Vérification du dataset BigQuery: ${DATASET}"

if bq ls -d --project_id=${PROJECT_ID} | grep -q ${DATASET}; then
    log_warning "Le dataset ${DATASET} existe déjà"
else
    log_info "Création du dataset BigQuery..."
    bq mk --dataset \
        --location=${REGION} \
        --description="Données marketing Brevo" \
        ${PROJECT_ID}:${DATASET}
    log_success "Dataset créé"
fi

# =============================================================================
# ÉTAPE 7: Déployer le Cloud Run Job
# =============================================================================

log_info "Déploiement du Cloud Run Job: ${JOB_NAME}"

gcloud run jobs create ${JOB_NAME} \
    --image=${IMAGE_NAME} \
    --region=${REGION} \
    --service-account=${SERVICE_ACCOUNT} \
    --max-retries=2 \
    --task-timeout=30m \
    --memory=1Gi \
    --cpu=1 \
    --set-secrets="/app/credentials/account-key.json=${SECRET_NAME}:latest" \
    --args="--days=7,--report-days=30" \
    --project=${PROJECT_ID} \
    2>/dev/null || \
gcloud run jobs update ${JOB_NAME} \
    --image=${IMAGE_NAME} \
    --region=${REGION} \
    --service-account=${SERVICE_ACCOUNT} \
    --max-retries=2 \
    --task-timeout=30m \
    --memory=1Gi \
    --cpu=1 \
    --set-secrets="/app/credentials/account-key.json=${SECRET_NAME}:latest" \
    --args="--days=7,--report-days=30" \
    --project=${PROJECT_ID}

log_success "Cloud Run Job déployé: ${JOB_NAME}"

# =============================================================================
# ÉTAPE 8: Test du Job
# =============================================================================

log_info "Test du Cloud Run Job..."
log_warning "Voulez-vous exécuter le job maintenant pour tester? (y/n)"
read -r response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    log_info "Exécution du job..."
    gcloud run jobs execute ${JOB_NAME} \
        --region=${REGION} \
        --project=${PROJECT_ID} \
        --wait
    log_success "Job exécuté avec succès!"
else
    log_info "Test ignoré. Vous pouvez exécuter le job manuellement avec:"
    log_info "  gcloud run jobs execute ${JOB_NAME} --region=${REGION} --project=${PROJECT_ID}"
fi

# =============================================================================
# RÉSUMÉ
# =============================================================================

echo ""
log_success "=========================================="
log_success "Déploiement terminé avec succès!"
log_success "=========================================="
echo ""
log_info "Informations du déploiement:"
echo "  - Projet GCP: ${PROJECT_ID}"
echo "  - Région: ${REGION}"
echo "  - Nom du Job: ${JOB_NAME}"
echo "  - Image Docker: ${IMAGE_NAME}"
echo "  - Service Account: ${SERVICE_ACCOUNT}"
echo "  - Dataset BigQuery: ${DATASET}"
echo ""
log_info "Prochaines étapes:"
echo "  1. Configurez le Cloud Scheduler avec: ./setup_scheduler.sh"
echo "  2. Vérifiez les logs: gcloud run jobs logs read ${JOB_NAME} --region=${REGION} --project=${PROJECT_ID}"
echo "  3. Exécutez manuellement: gcloud run jobs execute ${JOB_NAME} --region=${REGION} --project=${PROJECT_ID}"
echo ""
