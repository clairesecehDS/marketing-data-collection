# Cloud Run Job — LinkedIn Ads Library SOS (hebdomadaire)

Job Cloud Run qui collecte les publicités LinkedIn des **concurrents d'International SOS** (`international-sos-479209`) via l'Ads Library, avec un refresh complet chaque semaine.

## Ce que fait ce job

Recherche dans l'Ads Library LinkedIn les publicités actives pour chaque annonceur configuré dans `config.yaml` (section `linkedin.ads_library.advertisers`).

**Annonceurs surveillés :**
- Crisis24, Global Guardian, AlertMedia, Everbridge
- Global Rescue, Restrata, International SOS, Control Risks

**Dataset BigQuery :** `international-sos-479209.linkedin_ads_library.ads_library`

**Mode upload :** `WRITE_TRUNCATE` — les données sont remplacées entièrement à chaque run (pas d'accumulation de doublons).

**Planification :** tous les lundis à 1h du matin (Europe/Paris)

---

## Déploiement

### Prérequis

- `gcloud` CLI installé et configuré
- Accès au projet GCP `international-sos-479209`
- Fichier `config_sos.yaml` à jour avec un token LinkedIn valide
- Fichier `sos-linkedin-ads-library-key.json` (service account GCP)

### Commandes

```bash
cd linkedin/cloud_job_sos_ads_library
./prepare_deploy.sh   # Copie les scripts et la config dans ce dossier
./deploy.sh           # Build Docker, push image, configure Cloud Run + Scheduler
```

`prepare_deploy.sh` copie depuis le dossier parent :
- `../config_sos.yaml` → `config_sos.yaml` (copié dans l'image sous `config.yaml`)
- `../scripts/linkedin_ads_library.py` → `scripts/linkedin_ads_library.py`
- `../config_loader.py` → `config_loader.py`
- `../sos-linkedin-ads-library-key.json` → `sos-linkedin-ads-library-key.json`

### Tester manuellement sans attendre le scheduler

```bash
gcloud run jobs execute linkedin-ads-library-sos \
    --region=europe-west1 \
    --project=international-sos-479209
```

### Déclencher le scheduler manuellement

```bash
gcloud scheduler jobs run linkedin-ads-library-sos-weekly \
    --location=europe-west1 \
    --project=international-sos-479209
```

---

## Renouveler le token LinkedIn

Le token LinkedIn expire environ tous les 60 jours. Quand le job retourne des erreurs `401 EXPIRED_ACCESS_TOKEN` :

1. Générer un nouveau token sur [LinkedIn Developer Portal](https://www.linkedin.com/developers/tools/oauth/token-generator)
2. Mettre à jour `access_token` dans `../config_sos.yaml`
3. Redéployer :

```bash
./prepare_deploy.sh && ./deploy.sh
```

> Le token est baked dans l'image Docker. Un redéploiement est nécessaire à chaque renouvellement.

---

## Ajouter ou retirer un annonceur

Modifier la liste dans `../config_sos.yaml` :

```yaml
linkedin:
  ads_library:
    advertisers:
      - "Crisis24"
      - "Global Guardian"
      # Ajouter ou retirer ici
```

Puis redéployer : `./prepare_deploy.sh && ./deploy.sh`

---

## Note sur les stats nulles (normal)

Certaines publicités (AlertMedia, Global Guardian) n'ont **pas** de `first_impression_date` ni de `total_impressions`. C'est une limitation côté LinkedIn : les stats ne sont affichées que lorsque l'audience est suffisamment large pour respecter la vie privée. Ce n'est pas un bug.

---

## Voir les logs

```bash
gcloud logging read \
    "resource.type=cloud_run_job AND resource.labels.job_name=linkedin-ads-library-sos" \
    --limit=50 \
    --project=international-sos-479209

gcloud run jobs executions list \
    --job=linkedin-ads-library-sos \
    --region=europe-west1 \
    --project=international-sos-479209
```

---

## Structure des fichiers

```
cloud_job_sos_ads_library/
├── Dockerfile                      # Image Python
├── main.py                         # Point d'entrée
├── linkedin_ads_library_wrapper.py # Wrapper pour compatibilité locale
├── cloudbuild.yaml                 # Config Cloud Build
├── deploy.sh                       # Déploiement complet
├── prepare_deploy.sh               # Copie les sources depuis le dossier parent
├── scheduler_config.yaml           # Config du scheduler (cron, timezone, retries)
├── requirements.txt                # Dépendances Python
├── config_loader.py                # (copié par prepare_deploy.sh)
├── config.example.yaml             # Exemple de config avec placeholders
│
│   -- Générés par prepare_deploy.sh, non commités --
├── config_sos.yaml                 # Config réelle avec le token LinkedIn
├── sos-linkedin-ads-library-key.json  # Clé service account GCP
└── scripts/                        # (copié par prepare_deploy.sh)
```
