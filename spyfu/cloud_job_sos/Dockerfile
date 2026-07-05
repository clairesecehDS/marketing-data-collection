# Dockerfile pour Cloud Run Jobs - SpyFu SOS Collection
FROM python:3.11-slim

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements depuis la racine du contexte
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le config_loader depuis cloud_job_sos
COPY cloud_job_sos/config_loader.py /app/

# Copier tous les scripts et configs SpyFu
COPY scripts/ /app/spyfu/scripts/
COPY sql/ /app/spyfu/sql/

# Copier le fichier de configuration SOS uniquement
COPY cloud_job_sos/config_sos.yaml /app/spyfu/

# Créer le répertoire data
RUN mkdir -p /app/spyfu/data

# Copier le script d'entrée
COPY cloud_job_sos/entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Définir le répertoire de travail
WORKDIR /app/spyfu

# Point d'entrée
ENTRYPOINT ["/app/entrypoint.sh"]
