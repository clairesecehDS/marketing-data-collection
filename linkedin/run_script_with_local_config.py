#!/usr/bin/env python3
"""
Wrapper pour exécuter les scripts LinkedIn avec le config.yaml local
Force l'utilisation de linkedin/config.yaml au lieu du config.yaml à la racine
"""

import sys
import os
from pathlib import Path

# Forcer le répertoire courant à linkedin/
script_dir = Path(__file__).parent
os.chdir(script_dir)

# Ajouter le chemin vers le module config_loader
sys.path.insert(0, str(script_dir.parent))

# Déterminer le fichier de config à utiliser
# 1. Variable d'environnement LINKEDIN_CONFIG_PATH (définie par run_all_linkedin.sh)
# 2. Sinon, utiliser config.yaml par défaut
config_to_use = os.environ.get('LINKEDIN_CONFIG_PATH', str(script_dir / "config.yaml"))

print(f"🔧 [Wrapper] Utilisation du config: {config_to_use}")

# Monkey patch pour forcer l'utilisation du config spécifié
import config_loader

_original_load_config = config_loader.load_config

def patched_load_config(config_path: str = "config.yaml", skip_credentials_check: bool = False):
    """Version patchée qui utilise le config spécifié par LINKEDIN_CONFIG_PATH ou config.yaml"""
    return _original_load_config(config_to_use, skip_credentials_check)

config_loader.load_config = patched_load_config

# Maintenant importer et exécuter le script demandé
if len(sys.argv) < 2:
    print("Usage: python3 run_script_with_local_config.py <script_name.py>")
    sys.exit(1)

script_name = sys.argv[1]
script_path = script_dir / "scripts" / script_name

if not script_path.exists():
    print(f"❌ Script non trouvé: {script_path}")
    sys.exit(1)

# Exécuter le script
print(f"🚀 Exécution de {script_name} avec config local...")
with open(script_path) as f:
    code = compile(f.read(), script_path, 'exec')
    exec(code, {'__name__': '__main__', '__file__': str(script_path)})
