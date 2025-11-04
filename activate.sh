#!/bin/bash

# Script de activación del entorno virtual
# Proyecto: Predicción de Deserción Escolar

echo "🚀 Activando entorno virtual .venv..."

# Verificar que existe el entorno
if [ ! -d ".venv" ]; then
    echo "❌ Error: No se encuentra el entorno virtual .venv"
    echo "📦 Créalo con: python3.9 -m venv .venv"
    exit 1
fi

# Activar el entorno
source .venv/bin/activate

# Verificar activación
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "✅ Entorno virtual activado correctamente"
    echo ""
    echo "📍 Ubicación: $VIRTUAL_ENV"
    echo "🐍 Python: $(python --version)"
    echo "📦 Pip: $(pip --version | awk '{print $2}')"
    echo ""
    echo "📊 Paquetes instalados: $(pip list | wc -l | xargs)"
    echo ""
    echo "💡 Comandos disponibles:"
    echo "  • python modelos/modelo_desercion_nuevo.py"
    echo "  • python modelos/modelo_desercion_escolar.py"
    echo "  • python run.py  (iniciar Flask)"
    echo "  • deactivate     (salir del entorno)"
    echo ""
else
    echo "❌ Error: No se pudo activar el entorno virtual"
    exit 1
fi
