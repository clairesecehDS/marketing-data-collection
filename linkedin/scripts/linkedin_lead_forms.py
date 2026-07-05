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
            "LinkedIn-Version": "202601",
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

    def get_campaigns_using_forms(self, account_id: str) -> Dict[str, List[str]]:
        """
        Récupère le mapping form_id -> campaign_ids en listant les campagnes
        puis en vérifiant leurs creatives pour les lead forms
        
        Args:
            account_id: ID du compte publicitaire
            
        Returns:
            dict: Mapping {form_id: [campaign_id1, campaign_id2, ...]}
        """
        print(f"\n→ Récupération des campagnes utilisant les lead forms...")
        
        form_to_campaigns = {}
        
        try:
            # Étape 1: Récupérer toutes les campagnes du compte
            campaigns_url = f"{self.base_url}/adAccounts/{account_id}/adCampaigns"
            campaigns = []
            start = 0
            count = 100
            known_total = None

            while True:
                query_params = (
                    f"q=search"
                    f"&search=(status:(values:List(ACTIVE,PAUSED,COMPLETED)))"
                    f"&start={start}&count={count}"
                )
                full_url = f"{campaigns_url}?{query_params}"
                campaigns_response = requests.get(full_url, headers=self._get_headers())

                if campaigns_response.status_code != 200:
                    print(f"⚠️  Erreur lors de la récupération des campagnes: {campaigns_response.status_code}")
                    return form_to_campaigns

                campaigns_data = campaigns_response.json()
                paging = campaigns_data.get("paging", {})
                if known_total is None and "total" in paging:
                    known_total = paging["total"]

                elements = campaigns_data.get("elements", [])
                campaigns.extend(elements)

                if len(elements) < count:
                    break
                start += count
                if known_total is not None and start >= known_total:
                    break
                if len(campaigns) >= 5000:
                    print(f"  ⚠️  Cap de sécurité atteint ({len(campaigns)} campagnes)")
                    break

            print(f"  → {len(campaigns)} campagne(s) trouvée(s)")
            
            if not campaigns:
                print(f"⚠️  Aucune campagne trouvée")
                return form_to_campaigns
            
            # Étape 2: Récupérer tous les creatives avec projection complète
            print(f"  → Récupération des creatives avec détails complets...")
            
            # Utiliser l'endpoint /adCreatives avec projection pour avoir callToAction et variables
            creatives_url = f"{self.base_url}/adCreatives"
            account_urn = f"urn:li:sponsoredAccount:{account_id}"
            account_urn_encoded = account_urn.replace(':', '%3A')
            
            # Requête avec projection des champs nécessaires
            params = {
                "q": "search",
                "search": f"(account:(values:List({account_urn_encoded})))",
                "count": 100
            }
            
            all_creatives = []
            start = 0
            
            while True:
                params["start"] = start
                
                # Construire l'URL manuellement pour éviter les problèmes d'encodage
                query_parts = []
                for key, value in params.items():
                    if key == "start":
                        query_parts.append(f"{key}={value}")
                    elif key == "fields":
                        query_parts.append(f"{key}={value}")
                    elif key == "count":
                        query_parts.append(f"{key}={value}")
                    else:
                        query_parts.append(f"{key}={value}")
                
                full_url = f"{creatives_url}?{'&'.join(query_parts)}"
                
                response = requests.get(full_url, headers=self._get_headers())
                
                if response.status_code == 200:
                    data = response.json()
                    elements = data.get("elements", [])
                    
                    if not elements:
                        break
                    
                    all_creatives.extend(elements)
                    
                    # Vérifier s'il y a plus de résultats
                    paging = data.get("paging", {})
                    if "next" not in paging:
                        break
                    
                    start += len(elements)
                else:
                    print(f"⚠️  Erreur lors de la récupération des creatives: {response.status_code}")
                    if start == 0:  # Première tentative
                        print(f"     URL: {response.url}")
                        print(f"     Réponse: {response.text[:300]}")
                    break
            
            print(f"  → {len(all_creatives)} creative(s) récupérée(s)")
            
            # Analyser les creatives
            for creative in all_creatives:
                # DEBUG: Afficher la structure du premier creative
                if not hasattr(self, '_debug_creative_shown'):
                    print(f"\n  🔍 DEBUG - Structure d'un creative:")
                    print(f"     Keys: {list(creative.keys())}")
                    if "callToAction" in creative:
                        print(f"     callToAction: {creative.get('callToAction')}")
                    if "variables" in creative:
                        variables = creative.get('variables', {})
                        print(f"     variables keys: {list(variables.keys())}")
                    print(f"\n     Full creative sample:")
                    print(json.dumps(creative, indent=2)[:1000])
                    print("...\n")
                    self._debug_creative_shown = True
                
                lead_form_urn = None
                
                # 1. Dans callToAction.target (pour InMails et certains formats)
                call_to_action = creative.get("callToAction", {})
                cta_target = call_to_action.get("target")
                if cta_target and ("adForm:" in str(cta_target) or "leadGenForm:" in str(cta_target)):
                    lead_form_urn = cta_target
                
                # 2. Dans variables.data pour les creatives standard
                if not lead_form_urn:
                    variables = creative.get("variables", {})
                    data_obj = variables.get("data", {})
                    lead_form_urn = data_obj.get("com.linkedin.ads.LeadGenCreativeVariables", {}).get("leadGenFormUrn")
                
                # Extraire le form_id et campaign_id si trouvé
                if lead_form_urn:
                    form_id = None
                    
                    # Format: urn:li:adForm:123456
                    if "adForm:" in str(lead_form_urn):
                        form_id = str(lead_form_urn).split("adForm:")[-1].split(",")[0].split(")")[0]
                    # Format: urn:li:leadGenForm:123456
                    elif "leadGenForm:" in str(lead_form_urn):
                        form_id = str(lead_form_urn).split("leadGenForm:")[-1].split(",")[0].split(")")[0]
                    
                    if form_id:
                        # Récupérer le campaign_id du creative
                        campaign_id_raw = creative.get("campaign")
                        if campaign_id_raw:
                            if isinstance(campaign_id_raw, int):
                                campaign_id = str(campaign_id_raw)
                            else:
                                campaign_id = str(campaign_id_raw).split(":")[-1]
                            
                            if form_id not in form_to_campaigns:
                                form_to_campaigns[form_id] = []
                            if campaign_id not in form_to_campaigns[form_id]:
                                form_to_campaigns[form_id].append(campaign_id)
            
            if form_to_campaigns:
                print(f"✓ Mapping trouvé pour {len(form_to_campaigns)} formulaire(s)")
                for form_id, campaign_ids in form_to_campaigns.items():
                    print(f"  - Form {form_id}: {len(campaign_ids)} campagne(s)")
            else:
                print(f"⚠️  Aucun lead form trouvé dans les creatives")
                
        except Exception as e:
            print(f"⚠️  Erreur lors de la récupération du mapping: {e}")
            import traceback
            traceback.print_exc()
        
        return form_to_campaigns

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

            # Construire le lead_form_urn
            lead_form_urn = f"urn:li:leadGenForm:{form_id}" if form_id else None

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

            # Si organization_id n'est pas dans owner, utiliser celui du client
            if not organization_id and self.organization_id:
                organization_id = self.organization_id

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

            # Metadat
            created_at = None
            last_modified_at = None
            if form.get("created"):
                created_at = datetime.fromtimestamp(form.get("created") / 1000)
            if form.get("lastModified"):
                last_modified_at = datetime.fromtimestamp(form.get("lastModified") / 1000)

            result = {
                "form_id": form_id,
                "lead_form_urn": lead_form_urn,
                "organization_id": organization_id,
                "ad_account_id": ad_account_id,
                "name": name,
                "locale": locale,
                "status": state,
                "lead_type": "SPONSORED",
                "privacy_policy_url": privacy_policy_url,
                "created_at": created_at,
                "last_modified_at": last_modified_at,
            }

            results.append(result)

        return results

    def extract_lead_response_data(self, responses: List[Dict], lead_form_id: str,
                                   ad_account_id: str = None) -> List[Dict]:
        """
        Extrait et formate les données des réponses aux formulaires

        Args:
            responses: Liste des réponses brutes de l'API
            lead_form_id: ID du formulaire associé
            ad_account_id: ID du compte publicitaire (optionnel)

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

            # DEBUG: Log pour vérifier la présence de leadMetadata (uniquement pour la première réponse)
            if not hasattr(self, '_leadmetadata_debug_shown'):
                lead_metadata_present = "leadMetadata" in response
                sponsored_metadata_present = False
                campaign_present = False
                
                if lead_metadata_present:
                    lead_metadata_check = response.get("leadMetadata", {})
                    sponsored_metadata_present = "sponsoredLeadMetadata" in lead_metadata_check
                    if sponsored_metadata_present:
                        sponsored_check = lead_metadata_check.get("sponsoredLeadMetadata", {})
                        campaign_present = "campaign" in sponsored_check
                        campaign_value = sponsored_check.get("campaign")
                
                print(f"\n🔍 DEBUG - Structure leadMetadata (première réponse):")
                print(f"   leadMetadata présent: {lead_metadata_present}")
                if lead_metadata_present:
                    print(f"   leadMetadata.sponsoredLeadMetadata présent: {sponsored_metadata_present}")
                    if sponsored_metadata_present:
                        print(f"   leadMetadata.sponsoredLeadMetadata.campaign présent: {campaign_present}")
                        if campaign_present:
                            print(f"   Valeur: {campaign_value}")
                print(f"   associatedEntityUrn présent: {'associatedEntityUrn' in response}")
                if 'associatedEntityUrn' in response:
                    print(f"   Valeur: {response.get('associatedEntityUrn')}\n")
                self._leadmetadata_debug_shown = True

            # Priorité 1: Récupérer depuis leadMetadata (nouveau format recommandé)
            lead_metadata = response.get("leadMetadata", {})
            if lead_metadata and "sponsoredLeadMetadata" in lead_metadata:
                sponsored_metadata = lead_metadata.get("sponsoredLeadMetadata", {})
                campaign_urn = sponsored_metadata.get("campaign")
                if campaign_urn:
                    campaign_id = campaign_urn.split(':')[-1] if isinstance(campaign_urn, str) else str(campaign_urn)
            
            # Priorité 2: Fallback sur associatedEntityUrn (ancien format)
            if not campaign_id and response.get("associatedEntityUrn"):
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
            # LinkedIn ne fournit PAS de champ 'name' dans les réponses, seulement questionId
            # Il faut donc identifier les champs par leur contenu en 2 passes
            
            # Liste des pays possibles (étendue)
            COUNTRIES = [
                "France", "Poland", "Germany", "Spain", "Italy", "UK", "United Kingdom",
                "USA", "United States", "Canada", "Belgium", "Netherlands", "Switzerland",
                "Portugal", "Austria", "Sweden", "Norway", "Denmark", "Finland", "Ireland",
                "Luxembourg", "Greece", "Czech Republic", "Romania", "Hungary", "Bulgaria",
                "Croatia", "Slovakia", "Slovenia", "Estonia", "Latvia", "Lithuania",
                "Malta", "Cyprus", "Iceland", "Liechtenstein", "Monaco", "Andorra",
                "Russia", "Ukraine", "Belarus", "Turkey", "Israel", "Egypt", "Morocco",
                "Algeria", "Tunisia", "South Africa", "Nigeria", "Kenya", "Ghana",
                "China", "Japan", "South Korea", "India", "Singapore", "Malaysia",
                "Thailand", "Vietnam", "Indonesia", "Philippines", "Australia", "New Zealand",
                "Brazil", "Mexico", "Argentina", "Chile", "Colombia", "Peru", "Venezuela"
            ]
            
            if form_data and "answers" in form_data:
                # Première passe: collecter toutes les réponses et les classifier
                classified_answers = {
                    "email": None,
                    "country": None,
                    "phone": None,
                    "names": [],  # Pour first_name, last_name
                    "other": []   # Pour company, job_title
                }
                
                for answer in form_data.get("answers", []):
                    question_id = answer.get("questionId", "")
                    answer_details = answer.get("answerDetails", {})
                    
                    # Récupérer la valeur de la réponse
                    answer_value = None
                    if "textQuestionAnswer" in answer_details:
                        answer_value = answer_details.get("textQuestionAnswer", {}).get("answer")
                    elif "multipleChoiceAnswer" in answer_details:
                        options = answer_details.get("multipleChoiceAnswer", {}).get("options", [])
                        answer_value = ",".join(map(str, options)) if options else None

                    if not answer_value:
                        continue
                    
                    answer_value_str = str(answer_value).strip()
                    
                    # Classification par type
                    # 1. Email: contient @ et un point
                    if "@" in answer_value_str and "." in answer_value_str:
                        classified_answers["email"] = answer_value_str
                    
                    # 2. Pays: dans la liste des pays
                    elif answer_value_str in COUNTRIES:
                        classified_answers["country"] = answer_value_str
                    
                    # 3. Téléphone: commence par + ou format téléphone
                    elif (answer_value_str.startswith("+") or 
                          (all(c.isdigit() or c in " -.()" for c in answer_value_str) and 
                           len(answer_value_str) >= 8 and
                           sum(c.isdigit() for c in answer_value_str) >= 8)):
                        classified_answers["phone"] = answer_value_str
                    
                    # 4. Noms courts (prénom/nom): 2-50 chars, pas de @ ni chiffres au début
                    elif (len(answer_value_str) >= 2 and len(answer_value_str) <= 50 and 
                          "@" not in answer_value_str and 
                          not any(c.isdigit() for c in answer_value_str[:3]) and
                          # Exclure si ça ressemble à une entreprise (contient certains mots-clés)
                          not any(keyword in answer_value_str.lower() for keyword in 
                                 [" inc", " ltd", " llc", " gmbh", " sarl", " sas", " sa ", "corporation", "company"])):
                        classified_answers["names"].append(answer_value_str)
                    
                    # 5. Autres (company, job_title, etc.)
                    else:
                        classified_answers["other"].append(answer_value_str)
                
                # Deuxième passe: assigner aux bonnes variables
                email_address = classified_answers["email"]
                country = classified_answers["country"]
                phone_number = classified_answers["phone"]
                
                # Noms: premier = first_name, second = last_name
                if len(classified_answers["names"]) >= 1:
                    first_name = classified_answers["names"][0]
                if len(classified_answers["names"]) >= 2:
                    last_name = classified_answers["names"][1]
                
                # Autres champs: premier = company (si long), sinon job_title
                for other_value in classified_answers["other"]:
                    if not company_name and len(other_value) > 5:
                        company_name = other_value
                    elif not job_title:
                        job_title = other_value
                    else:
                        custom_fields[other_value[:20]] = other_value

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
                "organization_id": self.organization_id,  # Depuis le client
                "ad_account_id": ad_account_id,  # Passé en paramètre
                "lead_type": "SPONSORED",  # Type fixe selon l'API LinkedIn
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
                "custom_fields": custom_fields if custom_fields else None,
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

    def check_date_exists(self, table_name: str, date_to_check: datetime) -> bool:
        """Vérifie si des données existent déjà pour cette date dans la table"""
        try:
            client = self._get_bigquery_client()
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            date_str = date_to_check.strftime("%Y-%m-%d")

            # Pour lead_form_responses, on vérifie submitted_at
            if table_name == "lead_form_responses":
                query = f"""
                    SELECT COUNT(*) as count
                    FROM `{table_id}`
                    WHERE DATE(submitted_at) = '{date_str}'
                """
            else:
                # Pour d'autres tables
                query = f"""
                    SELECT COUNT(*) as count
                    FROM `{table_id}`
                    WHERE DATE(retrieved_at) = '{date_str}'
                """

            result = client.query(query).result()
            row = next(iter(result), None)

            if row and row.count > 0:
                print(f"ℹ️  Données existantes pour {date_str} dans {table_name} ({row.count} ligne(s))")
                return True
            return False

        except Exception as e:
            # Table n'existe pas encore ou autre erreur
            print(f"ℹ️  Vérification impossible pour {table_name}: {e}")
            return False

    def get_last_sync_date(self, table_name: str) -> Optional[datetime]:
        """Récupère la dernière date de synchronisation depuis BigQuery"""
        try:
            client = self._get_bigquery_client()
            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            if table_name == "lead_form_responses":
                query = f"""
                    SELECT MAX(DATE(submitted_at)) as last_date
                    FROM `{table_id}`
                """
            else:
                query = f"""
                    SELECT MAX(DATE(retrieved_at)) as last_date
                    FROM `{table_id}`
                """

            result = client.query(query).result()
            row = next(iter(result), None)

            if row and row.last_date:
                print(f"✓ Dernière sync {table_name}: {row.last_date}")
                return row.last_date
            else:
                print(f"ℹ️  Aucune donnée existante dans {table_name}, première synchronisation")
                return None

        except Exception as e:
            print(f"ℹ️  Table {table_name} non trouvée: {e}")
            print("   Première synchronisation")
            return None

    def calculate_lead_form_metrics(self, responses_data: List[Dict], 
                                   campaign_analytics: Optional[List[Dict]] = None,
                                   form_to_campaigns: Optional[Dict[str, List[str]]] = None) -> List[Dict]:
        """
        Calcule les métriques agrégées par form_id, campaign_id et date à partir des réponses
        Enrichit avec les données de campaign analytics si disponibles
        
        Si campaign_id est manquant dans les réponses mais qu'un mapping form_to_campaigns
        est fourni, utilise ce mapping pour retrouver les campagnes associées

        Args:
            responses_data: Liste des réponses de lead forms
            campaign_analytics: Liste optionnelle des analytics de campagne pour enrichissement
            form_to_campaigns: Mapping optionnel {form_id: [campaign_ids]} pour enrichir les données

        Returns:
            list: Liste de métriques agrégées par formulaire, campagne et date
        """
        if not responses_data:
            return []

        # Convertir en DataFrame pour faciliter les calculs
        df = pd.DataFrame(responses_data)
        
        # Créer un DataFrame des analytics si disponible
        analytics_df = None
        if campaign_analytics:
            analytics_df = pd.DataFrame(campaign_analytics)
            if 'date' in analytics_df.columns:
                analytics_df['date'] = pd.to_datetime(analytics_df['date']).dt.date

        # Convertir submitted_at en date si c'est un timestamp
        if 'submitted_at' in df.columns and not df['submitted_at'].isna().all():
            df['date'] = pd.to_datetime(df['submitted_at']).dt.date
        else:
            print("⚠️  Pas de données submitted_at disponibles")
            return []

        # Si le mapping form_to_campaigns est fourni et que campaign_id manque, l'ajouter
        if form_to_campaigns and 'campaign_id' in df.columns:
            for idx, row in df.iterrows():
                if pd.isna(row['campaign_id']) and row['form_id'] in form_to_campaigns:
                    # Prendre la première campagne du mapping (ou faire une métrique par campagne)
                    campaign_ids = form_to_campaigns[row['form_id']]
                    if campaign_ids:
                        df.at[idx, 'campaign_id'] = campaign_ids[0]  # Utiliser la première campagne
        
        # Grouper par form_id, campaign_id (si disponible) et date
        group_cols = ['form_id', 'date']
        if 'campaign_id' in df.columns and df['campaign_id'].notna().any():
            group_cols.insert(1, 'campaign_id')
        
        metrics_list = []

        for group_keys, group in df.groupby(group_cols):
            # Extraire les clés du groupe
            if len(group_cols) == 3:  # form_id, campaign_id, date
                form_id, campaign_id, date = group_keys
            else:  # form_id, date
                form_id, date = group_keys
                campaign_id = group['campaign_id'].iloc[0] if 'campaign_id' in group.columns else None
            
            total_leads = len(group)

            # Métriques de qualité des champs
            complete_leads = group[
                group['first_name'].notna() &
                group['last_name'].notna() &
                group['email_address'].notna()
            ].shape[0]
            field_completion_rate = round((complete_leads / total_leads) * 100, 2) if total_leads > 0 else 0.0

            # Validation des emails (exclure les emails personnels)
            personal_email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
            valid_business_emails = 0
            for email in group['email_address'].dropna():
                if isinstance(email, str) and '@' in email:
                    domain = email.split('@')[-1].lower()
                    if domain not in personal_email_domains:
                        valid_business_emails += 1
            email_validity_rate = round((valid_business_emails / total_leads) * 100, 2) if total_leads > 0 else 0.0

            # Taux de consentement
            consented_leads = group[group['consent_granted'] == True].shape[0]
            consent_opt_in_rate = round((consented_leads / total_leads) * 100, 2) if total_leads > 0 else 0.0

            # Score de qualité composite (pondéré)
            # 40% completion, 40% email validity, 20% consent
            lead_quality_score = round(
                (field_completion_rate * 0.4) +
                (email_validity_rate * 0.4) +
                (consent_opt_in_rate * 0.2),
                2
            )

            # Métriques de timing
            # Calculer les deltas en secondes
            notification_times = []
            fetch_times = []

            for _, row in group.iterrows():
                if pd.notna(row.get('submitted_at')) and pd.notna(row.get('notification_received_at')):
                    try:
                        submitted = pd.to_datetime(row['submitted_at'])
                        notified = pd.to_datetime(row['notification_received_at'])
                        delta_seconds = (notified - submitted).total_seconds()
                        if delta_seconds >= 0:  # Éviter les valeurs négatives
                            notification_times.append(delta_seconds)
                    except:
                        pass

                if pd.notna(row.get('notification_received_at')) and pd.notna(row.get('fetched_at')):
                    try:
                        notified = pd.to_datetime(row['notification_received_at'])
                        fetched = pd.to_datetime(row['fetched_at'])
                        delta_seconds = (fetched - notified).total_seconds()
                        if delta_seconds >= 0:
                            fetch_times.append(delta_seconds)
                    except:
                        pass

            avg_time_to_first_notification = round(sum(notification_times) / len(notification_times), 2) if notification_times else 0.0
            avg_time_to_full_fetch = round(sum(fetch_times) / len(fetch_times), 2) if fetch_times else 0.0

            # SLA Breaches (seuils: 5 min notification, 10 min fetch)
            notification_sla_seconds = 300  # 5 minutes
            fetch_sla_seconds = 600  # 10 minutes

            sla_breach_count = 0
            for nt in notification_times:
                if nt > notification_sla_seconds:
                    sla_breach_count += 1
            for ft in fetch_times:
                if ft > fetch_sla_seconds:
                    sla_breach_count += 1

            # Enrichir avec les données analytics si disponibles
            impressions = None
            clicks = None
            ad_spend = None
            submission_rate = None
            conversion_rate = None
            cost_per_lead = None
            
            if analytics_df is not None and campaign_id:
                # Chercher les analytics pour cette campagne et date
                analytics_match = analytics_df[
                    (analytics_df['campaign_id'] == campaign_id) &
                    (analytics_df['date'] == date)
                ]
                
                if not analytics_match.empty:
                    row = analytics_match.iloc[0]
                    impressions = int(row['impressions']) if pd.notna(row.get('impressions')) else None
                    clicks = int(row['clicks']) if pd.notna(row.get('clicks')) else None
                    ad_spend = float(row['cost_in_usd']) if pd.notna(row.get('cost_in_usd')) else None
                    
                    # Calculer les taux
                    if impressions and impressions > 0:
                        submission_rate = round((total_leads / impressions) * 100, 2)
                    if clicks and clicks > 0:
                        conversion_rate = round((total_leads / clicks) * 100, 2)
                    if ad_spend and ad_spend > 0 and total_leads > 0:
                        cost_per_lead = round(ad_spend / total_leads, 2)
            
            metrics = {
                "form_id": form_id,
                "campaign_id": campaign_id,
                "date": date.isoformat() if hasattr(date, 'isoformat') else str(date),
                "total_leads": total_leads,
                "impressions": impressions,
                "clicks": clicks,
                "ad_spend": ad_spend,
                "submission_rate": submission_rate,
                "conversion_rate": conversion_rate,
                "cost_per_lead": cost_per_lead,
                "avg_time_to_first_notification": avg_time_to_first_notification,
                "avg_time_to_full_fetch": avg_time_to_full_fetch,
                "field_completion_rate": field_completion_rate,
                "consent_opt_in_rate": consent_opt_in_rate,
                "email_validity_rate": email_validity_rate,
                "lead_quality_score": lead_quality_score,
                "lead_to_opportunity_count": None,  # Nécessite intégration CRM
                "lead_to_opportunity_rate": None,  # Nécessite intégration CRM
                "sla_breach_count": sla_breach_count,
                "anomaly_detected": False,  # Sera calculé après avec historique
                "anomaly_description": None,
                "calculated_at": datetime.now(),
            }

            metrics_list.append(metrics)

        # Détection d'anomalies (basée sur rolling average)
        if len(metrics_list) > 7:  # Besoin d'au moins 7 jours d'historique
            metrics_df = pd.DataFrame(metrics_list)
            metrics_df = metrics_df.sort_values('date')

            # Grouper par form_id pour calculer les moyennes mobiles
            for form_id in metrics_df['form_id'].unique():
                form_metrics = metrics_df[metrics_df['form_id'] == form_id].copy()

                if len(form_metrics) >= 7:
                    # Calculer rolling average sur 7 jours
                    form_metrics['rolling_avg'] = form_metrics['total_leads'].rolling(window=7, min_periods=1).mean()

                    # Détecter les anomalies (variation > 30%)
                    for idx, row in form_metrics.iterrows():
                        if pd.notna(row['rolling_avg']) and row['rolling_avg'] > 0:
                            pct_change = abs(row['total_leads'] - row['rolling_avg']) / row['rolling_avg']

                            if pct_change > 0.3:  # 30% de variation
                                anomaly_type = 'SPIKE' if row['total_leads'] > row['rolling_avg'] else 'DROP'
                                pct_change_display = round(pct_change * 100, 1)

                                # Mettre à jour dans metrics_list
                                for metric in metrics_list:
                                    if metric['form_id'] == row['form_id'] and metric['date'] == row['date']:
                                        metric['anomaly_detected'] = True
                                        metric['anomaly_description'] = f"{anomaly_type}: {pct_change_display}% variation from 7-day average"
                                        break

        print(f"\n✓ {len(metrics_list)} métriques calculées pour {len(set(m['form_id'] for m in metrics_list))} formulaire(s)")

        return metrics_list

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
                    # form_data est un RECORD BQ avec:
                    #   - answers: REPEATED RECORD (passer tel quel)
                    #   - consentResponses: REPEATED STRING (chaque élément doit être stringifié)
                    # custom_fields est un RECORD BQ avec des champs STRING (passer tel quel)
                    elif key == 'form_data' and value is not None:
                        try:
                            parsed = json.loads(value) if isinstance(value, str) else value
                            if isinstance(parsed, dict):
                                consent = parsed.get('consentResponses', [])
                                processed_row[key] = {
                                    'answers': parsed.get('answers', []),
                                    'consentResponses': [
                                        json.dumps(c) if isinstance(c, (dict, list)) else str(c)
                                        for c in (consent if isinstance(consent, list) else [])
                                    ],
                                }
                            else:
                                processed_row[key] = None
                        except (json.JSONDecodeError, TypeError):
                            processed_row[key] = None
                    elif key == 'custom_fields' and value is not None:
                        try:
                            parsed = json.loads(value) if isinstance(value, str) else value
                            processed_row[key] = parsed
                        except (json.JSONDecodeError, TypeError):
                            processed_row[key] = None
                    else:
                        processed_row[key] = value
                processed_data.append(processed_row)

            # Ajouter retrieved_at si absent (sauf pour lead_form_metrics qui utilise calculated_at)
            if table_name != "lead_form_metrics":
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

            # Retry logic pour les erreurs réseau SSL/timeout
            max_retries = 3
            for attempt in range(max_retries):
                try:
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
                    break  # Succès, sortir de la boucle

                except Exception as upload_error:
                    if attempt < max_retries - 1:
                        import time
                        wait_time = (attempt + 1) * 5  # 5s, 10s, 15s
                        print(f"⚠️  Tentative {attempt + 1}/{max_retries} échouée: {upload_error}")
                        print(f"   Nouvelle tentative dans {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        raise  # Dernière tentative, propager l'erreur

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
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
    from config_loader import load_config

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    # Détecter si on est dans Cloud Functions
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config_path = os.path.join(os.path.dirname(__file__), '../../config.yaml' if not is_cloud_function else '../config.yaml')
    config = load_config(config_path, skip_credentials_check=is_cloud_function)

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
    CREDENTIALS_PATH = None if is_cloud_function else google_config.get('credentials_file')

    print("=" * 70)
    print("LINKEDIN LEAD FORMS & RESPONSES")
    print("=" * 70)
    print(f"\nOrganisation: {ORGANIZATION_ID}")
    print(f"Ad Account: {AD_ACCOUNT_ID}")
    print(f"BigQuery: {PROJECT_ID}.{DATASET_ID}")
    print(f"Environment: {'Cloud Function' if is_cloud_function else 'Local'}\n")

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

        # Upload vers BigQuery (APPEND = ajoute les données sans supprimer l'existant)
        client.upload_to_bigquery(forms_data, "lead_forms", write_disposition="WRITE_APPEND")

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
                responses_data = client.extract_lead_response_data(responses, form_id, AD_ACCOUNT_ID)
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

            # Upload vers BigQuery (APPEND = ajoute les données sans supprimer l'existant)
            client.upload_to_bigquery(all_responses_data, "lead_form_responses", write_disposition="WRITE_APPEND")

            # Étape 3: Créer le mapping form_id -> campaign_ids
            print("\n" + "=" * 70)
            print("3. Mapping formulaires ↔ campagnes")
            print("=" * 70)
            
            form_to_campaigns = client.get_campaigns_using_forms(AD_ACCOUNT_ID)
            
            # Étape 4: Récupérer les analytics pour enrichir les métriques
            print("\n" + "=" * 70)
            print("4. Récupération des analytics de campagne")
            print("=" * 70)
            
            campaign_analytics = []
            try:
                # Importer le client de campaign analytics
                from .linkedin_campaign_analytics import LinkedInCampaignAnalytics
                
                analytics_client = LinkedInCampaignAnalytics(
                    access_token=ACCESS_TOKEN,
                    account_id=AD_ACCOUNT_ID,
                    project_id=None,  # Pas besoin d'uploader
                    dataset_id=None
                )
                
                # Récupérer les campagnes liées aux leads (depuis les réponses + le mapping)
                campaign_ids = set(r.get('campaign_id') for r in all_responses_data if r.get('campaign_id'))
                
                # Ajouter les campagnes du mapping
                for form_id, mapped_campaigns in form_to_campaigns.items():
                    campaign_ids.update(mapped_campaigns)
                
                # Filtrer les None
                campaign_ids = {cid for cid in campaign_ids if cid}
                
                if campaign_ids:
                    print(f"\n→ Récupération des analytics pour {len(campaign_ids)} campagne(s)...")
                    
                    # Créer les URNs
                    campaign_urns = [f"urn:li:sponsoredCampaign:{cid}" for cid in campaign_ids]
                    
                    # Récupérer les analytics
                    analytics = analytics_client.get_campaign_analytics(
                        campaign_urns=campaign_urns,
                        start_date=start_date,
                        end_date=end_date
                    )
                    
                    if analytics:
                        campaign_analytics = analytics_client.extract_campaign_data(analytics)
                        print(f"✓ {len(campaign_analytics)} lignes d'analytics récupérées")
                    else:
                        print("  Aucune analytics trouvée")
                else:
                    print("  Aucun campaign_id disponible")
                    
            except ImportError:
                print("⚠️  Module linkedin_campaign_analytics non disponible")
                print("   Les métriques seront calculées sans les données d'analytics")
            except Exception as e:
                print(f"⚠️  Erreur lors de la récupération des analytics: {e}")
                print("   Les métriques seront calculées sans les données d'analytics")
            
            # Étape 5: Calculer et uploader les métriques
            print("\n" + "=" * 70)
            print("5. Calcul des métriques de lead forms")
            print("=" * 70)

            metrics_data = client.calculate_lead_form_metrics(
                all_responses_data, 
                campaign_analytics=campaign_analytics if campaign_analytics else None,
                form_to_campaigns=form_to_campaigns
            )

            if metrics_data:
                # Afficher un résumé
                print("\nRésumé des métriques:")
                print("-" * 70)
                total_forms = len(set(m['form_id'] for m in metrics_data))
                avg_quality_score = sum(m['lead_quality_score'] for m in metrics_data) / len(metrics_data)
                total_anomalies = sum(1 for m in metrics_data if m['anomaly_detected'])
                print(f"Formulaires avec métriques: {total_forms}")
                print(f"Score qualité moyen: {avg_quality_score:.2f}/100")
                print(f"Anomalies détectées: {total_anomalies}")

                # Exporter
                client.export_to_json(metrics_data, "lead_form_metrics.json")
                client.export_to_csv(metrics_data, "lead_form_metrics.csv")

                # Upload vers BigQuery (APPEND = ajoute les données sans supprimer l'existant)
                client.upload_to_bigquery(metrics_data, "lead_form_metrics", write_disposition="WRITE_APPEND")

        print("\n" + "=" * 70)
        print("✓ EXTRACTION LEAD FORMS TERMINÉE!")
        print("=" * 70)
        print(f"📊 Fichiers locaux créés:")
        print(f"   - lead_forms.json / .csv")
        if all_responses_data:
            print(f"   - lead_form_responses.json / .csv")
            print(f"   - lead_form_metrics.json / .csv")
        print(f"☁️  Données uploadées dans BigQuery:")
        print(f"   - {PROJECT_ID}.{DATASET_ID}.lead_forms")
        if all_responses_data:
            print(f"   - {PROJECT_ID}.{DATASET_ID}.lead_form_responses")
            print(f"   - {PROJECT_ID}.{DATASET_ID}.lead_form_metrics")

    except Exception as e:
        print(f"✗ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
