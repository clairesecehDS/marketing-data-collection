#!/bin/bash
#
# Script master pour déployer tous les Cloud Run Jobs SpyFu
#

set -e

echo "============================================================"
echo "  Déploiement de tous les Cloud Run Jobs SpyFu"
echo "============================================================"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Rendre tous les scripts exécutables
chmod +x *.sh

echo "📋 Jobs à déployer:"
echo "  1. ecoledesponts"
echo "  2. international-sos-479209"
echo "  3. verbus-480211 - events"
echo "  4. verbus-480211 - scolaires"
echo "  5. verbus-480211 - transport"
echo "  6. verbus-480211 - voyages"
echo ""

read -p "Continuer avec le déploiement de tous les jobs? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Déploiement annulé"
    exit 1
fi

SUCCESS_COUNT=0
FAILED_COUNT=0
FAILED_JOBS=()

deploy_job() {
    local script=$1
    local name=$2

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🚀 Déploiement: $name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if ./$script; then
        echo "✅ SUCCESS: $name"
        ((SUCCESS_COUNT++))
    else
        echo "❌ FAILED: $name"
        ((FAILED_COUNT++))
        FAILED_JOBS+=("$name")
    fi

    echo ""
    sleep 5  # Pause entre chaque déploiement
}

# Déploiements
deploy_job "deploy_ecoledesponts.sh" "ecoledesponts"
deploy_job "deploy_international_sos.sh" "international-sos-479209"
deploy_job "deploy_verbus_events.sh" "verbus-480211 (events)"
deploy_job "deploy_verbus_scolaires.sh" "verbus-480211 (scolaires)"
deploy_job "deploy_verbus_transport.sh" "verbus-480211 (transport)"
deploy_job "deploy_verbus_voyages.sh" "verbus-480211 (voyages)"

# Résumé
echo ""
echo "============================================================"
echo "  Résumé du déploiement"
echo "============================================================"
echo "✅ Succès: $SUCCESS_COUNT"
echo "❌ Échecs: $FAILED_COUNT"
echo ""

if [ $FAILED_COUNT -gt 0 ]; then
    echo "⚠️  Jobs en échec:"
    for job in "${FAILED_JOBS[@]}"; do
        echo "   - $job"
    done
    echo ""
    exit 1
else
    echo "🎉 Tous les jobs ont été déployés avec succès!"
    echo ""
    echo "📅 Planning d'exécution (1er de chaque mois, heure de Paris):"
    echo "  1h00 - ecoledesponts"
    echo "  1h00 - international-sos-479209"
    echo "  1h10 - verbus (events)"
    echo "  1h20 - verbus (scolaires)"
    echo "  1h30 - verbus (transport)"
    echo "  1h40 - verbus (voyages)"
    echo ""
    exit 0
fi
