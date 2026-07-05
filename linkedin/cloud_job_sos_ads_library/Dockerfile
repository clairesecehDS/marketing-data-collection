# Utiliser l'image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier la configuration SOS comme config.yaml par défaut
COPY config_sos.yaml ./config.yaml

# Copier le config_loader
COPY config_loader.py .

# Copier le point d'entrée
COPY main.py .

# Copier le dossier scripts
COPY scripts/ ./scripts/

# Copier la clé de service account (pour l'authentification BigQuery)
COPY sos-linkedin-ads-library-key.json ./account-key.json

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/account-key.json
ENV CLOUD_RUN_JOB=true

# Commande de démarrage
CMD ["python", "main.py"]
