#!/bin/bash

# Script pour préparer les fichiers nécessaires au déploiement du Cloud Job

set -e

echo "📋 Préparation des fichiers pour le déploiement..."

# Copier les fichiers depuis le répertoire parent
cp ../config_sos.yaml ./config_sos.yaml
cp ../config_loader.py ./config_loader.py
cp ../sos-linkedin-ads-library-key.json ./sos-linkedin-ads-library-key.json

# Copier le script depuis la source principale
mkdir -p ./scripts
cp ../scripts/linkedin_ads_library.py ./scripts/linkedin_ads_library.py

echo "✅ Fichiers préparés avec succès!"
echo ""
echo "Fichiers copiés:"
echo "  - config_sos.yaml"
echo "  - config_loader.py"
echo "  - sos-linkedin-ads-library-key.json"
echo "  - scripts/linkedin_ads_library.py (depuis ../scripts/)"
