#!/bin/bash
#
# Script de collecte complète LinkedIn
# Exécute tous les scripts de collecte et upload vers BigQuery
#
# Dataset linkedin_ads_advertising:
# - campaign_analytics
# - campaign_budget
# - creative_analytics
# - creative_budget
#
# Dataset linkedin_ads_library:
# - ads_library
#
# Dataset linkedin_leadgen_form:
# - lead_form_metrics
# - lead_form_responses
# - lead_forms
#
# Usage: ./run_all_linkedin.sh [config_file]
# Exemples:
#   ./run_all_linkedin.sh              # Utilise config.yaml par défaut
#   ./run_all_linkedin.sh config_epbs.yaml  # Utilise config_epbs.yaml
#

# Note: Pas de set -e car on veut continuer même si un script échoue

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Forcer l'utilisation du config.yaml local (linkedin/config.yaml)
# Par défaut utiliser config.yaml, mais permettre de passer un autre fichier
CONFIG_FILE="${1:-config.yaml}"
export LINKEDIN_CONFIG_PATH="$SCRIPT_DIR/$CONFIG_FILE"

echo "🔧 Configuration: $CONFIG_FILE"

echo "============================================================"
echo "  LinkedIn - Collecte complète"
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
    local dataset=$3

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📊 Dataset: $dataset"
    echo "📋 Table: $table_name"
    echo "🔧 Script: $script_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if python3 run_script_with_local_config.py "$script_name"; then
        echo "✅ SUCCESS: $dataset.$table_name"
        ((SUCCESS_COUNT++))
    else
        echo "❌ FAILED: $dataset.$table_name"
        ((FAILED_COUNT++))
        FAILED_SCRIPTS+=("$script_name ($dataset.$table_name)")
    fi

    # Pause de 2 secondes entre chaque script pour éviter le rate limiting
    sleep 2
}

# ============================================================
# Dataset: linkedin_ads_advertising
# ============================================================

echo ""
echo "🎯 Dataset: linkedin_ads_advertising"
echo ""

# 1. Campaign Analytics (campaign_analytics)
run_script "linkedin_campaign_analytics.py" "campaign_analytics" "linkedin_ads_advertising"

# 2. Campaign Budget (campaign_budget) - Note: le script s'appelle linkedin_budget.py
run_script "linkedin_budget.py" "campaign_budget + creative_budget" "linkedin_ads_advertising"

# Note: creative_analytics et creative_budget sont inclus dans le script linkedin_campaign_analytics.py
# Le script linkedin_budget.py gère les deux tables campaign_budget et creative_budget

# ============================================================
# Dataset: linkedin_ads_library
# ============================================================

echo ""
echo "📚 Dataset: linkedin_ads_library"
echo ""

# 3. Ads Library (ads_library)
run_script "linkedin_ads_library.py" "ads_library" "linkedin_ads_library"

# ============================================================
# Dataset: linkedin_leadgen_form
# ============================================================

echo ""
echo "📝 Dataset: linkedin_leadgen_form"
echo ""

# 4. Lead Forms (lead_forms + lead_form_metrics + lead_form_responses)
run_script "linkedin_lead_forms.py" "lead_forms + lead_form_metrics + lead_form_responses" "linkedin_leadgen_form"

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
