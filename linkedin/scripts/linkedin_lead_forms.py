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
                 project_id: Optional[str] = None, dataset_id: str = "linkedin_ads_advertising",
                 credentials_path: Optional[str] = None):
        """
        Initialise le client avec le token d'accès

        Args:
            access_token: Token OAuth 2.0 LinkedIn avec les permissions lead sync
            organization_id: ID de l'organisation LinkedIn (optionnel)
            project_id: ID du projet Google Cloud (optionnel, utilise GOOGLE_CLOUD_PROJECT si non fourni)
            dataset_id: ID du dataset BigQuery (défaut: linkedin_ads_advertising)
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

    def get_lead_forms(self, organization_id: Optional[str] = None,
                       count: int = 100, start: int = 0) -> List[Dict]:
        """
        Récupère la liste des formulaires de leads pour une organisation

        Args:
            organization_id: ID de l'organisation (optionnel, utilise self.organization_id par défaut)
            count: Nombre de résultats par page (max 100)
            start: Index de départ pour la pagination

        Returns:
            list: Liste des formulaires de leads
        """
        org_id = organization_id or self.organization_id

        if not org_id:
            raise ValueError("organization_id est requis. Passez-le en paramètre ou lors de l'initialisation.")

        # Construire l'URN de l'organisation
        org_urn = f"urn:li:organization:{org_id}"
        org_urn_encoded = org_urn.replace(':', '%3A')

        # Construire l'URL avec le query string manuellement (comme pour analytics)
        url = f"{self.base_url}/leadForms"
        query_string = f"q=owner&owner=(organization:{org_urn_encoded})&count={count}&start={start}"
        full_url = f"{url}?{query_string}"

        response = requests.get(
            full_url,
            headers=self._get_headers()
        )

        if response.status_code != 200:
            print(f"Erreur API: {response.status_code}")
            print(f"URL: {response.url}")
            print(f"Réponse: {response.text}")
            response.raise_for_status()

        data = response.json()
        return data.get("elements", [])

    def get_lead_form_responses(self, lead_form_id: str,
                                start_date: Optional[datetime] = None,
                                end_date: Optional[datetime] = None,
                                count: int = 100, start: int = 0) -> List[Dict]:
        """
        Récupère les réponses pour un formulaire de lead donné

        Args:
            lead_form_id: ID du formulaire de lead
            start_date: Date de début pour filtrer les réponses (optionnel)
            end_date: Date de fin pour filtrer les réponses (optionnel)
            count: Nombre de résultats par page (max 100)
            start: Index de départ pour la pagination

        Returns:
            list: Liste des réponses au formulaire
        """
        # Construire l'URN du formulaire
        lead_form_urn = f"urn:li:leadGenForm:{lead_form_id}"
        lead_form_urn_encoded = lead_form_urn.replace(':', '%3A')

        url = f"{self.base_url}/leadFormResponses"
        params = {
            "q": "leadForm",
            "leadForm": lead_form_urn_encoded,
            "count": count,
            "start": start
        }

        response = requests.get(
            url,
            headers=self._get_headers(),
            params=params
        )

        if response.status_code != 200:
            print(f"⚠️  Erreur lors de la récupération des réponses pour {lead_form_id}: {response.status_code}")
            return []

        data = response.json()
        responses = data.get("elements", [])

        # Filtrer par date si spécifié
        if start_date or end_date:
            filtered_responses = []
            for response in responses:
                submitted_at = response.get("submittedAt")
                if submitted_at:
                    submitted_datetime = datetime.fromtimestamp(submitted_at / 1000)
                    if start_date and submitted_datetime < start_date:
                        continue
                    if end_date and submitted_datetime > end_date:
                        continue
                    filtered_responses.append(response)
            return filtered_responses

        return responses

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
            # Extraire l'ID depuis l'URN
            form_id_raw = form.get("id", "")
            if isinstance(form_id_raw, int):
                lead_form_id = str(form_id_raw)
                lead_form_urn = f"urn:li:leadGenForm:{lead_form_id}"
            else:
                lead_form_urn = form_id_raw
                lead_form_id = form_id_raw.split(':')[-1] if form_id_raw else ""

            # Extraire l'organisation
            owner = form.get("owner", "")
            if isinstance(owner, str) and "organization:" in owner:
                organization_urn = owner
                organization_id = owner.split(':')[-1]
            else:
                organization_urn = None
                organization_id = None

            # Informations du formulaire
            name = form.get("name", "")
            locale = form.get("locale", {}).get("language") if isinstance(form.get("locale"), dict) else None
            status = form.get("status")

            # Configuration
            privacy_policy_url = form.get("privacyPolicyUrl")
            custom_disclaimer = form.get("customDisclaimer")
            confirmation_message = form.get("confirmationMessage")

            # Metadata
            created_at = None
            last_modified_at = None
            if form.get("created"):
                created_at = datetime.fromtimestamp(form.get("created") / 1000)
            if form.get("lastModified"):
                last_modified_at = datetime.fromtimestamp(form.get("lastModified") / 1000)

            result = {
                "form_id": lead_form_id,
                "lead_form_urn": lead_form_urn,
                "organization_id": organization_id,
                "ad_account_id": None,  # À récupérer si disponible dans l'API
                "name": name,
                "locale": locale,
                "status": status,
                "lead_type": None,  # À récupérer si disponible dans l'API
                "privacy_policy_url": privacy_policy_url,
                "custom_disclaimer": custom_disclaimer,
                "confirmation_message": confirmation_message,
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
                    question_id = answer.get("questionId", "")
                    answer_details = answer.get("answerDetails", {})
                    answer_value = answer_details.get("textQuestionAnswer", {}).get("answer")

                    # Mapper les questions aux champs (LinkedIn utilise des IDs standards)
                    if "email" in question_id.lower() or (answer_value and "@" in str(answer_value)):
                        email_address = answer_value
                    elif "firstName" in question_id or "first_name" in question_id.lower():
                        first_name = answer_value
                    elif "lastName" in question_id or "last_name" in question_id.lower():
                        last_name = answer_value
                    elif "company" in question_id.lower() or "companyName" in question_id:
                        company_name = answer_value
                    elif "jobTitle" in question_id or "title" in question_id.lower():
                        job_title = answer_value
                    elif "phone" in question_id.lower():
                        phone_number = answer_value
                    elif "country" in question_id.lower():
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

            # Préparer les données pour BigQuery
            df = pd.DataFrame(data)

            # Ajouter retrieved_at si absent
            if 'retrieved_at' not in df.columns:
                df['retrieved_at'] = datetime.now()

            # Convertir les colonnes timestamp
            timestamp_columns = ['created_at', 'last_modified_at', 'submitted_at']
            for col in timestamp_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')

            # Construire le nom complet de la table
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            # Configuration du job
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED",
                autodetect=False
            )

            # Upload vers BigQuery
            print(f"\n→ Upload vers BigQuery: {table_id}")
            print(f"  Nombre de lignes: {len(df)}")

            job = client.load_table_from_dataframe(
                df,
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

    # Configuration
    ACCESS_TOKEN = "AQWzcqB3Ax4ZPIIcaTW5fDylKuVXIgnb3HbO_oCRGsLbfgGfc5LyAs5BdhuwUv7yWD0AKm_HYYphQi0Aec5epLuISR1QcykiyC4UX3PKi4kpYN6AKfNlZ0U4gBCctsRknr_uSHt8u2LYySydWhThF-k3O6HtzQKCi072WB-TkxaaAbMBSgLfIGcbBVhEkAXAFnZTr5lUUqmmJvvcuUuImZfqWVK4tX-1cHHSkpenmNmq_43m0QZqQ_1IRpmdfzJYKE11PKHUgkQUacrYEAGsDJXe1ClHiw9UegDFvsBQ-JIFE0VWeI5yl7D5uE3SxQrUjbrpOQOzVVQvdGsZ3j0bJi-6zddakw"
    ORGANIZATION_ID = "5509810"  # ID de l'organisation LinkedIn

    # Configuration BigQuery
    PROJECT_ID = "clean-avatar-466709-a0"
    DATASET_ID = "linkedin_ads_advertising"
    CREDENTIALS_PATH = "./.key.json"

    print("=" * 70)
    print("LINKEDIN LEAD FORMS & RESPONSES")
    print("=" * 70)
    print(f"\nOrganisation: {ORGANIZATION_ID}")
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
    print("=" * 70)
    print("1. Récupération des formulaires de leads")
    print("=" * 70)

    try:
        lead_forms = client.get_lead_forms()
        print(f"\n✓ {len(lead_forms)} formulaire(s) trouvé(s)\n")

        if not lead_forms:
            print("Aucun formulaire de lead trouvé.")
            return

        # Extraire les données
        forms_data = client.extract_lead_form_data(lead_forms)

        # Afficher un résumé
        print("Formulaires de leads:")
        print("-" * 70)
        for form in forms_data[:5]:
            print(f"  - {form['name']} (ID: {form['lead_form_id']}, Status: {form['status']})")

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
            lead_form_id = form['lead_form_id']
            form_name = form['name']

            print(f"\n→ Récupération des réponses pour '{form_name}'...")

            responses = client.get_lead_form_responses(
                lead_form_id=lead_form_id,
                start_date=start_date,
                end_date=end_date
            )

            if responses:
                responses_data = client.extract_lead_response_data(responses, lead_form_id)
                all_responses_data.extend(responses_data)
                print(f"✓ {len(responses_data)} réponse(s) trouvée(s)")
            else:
                print(f"  Aucune réponse trouvée")

        print(f"\n✓ Total: {len(all_responses_data)} réponse(s) récupérée(s)\n")

        if all_responses_data:
            # Afficher un résumé
            print("Résumé des réponses:")
            print("-" * 70)
            unique_emails = len(set(r['email'] for r in all_responses_data if r['email']))
            unique_companies = len(set(r['company'] for r in all_responses_data if r['company']))
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
