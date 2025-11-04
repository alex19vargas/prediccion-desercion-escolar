# 📦 Gestión de Dependencias del Proyecto

**Fecha**: 21 de octubre de 2025  
**Python**: 3.9.6  
**Entorno virtual**: `.venv`

---

## 📋 Archivos de Requirements

Este proyecto mantiene **dos archivos** de requirements para diferentes propósitos:

### 1️⃣ **`requirements.txt`** - PRODUCCIÓN ✅

**Propósito**: Despliegue en producción y entornos de prueba

**Características**:
- ✅ Versiones **exactas** con `==`
- ✅ Incluye **todas las dependencias** transitivas
- ✅ **53 paquetes** especificados
- ✅ 100% reproducible
- ✅ Generado desde el entorno real

**Cuándo usar**:
- 🚀 Despliegue en producción
- 🧪 Configuración de CI/CD
- 📦 Crear contenedores Docker
- 🔒 Entornos que requieren reproducibilidad exacta

**Comando**:
```bash
pip install -r requirements.txt
```

---

### 2️⃣ **`requirements-dev.txt`** - DESARROLLO 🛠️

**Propósito**: Desarrollo local y actualizaciones de paquetes

**Características**:
- 🔄 Versiones **mínimas** con `>=`
- 🎯 Solo dependencias **principales** (no transitivas)
- 📦 ~35 paquetes base
- 🔓 Permite actualizaciones compatibles
- 💡 Más flexible para desarrollo

**Cuándo usar**:
- 💻 Desarrollo local
- 🔧 Actualizar dependencias
- 🧑‍💻 Configuración inicial de entorno
- 🆕 Agregar nuevas librerías

**Comando**:
```bash
pip install -r requirements-dev.txt
```

---

## 🔄 Flujo de Trabajo Recomendado

### Para nuevos desarrolladores:

```bash
# 1. Crear entorno virtual
python3 -m venv .venv

# 2. Activar entorno
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 3. Instalar dependencias EXACTAS de producción
pip install -r requirements.txt
```

### Para desarrollo activo:

```bash
# Activar entorno
source .venv/bin/activate

# Instalar con versiones flexibles (permite actualizaciones)
pip install -r requirements-dev.txt

# Actualizar paquetes si es necesario
pip install --upgrade scikit-learn pandas
```

---

## 🔧 Mantenimiento

### Actualizar `requirements.txt` después de cambios:

```bash
# Activar entorno
source .venv/bin/activate

# Generar nuevo requirements.txt con versiones exactas
pip freeze > requirements.txt

# Revisar y limpiar el archivo (remover paquetes innecesarios)
# Mantener solo los necesarios para el proyecto
```

### Actualizar `requirements-dev.txt`:

Editar manualmente agregando nuevas dependencias con versiones mínimas:

```txt
# Ejemplo: agregar nueva librería
nueva-libreria>=1.0.0
```

---

## 📦 Dependencias Principales

### Machine Learning:
- `scikit-learn` - Algoritmos ML
- `catboost` - Gradient Boosting
- `xgboost` - Extreme Gradient Boosting

### Data Science:
- `pandas` - Manipulación de datos
- `numpy` - Operaciones numéricas
- `scipy` - Computación científica

### Web Framework:
- `Flask` - Framework web
- `SQLAlchemy` - ORM para base de datos
- `Flask-Login` - Autenticación

### Visualización:
- `matplotlib` - Gráficos estáticos
- `seaborn` - Gráficos estadísticos
- `plotly` - Gráficos interactivos

---

## ⚠️ Notas Importantes

### XGBoost en macOS:

Si encuentras errores con `xgboost`, instala `libomp`:

```bash
brew install libomp
```

### Verificar instalación:

```bash
# Ver paquetes instalados
pip list

# Verificar versión de Python
python --version

# Verificar ubicación del entorno
which python
```

### Conflictos de dependencias:

Si hay conflictos, usa `requirements.txt` (versiones exactas probadas):

```bash
pip install --force-reinstall -r requirements.txt
```

---

## 🎯 Resumen

| Archivo | Uso | Versiones | Cuándo |
|---------|-----|-----------|--------|
| **requirements.txt** | Producción | Exactas `==` | Despliegue, CI/CD |
| **requirements-dev.txt** | Desarrollo | Mínimas `>=` | Dev local, updates |

---

## 📚 Recursos

- [pip requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Managing Dependencies](https://packaging.python.org/tutorials/managing-dependencies/)

---

**Última actualización**: 21 de octubre de 2025  
**Mantenedor**: Proyecto Deserción Escolar  
**Python Version**: 3.9.6
