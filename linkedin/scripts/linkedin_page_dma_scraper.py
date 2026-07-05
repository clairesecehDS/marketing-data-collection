"""
Script de scraping complet pour les données LinkedIn Page via DMA API
Collecte TOUTES les données disponibles pour une page LinkedIn organisationnelle
"""

import requests
from datetime import datetime
from typing import Optional, List, Dict, Any
import json
import pandas as pd
from google.cloud import bigquery
import os
import sys
import time
from urllib.parse import urlencode, quote

# Ajouter le répertoire parent au path pour importer config_loader
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from config_loader import load_config


class LinkedInPageDMAClient:
    """
    Client complet pour scraper toutes les données disponibles via LinkedIn DMA API
    Basé sur la documentation: LinkedIn Pages Data Portability API
    """

    def __init__(self, access_token: str, organization_id: str,
                 page_id: Optional[str] = None,
                 project_id: Optional[str] = None,
                 dataset_id: str = "linkedin_page",
                 credentials_path: Optional[str] = None,
                 request_delay: float = 1.0,
                 api_version: str = "202511"):
        """
        Initialise le client DMA

        Args:
            access_token: Token OAuth 2.0 LinkedIn avec permissions DMA
            organization_id: ID de l'organisation LinkedIn (numérique)
            page_id: ID de la page organisationnelle LinkedIn (numérique, optionnel)
            project_id: ID du projet Google Cloud
            dataset_id: ID du dataset BigQuery
            credentials_path: Chemin vers le fichier JSON des credentials GCP
            request_delay: Délai en secondes entre chaque requête API
            api_version: Version de l'API LinkedIn (format YYYYMM)
        """
        self.access_token = access_token
        self.organization_id = organization_id
        self.base_url = "https://api.linkedin.com/rest"
        self.api_version = api_version

        # Construire les URNs
        # Si page_id est fourni, on l'utilise pour l'organizationalPage, sinon on utilise organization_id
        self.page_id = page_id or organization_id
        self.org_urn = f"urn:li:organizationalPage:{self.page_id}"
        self.organization_urn = f"urn:li:organization:{organization_id}"

        # Configuration BigQuery
        self.project_id = project_id or os.environ.get('GOOGLE_CLOUD_PROJECT')
        self.dataset_id = dataset_id
        self.credentials_path = credentials_path
        self.bq_client = None

        # Configuration du rate limiting
        self.request_delay = request_delay
        self.last_request_time = 0

        # Stats de collecte
        self.stats = {}

    def _get_headers(self) -> Dict[str, str]:
        """Retourne les headers requis pour l'API LinkedIn DMA"""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "LinkedIn-Version": self.api_version,
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json"
        }

    def _wait_for_rate_limit(self):
        """Attend le délai nécessaire entre les requêtes"""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time

        if time_since_last_request < self.request_delay:
            sleep_time = self.request_delay - time_since_last_request
            time.sleep(sleep_time)

        self.last_request_time = time.time()

    def _make_request(self, url: str, max_retries: int = 3) -> requests.Response:
        """Effectue une requête HTTP avec retry"""
        for attempt in range(max_retries):
            self._wait_for_rate_limit()

            try:
                response = requests.get(url, headers=self._get_headers())

                if response.status_code == 200:
                    return response

                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 60))
                    print(f"  ⚠️  Rate limit - attente de {retry_after}s...")
                    time.sleep(retry_after)
                    continue

                # Afficher l'erreur complète pour debug
                error_detail = response.text
                print(f"  ⚠️  Erreur {response.status_code}:")
                print(f"      URL: {url}")
                print(f"      Message: {error_detail[:500]}")

                if attempt < max_retries - 1:
                    continue
                response.raise_for_status()

            except Exception as e:
                print(f"  ⚠️  Exception: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue
                raise

        return response

    def _fetch_paginated_data(self, endpoint: str, params: Dict[str, Any],
                             max_results: int = 10000) -> List[Dict]:
        """
        Récupère toutes les données paginées d'un endpoint

        Args:
            endpoint: Nom de l'endpoint (ex: 'dmaPosts')
            params: Paramètres de requête de base
            max_results: Nombre maximum de résultats à récupérer

        Returns:
            Liste de tous les éléments récupérés
        """
        all_elements = []
        pagination_cursor = None
        count = 0

        while count < max_results:
            # Construire l'URL avec paramètres
            current_params = params.copy()
            current_params['maxPaginationCount'] = min(100, max_results - count)

            if pagination_cursor:
                current_params['paginationCursor'] = pagination_cursor

            url = f"{self.base_url}/{endpoint}?{urlencode(current_params)}"

            try:
                response = self._make_request(url)
                data = response.json()

                elements = data.get('elements', [])
                all_elements.extend(elements)
                count += len(elements)

                # Vérifier la pagination
                metadata = data.get('metadata', {})
                pagination_cursor = metadata.get('nextPaginationCursor')

                if not pagination_cursor or not elements:
                    break

            except Exception as e:
                print(f"    ⚠️  Erreur lors de la pagination: {e}")
                break

        return all_elements

    # ==================== ANALYTICS ENDPOINTS ====================

    def get_page_statistics(self, days: int = 365) -> List[Dict]:
        """
        Récupère les statistiques combinées de contenu et d'audience de la page
        Fusionne les données de Page Content Analytics et Page Edge Analytics
        
        Args:
            days: Nombre de jours d'historique à récupérer (défaut: 365 jours = 1 an)
        """
        print(f"\n→ Page Statistics (derniers {days} jours)")

        # Calculer les timestamps pour la période demandée
        from datetime import timedelta
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)

        # Convertir en timestamps millisecondes
        start_ts = int(start_time.timestamp() * 1000)
        end_ts = int(end_time.timestamp() * 1000)

        try:
            # ===== PARTIE 1: Content Analytics =====
            print("  → Collecte des métriques de contenu...")
            time_intervals = f"(timeRange:(start:{start_ts},end:{end_ts}))"
            metric_types = "List(IMPRESSIONS,CLICKS,COMMENTS,REACTIONS)"
            
            url = f"{self.base_url}/dmaOrganizationalPageContentAnalytics?q=trend&sourceEntity={quote(self.org_urn, safe='')}&timeIntervals={time_intervals}&metricTypes={metric_types}"
            
            response = self._make_request(url)
            data = response.json()
            elements = data.get('elements', [])

            # Agréger les métriques par type
            metrics = {
                'impression_count': 0,
                'click_count': 0,
                'reaction_count': 0,
                'comment_count': 0,
            }
            
            for elem in elements:
                metric_type = elem.get('type')
                metric_obj = elem.get('metric', {})
                value_obj = metric_obj.get('value', {})
                total_count_obj = value_obj.get('totalCount', {})
                
                if isinstance(total_count_obj, dict):
                    count = total_count_obj.get('long', 0)
                else:
                    count = total_count_obj or 0
                
                if metric_type == 'IMPRESSIONS':
                    metrics['impression_count'] = count
                elif metric_type == 'CLICKS':
                    metrics['click_count'] = count
                elif metric_type == 'REACTIONS':
                    metrics['reaction_count'] = count
                elif metric_type == 'COMMENTS':
                    metrics['comment_count'] = count
            
            print(f"    ✓ Contenu: {metrics['impression_count']:,} impressions, {metrics['click_count']:,} clicks, {metrics['reaction_count']:,} réactions")
            
            # ===== PARTIE 2: Visitor Count depuis Edge Analytics =====
            print("  → Collecte du nombre de visiteurs...")
            visitor_count = 0
            
            try:
                url_visitors = f"{self.base_url}/dmaOrganizationalPageEdgeAnalytics?q=trend&organizationalPage={quote(self.org_urn, safe='')}&analyticsType=VISITOR&timeIntervals={time_intervals}"
                response_visitors = self._make_request(url_visitors)
                data_visitors = response_visitors.json()
                elements_visitors = data_visitors.get('elements', [])
                
                for elem in elements_visitors:
                    value_obj = elem.get('value', {})
                    total_count_obj = value_obj.get('totalCount', {})
                    
                    if isinstance(total_count_obj, dict):
                        count = total_count_obj.get('long', 0)
                    else:
                        count = total_count_obj or 0
                    
                    visitor_count += count
                
                print(f"    ✓ Visiteurs: {visitor_count:,}")
            except Exception as e:
                print(f"    ⚠️  Visiteurs: erreur ({e})")
            
            # Créer un seul enregistrement avec toutes les métriques fusionnées
            results = [{
                'organization_id': self.organization_id,
                'page_follower_count': None,  # Non disponible via DMA API
                'visitor_count': visitor_count,  # Depuis Edge Analytics
                'impression_count': metrics['impression_count'],
                'click_count': metrics['click_count'],
                'comment_count': metrics['comment_count'],
                'reaction_count': metrics['reaction_count'],
                'retrieved_at': datetime.now()
            }]

            print(f"  ✓ Statistiques complètes: {metrics['impression_count']:,} impressions, {visitor_count:,} visiteurs")
            return results
            
        except Exception as e:
            print(f"  ✗ Erreur: {e}")
            return []

    def get_page_edge_analytics(self, days: int = 365) -> List[Dict]:
        """
        Récupère les analytics de followers et visiteurs
        
        Args:
            days: Nombre de jours d'historique à récupérer (défaut: 365 jours = 1 an)
        """
        print(f"\n→ Page Edge Analytics (derniers {days} jours)")

        # Calculer les timestamps pour la période demandée
        from datetime import timedelta
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)

        # Convertir en timestamps millisecondes
        start_ts = int(start_time.timestamp() * 1000)
        end_ts = int(end_time.timestamp() * 1000)

        # Format selon la doc: timeIntervals=(timeRange:(start:...,end:...))
        time_intervals = f"(timeRange:(start:{start_ts},end:{end_ts}))"
        
        # Collecter les données par type d'analytics
        analytics_data = {}
        
        for analytics_type in ['VISITOR', 'PAGE_FOLLOWER', 'ACTIVE_FOLLOWER', 'NEW_FOLLOWER']:
            # Construire l'URL manuellement
            url = f"{self.base_url}/dmaOrganizationalPageEdgeAnalytics?q=trend&organizationalPage={quote(self.org_urn, safe='')}&analyticsType={analytics_type}&timeIntervals={time_intervals}"

            try:
                response = self._make_request(url)
                data = response.json()
                elements = data.get('elements', [])

                total = 0
                for elem in elements:
                    value_obj = elem.get('value', {})
                    total_count_obj = value_obj.get('totalCount', {})
                    
                    # Le count est dans totalCount.long (pas juste totalCount)
                    if isinstance(total_count_obj, dict):
                        count = total_count_obj.get('long', 0)
                    else:
                        count = total_count_obj or 0
                    
                    total += count

                analytics_data[analytics_type] = total
                print(f"  ✓ {analytics_type}: {total}")
                
            except Exception as e:
                print(f"  ✗ {analytics_type}: {e}")
                analytics_data[analytics_type] = 0

        # Créer un seul enregistrement avec toutes les métriques
        results = []
        
        # Edge type MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE
        results.append({
            'organization_id': self.organization_id,
            'edge_type': 'MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE',
            'visitor_count': analytics_data.get('VISITOR', 0),
            'page_follower_count': analytics_data.get('PAGE_FOLLOWER', 0),
            'active_follower_count': analytics_data.get('ACTIVE_FOLLOWER', 0),
            'new_follower_count': analytics_data.get('NEW_FOLLOWER', 0),
            'retrieved_at': datetime.now()
        })

        return results

    def get_page_content_analytics_dma(self) -> List[Dict]:
        """
        Récupère les analytics de contenu de la page
        Peut être appelé sans URN de contenu spécifique pour obtenir des analytics agrégées
        """
        print("\n→ Page Content Analytics")

        # Construire l'URL avec le paramètre organizationalPage
        params = {
            'organizationalPage': self.org_urn
        }
        
        url = f"{self.base_url}/organizationalPageContentAnalyticsDMA?{urlencode(params)}"

        try:
            response = self._make_request(url)
            data = response.json()
            
            elements = data.get('elements', [])
            
            results = []
            for item in elements:
                results.append({
                    'organization_id': self.organization_id,
                    'content_urn': item.get('contentUrn'),
                    'impression_count': item.get('impressionCount', 0),
                    'reaction_count': item.get('reactionCount', 0),
                    'comment_count': item.get('commentCount', 0),
                    'repost_count': item.get('repostCount', 0),
                    'click_count': item.get('clickCount', 0),
                    'demographics_breakdown': json.dumps(item.get('demographicsBreakdown')) if item.get('demographicsBreakdown') else None,
                    'retrieved_at': datetime.now(),
                    'updated_at': datetime.now()
                })
            
            print(f"  ✓ {len(results)} contenus avec analytics")
            return results
            
        except Exception as e:
            print(f"  ✗ Erreur: {e}")
            return []

    def get_search_appearance_analytics(self) -> List[Dict]:
        """
        Note: Cet endpoint n'existe pas dans l'API DMA
        """
        print("\n→ Search Appearance Analytics")
        print("  ⚠️  Non disponible dans DMA API")
        return []

    # ==================== FEED & CONTENT ENDPOINTS ====================

    def get_posts(self, max_results: int = 1000) -> List[Dict]:
        """
        Récupère tous les posts de la page via deux étapes:
        1. Récupérer la liste des URNs via dmaFeedContentsExternal
        2. Récupérer les détails des posts via dmaPosts avec BATCH_GET
        """
        print("\n→ Posts")

        # ÉTAPE 1: Récupérer les URNs des posts
        print("  → Étape 1/2: Récupération des URNs des posts...")
        params = {
            'q': 'postsByAuthor',
            'author': self.org_urn
        }

        feed_elements = self._fetch_paginated_data('dmaFeedContentsExternal', params, max_results)
        post_urns = [elem.get('content') for elem in feed_elements if elem.get('content')]

        print(f"  ✓ {len(post_urns)} URNs de posts trouvés")

        if not post_urns:
            print("  ⚠️  Aucun post trouvé")
            return []

        # ÉTAPE 2: Récupérer les détails des posts par batch
        print("  → Étape 2/2: Récupération des détails des posts...")
        results = []
        batch_size = 100  # LinkedIn limite généralement à 100 IDs par requête

        for i in range(0, len(post_urns), batch_size):
            batch_urns = post_urns[i:i + batch_size]

            # Construire la liste des IDs pour le paramètre ids
            ids_param = ','.join(batch_urns)
            url = f"{self.base_url}/dmaPosts?ids=List({ids_param})"

            try:
                response = self._make_request(url)
                data = response.json()

                elements = data.get('results', {}).values() if 'results' in data else data.get('elements', [])

                for post in elements:
                    results.append({
                        'organization_id': self.organization_id,
                        'page_id': self.page_id,
                        'post_id': post.get('id'),
                        'post_urn': post.get('$URN'),
                        'text': post.get('commentary'),  # Le texte est dans 'commentary'
                        'author': post.get('author'),
                        'visibility': post.get('visibility'),
                        'created_time': datetime.fromtimestamp(post.get('createdAt', 0) / 1000) if post.get('createdAt') else None,
                        'last_modified_time': datetime.fromtimestamp(post.get('lastModifiedAt', 0) / 1000) if post.get('lastModifiedAt') else None,
                        'lifecycle_state': post.get('lifecycleState'),
                        'distribution': json.dumps(post.get('distribution')) if post.get('distribution') else None,
                        'content': json.dumps(post.get('content')) if post.get('content') else None,
                        'retrieved_at': datetime.now()
                    })

                print(f"  ✓ Batch {i//batch_size + 1}: {len(elements)} posts récupérés")

            except Exception as e:
                print(f"  ✗ Erreur batch {i//batch_size + 1}: {e}")

        print(f"  ✓ Total: {len(results)} posts avec détails")
        return results

    def get_comments(self) -> List[Dict]:
        """
        Récupère tous les commentaires via BATCH_GET
        Nécessite les URNs des posts (depuis get_posts)

        Note: L'API DMA ne fournit PAS de finder pour récupérer tous les commentaires
        Il faut d'abord avoir les URNs des posts, puis utiliser BATCH_GET avec
        le format: urn:li:comment:(<post_urn>,<comment_id>)

        Pour cette raison, cette méthode est désactivée car on ne peut pas
        récupérer les comment_ids sans connaître à l'avance tous les posts et leurs commentaires.
        """
        print("\n→ Comments")
        print("  ⚠️  Endpoint désactivé: DMA API ne fournit pas de finder pour lister les commentaires")
        print("  ℹ️  Les commentaires doivent être récupérés via BATCH_GET avec URNs spécifiques")
        print("  ℹ️  Format requis: urn:li:comment:(<post_urn>,<comment_id>)")
        print("  ℹ️  → Impossible sans connaître les comment_ids à l'avance")
        return []

    def get_reactions(self) -> List[Dict]:
        """
        Récupère toutes les réactions via BATCH_GET

        Note: L'API DMA ne fournit PAS de finder pour récupérer toutes les réactions
        Il faut utiliser BATCH_GET avec le format:
        urn:li:reaction:(urn:li:person:{person_id},urn:li:activity:{activity_id})

        Pour cette raison, cette méthode est désactivée car on ne peut pas
        récupérer les reaction URNs sans connaître à l'avance les person_ids et activity_ids.
        """
        print("\n→ Reactions")
        print("  ⚠️  Endpoint désactivé: DMA API ne fournit pas de finder pour lister les réactions")
        print("  ℹ️  Les réactions doivent être récupérées via BATCH_GET avec URNs spécifiques")
        print("  ℹ️  Format requis: urn:li:reaction:(urn:li:person:{person_id},urn:li:activity:{activity_id})")
        print("  ℹ️  → Impossible sans connaître les URNs à l'avance")
        return []

    # ==================== FOLLOWERS ENDPOINTS ====================

    def get_followers(self, max_results: int = 10000) -> List[Dict]:
        """
        Récupère tous les followers de la page
        Utilise le finder q=followee avec edgeType=MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE
        Note: Limite de 1 requête par 60 secondes, données jusqu'à 48h de retard
        """
        print("\n→ Followers")

        params = {
            'q': 'followee',
            'followee': self.org_urn,
            'edgeType': 'MEMBER_FOLLOWS_ORGANIZATIONAL_PAGE',
            'maxPaginationCount': 1000  # Maximum autorisé
        }

        elements = self._fetch_paginated_data('dmaOrganizationalPageFollows', params, max_results)

        results = []
        for follower_obj in elements:
            results.append({
                'organization_id': self.organization_id,
                'page_id': self.page_id,
                'follower_urn': follower_obj.get('follower'),  # Peut être obfusqué si membre sans permission
                'followee_urn': follower_obj.get('followee'),
                'edge_type': follower_obj.get('edgeType'),
                'last_modified_at': datetime.fromtimestamp(follower_obj.get('lastModifiedAt', 0) / 1000) if follower_obj.get('lastModifiedAt') else None,
                'retrieved_at': datetime.now()
            })

        print(f"  ✓ {len(results)} followers")
        return results

    # ==================== PROFILE ENDPOINTS ====================

    def get_page_profile(self) -> List[Dict]:
        """
        Récupère le profil de la page
        Utilise l'endpoint GET direct avec l'URN de la page
        """
        print("\n→ Page Profile")

        # Encoder l'URN pour l'URL
        encoded_urn = quote(self.org_urn, safe='')
        url = f"{self.base_url}/dmaOrganizationalPageProfiles/{encoded_urn}"

        try:
            response = self._make_request(url)
            data = response.json()

            result = [{
                'organization_id': self.organization_id,
                'page_id': self.page_id,
                'entity_urn': data.get('entityUrn'),
                'name': data.get('name'),
                'localized_name': data.get('localizedName'),
                'description': data.get('description'),
                'localized_description': data.get('localizedDescription'),
                'page_url': data.get('pageUrl'),
                'vanity_name': data.get('vanityName'),
                'logo': json.dumps(data.get('logo')) if data.get('logo') else None,
                'cover_image': json.dumps(data.get('coverImage')) if data.get('coverImage') else None,
                'page_profile_entity': json.dumps(data.get('pageProfileEntity')) if data.get('pageProfileEntity') else None,
                'primary_page_entity': json.dumps(data.get('primaryPageEntity')) if data.get('primaryPageEntity') else None,
                'created': json.dumps(data.get('created')) if data.get('created') else None,
                'last_modified': json.dumps(data.get('lastModified')) if data.get('lastModified') else None,
                'retrieved_at': datetime.now()
            }]
            print(f"  ✓ Profil récupéré")
            return result
        except Exception as e:
            print(f"  ✗ Erreur: {e}")
            return []

    # ==================== LEAD GEN ENDPOINTS ====================

    def get_lead_gen_forms(self, max_results: int = 100) -> List[Dict]:
        """
        Récupère tous les formulaires lead gen
        Utilise le finder q=owner avec pagination manuelle
        """
        print("\n→ Lead Gen Forms")

        # Utiliser l'URN de l'organisation (pas de la page)
        owner_urn = self.organization_urn

        all_elements = []
        start = 0
        count = 50

        while len(all_elements) < max_results:
            params = {
                'q': 'owner',
                'owner': owner_urn,
                'start': start,
                'count': count
            }

            url = f"{self.base_url}/dmaLeadGenForm?{urlencode(params)}"

            try:
                response = self._make_request(url)
                data = response.json()

                elements = data.get('elements', [])
                if not elements:
                    break

                all_elements.extend(elements)
                start += count

                # Vérifier la pagination
                paging = data.get('paging', {})
                if not paging.get('links') or start >= max_results:
                    break

            except Exception as e:
                print(f"  ✗ Erreur: {e}")
                break

        results = []
        for form in all_elements:
            # Extraire le headline depuis content.headline (objet localisé)
            headline = None
            content = form.get('content', {})
            if content:
                headline_obj = content.get('headline')
                if headline_obj and isinstance(headline_obj, dict):
                    localized = headline_obj.get('localized', {})
                    if localized:
                        headline = next(iter(localized.values()), None)
            
            # Extraire les questions depuis content.questions
            questions = None
            if content:
                questions_list = content.get('questions')
                if questions_list:
                    questions = json.dumps(questions_list)
            
            # Convertir les timestamps millisecondes en datetime ISO
            created_time = None
            created_timestamp = form.get('created')
            if created_timestamp:
                created_time = datetime.fromtimestamp(created_timestamp / 1000).isoformat()
            
            last_modified_time = None
            last_modified_timestamp = form.get('lastModified')
            if last_modified_timestamp:
                last_modified_time = datetime.fromtimestamp(last_modified_timestamp / 1000).isoformat()
            
            results.append({
                'organization_id': self.organization_id,
                'page_id': self.page_id,
                'form_urn': form.get('$URN'),
                'form_id': form.get('id'),
                'form_name': form.get('name'),
                'headline': headline,
                'description': form.get('description'),
                'questions': questions,
                'created_time': created_time,
                'last_modified_time': last_modified_time,
                'owner': form.get('owner'),
                'state': form.get('state'),
                'version_id': form.get('versionId'),
                'creation_locale': json.dumps(form.get('creationLocale')) if form.get('creationLocale') else None,
                'content': json.dumps(content) if content else None,
                'retrieved_at': datetime.now()
            })

        print(f"  ✓ {len(results)} formulaires")
        return results

    # ==================== EVENTS ENDPOINTS ====================

    def get_events(self, max_results: int = 100) -> List[Dict]:
        """
        Récupère tous les événements
        Utilise le finder q=organizer avec l'URN de l'organisation
        """
        print("\n→ Events")

        # L'API attend urn:li:organization:{ID}, pas organizationalPage
        organizer_urn = self.organization_urn

        params = {
            'q': 'organizer',
            'organizer': organizer_urn,
            'maxPaginationCount': 10  # Valeur par défaut selon la doc
        }

        elements = self._fetch_paginated_data('dmaEvents', params, max_results)

        results = []
        for event in elements:
            # Extraire le titre depuis l'objet localisé 'name' (pas 'title')
            title = None
            name_obj = event.get('name')
            if name_obj and isinstance(name_obj, dict):
                localized = name_obj.get('localized', {})
                if localized:
                    # Prendre la première valeur disponible
                    title = next(iter(localized.values()), None)
            
            # Extraire la description depuis l'objet localisé (si présent)
            description = None
            desc_obj = event.get('description')
            if desc_obj and isinstance(desc_obj, dict):
                localized = desc_obj.get('localized', {})
                if localized:
                    # Prendre la première valeur disponible
                    description = next(iter(localized.values()), {}).get('rawText') if isinstance(next(iter(localized.values())), dict) else next(iter(localized.values()), None)
            
            # Extraire les dates depuis timeRangeV2 (timestamps en millisecondes)
            start_date = None
            end_date = None
            time_range = event.get('timeRangeV2')
            if time_range:
                starts_at = time_range.get('startsAt')
                ends_at = time_range.get('endsAt')
                
                # Convertir les timestamps millisecondes en datetime
                if starts_at:
                    start_date = datetime.fromtimestamp(starts_at / 1000).isoformat()
                if ends_at:
                    end_date = datetime.fromtimestamp(ends_at / 1000).isoformat()
            
            # Extraire la location (si présente)
            location = event.get('location')
            if location and isinstance(location, dict):
                location = json.dumps(location)
            
            # Extraire le mode d'assistance depuis settings
            attendee_mode = None
            settings = event.get('settings', {})
            if settings:
                attendee_mode = settings.get('attendanceMode')
            
            results.append({
                'organization_id': self.organization_id,
                'page_id': self.page_id,
                'event_urn': event.get('$URN'),
                'event_id': event.get('id'),
                'organizer': event.get('organizer'),
                'title': title,
                'description': description,
                'start_date': start_date,
                'end_date': end_date,
                'time_zone': event.get('eventTimezone'),
                'lifecycle_state': event.get('lifeCycleState'),
                'attendee_mode': attendee_mode,
                'location': location,
                'registration_count': event.get('registrationCount', 0),
                'vanity_name': event.get('vanityName'),
                'ugc_post': event.get('ugcPost'),
                'broadcast_tool': event.get('broadcastTool'),
                'settings': json.dumps(settings) if settings else None,
                'retrieved_at': datetime.now()
            })

        print(f"  ✓ {len(results)} événements")
        return results

    # ==================== PUBLISHING ENDPOINTS ====================

    def get_content_series(self, max_results: int = 100) -> List[Dict]:
        """
        Récupère les séries de contenu (newsletters)
        Utilise le finder q=owner avec urn:li:organization (pas organizationalPage)
        """
        print("\n→ Content Series")

        # IMPORTANT: Doit utiliser urn:li:organization, pas organizationalPage
        owner_urn = self.organization_urn

        all_elements = []
        start = 0
        count = 10  # Taille de page selon la doc

        while len(all_elements) < max_results:
            params = {
                'q': 'owner',
                'owner': owner_urn,
                'start': start,
                'count': count
            }

            url = f"{self.base_url}/dmaContentSeries?{urlencode(params)}"

            try:
                response = self._make_request(url)
                data = response.json()

                elements = data.get('elements', [])
                if not elements:
                    break

                all_elements.extend(elements)
                start += count

                # Vérifier s'il y a plus de résultats
                paging = data.get('paging', {})
                if not paging.get('links') or start >= max_results:
                    break

            except Exception as e:
                print(f"  ✗ Erreur: {e}")
                break

        results = []
        for series in all_elements:
            results.append({
                'organization_id': self.organization_id,
                'page_id': self.page_id,
                'series_urn': series.get('contentSeriesUrn'),
                'owner': series.get('owner'),
                'title': json.dumps(series.get('title')) if series.get('title') else None,
                'description': json.dumps(series.get('description')) if series.get('description') else None,
                'issues': json.dumps(series.get('issues')) if series.get('issues') else None,
                'subscriber_count': series.get('subscriberCount'),
                'cadence': series.get('cadence'),
                'latest_issue': series.get('latestIssue'),
                'created': json.dumps(series.get('created')) if series.get('created') else None,
                'last_modified': json.dumps(series.get('lastModified')) if series.get('lastModified') else None,
                'retrieved_at': datetime.now()
            })

        print(f"  ✓ {len(results)} séries")
        return results

    def get_original_articles(self, max_results: int = 500) -> List[Dict]:
        """
        Récupère les articles originaux
        Utilise le finder q=author avec urn:li:organization (pas organizationalPage)
        """
        print("\n→ Original Articles")

        # IMPORTANT: Doit utiliser urn:li:organization, pas organizationalPage
        author_urn = self.organization_urn

        all_elements = []
        start = 0
        count = 50  # Taille de batch raisonnable

        while len(all_elements) < max_results:
            params = {
                'q': 'author',
                'author': author_urn,
                'start': start,
                'count': count
                # Note: 'state' n'est pas un paramètre valide pour dmaOriginalArticles
            }

            url = f"{self.base_url}/dmaOriginalArticles?{urlencode(params)}"

            try:
                response = self._make_request(url)
                data = response.json()

                elements = data.get('elements', [])
                if not elements:
                    break

                all_elements.extend(elements)
                start += count

                # Vérifier s'il y a plus de résultats
                paging = data.get('paging', {})
                if not paging.get('links') or start >= max_results:
                    break

            except Exception as e:
                print(f"  ✗ Erreur: {e}")
                break

        results = []
        for article in all_elements:
            results.append({
                'organization_id': self.organization_id,
                'page_id': self.page_id,
                'article_urn': article.get('linkedInArticleUrn'),
                'title': json.dumps(article.get('title')) if article.get('title') else None,
                'content_html': article.get('contentHtml'),
                'state': article.get('state'),
                'author': article.get('author'),
                'published_at': datetime.fromtimestamp(article.get('publishedAt', 0) / 1000) if article.get('publishedAt') else None,
                'created_at': datetime.fromtimestamp(article.get('createdAt', 0) / 1000) if article.get('createdAt') else None,
                'last_modified_at': datetime.fromtimestamp(article.get('lastModifiedAt', 0) / 1000) if article.get('lastModifiedAt') else None,
                'cover_image': json.dumps(article.get('coverImage')) if article.get('coverImage') else None,
                'retrieved_at': datetime.now()
            })

        print(f"  ✓ {len(results)} articles")
        return results

    # ==================== BIGQUERY UPLOAD ====================

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
            else:
                self.bq_client = bigquery.Client(project=self.project_id)
        return self.bq_client

    def upload_to_bigquery(self, data: List[Dict], table_name: str,
                          schema: List[bigquery.SchemaField],
                          write_disposition: str = "WRITE_TRUNCATE") -> None:
        """Upload les données vers BigQuery"""
        if not data:
            print(f"  ⚠️  Aucune donnée pour {table_name}")
            return

        try:
            client = self._get_bigquery_client()
            df = pd.DataFrame(data)

            table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"

            job_config = bigquery.LoadJobConfig(
                schema=schema,
                write_disposition=write_disposition,
                create_disposition="CREATE_IF_NEEDED"
            )

            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
            job.result()

            table = client.get_table(table_id)
            print(f"  ✓ {table_name}: {table.num_rows:,} lignes")

        except Exception as e:
            print(f"  ✗ Erreur {table_name}: {e}")
            raise

    # ==================== MAIN SCRAPER ====================

    def scrape_all(self) -> Dict[str, List[Dict]]:
        """
        Scrape les 3 tables principales pour la page LinkedIn

        Returns:
            Dictionnaire avec les données de chaque endpoint
        """
        print("=" * 80)
        print("LINKEDIN PAGE DMA - SCRAPING COMPLET")
        print("=" * 80)
        print(f"\nOrganisation: {self.org_urn}")
        print(f"BigQuery: {self.project_id}.{self.dataset_id}")

        all_data = {}

        # Table 1: Page Statistics (métriques globales agrégées)
        print("\n" + "=" * 80)
        print("TABLE 1: PAGE STATISTICS")
        print("=" * 80)
        all_data['page_statistics'] = self.get_page_statistics()

        # Table 2: Followers (liste des followers avec consentement DMA)
        print("\n" + "=" * 80)
        print("TABLE 2: FOLLOWERS")
        print("=" * 80)
        all_data['followers'] = self.get_followers()

        # Table 3: Page Content Analytics (analytics par post - vide pour le moment)
        print("\n" + "=" * 80)
        print("TABLE 3: PAGE CONTENT ANALYTICS")
        print("=" * 80)
        all_data['page_content_analytics'] = self.get_page_content_analytics_dma()

        return all_data


def main():
    """Script principal"""

    # Charger la configuration
    print("📋 Chargement de la configuration...")
    is_cloud_function = os.getenv('FUNCTION_TARGET') is not None
    config_path = os.path.join(os.path.dirname(__file__), '../../config.yaml' if not is_cloud_function else '../config.yaml')
    config = load_config(config_path, skip_credentials_check=is_cloud_function)

    linkedin_config = config.get_linkedin_config()
    google_config = config.get_google_cloud_config()

    # Récupérer les paramètres
    ACCESS_TOKEN = linkedin_config.get('access_token')
    ORGANIZATION_ID = linkedin_config.get('organization_id')
    PAGE_ID = linkedin_config.get('page_id')  # Récupérer le page_id de la config

    if not ACCESS_TOKEN or not ORGANIZATION_ID:
        print("❌ ERREUR: access_token ou organization_id manquant dans config.yaml")
        return

    PROJECT_ID = google_config['project_id']
    DATASET_ID = google_config.get('datasets', {}).get('linkedin_page', 'linkedin_page')
    CREDENTIALS_PATH = None if is_cloud_function else google_config.get('credentials_file')

    # Initialiser le client avec le page_id
    client = LinkedInPageDMAClient(
        access_token=ACCESS_TOKEN,
        organization_id=ORGANIZATION_ID,
        page_id=PAGE_ID,  # Passer le page_id explicitement
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        credentials_path=CREDENTIALS_PATH
    )

    # Scraper toutes les données
    all_data = client.scrape_all()

    # Sauvegarder en JSON local
    print("\n" + "=" * 80)
    print("EXPORT LOCAL")
    print("=" * 80)

    os.makedirs('data_exports', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    for table_name, data in all_data.items():
        if data:
            filename = f"data_exports/{table_name}_{timestamp}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            print(f"  ✓ {filename}: {len(data)} lignes")

    print("\n" + "=" * 80)
    print("✓ SCRAPING TERMINÉ!")
    print("=" * 80)

    # Afficher le résumé
    print("\n📊 Résumé:")
    for table_name, data in all_data.items():
        print(f"  - {table_name}: {len(data)} lignes")


if __name__ == "__main__":
    main()
