# Sistema de Predicción de Deserción Escolar

## 📋 Descripción
Este proyecto implementa un sistema web para la predicción de deserción escolar utilizando técnicas de aprendizaje automático. El sistema proporciona una interfaz web interactiva que permite visualizar y analizar los resultados de diferentes modelos de machine learning, facilitando la identificación temprana de estudiantes en riesgo de deserción.

## 🎯 Objetivos
- Predecir con precisión el riesgo de deserción escolar
- Identificar factores clave que influyen en la deserción
- Proporcionar una interfaz web intuitiva para analizar resultados
- Visualizar y comparar el rendimiento de diferentes modelos
- Facilitar la toma de decisiones preventivas basada en datos

## 🏗️ Estructura del Proyecto
```
proyecto_desercion/
├── backend/                    # Backend Flask
│   ├── routes/
│   │   ├── auth_routes.py     # Rutas de autenticación
│   │   └── dashboard_routes.py # Rutas del dashboard
│   ├── app.py                 # Aplicación Flask principal
│   ├── config.py             # Configuración de la aplicación
│   └── models.py             # Modelos de la base de datos
├── frontend/                   # Frontend web
│   ├── static/
│   │   ├── css/             # Estilos CSS
│   │   ├── js/              # Scripts JavaScript
│   │   └── img/             # Imágenes y gráficos generados
│   └── templates/
│       ├── base.html        # Plantilla base
│       ├── login.html       # Página de inicio de sesión
│       └── dashboard.html   # Dashboard principal
├── modelos/                    # Modelos de Machine Learning
│   ├── modelo_desercion_escolar.py     # Modelo Base (BD original)
│   ├── modelo_desercion_nuevo.py       # Modelo Nuevo (BD completa)
│   ├── modelo_desercion_balanceado.py  # Modelo Balanceado (75/25) ✨ NUEVO
│   ├── modelo_desercion.py             # Modelo alternativo
│   ├── evaluador.py                    # Evaluación y métricas
│   ├── gestionar_resultados.py         # Gestión de resultados
│   ├── modelo_con_inscrito.py          # Modelo legacy (inscrito)
│   └── modelo_con_terminado.py         # Modelo legacy (terminado)
├── resultados/                 # Resultados organizados por modelo
│   ├── modelo_base/           # 9 modelos entrenados
│   ├── modelo_nuevo/          # 9 modelos entrenados
│   └── modelo_balanceado/     # 9 modelos con dataset balanceado ✨ NUEVO
├── datos/                      # Datasets y bases de datos
│   ├── crear_dataset_balanceado.py  # Script para balancear datos ✨ NUEVO
│   └── datos_finales_75_25.csv      # Dataset balanceado (75/25) ✨ NUEVO
├── .venv/                      # Entorno virtual Python (589 MB, 53 paquetes)
├── .vscode/                    # Configuración de VS Code
├── instance/                   # Instancia de base de datos
├── .env                       # Variables de entorno
├── .python-version            # Versión de Python (3.9.6)
├── activate.sh                # Script de activación del entorno
├── requirements.txt           # Dependencias producción (53 paquetes exactos)
├── requirements-dev.txt       # Dependencias desarrollo (versiones flexibles)
├── run.py                     # Script para ejecutar la aplicación
├── init_db.py                 # Inicialización de base de datos
├── README.md                  # Este archivo
└── documentacion/             # 11 archivos de documentación técnica
    ├── INDICE_DOCUMENTACION.md              # Índice maestro
    ├── REQUIREMENTS_INFO.md                 # Guía de dependencias
    ├── CORRECCION_COMPLETA_TIPOS.md         # Correcciones de tipos
    ├── MIGRACION_VENV_COMPLETA.md           # Migración de entorno
    ├── VERIFICACION_COMPLETA_MODELOS.md     # Resultados de modelos
    ├── RESUMEN_GRAFICOS_INTUITIVOS.md       # Gráficos implementados
    ├── RESUMEN_REORGANIZACION_FINAL.md      # Reorganización
    ├── REORGANIZACION_REQUIREMENTS.md       # Cambios en requirements
    ├── ANALISIS_ENTORNOS_VIRTUALES.md       # Análisis de entornos
    ├── CORRECCION_LEARNING_CURVE.md         # Fix de learning_curve
    └── ACTUALIZACION_README.md              # Actualización del README
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.9.6**: Lenguaje principal
- **Flask 3.1.2**: Framework web
- **SQLAlchemy 2.0.44**: ORM para base de datos
- **Flask-Login 0.6.3**: Manejo de autenticación
- **Flask-Migrate 4.1.0**: Migraciones de base de datos

### Machine Learning
- **scikit-learn 1.6.1**: Implementación de modelos ML
- **pandas 2.3.3**: Manipulación y análisis de datos
- **numpy 2.0.2**: Operaciones numéricas
- **scipy 1.13.1**: Computación científica
- **catboost 1.2.8**: Gradient Boosting avanzado
- **xgboost 2.1.4**: Extreme Gradient Boosting
- **joblib 1.5.2**: Serialización de modelos

### Visualización
- **matplotlib 3.9.4**: Gráficos estáticos profesionales
- **seaborn 0.13.2**: Gráficos estadísticos elegantes
- **plotly 5.18.0**: Gráficos interactivos y dinámicos

### Frontend
- **HTML5/CSS3**: Estructura y estilos
- **JavaScript**: Interactividad en el cliente
- **Bootstrap**: Framework CSS para diseño responsivo

## 🚀 Instalación y Configuración

### Requisitos Previos
- **Python 3.9.6** (recomendado) o superior
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)
- **Navegador web moderno** (Chrome, Firefox, Safari)
- **~589 MB** de espacio en disco para el entorno virtual
- **macOS** (libomp requerido para XGBoost): `brew install libomp`

### Pasos de Instalación

1. **Clonar el repositorio** (o descargar el código):
```bash
git clone [URL_DEL_REPOSITORIO]
cd proyecto_desercion
```

2. **Activar el entorno virtual existente**:
```bash
# El proyecto ya incluye un entorno .venv configurado
source .venv/bin/activate  # macOS/Linux

# O usar el script de activación
./activate.sh
```

**Nota**: Si necesitas crear un nuevo entorno desde cero:
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

3. Instalar dependencias:

   **Para producción** (versiones exactas probadas):
   ```bash
   pip install -r requirements.txt
   ```
   
   **Para desarrollo** (versiones flexibles):
   ```bash
   pip install -r requirements-dev.txt
   ```
   
   > 📚 Ver [REQUIREMENTS_INFO.md](documentacion/REQUIREMENTS_INFO.md) para más detalles sobre la gestión de dependencias.

4. Configurar variables de entorno:
```bash
# Crear archivo .env en la raíz del proyecto
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///app.db  # O tu URL de base de datos
```

5. Inicializar la base de datos:
```bash
python backend/init_db.py
```

6. Crear directorio para imágenes:
```bash
mkdir -p frontend/static/img
```

7. Ejecutar la aplicación:
```bash
python run.py
```

### Acceso a la Aplicación
- URL: `http://localhost:5000`
- Credenciales de prueba:
  - Admin: `admin` / `admin123`
  - Docente: `docente` / `docente123`

## 📊 Características del Sistema

### Interfaz Web Rediseñada para Docentes ✨ NUEVO
- **Dashboard para Educadores**: Interfaz no técnica enfocada en identificación de estudiantes en riesgo
- **Resumen Ejecutivo**: Página principal con estadísticas clave y alertas visuales
- **Sistema de Autenticación**: Control de acceso seguro con roles
- **Visualización Interactiva**: Modal de zoom para imágenes, tablas expandibles, código de colores
- **API REST**: Endpoints que sirven datos en tiempo real desde el dataset
- **6 Secciones Organizadas**: 
  - Resumen Ejecutivo (principal)
  - Métricas de Rendimiento
  - Curvas de Aprendizaje
  - Gráficos Intuitivos
  - Matrices de Confusión
  - Galería Completa

### Gestión de Estudiantes en Riesgo ✨ NUEVO
- **Análisis en Tiempo Real**: Datos actualizados desde `datos_balanceados_75_25.xlsx`
- **Clasificación por Niveles**: Alto, Medio y Bajo riesgo con códigos de color
- **Identificación de Factores**: Muestra factores específicos de riesgo por estudiante
- **Acciones Sugeridas**: Recomendaciones personalizadas para cada caso
- **Vista Expandible**: "Ver todos" para mostrar la lista completa de estudiantes

### Modelos de Machine Learning Implementados
El sistema entrena y compara **9 algoritmos diferentes**:

1. **Random Forest** - Ensamble de árboles de decisión
2. **Gradient Boosting** - Boosting secuencial robusto
3. **CatBoost** - Gradient Boosting optimizado para categóricas
4. **XGBoost** - Extreme Gradient Boosting de alto rendimiento
5. **AdaBoost** - Adaptive Boosting
6. **Decision Tree** - Árbol de decisión interpretable
7. **K-Nearest Neighbors (KNN)** - Clasificación por vecindad
8. **Logistic Regression** - Regresión logística baseline
9. **Neural Network (MLP)** - Red neuronal multicapa

### Datasets Disponibles
El proyecto incluye **3 conjuntos de datos** para experimentación:

1. **Dataset Original** (`modelo_base`) - 84% No Desertor / 16% Desertor
2. **Dataset Completo** (`modelo_nuevo`) - Base de datos ampliada
3. **Dataset Balanceado** (`modelo_balanceado`) ✨ **NUEVO**
   - Proporción: 75% No Desertor / 25% Desertor
   - Total: 5,000 registros
   - Técnica: Oversampling con `sklearn.utils.resample`
   - Mejora significativa en la detección de desertores

**Total de modelos entrenados**: 27 (9 algoritmos × 3 datasets)

### Visualizaciones y Métricas

#### Gráficos Tradicionales (para expertos):
- **Matrices de Confusión**: Evaluación visual del rendimiento
- **Curvas ROC y AUC**: Análisis de la capacidad predictiva
- **Curvas Precisión-Recall**: Evaluación del balance precisión-recall
- **Curvas de Aprendizaje**: Análisis de convergencia del modelo
- **Importancia de Características**: Análisis de variables relevantes

#### Gráficos Intuitivos (para público no técnico):
- **Gráficos de Barras de Predicción**: Comparación visual de predicciones correctas vs incorrectas
- **Distribución de Clases**: Visualización del balance entre clases
- **Análisis de Errores**: Desglose detallado de tipos de error
- **Rendimiento Comparativo**: Comparación entre modelos de forma accesible

> 📊 Ver [RESUMEN_GRAFICOS_INTUITIVOS.md](documentacion/RESUMEN_GRAFICOS_INTUITIVOS.md) para más detalles

### API REST ✨ ACTUALIZADO
El backend proporciona **3 endpoints principales**:

#### `/api/metricas`
- Devuelve métricas de rendimiento de los 9 algoritmos
- Formato: JSON con accuracy, precision, recall, f1-score, ROC AUC
- Uso: Alimenta la sección "Métricas" del dashboard

#### `/api/imagenes`
- Lista todas las visualizaciones disponibles del modelo activo
- Formato: JSON con URL, categoría, nombre del modelo y archivo
- Categorías: `curvas`, `graficos_intuitivos`, `matrices`
- Uso: Alimenta las galerías de imágenes del dashboard

#### `/api/estudiantes-riesgo` ✨ NUEVO
- Analiza el dataset y devuelve estudiantes en riesgo de deserción
- Lee desde: `datos_balanceados_75_25.xlsx`
- Formato: JSON con totales por nivel y array de estudiantes
- Estructura de respuesta:
  ```json
  {
    "total": 5000,
    "riesgo_alto": 22,
    "riesgo_medio": 45,
    "riesgo_bajo": 78,
    "estudiantes": [
      {
        "id": "EST001",
        "nivel_riesgo": "alto",
        "probabilidad": 87,
        "factores": "Bajo rendimiento académico, Faltas frecuentes",
        "accion_sugerida": "Intervención inmediata del orientador"
      }
    ]
  }
  ```
- Uso: Alimenta el Resumen Ejecutivo con datos reales

**Características de la API:**
- ✅ Rutas protegidas con autenticación (`@login_required`)
- ✅ Serve imágenes desde `resultados/{MODELO_ACTIVO}/` dinámicamente
- ✅ Sin necesidad de copiar archivos a carpetas estáticas
- ✅ Actualización automática al cambiar MODELO_ACTIVO

## 🔍 Uso del Sistema

### Acceso al Dashboard
1. Iniciar sesión en `http://localhost:5000`
2. Navegar por las diferentes secciones del dashboard:
   - **Resumen Ejecutivo**: Vista principal con estadísticas de estudiantes en riesgo
   - **Métricas**: Rendimiento técnico de los 9 algoritmos
   - **Curvas**: Curvas ROC, Precision-Recall y Learning Curves
   - **Gráficos Intuitivos**: Visualizaciones simplificadas para docentes
   - **Matrices**: Matrices de confusión de todos los modelos
   - **Todas**: Galería completa de visualizaciones

### 🎯 Configuración del Modelo Activo en la Interfaz Web

El dashboard web lee directamente desde la carpeta del **modelo configurado como activo**. Por defecto, está configurado `modelo_balanceado` (mejor balance entre clases).

#### Cambiar el Modelo Mostrado en el Dashboard

**Archivo a modificar:** `backend/routes/dashboard_routes.py` (Línea 16)

```python
# ╔═══════════════════════════════════════════════════════════════════╗
# ║  🎯 CONFIGURACIÓN DEL MODELO ACTIVO - CAMBIAR AQUÍ               ║
# ╚═══════════════════════════════════════════════════════════════════╝

MODELO_ACTIVO = 'modelo_balanceado'  # ← CAMBIAR ESTA LÍNEA
```

**Opciones disponibles:**
- `'modelo_balanceado'` ✨ (Actual - Dataset balanceado 75/25 - Mejor detección de desertores)
- `'modelo_nuevo'` (BD completa - Mejor rendimiento general)
- `'modelo_base'` (Modelo base original con BD del 84/16)

#### Proceso de Cambio (2 pasos):

```bash
# 1. Editar el archivo y cambiar MODELO_ACTIVO (línea 16)
# Cambiar la variable MODELO_ACTIVO en backend/routes/dashboard_routes.py

# 2. Reiniciar el servidor Flask (el cambio es automático)
python run.py
```

**Nota**: Ya no es necesario sincronizar imágenes. El dashboard lee directamente desde `resultados/MODELO_ACTIVO/` usando rutas dinámicas.

#### Verificación del Cambio

Después del cambio, el dashboard mostrará:
- ✅ Estadísticas actualizadas del modelo seleccionado
- ✅ Gráficos y matrices desde `resultados/{MODELO_ACTIVO}/`
- ✅ Métricas de los 9 algoritmos del modelo activo

### 📊 Características del Dashboard Rediseñado

#### Resumen Ejecutivo (Página Principal)
Diseñado específicamente para **docentes sin conocimientos técnicos**:

- **4 Tarjetas de Estadísticas**:
  - Total de estudiantes analizados
  - Estudiantes en riesgo alto
  - Estudiantes en riesgo medio
  - Precisión del modelo

- **3 Cajas de Alertas** (código de colores):
  - � **Roja**: Acción requerida urgente (riesgo alto)
  - 🟡 **Amarilla**: Monitoreo continuo (riesgo medio)
  - 🔵 **Azul**: Información general

- **Tabla de Estudiantes en Riesgo**:
  - Top 10 estudiantes de riesgo alto
  - ID, nivel de riesgo, probabilidad, factores, acción sugerida
  - Enlace "Ver todos" para expandir la lista completa
  - Datos reales del dataset `datos_balanceados_75_25.xlsx`

#### Visualizaciones Interactivas
- **Modal de Zoom**: Clic en cualquier imagen para verla en tamaño completo
- **Organización por Categorías**: Curvas, Gráficos, Matrices separadas
- **Carga Dinámica**: API REST que sirve imágenes desde `resultados/`

### Entrenamiento de Modelos

#### Modelo con Dataset Original/Completo
```python
from modelos.modelo_desercion_nuevo import entrenar_modelos

# Entrenar todos los modelos con dataset completo
resultados = entrenar_modelos()
```

#### Modelo con Dataset Balanceado ✨ NUEVO
```python
# Ejecutar el modelo con dataset balanceado (75/25)
python modelos/modelo_desercion_balanceado.py

# O en segundo plano con log
python modelos/modelo_desercion_balanceado.py > modelo_balanceado.log 2>&1 &
```

**Ventajas del Dataset Balanceado:**
- 📊 Mejor detección de la clase minoritaria (desertores)
- ⚖️ Reduce el sesgo hacia la clase mayoritaria
- 🎯 Mejora el recall para estudiantes en riesgo
- 🔬 Permite comparación científica con dataset original

### Evaluación de Modelos
```python
from modelos.evaluador import EvaluadorModelo

# Crear evaluador
evaluador = EvaluadorModelo(output_dir='resultados/mi_modelo')

# Evaluar modelo
evaluador.evaluar_modelo(
    modelo=modelo_entrenado,
    X_test=X_test,
    y_test=y_test,
    feature_names=X_test.columns,
    nombre_modelo="MiModelo"
)
```

### Creación de Dataset Balanceado ✨ NUEVO

Para experimentar con diferentes proporciones de clases:

```bash
# Crear dataset balanceado con proporciones personalizadas
cd datos
python crear_dataset_balanceado.py
```

El script `crear_dataset_balanceado.py` permite:
- ✅ Definir proporciones personalizadas (ej: 70/30, 75/25, 80/20)
- ✅ Usar técnica de oversampling (duplica clase minoritaria)
- ✅ Usar técnica de undersampling (reduce clase mayoritaria)
- ✅ Generar múltiples versiones para experimentación
- ✅ Mantener distribución estadística de las variables

**Configuración actual:**
- Proporción: 75% No Desertor / 25% Desertor
- Total registros: 5,000
- Técnica: Oversampling con `random_state=42`
- Archivo generado: `datos_finales_75_25.csv`

### Visualización de Resultados
1. Los resultados se guardan automáticamente en `resultados/modelo_*/`
2. El dashboard se actualiza automáticamente con nuevos resultados
3. Acceso a métricas detalladas a través de la interfaz web
4. Exportación de resultados en diferentes formatos
5. Comparación entre datasets original y balanceado ✨

## 📊 Interpretación de Resultados

### Estructura de Resultados
Los resultados están organizados profesionalmente en **tres conjuntos**:

```
resultados/
├── modelo_base/              # 9 modelos con BD original (84/16)
│   ├── randomforest/
│   ├── gradientboosting/
│   ├── adaboost/
│   ├── decisiontree/
│   ├── kneighbors/
│   ├── logisticregression/
│   ├── svm/
│   ├── neuralnetwork/
│   └── naivebayes/
├── modelo_nuevo/             # 9 modelos con BD completa
│   └── [misma estructura]
└── modelo_balanceado/        # 9 modelos con dataset balanceado (75/25) ✨ NUEVO
    ├── randomforest/
    ├── gradientboosting/
    ├── adaboost/
    ├── decisiontree/
    ├── kneighbors/
    ├── logisticregression/
    ├── svm/
    ├── neuralnetwork/
    ├── naivebayes/
    ├── graficos/            # Gráfico comparativo de todos los modelos
    └── metricas/            # CSV con comparación de métricas
```

### Archivos Generados por Modelo
Cada modelo genera **8 archivos de visualización**:

#### Gráficos Tradicionales:
1. `matriz_confusion.png` - Matriz de confusión
2. `curva_roc.png` - Curva ROC y AUC
3. `curva_precision_recall.png` - Curva Precisión-Recall
4. `learning_curve.png` - Curva de aprendizaje

#### Gráficos Intuitivos (NUEVO):
5. `grafico_barras_predicciones.png` - Predicciones correctas vs incorrectas
6. `distribucion_clases.png` - Balance de clases
7. `comparacion_metricas.png` - Comparación de métricas
8. `analisis_errores.png` - Análisis detallado de errores

#### Archivos de Datos:
- `metricas.txt` - Resumen completo en formato legible
- `metricas_clasificacion.csv` - Métricas detalladas en formato CSV
- `importancia_caracteristicas.csv` - Ranking de variables importantes

#### Archivos Adicionales del Dataset Balanceado ✨
- `resultados/modelo_balanceado/metricas/comparacion_modelos.csv` - Tabla comparativa
- `resultados/modelo_balanceado/graficos/comparacion_todos_modelos.png` - Gráfico comparativo

> 📁 Total: **200+ archivos de resultados** organizados profesionalmente (27 modelos × ~8 archivos)

## 🤝 Contribución
Las contribuciones son bienvenidas. Por favor, sigue estos pasos:
1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas Importantes

### Estado del Proyecto
- ✅ **27 modelos entrenados** (9 algoritmos × 3 datasets)
- ✅ **Dashboard rediseñado para docentes** con interfaz no técnica ✨ NUEVO
- ✅ **Sistema de análisis de riesgo** integrado con datos reales ✨ NUEVO
- ✅ **Dataset balanceado (75/25)** para mejorar detección de desertores
- ✅ **200+ archivos de resultados** organizados profesionalmente
- ✅ **API REST con 3 endpoints** para servir datos y visualizaciones
- ✅ **0 errores de tipo** en el código (verificado con Pylance)
- ✅ **Entorno virtual `.venv`** configurado y optimizado (589 MB)
- ✅ **Documentación completa** (11 archivos .md)

### Características del Dashboard ✨ NUEVO
- **Interfaz para educadores**: Diseño enfocado en usuarios sin conocimientos técnicos
- **Datos en tiempo real**: Lee directamente desde el dataset sin necesidad de sincronización
- **Modal de zoom**: Clic en cualquier imagen para verla en tamaño completo
- **Tabla expandible**: "Ver todos" muestra la lista completa de estudiantes en riesgo
- **Código de colores**: Rojo (urgente), Amarillo (precaución), Verde (positivo)
- **6 secciones organizadas**: Resumen Ejecutivo, Métricas, Curvas, Gráficos, Matrices, Todas
- **Servicio dinámico de imágenes**: Sin copiar archivos, lee desde `resultados/{MODELO_ACTIVO}/`
- **Cambio de modelo simple**: Solo editar `MODELO_ACTIVO` en `dashboard_routes.py`

### Características Importantes
- Los modelos se guardan automáticamente después del entrenamiento
- Cada ejecución genera un conjunto completo de 8 visualizaciones por modelo
- Las advertencias de convergencia en algunos modelos (MLP, LogisticRegression) son normales
- Los **gráficos intuitivos** facilitan la comprensión para público no técnico
- Se recomienda revisar la importancia de características para entender los factores más influyentes
- El sistema está optimizado para Python 3.9.6 (versiones exactas en `requirements.txt`)
- **Ya no se usa `sync_images.py`**: El dashboard lee imágenes dinámicamente ✨

### Tiempo de Ejecución
- **Entrenamiento completo**: ~15-20 minutos por conjunto (27 modelos total)
- **Mejor modelo típico**: RandomForest o GradientBoosting (AUC > 0.85)
- **Modelos más rápidos**: DecisionTree, LogisticRegression
- **Modelos más lentos**: SVM, MLP (requieren muchas iteraciones)
- **Dataset balanceado**: Mismo tiempo, mejor detección de clase minoritaria ✨

## 🔒 Seguridad y Privacidad
- Los datos de estudiantes deben ser anonimizados
- Se recomienda no compartir resultados individuales
- Mantener la confidencialidad de la información sensible

## ⚠️ Solución de Problemas Comunes

### Errores de Entorno Virtual
- **`.venv` no encontrado**: Crear nuevo entorno con `python3 -m venv .venv`
- **Módulo no encontrado**: Verificar que el entorno está activado y ejecutar `pip install -r requirements.txt`
- **Python version mismatch**: Verificar versión con `python --version` (debe ser 3.9.6+)

### Errores de Dependencias
- **XGBoost error en macOS**: Instalar libomp con `brew install libomp`
- **Conflictos de versiones**: Usar `requirements.txt` (versiones exactas probadas)
- **pip install falla**: Actualizar pip con `pip install --upgrade pip`

### Errores de Base de Datos
- **Error al inicializar la BD**: Verifica permisos de escritura en el directorio
- **Error de migración**: Elimina el archivo `instance/app.db` y ejecuta `python init_db.py`
- **Error de autenticación**: Verifica las credenciales en `init_db.py`

### Errores de Visualización
- **Gráficos no visibles**: Verifica que exista el directorio `resultados/`
- **Error 404 en imágenes**: Asegúrate de que los modelos se ejecutaron correctamente
- **Dashboard no actualiza**: Limpia la caché del navegador (Cmd+Shift+R en macOS)

### Errores de Modelo
- **Error al entrenar**: Verifica la estructura de los datos en `datos/`
- **Métricas no disponibles**: Ejecuta primero `python modelos/modelo_desercion_escolar.py`
- **Error de memoria**: Reduce el número de modelos a entrenar simultáneamente
- **Pylance type errors**: Consultar [CORRECCION_COMPLETA_TIPOS.md](CORRECCION_COMPLETA_TIPOS.md)

### Recursos Adicionales
- 📚 [INDICE_DOCUMENTACION.md](documentacion/INDICE_DOCUMENTACION.md) - Índice completo de documentación
- 🔧 [REQUIREMENTS_INFO.md](documentacion/REQUIREMENTS_INFO.md) - Guía de gestión de dependencias
- 🐛 [CORRECCION_COMPLETA_TIPOS.md](documentacion/CORRECCION_COMPLETA_TIPOS.md) - Solución de errores de tipos

## � Documentación Adicional


El proyecto incluye **documentación técnica completa** en la carpeta `documentacion/`:

| Documento | Descripción |
|-----------|-------------|
| **[INDICE_DOCUMENTACION.md](documentacion/INDICE_DOCUMENTACION.md)** | 📖 Índice maestro - **LEER PRIMERO** |
| **[CONFIGURACION_MODELO_ACTIVO.md](documentacion/CONFIGURACION_MODELO_ACTIVO.md)** | 🎯 **Cómo cambiar el modelo en el dashboard web** |
| **[REORGANIZACION_IMAGENES_MODELOS.md](documentacion/REORGANIZACION_IMAGENES_MODELOS.md)** | 📁 Estructura de carpetas por modelo |
| **[ANALISIS_ORGANIZACION_IMAGENES.md](documentacion/ANALISIS_ORGANIZACION_IMAGENES.md)** | 🔍 Análisis de organización de imágenes |
| **[REQUIREMENTS_INFO.md](documentacion/REQUIREMENTS_INFO.md)** | 📦 Guía completa de gestión de dependencias |
| **[CORRECCION_COMPLETA_TIPOS.md](documentacion/CORRECCION_COMPLETA_TIPOS.md)** | 🔧 Correcciones de tipos aplicadas (7 correcciones) |
| **[MIGRACION_VENV_COMPLETA.md](documentacion/MIGRACION_VENV_COMPLETA.md)** | 🔄 Migración a entorno `.venv` profesional |
| **[VERIFICACION_COMPLETA_MODELOS.md](documentacion/VERIFICACION_COMPLETA_MODELOS.md)** | ✅ Verificación de 18 modelos entrenados |
| **[RESUMEN_GRAFICOS_INTUITIVOS.md](documentacion/RESUMEN_GRAFICOS_INTUITIVOS.md)** | 📊 Gráficos intuitivos implementados |
| **[RESUMEN_REORGANIZACION_FINAL.md](documentacion/RESUMEN_REORGANIZACION_FINAL.md)** | 🗂️ Reorganización de 136 archivos |
| **[REORGANIZACION_REQUIREMENTS.md](documentacion/REORGANIZACION_REQUIREMENTS.md)** | 📋 Historial de cambios en requirements |
| **[ANALISIS_ENTORNOS_VIRTUALES.md](documentacion/ANALISIS_ENTORNOS_VIRTUALES.md)** | 🔍 Análisis y limpieza de entornos |

> 💡 **Tip**: Consulta [INDICE_DOCUMENTACION.md](documentacion/INDICE_DOCUMENTACION.md) para acceso rápido a toda la documentación
| **[REORGANIZACION_REQUIREMENTS.md](documentacion/REORGANIZACION_REQUIREMENTS.md)** | 📋 Historial de cambios en requirements |
| **[ANALISIS_ENTORNOS_VIRTUALES.md](documentacion/ANALISIS_ENTORNOS_VIRTUALES.md)** | 🔍 Análisis y limpieza de entornos |

> 💡 **Tip**: Consulta [INDICE_DOCUMENTACION.md](documentacion/INDICE_DOCUMENTACION.md) para acceso rápido a toda la documentación

---

## 📫 Contacto y Soporte

### Autor
- **Nombre**: David Alexander Vargas Pineda
- **Correo**: david.vargaspi@amigo.edu.co
- **Institución**: Universidad Católica Luis Amigó

### Soporte
- **Issues**: Crear un nuevo issue en el repositorio
- **Documentación**: Consultar los 11 archivos .md en la raíz del proyecto
- **Wiki**: Consultar la documentación detallada en la wiki del proyecto

---

## 🎓 Información del Proyecto

- **Tipo**: Trabajo de Grado
- **Área**: Ingeniería de Sistemas / Machine Learning
- **Fecha**: 2025
- **Tecnología Principal**: Python 3.9.6 + Flask + scikit-learn
- **Estado**: ✅ Completado y listo para producción
