#!/bin/bash

# 🚀 INICIO RÁPIDO - Proyecto Deserción Escolar
# ============================================

clear

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║   🎓 PROYECTO DESERCIÓN ESCOLAR                          ║"
echo "║   📊 Sistema de Predicción con Machine Learning          ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar si el entorno está activado
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}⚠️  El entorno virtual no está activado${NC}"
    echo ""
    echo "Activando entorno virtual..."
    source .venv/bin/activate
    echo -e "${GREEN}✅ Entorno activado${NC}"
else
    echo -e "${GREEN}✅ Entorno virtual ya está activado${NC}"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${BLUE}📋 OPCIONES DISPONIBLES:${NC}"
echo ""
echo "  1) Iniciar servidor Flask (Dashboard Web)"
echo "  2) Ejecutar modelo base"
echo "  3) Ejecutar modelo nuevo"
echo "  4) Ejecutar modelo balanceado"
echo "  5) Verificar entorno"
echo "  6) Ver documentación"
echo "  7) Salir"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -n "Selecciona una opción [1-7]: "

read option

case $option in
    1)
        echo ""
        echo -e "${GREEN}🚀 Iniciando servidor Flask...${NC}"
        echo ""
        echo "  📍 URL: http://localhost:5000"
        echo "  🛑 Presiona Ctrl+C para detener el servidor"
        echo ""
        python run.py
        ;;
    2)
        echo ""
        echo -e "${GREEN}🤖 Ejecutando Modelo Base...${NC}"
        echo ""
        python modelos/modelo_desercion_escolar.py
        ;;
    3)
        echo ""
        echo -e "${GREEN}🤖 Ejecutando Modelo Nuevo...${NC}"
        echo ""
        python modelos/modelo_desercion_nuevo.py
        ;;
    4)
        echo ""
        echo -e "${GREEN}🤖 Ejecutando Modelo Balanceado...${NC}"
        echo ""
        python modelos/modelo_desercion_balanceado.py
        ;;
    5)
        echo ""
        ./verificar_entorno.sh
        ;;
    6)
        echo ""
        echo -e "${BLUE}📚 Abriendo documentación...${NC}"
        open documentacion/INDICE_DOCUMENTACION.md
        ;;
    7)
        echo ""
        echo -e "${GREEN}👋 ¡Hasta luego!${NC}"
        echo ""
        exit 0
        ;;
    *)
        echo ""
        echo -e "${YELLOW}⚠️  Opción inválida${NC}"
        echo ""
        ;;
esac
