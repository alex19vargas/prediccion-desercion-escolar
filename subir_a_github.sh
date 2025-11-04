#!/bin/bash

# ============================================
# Script de Preparación para GitHub y Despliegue
# Proyecto: Predicción de Deserción Escolar
# ============================================

clear

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║          🚀 PREPARACIÓN PARA DESPLIEGUE - GITHUB & RENDER                ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función para pausar
pause() {
    echo ""
    read -p "Presiona ENTER para continuar..."
    echo ""
}

# ============================================
# PASO 1: Verificar archivos necesarios
# ============================================

echo -e "${BLUE}📋 PASO 1: Verificando archivos necesarios...${NC}"
echo ""

required_files=("Procfile" "runtime.txt" "requirements-production.txt" ".gitignore" "README.md")
all_present=true

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✅${NC} $file"
    else
        echo -e "  ${RED}❌${NC} $file - FALTA"
        all_present=false
    fi
done

if [ "$all_present" = false ]; then
    echo ""
    echo -e "${RED}⚠️  Faltan archivos necesarios. Ejecuta los pasos de preparación primero.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Todos los archivos necesarios están presentes${NC}"
pause

# ============================================
# PASO 2: Inicializar Git
# ============================================

echo -e "${BLUE}📦 PASO 2: Inicializando repositorio Git...${NC}"
echo ""

if [ -d ".git" ]; then
    echo -e "${YELLOW}⚠️  Ya existe un repositorio git${NC}"
    read -p "¿Deseas reinicializar? (s/n): " reinit
    if [ "$reinit" = "s" ]; then
        rm -rf .git
        git init
        echo -e "${GREEN}✅ Repositorio reinicializado${NC}"
    fi
else
    git init
    echo -e "${GREEN}✅ Repositorio inicializado${NC}"
fi

pause

# ============================================
# PASO 3: Configurar Git (si es necesario)
# ============================================

echo -e "${BLUE}👤 PASO 3: Configurando Git...${NC}"
echo ""

git_name=$(git config user.name 2>/dev/null)
git_email=$(git config user.email 2>/dev/null)

if [ -z "$git_name" ]; then
    read -p "Tu nombre: " name
    git config --global user.name "$name"
    echo -e "${GREEN}✅ Nombre configurado${NC}"
else
    echo -e "${GREEN}✅ Nombre: $git_name${NC}"
fi

if [ -z "$git_email" ]; then
    read -p "Tu email: " email
    git config --global user.email "$email"
    echo -e "${GREEN}✅ Email configurado${NC}"
else
    echo -e "${GREEN}✅ Email: $git_email${NC}"
fi

pause

# ============================================
# PASO 4: Agregar archivos a Git
# ============================================

echo -e "${BLUE}📁 PASO 4: Agregando archivos al repositorio...${NC}"
echo ""

echo "Archivos que se van a subir:"
git add .
git status --short | head -20
echo ""
echo "(Mostrando primeros 20 archivos...)"

pause

# ============================================
# PASO 5: Hacer commit inicial
# ============================================

echo -e "${BLUE}💾 PASO 5: Haciendo commit inicial...${NC}"
echo ""

git commit -m "Initial commit: Sistema de Predicción de Deserción Escolar

- Implementación completa del sistema web con Flask
- 9 algoritmos de ML entrenados (3 datasets)
- Mejor modelo: Random Forest (99.80% accuracy)
- Dashboard interactivo con visualizaciones
- Documentación completa del proyecto
- Listo para despliegue en producción"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Commit realizado exitosamente${NC}"
else
    echo -e "${RED}❌ Error al hacer commit${NC}"
    exit 1
fi

pause

# ============================================
# PASO 6: Instrucciones para GitHub
# ============================================

echo -e "${BLUE}🌐 PASO 6: Crear repositorio en GitHub${NC}"
echo ""
echo "Por favor, sigue estos pasos:"
echo ""
echo "1. Ve a https://github.com"
echo "2. Haz clic en '+' (arriba derecha) → 'New repository'"
echo "3. Configura:"
echo "   • Name: prediccion-desercion-escolar"
echo "   • Description: Sistema de predicción de deserción escolar con ML"
echo "   • Visibility: Public"
echo "   • NO marques 'Initialize with README'"
echo "4. Clic en 'Create repository'"
echo ""

pause

echo -e "${BLUE}🔗 PASO 7: Conectar con GitHub${NC}"
echo ""
echo "Copia y pega el comando que GitHub te muestra."
echo "Será algo como:"
echo ""
echo -e "${YELLOW}git remote add origin https://github.com/TU_USUARIO/prediccion-desercion-escolar.git${NC}"
echo ""
read -p "Ingresa el comando completo aquí: " remote_cmd
echo ""

eval $remote_cmd

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Repositorio remoto configurado${NC}"
else
    echo -e "${RED}❌ Error al configurar repositorio remoto${NC}"
    exit 1
fi

pause

# ============================================
# PASO 8: Subir a GitHub
# ============================================

echo -e "${BLUE}⬆️  PASO 8: Subiendo código a GitHub...${NC}"
echo ""

git branch -M main
echo -e "${GREEN}✅ Rama principal configurada como 'main'${NC}"
echo ""

echo "Subiendo código..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅✅✅ ¡CÓDIGO SUBIDO EXITOSAMENTE A GITHUB! ✅✅✅${NC}"
else
    echo ""
    echo -e "${YELLOW}⚠️  Si te pide autenticación:${NC}"
    echo "   • Username: tu usuario de GitHub"
    echo "   • Password: usa un Personal Access Token (no tu contraseña)"
    echo ""
    echo "Para crear un token:"
    echo "   GitHub → Settings → Developer settings → Personal access tokens"
    echo "   → Tokens (classic) → Generate new token"
    echo "   Permisos necesarios: repo"
    exit 1
fi

pause

# ============================================
# PASO 9: Siguiente paso - Despliegue
# ============================================

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║                   ✅ PROYECTO SUBIDO A GITHUB ✅                          ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}🎉 ¡Felicidades! Tu proyecto ya está en GitHub${NC}"
echo ""
echo -e "${BLUE}📍 PRÓXIMOS PASOS:${NC}"
echo ""
echo "1. Ve a tu repositorio en GitHub y verifica que todo esté ahí"
echo "2. Lee la GUIA_DESPLIEGUE.md para desplegar en Render"
echo "3. Sigue las instrucciones de la guía paso a paso"
echo ""
echo -e "${YELLOW}📖 Comandos útiles:${NC}"
echo ""
echo "  # Ver el README de despliegue"
echo "  open GUIA_DESPLIEGUE.md"
echo ""
echo "  # Actualizar el código en el futuro"
echo "  git add ."
echo "  git commit -m 'Descripción de cambios'"
echo "  git push origin main"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${GREEN}🚀 Listo para desplegar en Render o Vercel${NC}"
echo ""
