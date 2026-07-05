#!/usr/bin/env python3
"""
Wrapper pour linkedin_ads_library.py
Patch le chemin de configuration pour Cloud Run Jobs
"""

import os
import sys

# Forcer le chemin de configuration pour Cloud Run Job
CONFIG_PATH = '/app/config.yaml'

# Importer et patcher le module
sys.path.insert(0, os.path.dirname(__file__))

# Monkey patch pour forcer le bon chemin de config
original_join = os.path.join

def patched_join(*args):
    """Version patchée de os.path.join qui détecte et corrige le chemin config"""
    result = original_join(*args)
    # Si le chemin ressemble à un chemin relatif vers config.yaml depuis scripts/
    if 'config.yaml' in result and ('../..' in result or '..' in result):
        return CONFIG_PATH
    return result

# Appliquer le patch
os.path.join = patched_join

# Maintenant importer le script original
from scripts import linkedin_ads_library

# Restaurer os.path.join
os.path.join = original_join

def main():
    """Execute le script avec le bon chemin de config"""
    linkedin_ads_library.main()

if __name__ == "__main__":
    main()
