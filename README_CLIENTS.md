# Guide de préparation des accès et informations

Ce document vous aide à rassembler les accès et informations nécessaires pour que nous puissions connecter vos outils marketing. Nous vous recommandons de lire l'ensemble du guide avant de commencer et de prévoir des captures d'écran en cas de doute.

## 1. Microsoft Clarity

### Informations à transmettre
- `project_id` (identifiant unique du projet)
- Clé API Clarity (clé de type `CLARITY-XXXX`)

### Étapes pour trouver le `project_id`
1. Connectez-vous à https://clarity.microsoft.com/
2. Sélectionnez le site concerné dans la liste de vos projets.
3. Dans le menu latéral, cliquez sur **Settings**.
4. Sous **Setup** ou **Project Info**, repérez le bloc **Project ID**.
5. Copiez l'identifiant tel qu'il apparaît (exemple : `abcdef12-3456-7890-abcd-ef1234567890`).

![alt text](image-1.png)


### Étapes pour générer une clé API
1. Depuis la page **Settings** du projet sélectionné, ouvrez l'onglet **API Access** (ou **API Keys** selon la version de l'interface).
2. Cliquez sur **Generate new key**.
3. Donnez un nom explicite à la clé (ex. `Partage agence <mois/année>`).
4. Validez puis copiez immédiatement la clé créée (elle n'est affichée qu'une seule fois).
5. Transmettez la clé.

![alt text](image.png)

## 2. Google Search Console

### Informations à transmettre
- URL exacte de la propriété (ex. `https://www.votresite.com/`)
- `property_id` (ex. `sc-domain:votresite.com`)
- Confirmation que l'adresse e-mail fournie dispose des droits **Owner** ou **Full**

### Étapes pour récupérer le `property_id`
1. Connectez-vous à https://search.google.com/search-console/
2. Sélectionnez la propriété concernée dans la liste déroulante en haut à gauche.
3. Cliquez sur la propriété pour l'ouvrir : l'URL du navigateur contient `resource_id=...`.
4. Copiez la valeur après `resource_id=` puis remplacez les codes `%3A` par `:` (ex. `sc-domain%3Avotresite.com` devient `sc-domain:votresite.com`).
5. En cas de doute, ouvrez le sélecteur de propriétés et survolez l'entrée : un tooltip affiche l'identifiant complet.

### Accorder l'accès à notre équipe
1. Toujours dans **Paramètres de la propriété**, ouvrez **Utilisateurs et autorisations**.
2. Cliquez sur **Ajouter un utilisateur**.
3. Renseignez l'adresse e-mail fournie par notre équipe.
4. Sélectionnez le rôle **Full**.
5. Validez.

![alt text](image-2.png)
![alt text](image-3.png)

## 3. Google Analytics (GA4 recommandé)

### Informations à transmettre
- Nom de la propriété et de l'application/sites associés
- `property_id` (numérique, ex. `123456789`)
- `measurement_id` par flux de données (ex. `G-ABCDE12345`)
- Accès accordé à notre adresse e-mail avec le rôle **Editor** (ou supérieur)

### Étapes pour récupérer les identifiants
1. Connectez-vous à https://analytics.google.com/
2. Sélectionnez la bonne propriété via le sélecteur en haut de l'interface.
3. Cliquez sur **Admin** (icône engrenage en bas à gauche).
4. Sous la colonne **Property**, choisissez **Property details** pour le `property_id`.
5. Dans **Data collection and modification > Data Streams**, ouvrez chaque flux et copiez le `measurement_id` correspondant.

![alt text](image-4.png)
![alt text](image-6.png)
![alt text](image-7.png)

### Accorder l'accès à notre équipe
1. Depuis la section **Admin**, sous la colonne **Property**, ouvrez **Access Management**.
2. Cliquez sur **+** puis **Add users**.
3. Entrez l'adresse e-mail fournie par notre équipe.
4. Cochez au minimum le rôle **Editor**.
5. Validez.
![alt text](image-5.png)


## Checklist avant envoi
- [ ] Microsoft Clarity : `project_id` + clé API
- [ ] Google Search Console : propriété partagée + `property_id`
- [ ] Google Analytics : accès accordé + `property_id` + `measurement_id`

