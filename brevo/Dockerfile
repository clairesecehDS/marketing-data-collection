# Dockerfile pour Cloud Run Job - Brevo Data Sync
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers nécessaires
COPY sync_brevo_data.py .
COPY config.yaml .
COPY scripts/ scripts/
COPY sql/ sql/

# Copier les credentials GCP (sera monté comme secret dans Cloud Run)
# Note: Le fichier account-key.json sera fourni via Secret Manager ou variable d'environnement

# Définir les variables d'environnement par défaut
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials/account-key.json

# Script d'entrée qui sera exécuté par Cloud Run Job
ENTRYPOINT ["python", "sync_brevo_data.py"]

# Arguments par défaut (synchronisation complète)
CMD ["--days", "7", "--report-days", "30"]
