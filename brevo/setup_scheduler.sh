#!/bin/bash

# =============================================================================
# Script de configuration Cloud Scheduler pour Brevo Data Sync
# =============================================================================
#
# Ce script configure un Cloud Scheduler qui exécute le Cloud Run Job
# de manière hebdomadaire (tous les lundis à 3h du matin)
#
# Usage:
#   ./setup_scheduler.sh
#
# Prérequis:
#   - Le Cloud Run Job doit être déployé (exécuter deploy_cloud_run_job.sh d'abord)
#   - gcloud CLI installé et authentifié
# =============================================================================

set -e  # Arrêter en cas d'erreur

# =============================================================================
# CONFIGURATION
# =============================================================================

PROJECT_ID="ecoledesponts"
REGION="europe-west9"  # Région du Cloud Run Job
SCHEDULER_REGION="europe-west1"  # Région pour Cloud Scheduler (Belgique - la plus proche supportée)
JOB_NAME="brevo-data-sync"
SCHEDULER_NAME="brevo-weekly-sync"
SERVICE_ACCOUNT="brevo-sync-sa@${PROJECT_ID}.iam.gserviceaccount.com"

# Configuration du planning
# Format cron: minute hour day month day_of_week
# Par défaut: tous les lundis à 2h du matin (heure de Paris)
SCHEDULE="0 2 * * 1"
TIMEZONE="Europe/Paris"
DESCRIPTION="Synchronisation hebdomadaire des données Brevo vers BigQuery"

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
# MENU DE CONFIGURATION
# =============================================================================

echo ""
log_info "=========================================="
log_info "Configuration du Cloud Scheduler"
log_info "=========================================="
echo ""

# Afficher les options de planning
echo "Choisissez la fréquence de synchronisation:"
echo "  1) Hebdomadaire - Lundi à 3h (défaut)"
echo "  2) Hebdomadaire - Dimanche à 2h"
echo "  3) Bi-hebdomadaire - Lundi et Jeudi à 3h"
echo "  4) Quotidien - Tous les jours à 3h"
echo "  5) Personnalisé - Entrer une expression cron"
echo ""
read -p "Votre choix (1-5) [1]: " choice
choice=${choice:-1}

case $choice in
    1)
        SCHEDULE="0 3 * * 1"
        DESCRIPTION="Synchronisation hebdomadaire (lundi 3h) des données Brevo vers BigQuery"
        ;;
    2)
        SCHEDULE="0 2 * * 0"
        DESCRIPTION="Synchronisation hebdomadaire (dimanche 2h) des données Brevo vers BigQuery"
        ;;
    3)
        SCHEDULE="0 3 * * 1,4"
        DESCRIPTION="Synchronisation bi-hebdomadaire (lundi et jeudi 3h) des données Brevo vers BigQuery"
        ;;
    4)
        SCHEDULE="0 3 * * *"
        DESCRIPTION="Synchronisation quotidienne (3h) des données Brevo vers BigQuery"
        ;;
    5)
        read -p "Entrez l'expression cron: " SCHEDULE
        read -p "Entrez la description: " DESCRIPTION
        ;;
    *)
        log_error "Choix invalide"
        exit 1
        ;;
esac

log_info "Planning sélectionné: ${SCHEDULE}"
log_info "Timezone: ${TIMEZONE}"
log_info "Description: ${DESCRIPTION}"

# =============================================================================
# VÉRIFICATIONS PRÉALABLES
# =============================================================================

log_info "Vérification des prérequis..."

# Vérifier que gcloud est installé
if ! command -v gcloud &> /dev/null; then
    log_error "gcloud CLI n'est pas installé"
    exit 1
fi

# Définir le projet
gcloud config set project ${PROJECT_ID}

# Vérifier que le Cloud Run Job existe
log_info "Vérification que le Cloud Run Job existe..."
if ! gcloud run jobs describe ${JOB_NAME} --region=${REGION} --project=${PROJECT_ID} &> /dev/null; then
    log_error "Le Cloud Run Job '${JOB_NAME}' n'existe pas"
    log_info "Veuillez d'abord déployer le job avec: ./deploy_cloud_run_job.sh"
    exit 1
fi

log_success "Cloud Run Job trouvé"

# =============================================================================
# CRÉATION DU SERVICE ACCOUNT POUR CLOUD SCHEDULER (si nécessaire)
# =============================================================================

SCHEDULER_SA="cloud-scheduler-sa@${PROJECT_ID}.iam.gserviceaccount.com"

log_info "Vérification du Service Account pour Cloud Scheduler..."

if gcloud iam service-accounts describe ${SCHEDULER_SA} --project=${PROJECT_ID} &> /dev/null; then
    log_warning "Le Service Account Scheduler existe déjà"
else
    log_info "Création du Service Account pour Scheduler..."
    gcloud iam service-accounts create cloud-scheduler-sa \
        --display-name="Cloud Scheduler Service Account" \
        --project=${PROJECT_ID}
    log_success "Service Account créé"
fi

# Donner la permission d'invoquer le Cloud Run Job
log_info "Attribution des permissions au Service Account Scheduler..."
gcloud run jobs add-iam-policy-binding ${JOB_NAME} \
    --region=${REGION} \
    --member="serviceAccount:${SCHEDULER_SA}" \
    --role="roles/run.invoker" \
    --project=${PROJECT_ID}

log_success "Permissions accordées"

# =============================================================================
# CONFIGURATION DU CLOUD SCHEDULER
# =============================================================================

log_info "Configuration du Cloud Scheduler: ${SCHEDULER_NAME}"

# Obtenir l'URI du Cloud Run Job
JOB_URI="https://${REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${PROJECT_ID}/jobs/${JOB_NAME}:run"

# Créer ou mettre à jour le job scheduler
if gcloud scheduler jobs describe ${SCHEDULER_NAME} --location=${SCHEDULER_REGION} --project=${PROJECT_ID} &> /dev/null; then
    log_warning "Le scheduler existe déjà, mise à jour..."

    gcloud scheduler jobs update http ${SCHEDULER_NAME} \
        --location=${SCHEDULER_REGION} \
        --schedule="${SCHEDULE}" \
        --time-zone="${TIMEZONE}" \
        --uri="${JOB_URI}" \
        --http-method=POST \
        --oauth-service-account-email="${SCHEDULER_SA}" \
        --description="${DESCRIPTION}" \
        --project=${PROJECT_ID}

    log_success "Scheduler mis à jour"
else
    log_info "Création du scheduler..."

    gcloud scheduler jobs create http ${SCHEDULER_NAME} \
        --location=${SCHEDULER_REGION} \
        --schedule="${SCHEDULE}" \
        --time-zone="${TIMEZONE}" \
        --uri="${JOB_URI}" \
        --http-method=POST \
        --oauth-service-account-email="${SCHEDULER_SA}" \
        --description="${DESCRIPTION}" \
        --project=${PROJECT_ID}

    log_success "Scheduler créé"
fi

# =============================================================================
# TEST DU SCHEDULER
# =============================================================================

log_info "Test du Cloud Scheduler..."
log_warning "Voulez-vous exécuter le scheduler maintenant pour tester? (y/n)"
read -r response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    log_info "Exécution du scheduler..."
    gcloud scheduler jobs run ${SCHEDULER_NAME} \
        --location=${SCHEDULER_REGION} \
        --project=${PROJECT_ID}

    log_success "Scheduler déclenché!"
    log_info "Vérifiez l'exécution du job avec:"
    log_info "  gcloud run jobs executions list --job=${JOB_NAME} --region=${REGION} --project=${PROJECT_ID}"
else
    log_info "Test ignoré. Vous pouvez déclencher manuellement le scheduler avec:"
    log_info "  gcloud scheduler jobs run ${SCHEDULER_NAME} --location=${SCHEDULER_REGION} --project=${PROJECT_ID}"
fi

# =============================================================================
# RÉSUMÉ
# =============================================================================

echo ""
log_success "=========================================="
log_success "Configuration terminée avec succès!"
log_success "=========================================="
echo ""
log_info "Informations du scheduler:"
echo "  - Nom: ${SCHEDULER_NAME}"
echo "  - Région Scheduler: ${SCHEDULER_REGION}"
echo "  - Région Cloud Run Job: ${REGION}"
echo "  - Planning: ${SCHEDULE}"
echo "  - Timezone: ${TIMEZONE}"
echo "  - Description: ${DESCRIPTION}"
echo "  - Cloud Run Job: ${JOB_NAME}"
echo ""
log_info "Commandes utiles:"
echo ""
echo "  # Voir le statut du scheduler"
echo "  gcloud scheduler jobs describe ${SCHEDULER_NAME} --location=${SCHEDULER_REGION} --project=${PROJECT_ID}"
echo ""
echo "  # Lister les prochaines exécutions"
echo "  gcloud scheduler jobs list --location=${SCHEDULER_REGION} --project=${PROJECT_ID}"
echo ""
echo "  # Déclencher manuellement"
echo "  gcloud scheduler jobs run ${SCHEDULER_NAME} --location=${SCHEDULER_REGION} --project=${PROJECT_ID}"
echo ""
echo "  # Voir les logs du Cloud Run Job"
echo "  gcloud run jobs logs read ${JOB_NAME} --region=${REGION} --project=${PROJECT_ID}"
echo ""
echo "  # Voir l'historique des exécutions"
echo "  gcloud run jobs executions list --job=${JOB_NAME} --region=${REGION} --project=${PROJECT_ID}"
echo ""
echo "  # Désactiver le scheduler"
echo "  gcloud scheduler jobs pause ${SCHEDULER_NAME} --location=${SCHEDULER_REGION} --project=${PROJECT_ID}"
echo ""
echo "  # Réactiver le scheduler"
echo "  gcloud scheduler jobs resume ${SCHEDULER_NAME} --location=${SCHEDULER_REGION} --project=${PROJECT_ID}"
echo ""
log_success "La synchronisation Brevo → BigQuery est maintenant automatisée!"
echo ""
