#!/bin/bash
#
# Déploiement complet de tous les Cloud Run Jobs Verbus
# Build l'image une seule fois, puis déploie les 4 jobs
#

set -e

PROJECT_ID="verbus-480211"
REGION="europe-west1"
IMAGE_NAME="gcr.io/${PROJECT_ID}/spyfu-verbus-collection"

echo "============================================================"
echo "  Déploiement complet - Verbus (4 jobs)"
echo "============================================================"
echo "📦 Project: $PROJECT_ID"
echo "🌍 Region: $REGION"
echo "🖼️  Image: $IMAGE_NAME"
echo ""

# Se placer dans le bon répertoire (racine du contexte spyfu/)
cd "$(dirname "$0")/.."

# 1. Build de l'image Docker (une seule fois pour tous les jobs)
echo "🐳 Build de l'image Docker (commune aux 4 jobs)..."
gcloud builds submit \
    --config=cloud_job_verbus/cloudbuild.yaml \
    --substitutions=_IMAGE_NAME=$IMAGE_NAME \
    --project=$PROJECT_ID \
    .

echo ""
echo "============================================================"
echo "  Déploiement des 4 jobs (sans rebuild)"
echo "============================================================"
echo ""

# 2. Déployer chaque job sans rebuilder l'image
echo "1/4 - Déploiement Events..."
cd "$(dirname "$0")"
./deploy_events.sh --skip-build

echo ""
echo "2/4 - Déploiement Scolaires..."
./deploy_scolaires.sh --skip-build

echo ""
echo "3/4 - Déploiement Transport..."
./deploy_transport.sh --skip-build

echo ""
echo "4/4 - Déploiement Voyages..."
./deploy_voyages.sh --skip-build

echo ""
echo "============================================================"
echo "✅ Déploiement complet terminé!"
echo "============================================================"
echo "🖼️  Image: $IMAGE_NAME"
echo "☁️  Jobs déployés:"
echo "   - spyfu-verbus-events    (1er du mois à 0h UTC)"
echo "   - spyfu-verbus-scolaires (1er du mois à 2h UTC)"
echo "   - spyfu-verbus-transport (1er du mois à 4h UTC)"
echo "   - spyfu-verbus-voyages   (1er du mois à 6h UTC)"
echo ""
