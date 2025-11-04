#!/bin/bash

# Script de verificación del entorno de desarrollo
# Proyecto: Predicción de Deserción Escolar

echo "🔍 Verificando configuración del proyecto..."
echo ""

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar Python
echo "1️⃣  Verificando Python..."
if command -v python3.9 &> /dev/null; then
    PYTHON_VERSION=$(python3.9 --version)
    echo -e "${GREEN}✅ $PYTHON_VERSION instalado${NC}"
else
    echo -e "${RED}❌ Python 3.9 no encontrado${NC}"
fi
echo ""

# Verificar entorno virtual
echo "2️⃣  Verificando entorno virtual..."
if [ -d ".venv" ]; then
    echo -e "${GREEN}✅ Entorno virtual .venv existe${NC}"
    
    # Activar y verificar paquetes
    source .venv/bin/activate
    
    echo "   Verificando paquetes principales:"
    
    # Flask
    if python -c "import flask" 2>/dev/null; then
        FLASK_VERSION=$(python -c "import flask; print(flask.__version__)")
        echo -e "   ${GREEN}✅ Flask $FLASK_VERSION${NC}"
    else
        echo -e "   ${RED}❌ Flask no instalado${NC}"
    fi
    
    # Pandas
    if python -c "import pandas" 2>/dev/null; then
        PANDAS_VERSION=$(python -c "import pandas; print(pandas.__version__)")
        echo -e "   ${GREEN}✅ Pandas $PANDAS_VERSION${NC}"
    else
        echo -e "   ${RED}❌ Pandas no instalado${NC}"
    fi
    
    # Scikit-learn
    if python -c "import sklearn" 2>/dev/null; then
        SKLEARN_VERSION=$(python -c "import sklearn; print(sklearn.__version__)")
        echo -e "   ${GREEN}✅ Scikit-learn $SKLEARN_VERSION${NC}"
    else
        echo -e "   ${RED}❌ Scikit-learn no instalado${NC}"
    fi
    
    # CatBoost
    if python -c "import catboost" 2>/dev/null; then
        CATBOOST_VERSION=$(python -c "import catboost; print(catboost.__version__)")
        echo -e "   ${GREEN}✅ CatBoost $CATBOOST_VERSION${NC}"
    else
        echo -e "   ${RED}❌ CatBoost no instalado${NC}"
    fi
    
    # XGBoost
    if python -c "import xgboost" 2>/dev/null; then
        XGBOOST_VERSION=$(python -c "import xgboost; print(xgboost.__version__)")
        echo -e "   ${GREEN}✅ XGBoost $XGBOOST_VERSION${NC}"
    else
        echo -e "   ${RED}❌ XGBoost no instalado${NC}"
    fi
    
else
    echo -e "${RED}❌ Entorno virtual no encontrado${NC}"
fi
echo ""

# Verificar base de datos
echo "3️⃣  Verificando base de datos..."
if [ -f "instance/app.db" ]; then
    DB_SIZE=$(du -h instance/app.db | cut -f1)
    echo -e "${GREEN}✅ Base de datos existe ($DB_SIZE)${NC}"
else
    echo -e "${YELLOW}⚠️  Base de datos no encontrada${NC}"
    echo "   Ejecuta: python init_db.py"
fi
echo ""

# Verificar archivos de configuración
echo "4️⃣  Verificando configuración..."
if [ -f ".env" ]; then
    echo -e "${GREEN}✅ Archivo .env existe${NC}"
else
    echo -e "${YELLOW}⚠️  Archivo .env no encontrado${NC}"
fi

if [ -d ".vscode" ]; then
    echo -e "${GREEN}✅ Configuración de VS Code existe${NC}"
else
    echo -e "${YELLOW}⚠️  Configuración de VS Code no encontrada${NC}"
fi
echo ""

# Verificar datos
echo "5️⃣  Verificando datos..."
if [ -d "datos/Dataset_Completa" ]; then
    echo -e "${GREEN}✅ Dataset completo encontrado${NC}"
else
    echo -e "${YELLOW}⚠️  Dataset completo no encontrado${NC}"
fi

if [ -d "resultados" ]; then
    echo -e "${GREEN}✅ Directorio de resultados existe${NC}"
else
    echo -e "${YELLOW}⚠️  Directorio de resultados no encontrado${NC}"
fi
echo ""

# Verificar que Flask puede iniciar
echo "6️⃣  Verificando Flask..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
    if python -c "from backend.app import create_app; create_app()" 2>/dev/null; then
        echo -e "${GREEN}✅ Flask se inicializa correctamente${NC}"
    else
        echo -e "${RED}❌ Error al inicializar Flask${NC}"
    fi
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 COMANDOS ÚTILES:"
echo ""
echo "  Activar entorno virtual:"
echo "    source .venv/bin/activate"
echo ""
echo "  Iniciar servidor Flask:"
echo "    python run.py"
echo ""
echo "  Ejecutar modelo:"
echo "    python modelos/modelo_desercion_escolar.py"
echo ""
echo "  Ver documentación:"
echo "    open documentacion/INDICE_DOCUMENTACION.md"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
