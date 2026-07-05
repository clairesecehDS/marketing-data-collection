#!/bin/bash
#
# Script de collecte complète SpyFu pour EPBS
# Exécute tous les scripts de collecte et upload vers BigQuery
#
# Tables concernées:
# - domain_ad_history
# - domain_stats
# - most_valuable_keywords
# - new_keywords
# - newly_ranked_keywords
# - ppc_keywords
# - related_keywords
# - seo_keywords
# - term_ad_history
# - top_pages
#
# Usage: ./run_all_spyfu_epbs.sh
#

# Note: Pas de set -e car on veut continuer même si un script échoue

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Forcer l'utilisation du config.yaml local (spyfu/config.yaml)
# Par défaut utiliser config.yaml, mais permettre de passer un autre fichier
CONFIG_FILE="${1:-config.yaml}"
export SPYFU_CONFIG_PATH="$SCRIPT_DIR/$CONFIG_FILE"

echo "🔧 Configuration: $CONFIG_FILE"

echo "============================================================"
echo "  SpyFu - Collecte complète pour EPBS"
echo "============================================================"
echo "📅 Démarré le: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

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

    if python3 run_script_with_local_config.py "$script_name"; then
        echo "✅ SUCCESS: $table_name"
        ((SUCCESS_COUNT++))
    else
        echo "❌ FAILED: $table_name"
        ((FAILED_COUNT++))
        FAILED_SCRIPTS+=("$script_name ($table_name)")
    fi

    # Pause de 2 secondes entre chaque script pour éviter le rate limiting
    sleep 2
}

# ============================================================
# Exécution des scripts
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
