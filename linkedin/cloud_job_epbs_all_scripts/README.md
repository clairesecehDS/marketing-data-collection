# Cloud Run Job — LinkedIn EPBS (hebdomadaire)

Job Cloud Run qui exécute tous les scripts LinkedIn pour le client **École des Ponts** (`ecoledesponts`), déclenché automatiquement chaque lundi.

## Ce que fait ce job

| Script | Dataset BigQuery | Description |
|--------|-----------------|-------------|
| `linkedin_ads_library` | `linkedin_ads_library` | Publicités des concurrents (Ads Library) |
| `linkedin_budget` | `linkedin_ads_advertising` | Budget et paramètres des campagnes |
| `linkedin_campaign_analytics` | `linkedin_ads_advertising` | Performances des campagnes (clics, impressions, coûts) |
| `linkedin_lead_forms` | `linkedin_leadgen_form` | Réponses aux formulaires Lead Gen |
| `linkedin_page_stats` | `linkedin_page` | Statistiques de la page LinkedIn |
| `sync_linkedin_stats` | `linkedin_page` | Followers, page views et content statistics |

**Planification :** tous les lundis à 1h du matin (Europe/Paris)

---

## Déploiement

### Prérequis

- `gcloud` CLI installé et configuré
- Accès au projet GCP `ecoledesponts`
- Fichier `config_epbs.yaml` à jour avec un token LinkedIn valide
- Fichier `account-key.json` (service account GCP)

### Commandes

```bash
cd linkedin/cloud_job_epbs_all_scripts
./prepare_deploy.sh   # Copie les scripts et la config dans ce dossier
./deploy.sh           # Build Docker, push image, configure Cloud Run + Scheduler
```

`prepare_deploy.sh` copie depuis le dossier parent :
- `../config_epbs.yaml` → `config.yaml` (copié dans l'image)
- `../scripts/` → `scripts/` (tous les scripts Python)
- `../sync_linkedin_stats.py` → `scripts/sync_linkedin_stats.py`
- `../config_loader.py` → `config_loader.py`
- `../account-key.json` → `account-key.json`

### Tester manuellement sans attendre le scheduler

```bash
gcloud run jobs execute linkedin-epbs-all-scripts \
    --region=europe-west1 \
    --project=ecoledesponts
```

### Déclencher le scheduler manuellement

```bash
gcloud scheduler jobs run linkedin-epbs-all-weekly \
    --location=europe-west1 \
    --project=ecoledesponts
```

---

## Renouveler le token LinkedIn

Le token LinkedIn expire environ tous les 60 jours. Quand le job commence à retourner des erreurs `401 EXPIRED_ACCESS_TOKEN` :

1. Générer un nouveau token OAuth sur [LinkedIn Developer Portal](https://www.linkedin.com/developers/tools/oauth/token-generator)
2. Mettre à jour `access_token` dans `../config_epbs.yaml`
3. Redéployer :

```bash
./prepare_deploy.sh && ./deploy.sh
```

> Le token est baked dans l'image Docker à chaque déploiement. Un redéploiement est donc nécessaire à chaque renouvellement.

---

## Voir les logs

```bash
# 50 dernières lignes de logs
gcloud logging read \
    "resource.type=cloud_run_job AND resource.labels.job_name=linkedin-epbs-all-scripts" \
    --limit=50 \
    --project=ecoledesponts

# Lister les dernières exécutions
gcloud run jobs executions list \
    --job=linkedin-epbs-all-scripts \
    --region=europe-west1 \
    --project=ecoledesponts
```

---

## Structure des fichiers

```
cloud_job_epbs_all_scripts/
├── Dockerfile              # Image Python avec toutes les dépendances
├── main.py                 # Point d'entrée : orchestre les 6 scripts
├── cloudbuild.yaml         # Config Cloud Build (build + push image)
├── deploy.sh               # Déploiement complet (build + Cloud Run + Scheduler)
├── prepare_deploy.sh       # Copie les sources depuis le dossier parent
├── requirements.txt        # Dépendances Python
├── config_loader.py        # (copié par prepare_deploy.sh)
├── config.example.yaml     # Exemple de config avec placeholders
│
│   -- Générés par prepare_deploy.sh, non commités --
├── config.yaml             # Config réelle avec le token LinkedIn
├── account-key.json        # Clé service account GCP
└── scripts/                # Scripts Python (copies depuis ../scripts/)
```

---

## Exécuter un seul script (debug)

La variable d'environnement `LINKEDIN_SCRIPTS` permet de n'exécuter qu'une partie des scripts :

```bash
gcloud run jobs execute linkedin-epbs-all-scripts \
    --region=europe-west1 \
    --project=ecoledesponts \
    --update-env-vars=LINKEDIN_SCRIPTS=page_stats,sync_stats
```

Valeurs possibles : `ads_library`, `budget`, `campaign_analytics`, `lead_forms`, `page_stats`, `sync_stats`, ou `all` (défaut).
