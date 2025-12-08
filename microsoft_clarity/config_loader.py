#!/usr/bin/env python3
"""
Configuration Loader
Charge et valide le fichier de configuration YAML
"""

import yaml
import os
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigLoader:
    """Charge et gère la configuration depuis config.yaml"""

    def __init__(self, config_path: str = "config.yaml"):
        """
        Initialise le loader de configuration

        Args:
            config_path: Chemin vers le fichier config.yaml
        """
        # Si le chemin est relatif, chercher à partir de la racine du projet
        config_path_obj = Path(config_path)
        
        if not config_path_obj.is_absolute():
            # Remonter jusqu'à trouver config.yaml à la racine du projet
            current_dir = Path(__file__).parent
            
            # Chercher config.yaml dans le répertoire courant et les parents
            for parent in [current_dir] + list(current_dir.parents):
                potential_config = parent / config_path
                if potential_config.exists():
                    config_path_obj = potential_config
                    break
        
        self.config_path = config_path_obj
        self.config = None
        self._load_config()

    def _load_config(self):
        """Charge le fichier de configuration"""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"❌ Fichier de configuration non trouvé : {self.config_path}\n"
                f"   Copiez config.example.yaml en config.yaml et configurez-le."
            )

        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        print(f"✓ Configuration chargée depuis {self.config_path}")

    def get(self, path: str, default: Any = None) -> Any:
        """
        Récupère une valeur de configuration par son chemin

        Args:
            path: Chemin de la clé (ex: "linkedin.oauth.client_id")
            default: Valeur par défaut si la clé n'existe pas

        Returns:
            Valeur de configuration
        """
        keys = path.split('.')
        value = self.config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value

    def get_google_cloud_config(self) -> Dict[str, Any]:
        """Récupère la configuration Google Cloud"""
        credentials_file = self.get('google_cloud.credentials_file')
        
        # Convertir le chemin relatif en chemin absolu par rapport au fichier config.yaml
        if credentials_file and not os.path.isabs(credentials_file):
            # Si le chemin est relatif, le résoudre par rapport au répertoire du config.yaml
            config_dir = self.config_path.parent
            credentials_file = str(config_dir / credentials_file)
        
        return {
            'project_id': self.get('google_cloud.project_id'),
            'credentials_file': credentials_file,
            'location': self.get('google_cloud.location', 'EU'),
            'datasets': {
                # LinkedIn datasets (4 datasets selon SETUP_GUIDE.md)
                'linkedin_ads_advertising': self.get('google_cloud.datasets.linkedin_ads'),
                'linkedin_ads_library': self.get('google_cloud.datasets.linkedin_library'),
                'linkedin_leadgen_form': self.get('google_cloud.datasets.linkedin_leadgen'),
                'linkedin_page': self.get('google_cloud.datasets.linkedin_page'),
                # Autres datasets
                'microsoft_clarity': self.get('google_cloud.datasets.clarity'),
                'spyfu': self.get('google_cloud.datasets.spyfu'),
                # Alias pour compatibilité
                'linkedin': self.get('google_cloud.datasets.linkedin_ads'),
            }
        }

    def get_linkedin_config(self) -> Dict[str, Any]:
        """Récupère la configuration LinkedIn"""
        return {
            'access_token': self.get('linkedin.oauth.access_token'),
            'client_id': self.get('linkedin.oauth.client_id'),
            'client_secret': self.get('linkedin.oauth.client_secret'),
            'refresh_token': self.get('linkedin.oauth.refresh_token'),
            'account_id': self.get('linkedin.account_id'),
            'organization_id': self.get('linkedin.organization_id'),
            'start_date': self.get('linkedin.collection.start_date'),
            'end_date': self.get('linkedin.collection.end_date'),
            'granularity': self.get('linkedin.collection.granularity', 'DAILY'),
            'api_version': self.get('linkedin.collection.api_version', '202509'),
            'pivots': self.get('linkedin.analytics.pivots', ['CAMPAIGN', 'CREATIVE']),
            'metrics': self.get('linkedin.metrics', {}),
            'oauth': self.get('linkedin.oauth', {}),
            'ads_library': {
                'keywords': self.get('linkedin.ads_library.keywords', []),
                'advertisers': self.get('linkedin.ads_library.advertisers', []),
                'countries': self.get('linkedin.ads_library.countries', ['FR']),
                'max_results_per_search': self.get('linkedin.ads_library.max_results_per_search', 500),
            },
        }

    def get_clarity_config(self) -> Dict[str, Any]:
        """Récupère la configuration Microsoft Clarity"""
        return {
            'project_id': self.get('microsoft_clarity.project_id'),
            'api_key': self.get('microsoft_clarity.api_key'),
            'base_url': self.get('microsoft_clarity.api.base_url'),
            'num_of_days': self.get('microsoft_clarity.api.num_of_days', 1),
            'metrics': self.get('microsoft_clarity.metrics', {}),
            'name': self.get('microsoft_clarity.name', self.get('microsoft_clarity.project_id')),
        }

    def get_spyfu_config(self) -> Dict[str, Any]:
        """Récupère la configuration SpyFu"""
        return {
            'api_key': self.get('spyfu.api_key'),
            'country_code': self.get('spyfu.global.country_code', 'FR'),
            'page_size': self.get('spyfu.global.page_size', 1000),
            'domains': {
                'primary': self.get('spyfu.domains.primary'),
                'competitors': self.get('spyfu.domains.competitors', []),
                'all': [self.get('spyfu.domains.primary')] +
                       self.get('spyfu.domains.competitors', [])
            },
            'comparisons': self.get('spyfu.comparisons', []),
            'filters': self.get('spyfu.filters', {}),
            'endpoints': {
                'ppc_keywords': self.get('spyfu.ppc_keywords', {}),
                'new_keywords': self.get('spyfu.new_keywords', {}),
                'paid_serps': self.get('spyfu.paid_serps', {}),
                'seo_keywords': self.get('spyfu.seo_keywords', {}),
                'newly_ranked': self.get('spyfu.newly_ranked', {}),
                'outrank_comparison': self.get('spyfu.outrank_comparison', {}),
                'top_pages': self.get('spyfu.top_pages', {}),
                'ppc_competitors': self.get('spyfu.ppc_competitors', {}),
            }
        }

    def get_automation_config(self) -> Dict[str, Any]:
        """Récupère la configuration d'automatisation"""
        return {
            'schedules': self.get('automation.schedules', {}),
            'logging': self.get('automation.logging', {}),
        }

    def get_export_config(self) -> Dict[str, Any]:
        """Récupère la configuration d'export"""
        return {
            'formats': self.get('export.formats', {}),
            'backup': self.get('export.backup', {}),
        }

    def get_monitoring_config(self) -> Dict[str, Any]:
        """Récupère la configuration de monitoring"""
        return {
            'alerts': self.get('monitoring.alerts', {}),
            'dashboard': self.get('monitoring.dashboard', {}),
        }

    def get_advanced_config(self) -> Dict[str, Any]:
        """Récupère les paramètres avancés"""
        return {
            'timeouts': self.get('advanced.timeouts', {}),
            'retry': self.get('advanced.retry', {}),
            'rate_limiting': self.get('advanced.rate_limiting', {}),
            'deduplication': self.get('advanced.deduplication', {}),
        }

    def get_development_config(self) -> Dict[str, Any]:
        """Récupère la configuration de développement"""
        return {
            'debug_mode': self.get('development.debug_mode', False),
            'dry_run': self.get('development.dry_run', False),
            'limit_results': self.get('development.limit_results'),
            'verbose': self.get('development.verbose', False),
        }

    def validate(self, skip_credentials_check: bool = False) -> bool:
        """
        Valide la configuration

        Args:
            skip_credentials_check: Si True, ne valide pas l'existence du fichier credentials
                                   (utile pour Cloud Functions avec authentification par défaut)

        Returns:
            True si valide, False sinon
        """
        errors = []

        # Vérifier Google Cloud
        if not self.get('google_cloud.project_id'):
            errors.append("❌ google_cloud.project_id manquant")

        # Vérifier le fichier credentials avec chemin absolu (sauf si skip_credentials_check=True)
        if not skip_credentials_check:
            google_config = self.get_google_cloud_config()
            credentials_file = google_config.get('credentials_file')
            if credentials_file and not os.path.exists(credentials_file):
                errors.append(f"❌ Fichier credentials non trouvé : {credentials_file}")

        # Vérifier LinkedIn
        if not self.get('linkedin.oauth.client_id'):
            errors.append("⚠️  linkedin.oauth.client_id manquant")

        if not self.get('linkedin.oauth.refresh_token'):
            errors.append("⚠️  linkedin.oauth.refresh_token manquant")

        # Vérifier Clarity
        if not self.get('microsoft_clarity.project_id'):
            errors.append("⚠️  microsoft_clarity.project_id manquant")

        if not self.get('microsoft_clarity.api_key'):
            errors.append("⚠️  microsoft_clarity.api_key manquant")

        # Vérifier SpyFu
        if not self.get('spyfu.api_key'):
            errors.append("⚠️  spyfu.api_key manquant")

        if not self.get('spyfu.domains.primary'):
            errors.append("⚠️  spyfu.domains.primary manquant")

        # Afficher les erreurs
        if errors:
            print("\n🔧 Validation de la configuration :")
            for error in errors:
                print(f"  {error}")
            print()

            # Seulement les erreurs critiques empêchent l'exécution
            critical_errors = [e for e in errors if e.startswith("❌")]
            if critical_errors:
                return False

        return True

    def print_summary(self):
        """Affiche un résumé de la configuration"""
        print("\n" + "=" * 60)
        print("Configuration Summary")
        print("=" * 60)

        print("\n📊 Google Cloud:")
        print(f"  Project ID: {self.get('google_cloud.project_id')}")
        print(f"  Location: {self.get('google_cloud.location')}")

        print("\n🔗 LinkedIn:")
        print(f"  Account ID: {self.get('linkedin.account_id')}")
        print(f"  Pivots: {', '.join(self.get('linkedin.analytics.pivots', []))}")

        print("\n🔍 Microsoft Clarity:")
        print(f"  Project ID: {self.get('microsoft_clarity.project_id')}")
        print(f"  Days: {self.get('microsoft_clarity.api.num_of_days')}")

        print("\n🎯 SpyFu:")
        print(f"  Primary Domain: {self.get('spyfu.domains.primary')}")
        competitors = self.get('spyfu.domains.competitors', [])
        print(f"  Competitors: {len(competitors)} domaines")
        for comp in competitors:
            print(f"    - {comp}")

        print("\n⏰ Automation:")
        linkedin_schedule = self.get('automation.schedules.linkedin', {})
        clarity_schedule = self.get('automation.schedules.clarity', {})
        spyfu_schedule = self.get('automation.schedules.spyfu', {})
        print(f"  LinkedIn Analytics: {linkedin_schedule.get('campaign_analytics', 'N/A')}")
        print(f"  Clarity: {clarity_schedule.get('analytics', 'N/A')}")
        print(f"  SpyFu Keywords: {spyfu_schedule.get('ppc_keywords', 'N/A')}")

        print("\n" + "=" * 60 + "\n")


# Fonction helper pour charger rapidement la config
def load_config(config_path: str = "config.yaml", skip_credentials_check: bool = False) -> ConfigLoader:
    """
    Charge et valide la configuration

    Args:
        config_path: Chemin vers le fichier config.yaml
        skip_credentials_check: Si True, ne valide pas l'existence du fichier credentials

    Returns:
        Instance de ConfigLoader

    Raises:
        FileNotFoundError: Si config.yaml n'existe pas
        SystemExit: Si la configuration est invalide
    """
    try:
        config = ConfigLoader(config_path)

        if not config.validate(skip_credentials_check=skip_credentials_check):
            print("\n❌ Configuration invalide. Veuillez corriger les erreurs ci-dessus.")
            raise SystemExit(1)

        return config

    except FileNotFoundError as e:
        print(f"\n{e}")
        print("\n💡 Pour commencer :")
        print("   1. cp config.example.yaml config.yaml")
        print("   2. Éditer config.yaml avec vos credentials")
        print("   3. Relancer le script")
        raise SystemExit(1)


# Exemple d'utilisation
if __name__ == "__main__":
    # Charger et valider la configuration
    config = load_config()

    # Afficher le résumé
    config.print_summary()

    # Exemples d'accès aux valeurs
    print("\n📝 Exemples d'utilisation :\n")

    # Accès simple
    print(f"Project ID: {config.get('google_cloud.project_id')}")

    # Accès avec valeur par défaut
    print(f"Debug mode: {config.get('development.debug_mode', False)}")

    # Récupérer toute une section
    linkedin_config = config.get_linkedin_config()
    print(f"LinkedIn Account: {linkedin_config['account_id']}")

    spyfu_config = config.get_spyfu_config()
    print(f"SpyFu Domains: {spyfu_config['domains']['all']}")
