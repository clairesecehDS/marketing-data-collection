import requests
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import json
import pandas as pd
from google.cloud import bigquery
import os


class LinkedInLeadFormsClient:
    """
    Client pour récupérer les formulaires de génération de leads LinkedIn et leurs réponses
    Documentation: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/lead-sync
    """

    def __init__(self, access_token: str, organization_id: Optional[str] = None,
                 project_id: Optional[str] = None, dataset_id: str = "linkedin_leadgen_form",
                 credentials_path: Optional[str] = None):
        """
        Initialise le client avec le token d'accès

        Args:
            access_token: Token OAuth 2.0 LinkedIn avec les permissions lead sync
            organization_id: ID de l'organisation LinkedIn (optionnel)
            project_id: ID du projet Google Cloud (optionnel, utilise GOOGLE_CLOUD_PROJECT si non fourni)
            dataset_id: ID du dataset BigQuery (défaut: linkedin_leadgen_form)
            credentials_path: Chemin vers le fichier JSON des credentials GCP (optionnel)
        """
        self.access_token = access_token
        self.organization_id = organization_id
        self.base_url = "https://api.linkedin.com/rest"

        # Configuration BigQuery
        self.project_id = project_id or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.dataset_id = dataset_id
        self.credentials_path = credentials_path
        self.bq_client = None

    def _get_headers(self) -> Dict[str, str]:
        """Retourne les headers requis pour l'API LinkedIn Marketing"""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "LinkedIn-Version": "202509",
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json"
        }

    def get_ad_accounts(self) -> List[Dict]:
        """
        Récupère la liste des ad accounts accessibles
        Utile pour identifier l'ad account à utiliser pour les Lead Forms
        
        Returns:
            list: Liste des ad accounts
        """
        url = f"{self.base_url}/adAccounts"
        params = {
            "q": "search",
            "count": 100
        }
        
        print("\n→ Récupération des Ad Accounts...")
        
        response = requests.get(url, headers=self._get_headers(), params=params)
        
        if response.status_code == 200:
            data = response.json()
            elements = data.get("elements", [])
            print(f"✓ {len(elements)} ad account(s) trouvé(s)")
            
            for account in elements:
                account_id = account.get("id")
                account_name = account.get("name", "N/A")
                account_status = account.get("status", "N/A")
                print(f"  - {account_name} (ID: {account_id}, Status: {account_status})")
            
            return elements
        else:
            print(f"✗ Erreur {response.status_code}: {response.text}")
            return []

    def check_token_info(self) -> Dict:
        """
        Vérifie les informations du token d'accès (pour debug)
        
        Returns:
            dict: Informations sur le token
        """
        url = "https://api.linkedin.com/v2/userinfo"
        
        print("\n→ Vérification du token d'accès...")
        
        response = requests.get(url, headers={
            "Authorization": f"Bearer {self.access_token}"
        })
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Token valide - User: {data.get('name', 'N/A')}")
            return data
        else:
            print(f"✗ Erreur {response.status_code}: {response.text}")
            return {}

    def get_lead_forms(self, account_id: str,
                       count: int = 100, start: int = 0) -> List[Dict]:
        """
        Récupère la liste des formulaires de leads pour un ad account

        Args:
            account_id: ID du compte publicitaire LinkedIn (requis)
            count: Nombre de résultats par page (max 100)
            start: Index de départ pour la pagination

        Returns:
            list: Liste des formulaires de leads
        """
        if not account_id:
            raise ValueError("account_id est requis pour récupérer les Lead Forms")
        
        # Construire l'URN du compte publicitaire
        account_urn = f"urn:li:sponsoredAccount:{account_id}"
        account_urn_encoded = account_urn.replace(':', '%3A')
        
        url = f"{self.base_url}/leadForms"
        # Format: q=owner&owner=(sponsoredAccount:URN)
        query_string = f"q=owner&owner=(sponsoredAccount:{account_urn_encoded})&count={count}&start={start}"
        full_url = f"{url}?{query_string}"
        
        print(f"\n→ Récupération des Lead Forms...")
        print(f"   Account ID: {account_id}")
        print(f"   URL: {full_url}")
        
        response = requests.get(full_url, headers=self._get_headers())
        
        if response.status_code != 200:
            print(f"✗ Erreur API: {response.status_code}")
            print(f"  Réponse: {response.text}")
            response.raise_for_status()
        
        data = response.json()
        elements = data.get("elements", [])
        
        print(f"✓ {len(elements)} formulaire(s) trouvé(s)")
        
        return elements

    def get_lead_form_responses(self, account_id: str, lead_form_id: Optional[str] = None,
                                start_date: Optional[datetime] = None,
                                end_date: Optional[datetime] = None,
                                count: int = 100, start: int = 0) -> List[Dict]:
        """
        Récupère les réponses pour un ad account (et optionnellement un formulaire spécifique)
        Gère automatiquement la pagination pour récupérer toutes les réponses

        Args:
            account_id: ID du compte publicitaire (requis)
            lead_form_id: ID du formulaire de lead (optionnel, pour filtrer sur un formulaire)
            start_date: Date de début pour filtrer les réponses (optionnel, filtre côté client)
            end_date: Date de fin pour filtrer les réponses (optionnel, filtre côté client)
            count: Nombre de résultats par page (max 100)
            start: Index de départ pour la pagination

        Returns:
            list: Liste des réponses au formulaire
        """
        # Construire l'URN du compte
        account_urn = f"urn:li:sponsoredAccount:{account_id}"
        account_urn_encoded = account_urn.replace(':', '%3A')

        url = f"{self.base_url}/leadFormResponses"
        
        all_responses = []
        current_start = start
        
        # Pagination pour récupérer toutes les réponses
        while True:
            # Construire les paramètres selon la doc LinkedIn
            # Format: q=owner&owner=(sponsoredAccount:URN)&leadType=(leadType:SPONSORED)
            params_str = f"q=owner&owner=(sponsoredAccount:{account_urn_encoded})&leadType=(leadType:SPONSORED)&count={count}&start={current_start}"
            
            # Ajouter le filtre sur le formulaire si spécifié
            if lead_form_id:
                versioned_form_urn = f"urn:li:versionedLeadGenForm:(urn:li:leadGenForm:{lead_form_id},1)"
                versioned_form_urn_encoded = versioned_form_urn.replace(':', '%3A').replace('(', '%28').replace(')', '%29').replace(',', '%2C')
                params_str += f"&versionedLeadGenFormUrn={versioned_form_urn_encoded}"
            
            full_url = f"{url}?{params_str}"

            response = requests.get(full_url, headers=self._get_headers())

            if response.status_code != 200:
                print(f"  ⚠️  Erreur {response.status_code} pour l'ad account {account_id}")
                if lead_form_id:
                    print(f"      Formulaire: {lead_form_id}")
                print(f"      Réponse: {response.text}")
                break

            data = response.json()
            elements = data.get("elements", [])
            
            if not elements:
                # Plus de résultats
                break
            
            all_responses.extend(elements)
            
            # Vérifier s'il y a plus de résultats
            paging = data.get("paging", {})
            total = paging.get("total", 0)
            
            # Si on a récupéré moins que count, c'est la dernière page
            if len(elements) < count:
                break
            
            # Si on a atteint le total, on arrête
            if total > 0 and len(all_responses) >= total:
                break
            
            # Passer à la page suivante
            current_start += count
        
        # Filtrer par date côté client si spécifié
        if start_date or end_date:
            filtered_responses = []
            for resp in all_responses:
                submitted_at = resp.get("submittedAt")
                if submitted_at:
                    submitted_datetime = datetime.fromtimestamp(submitted_at / 1000)
                    if start_date and submitted_datetime < start_date:
                        continue
                    if end_date and submitted_datetime > end_date:
                        continue
                    filtered_responses.append(resp)
            return filtered_responses

        return all_responses

    def extract_lead_form_data(self, lead_forms: List[Dict]) -> List[Dict]:
        """
        Extrait et formate les données des formulaires de leads

        Args:
            lead_forms: Liste des formulaires bruts de l'API

        Returns:
            list: Liste de dictionnaires avec les données formatées
        """
        results = []

        for form in lead_forms:
            # Extraire l'ID depuis l'URN ou directement
            form_id_raw = form.get("id", "")
            if isinstance(form_id_raw, int):
                form_id = str(form_id_raw)
            else:
                form_id = str(form_id_raw)

            # Extraire owner (sponsoredAccount ou organization)
            owner = form.get("owner", {})
            ad_account_id = None
            organization_id = None
            
            if isinstance(owner, dict):
                # Cas sponsoredAccount
                if "sponsoredAccount" in owner:
                    ad_account_urn = owner.get("sponsoredAccount", "")
                    if isinstance(ad_account_urn, str) and ":" in ad_account_urn:
                        ad_account_id = ad_account_urn.split(':')[-1]
                    else:
                        ad_account_id = str(ad_account_urn)
                
                # Cas organization
                if "organization" in owner:
                    org_urn = owner.get("organization", "")
                    if isinstance(org_urn, str) and ":" in org_urn:
                        organization_id = org_urn.split(':')[-1]
                    else:
                        organization_id = str(org_urn)

            # Informations du formulaire
            name = form.get("name", "")
            state = form.get("state", "")
            
            # Locale
            locale = None
            creation_locale = form.get("creationLocale", {})
            if isinstance(creation_locale, dict):
                language = creation_locale.get("language", "")
                country = creation_locale.get("country", "")
                locale = f"{language}_{country}" if language and country else language

            # Content du formulaire
            content = form.get("content", {})
            privacy_policy_url = None
            if isinstance(content, dict):
                legal_info = content.get("legalInfo", {})
                if isinstance(legal_info, dict):
                    privacy_policy_url = legal_info.get("privacyPolicyUrl")

            # Metadata
            created_at = None
            last_modified_at = None
            if form.get("created"):
                created_at = datetime.fromtimestamp(form.get("created") / 1000)
            if form.get("lastModified"):
                last_modified_at = datetime.fromtimestamp(form.get("lastModified") / 1000)

            result = {
                "form_id": form_id,
                "organization_id": organization_id,
                "ad_account_id": ad_account_id,
                "name": name,
                "locale": locale,
                "status": state,
                "privacy_policy_url": privacy_policy_url,
                "created_at": created_at,
                "last_modified_at": last_modified_at,
            }

            results.append(result)

        return results

    def extract_lead_response_data(self, responses: List[Dict], lead_form_id: str) -> List[Dict]:
        """
        Extrait et formate les données des réponses aux formulaires

        Args:
            responses: Liste des réponses brutes de l'API
            lead_form_id: ID du formulaire associé

        Returns:
            list: Liste de dictionnaires avec les données formatées
        """
        results = []

        for response in responses:
            # Extraire l'ID de la réponse
            response_id_raw = response.get("id", "")
            if isinstance(response_id_raw, int):
                response_id = str(response_id_raw)
            else:
                response_id = response_id_raw.split(':')[-1] if response_id_raw else ""

            # Date de soumission
            submitted_at = None
            if response.get("submittedAt"):
                submitted_at = datetime.fromtimestamp(response.get("submittedAt") / 1000)

            # Member ID
            member_id = None
            if response.get("member"):
                member_urn = response.get("member")
                member_id = member_urn.split(':')[-1] if isinstance(member_urn, str) else None

            # Campaign et Creative
            campaign_id = None
            campaign_urn = None
            creative_id = None
            creative_urn = None

            if response.get("associatedEntityUrn"):
                entity_urn = response.get("associatedEntityUrn")
                if "sponsoredCampaign" in entity_urn:
                    campaign_urn = entity_urn
                    campaign_id = entity_urn.split(':')[-1]
                elif "sponsoredCreative" in entity_urn:
                    creative_urn = entity_urn
                    creative_id = entity_urn.split(':')[-1]

            # Données du formulaire (réponses aux questions)
            form_data = response.get("formResponse", {})
            form_data_json = json.dumps(form_data) if form_data else None

            # Extraire les champs communs
            email_address = None
            first_name = None
            last_name = None
            company_name = None
            job_title = None
            phone_number = None
            country = None
            consent_granted = None
            custom_fields = {}

            # Parcourir les réponses pour extraire les champs standards
            if form_data and "answers" in form_data:
                for answer in form_data.get("answers", []):
                    question_id_raw = answer.get("questionId", "")
                    question_id = str(question_id_raw) if question_id_raw else ""
                    answer_details = answer.get("answerDetails", {})
                    answer_value = answer_details.get("textQuestionAnswer", {}).get("answer")

                    # Mapper les questions aux champs (LinkedIn utilise des IDs standards)
                    question_id_lower = question_id.lower()
                    if "email" in question_id_lower or (answer_value and "@" in str(answer_value)):
                        email_address = answer_value
                    elif "firstName" in question_id or "first_name" in question_id_lower:
                        first_name = answer_value
                    elif "lastName" in question_id or "last_name" in question_id_lower:
                        last_name = answer_value
                    elif "company" in question_id_lower or "companyName" in question_id:
                        company_name = answer_value
                    elif "jobTitle" in question_id or "title" in question_id_lower:
                        job_title = answer_value
                    elif "phone" in question_id_lower:
                        phone_number = answer_value
                    elif "country" in question_id_lower:
                        country = answer_value
                    else:
                        # Custom fields
                        custom_fields[question_id] = answer_value

            # Consent (peut être dans un champ spécifique de l'API)
            if response.get("consentResponses"):
                consent_granted = any(c.get("granted", False) for c in response.get("consentResponses", []))

            # Campaign Group ID (si disponible)
            campaign_group_id = None
            if response.get("campaignGroup"):
                campaign_group_urn = response.get("campaignGroup")
                campaign_group_id = campaign_group_urn.split(':')[-1] if isinstance(campaign_group_urn, str) else None

            # Device Type (si disponible)
            device_type = response.get("deviceType")

            # Timing (pour SLA tracking)
            notification_received_at = datetime.now()  # Timestamp actuel = quand on récupère via API
            fetched_at = datetime.now()

            result = {
                "lead_response_id": response_id,
                "form_id": lead_form_id,
                "organization_id": None,  # À enrichir si disponible
                "ad_account_id": None,  # À enrichir si disponible
                "lead_type": None,  # À enrichir si disponible
                "submitted_at": submitted_at,
                "notification_received_at": notification_received_at,
                "fetched_at": fetched_at,
                "first_name": first_name,
                "last_name": last_name,
                "email_address": email_address,
                "phone_number": phone_number,
                "company_name": company_name,
                "job_title": job_title,
                "country": country,
                "campaign_id": campaign_id,
                "campaign_group_id": campaign_group_id,
                "creative_id": creative_id,
                "device_type": device_type,
                "custom_fields": json.dumps(custom_fields) if custom_fields else None,
                "consent_granted": consent_granted,
                "form_data": form_data_json,
            }

            results.append(result)

        return results

    def export_to_csv(self, data: List[Dict], filename: str):
        """Exporte les données au format CSV"""
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"✓ Données exportées: {filename}")

    def export_to_json(self, data: List[Dict], filename: str):
        """Exporte les données au format JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"✓ Données exportées: {filename}")

    def _get_bigquery_client(self) -> bigquery.Client:
        """Initialise et retourne le client BigQuery"""
        if self.bq_client is None:
            if self.credentials_path:
                from google.oauth2 import service_account
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
                self.bq_client = bigquery.Client(
                    credentials=credentials,
                    project=self.project_id or credentials.project_id
                )
            elif self.project_id:
                self.bq_client = bigquery.Client(project=self.project_id)
            else:
                self.bq_client = bigquery.Client()
        return self.bq_client

    def upload_to_bigquery(self, data: List[Dict], table_name: str,
                          write_disposition: str = "WRITE_APPEND") -> None:
        """
        Upload les données vers BigQuery

        Args:
            data: Données à uploader (liste de dictionnaires)
            table_name: Nom de la table (lead_forms ou lead_form_responses)
            write_disposition: Mode d'écriture (WRITE_APPEND, WRITE_TRUNCATE, WRITE_EMPTY)
        """
        if not data:
            print(f"⚠️  Aucune donnée à uploader pour {table_name}")
            return

        try:
            client = self._get_bigquery_client()

            # Construire le nom complet de la table
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            # Fonction pour convertir les datetime en strings ISO
            def convert_datetime(obj):
                if isinstance(obj, datetime):
                    return obj.isoformat()
                elif isinstance(obj, dict):
                    return {k: convert_datetime(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_datetime(item) for item in obj]
                else:
                    return obj

            # Pour les champs JSON, on doit convertir les strings JSON en objets dict
            # avant l'upload pour que BigQuery les reconnaisse comme JSON
            processed_data = []
            for row in data:
                processed_row = {}
                for key, value in row.items():
                    # Convertir les datetime en ISO string
                    if isinstance(value, datetime):
                        processed_row[key] = value.isoformat()
                    # Pour custom_fields et form_data, parser le JSON string en dict
                    elif key in ['custom_fields', 'form_data'] and value is not None:
                        try:
                            # Si c'est déjà une string JSON, la parser
                            if isinstance(value, str):
                                processed_row[key] = json.loads(value)
                            else:
                                processed_row[key] = value
                        except (json.JSONDecodeError, TypeError):
                            processed_row[key] = None
                    else:
                        processed_row[key] = value
                processed_data.append(processed_row)

            # Ajouter retrieved_at si absent
            for row in processed_data:
                if 'retrieved_at' not in row:
                    row['retrieved_at'] = datetime.now().isoformat()

            # Configuration du job
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
                autodetect=False
            )

            # Upload vers BigQuery en utilisant load_table_from_json
            # Cette méthode supporte les types JSON nativement
            print(f"\n→ Upload vers BigQuery: {table_id}")
            print(f"  Nombre de lignes: {len(processed_data)}")

            job = client.load_table_from_json(
                processed_data,
                table_id,
                job_config=job_config
            )

            # Attendre la fin du job
            job.result()

            # Vérifier le résultat
            table = client.get_table(table_id)
            print(f"✓ Upload réussi! Total lignes dans la table: {table.num_rows:,}")

        except Exception as e:
            print(f"✗ Erreur lors de l'upload vers BigQuery: {e}")
            import traceback
            traceback.print_exc()
            raise


def main():
    """
    Exemple d'utilisation du client LinkedIn Lead Forms
    """
    
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
    from config_loader import load_config

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    config = load_config()

    # Récupérer les configurations
    linkedin_config = config.get_linkedin_config()
    google_config = config.get_google_cloud_config()

    # Récupérer l'access token depuis la configuration
    ACCESS_TOKEN = linkedin_config.get('access_token')
    if not ACCESS_TOKEN:
        print("❌ ERREUR: access_token LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'access_token' dans la section linkedin.oauth")
        return
    
    # Récupérer l'organization_id depuis la config
    ORGANIZATION_ID = linkedin_config.get('organization_id')
    if not ORGANIZATION_ID:
        print("❌ ERREUR: organization_id LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'organization_id' dans la section linkedin")
        return
    
    # Récupérer l'account_id depuis la config (requis)
    AD_ACCOUNT_ID = linkedin_config.get('account_id')
    if not AD_ACCOUNT_ID:
        print("❌ ERREUR: account_id LinkedIn non configuré dans config.yaml")
        print("   Veuillez ajouter 'account_id' dans la section linkedin de config.yaml")
        return

    # Configuration BigQuery
    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config['datasets']['linkedin_leadgen_form']
    CREDENTIALS_PATH = google_config['credentials_file']

    print("=" * 70)
    print("LINKEDIN LEAD FORMS & RESPONSES")
    print("=" * 70)
    print(f"\nOrganisation: {ORGANIZATION_ID}")
    print(f"Ad Account: {AD_ACCOUNT_ID}")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}\n")

    # Initialiser le client
    client = LinkedInLeadFormsClient(
        access_token=ACCESS_TOKEN,
        organization_id=ORGANIZATION_ID,
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

    # Étape 1: Récupérer les formulaires de leads
    print("\n" + "=" * 70)
    print("1. Récupération des formulaires de leads")
    print("=" * 70)

    try:
        # Récupérer les formulaires avec l'ad account
        lead_forms = client.get_lead_forms(account_id=AD_ACCOUNT_ID)

        if not lead_forms:
            print("Aucun formulaire de lead trouvé.")
            return

        # Extraire les données
        forms_data = client.extract_lead_form_data(lead_forms)
        
        print(f"\n✓ {len(forms_data)} formulaire(s) extrait(s)\n")

        # Afficher un résumé
        print("Formulaires de leads:")
        print("-" * 70)
        for form in forms_data[:5]:
            print(f"  - {form['name']} (ID: {form['form_id']}, Status: {form['status']})")

        if len(forms_data) > 5:
            print(f"  ... et {len(forms_data) - 5} autres formulaires")
        print()

        # Exporter
        client.export_to_json(forms_data, "lead_forms.json")
        client.export_to_csv(forms_data, "lead_forms.csv")

        # Upload vers BigQuery
        client.upload_to_bigquery(forms_data, "lead_forms")

    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return

    # Étape 2: Récupérer les réponses pour chaque formulaire
    print("\n" + "=" * 70)
    print("2. Récupération des réponses aux formulaires")
    print("=" * 70)

    all_responses_data = []

    try:
        # Période: 1800 derniers jours
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1800)

        print(f"\nPériode: {start_date.date()} à {end_date.date()}\n")

        for form in forms_data:
            form_id = form['form_id']
            form_name = form['name']

            print(f"\n→ Récupération des réponses pour '{form_name}'...")

            responses = client.get_lead_form_responses(
                account_id=AD_ACCOUNT_ID,
                lead_form_id=form_id,
                start_date=start_date,
                end_date=end_date
            )

            if responses:
                responses_data = client.extract_lead_response_data(responses, form_id)
                all_responses_data.extend(responses_data)
                print(f"✓ {len(responses_data)} réponse(s) trouvée(s)")
            else:
                print("  Aucune réponse trouvée")

        print(f"\n✓ Total: {len(all_responses_data)} réponse(s) récupérée(s)\n")

        if all_responses_data:
            # Afficher un résumé
            print("Résumé des réponses:")
            print("-" * 70)
            unique_emails = len(set(r['email_address'] for r in all_responses_data if r.get('email_address')))
            unique_companies = len(set(r['company_name'] for r in all_responses_data if r.get('company_name')))
            print(f"Emails uniques: {unique_emails}")
            print(f"Entreprises uniques: {unique_companies}")

            # Exporter
            client.export_to_json(all_responses_data, "lead_form_responses.json")
            client.export_to_csv(all_responses_data, "lead_form_responses.csv")

            # Upload vers BigQuery
            client.upload_to_bigquery(all_responses_data, "lead_form_responses")

        print("\n" + "=" * 70)
        print("✓ EXTRACTION LEAD FORMS TERMINÉE!")
        print("=" * 70)
        print(f"📊 Fichiers locaux créés:")
        print(f"   - lead_forms.json / .csv")
        if all_responses_data:
            print(f"   - lead_form_responses.json / .csv")
        print(f"☁️  Données uploadées dans BigQuery:")
        print(f"   - {PROJECT_ID}.{DATASET_ID}.lead_forms")
        if all_responses_data:
            print(f"   - {PROJECT_ID}.{DATASET_ID}.lead_form_responses")

    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
