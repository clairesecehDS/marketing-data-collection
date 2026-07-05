#!/bin/bash

# Script pour préparer les fichiers nécessaires au déploiement du Cloud Job EPBS

set -e

echo "📋 Préparation des fichiers pour le déploiement EPBS..."

# Copier les fichiers depuis le répertoire parent
cp ../config_epbs.yaml ./config_epbs.yaml
cp ../config_loader.py ./config_loader.py
cp ../account-key.json ./account-key.json

# Copier le dossier scripts depuis la source principale
rm -rf ./scripts
cp -r ../scripts ./scripts

# Copier sync_linkedin_stats.py dans scripts/ pour le cloud job
cp ../sync_linkedin_stats.py ./scripts/sync_linkedin_stats.py

echo "✅ Fichiers préparés avec succès!"
echo ""
echo "Fichiers copiés:"
echo "  - config_epbs.yaml"
echo "  - config_loader.py"
echo "  - account-key.json"
echo "  - scripts/ (depuis ../scripts/)"
echo "  - scripts/sync_linkedin_stats.py"
