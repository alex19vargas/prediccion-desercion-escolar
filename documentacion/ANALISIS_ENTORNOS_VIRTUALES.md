# 🔍 Análisis de Entornos Virtuales

**Fecha**: 20 de octubre de 2025  
**Proyecto**: Predicción de Deserción Escolar

---

## 🎯 Resumen Ejecutivo

Se encontraron **3 entornos virtuales** en el proyecto:

1. **`/Trabajo_Grado/.venv`** (Raíz) - ❌ **INNECESARIO - ELIMINAR**
2. **`/proyecto_desercion/.venv`** - ✅ **PRINCIPAL - CONSERVAR**
3. **`/proyecto_desercion/venv`** - ⚠️ **ANTIGUO - ELIMINAR**

---

## 📊 Comparación Detallada

### 1️⃣ Trabajo_Grado/.venv (RAÍZ)

```
📍 Ubicación: /Users/alexandervargas/Trabajo_Grado/.venv
📦 Tamaño: 545 MB
🐍 Python: 3.9.6
📚 Paquetes: 33
📅 Última modificación: 2 de octubre
```

**Paquetes clave instalados:**
- scikit-learn 1.6.1
- pandas 2.3.3
- numpy 2.0.2
- seaborn 0.13.2
- plotly 6.3.1
- xgboost 2.1.4
- catboost 1.2.8
- ❌ **NO tiene Flask** (necesario para la app web)
- ❌ **NO tiene SQLAlchemy** (necesario para la base de datos)

**Análisis:**
- Este entorno está en la **carpeta padre** del proyecto
- **NO es necesario** porque el proyecto real está en `proyecto_desercion/`
- Fue creado primero (2 de octubre) pero luego se creó el correcto dentro del proyecto
- **NO tiene las dependencias web** (Flask, SQLAlchemy)

**🚫 RECOMENDACIÓN: ELIMINAR**

---

### 2️⃣ proyecto_desercion/.venv (PRINCIPAL)

```
📍 Ubicación: /Users/alexandervargas/Trabajo_Grado/proyecto_desercion/.venv
📦 Tamaño: 589 MB
🐍 Python: 3.9.6
📚 Paquetes: 53
📅 Última modificación: 14 de octubre
```

**Paquetes clave instalados:**
- ✅ **Flask 3.1.2** (App web)
- ✅ **SQLAlchemy 2.0.44** (Base de datos)
- ✅ **WTForms 3.2.1** (Formularios)
- ✅ **Flask-Login** (Autenticación)
- ✅ **Werkzeug 3.1.3** (WSGI)
- ✅ scikit-learn 1.6.1 (ML)
- ✅ pandas 2.3.3 (Data)
- ✅ numpy 2.0.2 (Numerical)
- ✅ seaborn 0.13.2 (Viz)
- ✅ catboost 1.2.8 (ML)
- ✅ plotly 5.18.0 (Viz)
- ✅ python-dotenv 1.1.1 (Config)

**Análisis:**
- Este es el entorno **MÁS COMPLETO** (53 paquetes)
- Tiene **TODAS las dependencias** necesarias:
  - ✅ Machine Learning (scikit-learn, catboost, xgboost)
  - ✅ Data Science (pandas, numpy, scipy)
  - ✅ Visualización (matplotlib, seaborn, plotly)
  - ✅ Web (Flask, SQLAlchemy, WTForms)
- Está en la **ubicación correcta** (dentro de proyecto_desercion/)
- Es el **más reciente** (14 de octubre)

**✅ RECOMENDACIÓN: CONSERVAR (Este es el correcto)**

---

### 3️⃣ proyecto_desercion/venv (ANTIGUO)

```
📍 Ubicación: /Users/alexandervargas/Trabajo_Grado/proyecto_desercion/venv
📦 Tamaño: 472 MB
🐍 Python: 3.9.6
📚 Paquetes: 41
📅 Última modificación: 14 de octubre
```

**Paquetes clave instalados:**
- Flask 2.0.1 (versión antigua)
- Flask-Login 0.5.0 (versión antigua)
- Flask-SQLAlchemy 2.5.1 (versión antigua)
- numpy 1.24.4 (versión antigua)
- pandas 2.0.3 (versión antigua)
- scikit-learn 1.3.2 (versión antigua)

**Análisis:**
- Este fue el primer intento de entorno dentro del proyecto
- Tiene **versiones antiguas** de los paquetes
- Fue reemplazado por `.venv` el mismo día (14 de octubre)
- **NO se está usando** actualmente

**🚫 RECOMENDACIÓN: ELIMINAR**

---

## 🎯 ¿Cuál se está usando actualmente?

### Análisis de uso:

1. **Python del sistema**: `/Users/alexandervargas/opt/anaconda3/bin/python` (3.8.8)
   - ⚠️ Los modelos se están ejecutando con **Anaconda 3.8.8**, NO con ningún venv

2. **Evidencia**:
   - Ejecutaste los modelos exitosamente
   - Los modelos se ejecutaron con el Python de Anaconda
   - Las dependencias están instaladas en Anaconda

3. **Conclusión**:
   - ✅ **Actualmente usas Anaconda 3.8.8** para ejecutar los modelos
   - ⚠️ Los entornos virtuales existen pero **NO se están usando**

---

## 📋 Plan de Acción Recomendado

### Opción 1: Usar Anaconda (Actual) ✅ RECOMENDADO

**Pros:**
- ✅ Ya funciona todo
- ✅ No requiere cambios
- ✅ Anaconda tiene todo instalado

**Contras:**
- ⚠️ Mezcla proyectos
- ⚠️ No es reproducible

**Acciones:**
```bash
# Eliminar los 3 entornos virtuales no usados
rm -rf /Users/alexandervargas/Trabajo_Grado/.venv
rm -rf /Users/alexandervargas/Trabajo_Grado/proyecto_desercion/.venv
rm -rf /Users/alexandervargas/Trabajo_Grado/proyecto_desercion/venv

# Esto liberará ~1.6 GB de espacio en disco
```

### Opción 2: Migrar a .venv (Mejor práctica) ⭐ IDEAL

**Pros:**
- ✅ Entorno aislado
- ✅ Reproducible
- ✅ Mejores prácticas
- ✅ Fácil de compartir

**Contras:**
- ⚠️ Requiere reconfigurar VS Code
- ⚠️ Necesitas activar el entorno

**Acciones:**
```bash
# 1. Eliminar entornos innecesarios
rm -rf /Users/alexandervargas/Trabajo_Grado/.venv
rm -rf /Users/alexandervargas/Trabajo_Grado/proyecto_desercion/venv

# 2. Conservar solo proyecto_desercion/.venv

# 3. Activar el entorno en VS Code
# En VS Code: Cmd+Shift+P -> "Python: Select Interpreter"
# Elegir: ./proyecto_desercion/.venv/bin/python

# 4. Instalar dependencias faltantes (si hay)
cd /Users/alexandervargas/Trabajo_Grado/proyecto_desercion
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install flask flask-sqlalchemy flask-login wtforms

# 5. Ejecutar modelos con el nuevo entorno
.venv/bin/python modelos/modelo_desercion_nuevo.py
```

---

## 🎁 Beneficios de Limpiar

### Espacio liberado:
- Trabajo_Grado/.venv: **545 MB**
- proyecto_desercion/venv: **472 MB**
- **Total liberado: ~1 GB** 🎉

### Simplicidad:
- ✅ Solo 1 entorno (o ninguno si usas Anaconda)
- ✅ Menos confusión
- ✅ Más fácil de mantener

---

## ⚠️ Antes de Eliminar

### Backup de seguridad (opcional):

```bash
# Si quieres hacer backup antes de eliminar
cd /Users/alexandervargas/Trabajo_Grado
tar -czf backup_venvs_$(date +%Y%m%d).tar.gz .venv proyecto_desercion/.venv proyecto_desercion/venv
```

---

## 🚀 Comandos para Limpiar

### Si decides usar Anaconda (Opción 1):

```bash
cd /Users/alexandervargas/Trabajo_Grado

# Eliminar todos los venv
rm -rf .venv
rm -rf proyecto_desercion/.venv
rm -rf proyecto_desercion/venv

echo "✅ Entornos virtuales eliminados. Espacio liberado: ~1.6 GB"
```

### Si decides usar .venv (Opción 2):

```bash
cd /Users/alexandervargas/Trabajo_Grado

# Eliminar solo los innecesarios
rm -rf .venv
rm -rf proyecto_desercion/venv

# Conservar proyecto_desercion/.venv

echo "✅ Entornos innecesarios eliminados. Espacio liberado: ~1 GB"
echo "⚠️ Recuerda configurar VS Code para usar proyecto_desercion/.venv"
```

---

## 📝 Resumen Final

### Situación actual:
- Tienes **3 entornos virtuales** pero usas **Anaconda**
- Los venv ocupan **~1.6 GB** sin uso
- Todo funciona correctamente con Anaconda

### Recomendación:

**Mi recomendación es la Opción 1**: Eliminar todos los venv y seguir usando Anaconda

**Razones:**
1. ✅ Ya funciona todo perfectamente
2. ✅ No requiere cambios de configuración
3. ✅ Liberas 1.6 GB de espacio
4. ✅ Más simple

**Si prefieres seguir mejores prácticas**, usa la Opción 2 y migra a `.venv`

---

## 🎯 Decisión

### ¿Qué entornos eliminar?

| Entorno | Acción | Razón |
|---------|--------|-------|
| `Trabajo_Grado/.venv` | ❌ **ELIMINAR** | Fuera del proyecto, incompleto |
| `proyecto_desercion/.venv` | ✅ **CONSERVAR** | Más completo, correcta ubicación |
| `proyecto_desercion/venv` | ❌ **ELIMINAR** | Antiguo, versiones desactualizadas |

### O bien:

Si sigues usando Anaconda:
- ❌ Eliminar **TODOS** (liberas 1.6 GB)

---

**Creado**: 20 de octubre de 2025  
**Estado**: Análisis completo  
**Próxima acción**: Decidir entre Opción 1 (Anaconda) u Opción 2 (.venv)
