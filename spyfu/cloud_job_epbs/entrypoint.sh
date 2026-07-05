#!/bin/bash
#
# Entrypoint pour Cloud Run Job - SpyFu Monthly Collection
# Exécute tous les scripts SpyFu mensuels
#

set -e

echo "============================================================"
echo "  SpyFu Monthly Collection - Cloud Run Job"
echo "============================================================"
echo "📅 Démarré le: $(date '+%Y-%m-%d %H:%M:%S')"
echo "🔧 Config: ${SPYFU_CONFIG_FILE:-config.yaml}"
echo ""

# Se placer dans le répertoire spyfu
cd /app/spyfu

# Utiliser le fichier de config spécifié par la variable d'environnement
export SPYFU_CONFIG_PATH="${SPYFU_CONFIG_FILE:-config.yaml}"

# Compteur de succès/échecs
SUCCESS_COUNT=0
FAILED_COUNT=0
FAILED_SCRIPTS=()

# Fonction pour exécuter un script
run_script() {
    local script_name=$1
    local table_name=$2

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📊 Table: $table_name"
    echo "🔧 Script: $script_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if python3 -c "
import sys
import os
sys.path.insert(0, '/app')
os.chdir('/app/spyfu')

# Forcer le config
os.environ['SPYFU_CONFIG_PATH'] = '/app/spyfu/${SPYFU_CONFIG_PATH}'

# Importer et patcher config_loader
import config_loader
_original_load_config = config_loader.load_config

def patched_load_config(config_path='config.yaml', skip_credentials_check=False):
    return _original_load_config(os.environ['SPYFU_CONFIG_PATH'], True)

config_loader.load_config = patched_load_config

# Exécuter le script
with open('scripts/${script_name}') as f:
    code = compile(f.read(), 'scripts/${script_name}', 'exec')
    exec(code, {'__name__': '__main__', '__file__': 'scripts/${script_name}'})
"; then
        echo "✅ SUCCESS: $table_name"
        ((SUCCESS_COUNT++))
    else
        echo "❌ FAILED: $table_name"
        ((FAILED_COUNT++))
        FAILED_SCRIPTS+=("$script_name ($table_name)")
    fi

    # Pause de 2 secondes entre chaque script
    sleep 2
}

# ============================================================
# Exécution des scripts mensuels
# ============================================================

# 1. Domain Ad History
run_script "spyfu_domain_ad_history.py" "domain_ad_history"

# 2. Domain Stats
run_script "spyfu_domain_stats.py" "domain_stats"

# 3. Most Valuable Keywords
run_script "spyfu_most_valuable_keywords.py" "most_valuable_keywords"

# 4. New Keywords
run_script "spyfu_new_keywords.py" "new_keywords"

# 5. Newly Ranked Keywords
run_script "spyfu_newly_ranked_keywords.py" "newly_ranked_keywords"

# 6. PPC Keywords
run_script "spyfu_ppc_keywords.py" "ppc_keywords"

# 7. Related Keywords
run_script "spyfu_related_keywords.py" "related_keywords"

# 8. SEO Keywords
run_script "spyfu_seo_keywords.py" "seo_keywords"

# 9. Term Ad History
run_script "spyfu_term_ad_history.py" "term_ad_history"

# 10. Top Pages
run_script "spyfu_top_pages.py" "top_pages"

# ============================================================
# Résumé
# ============================================================

echo ""
echo "============================================================"
echo "  Résumé de l'exécution"
echo "============================================================"
echo "✅ Succès: $SUCCESS_COUNT"
echo "❌ Échecs: $FAILED_COUNT"
echo ""

if [ $FAILED_COUNT -gt 0 ]; then
    echo "⚠️  Scripts en échec:"
    for script in "${FAILED_SCRIPTS[@]}"; do
        echo "   - $script"
    done
    echo ""
fi

echo "📅 Terminé le: $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"

# Code de sortie
if [ $FAILED_COUNT -gt 0 ]; then
    exit 1
else
    exit 0
fi
