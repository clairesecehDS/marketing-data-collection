# ❌ Erreur : Access Denied BigQuery

## Problème
```
403 POST: User does not have bigquery.jobs.create permission in project clean-avatar-466709-a0
```

## Solution : Ajouter les permissions au Service Account

### Option 1 : Via Console GCP (Recommandé)

1. **Allez dans IAM & Admin** :
   - https://console.cloud.google.com/iam-admin/iam?project=clean-avatar-466709-a0

2. **Trouvez votre Service Account** :
   - Cherchez l'email du service account (format: `xxx@clean-avatar-466709-a0.iam.gserviceaccount.com`)

3. **Modifier les permissions** :
   - Cliquez sur l'icône "crayon" (✏️) à droite
   - Cliquez sur "ADD ANOTHER ROLE"
   - Ajoutez ces rôles :
     - ✅ **BigQuery Data Editor** (`roles/bigquery.dataEditor`)
     - ✅ **BigQuery Job User** (`roles/bigquery.jobUser`)

4. **Sauvegarder** et réessayer le script

### Option 2 : Via gcloud CLI

```bash
# Remplacez SERVICE_ACCOUNT_EMAIL par l'email de votre service account
export PROJECT_ID="clean-avatar-466709-a0"
export SERVICE_ACCOUNT_EMAIL="votre-sa@clean-avatar-466709-a0.iam.gserviceaccount.com"

# Ajouter les rôles
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
    --role="roles/bigquery.dataEditor"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
    --role="roles/bigquery.jobUser"
```

### Option 3 : Créer un nouveau Service Account avec les bonnes permissions

1. **Console GCP** → IAM & Admin → Service Accounts
2. **Create Service Account**
3. **Nom** : `linkedin-ads-to-bigquery`
4. **Grant Access** :
   - Ajouter : `BigQuery Data Editor`
   - Ajouter : `BigQuery Job User`
5. **Done** → Créer une clé JSON
6. **Télécharger la clé** et mettre le chemin dans le script Python

---

## Vérifier que ça fonctionne

Après avoir ajouté les permissions, relancez :

```bash
python linkedin_ads_library.py
```

Si vous voyez :
```
✅ Données envoyées avec succès!
```
C'est bon ! ✨
