# Análisis de Organización de Imágenes de Modelos

**Fecha:** 21 de octubre de 2025  
**Propósito:** Verificar que cada modelo genere todas sus imágenes en carpetas organizadas por nombre de modelo

## 🔍 Situación Actual

### Estructura de Carpetas en `/resultados/`

```
resultados/
├── adaboost/               ✅ Por algoritmo
├── decisiontree/           ✅ Por algoritmo
├── gradientboosting/       ✅ Por algoritmo
├── kneighbors/            ✅ Por algoritmo
├── logisticregression/    ✅ Por algoritmo
├── mlpclassifier/         ✅ Por algoritmo
├── naivebayes/            ✅ Por algoritmo
├── randomforest/          ✅ Por algoritmo
├── svm/                   ✅ Por algoritmo
├── modelo_base/           ⚠️ Estructura inconsistente
├── modelo_nuevo/          ⚠️ Estructura mixta
└── experimentos_antiguos/
```

### Problema Identificado en `modelo_nuevo/`

**Estructura actual de `modelo_nuevo/graficos/`:**

```
graficos/
├── adaboost/                      ✅ Subcarpeta de modelo (curvas ROC, PR)
├── decisiontree/                  ✅ Subcarpeta de modelo
├── gradientboosting/              ✅ Subcarpeta de modelo
├── kneighbors/                    ✅ Subcarpeta de modelo
├── logisticregression/            ✅ Subcarpeta de modelo
├── naivebayes/                    ✅ Subcarpeta de modelo
├── neuralnetwork/                 ✅ Subcarpeta de modelo
├── randomforest/                  ✅ Subcarpeta de modelo
├── svm/                           ✅ Subcarpeta de modelo
├── learning_curve_adaboost.png    ❌ Imagen suelta
├── learning_curve_decisiontree.png ❌ Imagen suelta
├── learning_curve_gradientboosting.png ❌ Imagen suelta
├── learning_curve_kneighbors.png  ❌ Imagen suelta
├── learning_curve_logisticregression.png ❌ Imagen suelta
├── learning_curve_naivebayes.png  ❌ Imagen suelta
├── learning_curve_neuralnetwork.png ❌ Imagen suelta
├── learning_curve_randomforest.png ❌ Imagen suelta
├── learning_curve_svm.png         ❌ Imagen suelta
├── importancia_adaboost.png       ❌ Imagen suelta
├── importancia_decisiontree.png   ❌ Imagen suelta
├── importancia_gradientboosting.png ❌ Imagen suelta
├── importancia_randomforest.png   ❌ Imagen suelta
└── comparacion_todos_modelos.png  ✅ Imagen general (correcto)
```

**Estructura actual de `modelo_nuevo/matrices/`:**

```
matrices/
├── matriz_confusion_adaboost.png       ❌ Imagen suelta
├── matriz_confusion_decisiontree.png   ❌ Imagen suelta
├── matriz_confusion_gradientboosting.png ❌ Imagen suelta
├── matriz_confusion_kneighbors.png     ❌ Imagen suelta
├── matriz_confusion_logisticregression.png ❌ Imagen suelta
├── matriz_confusion_naivebayes.png     ❌ Imagen suelta
├── matriz_confusion_neuralnetwork.png  ❌ Imagen suelta
├── matriz_confusion_randomforest.png   ❌ Imagen suelta
└── matriz_confusion_svm.png            ❌ Imagen suelta
```

## 📊 Inventario de Archivos por Modelo

### Archivos Python de Modelos

1. **modelo_desercion_nuevo.py** ⚠️
   - Genera: 9 modelos (LR, DT, RF, GB, AB, KNN, SVM, NN, NB)
   - Guarda en: `resultados/modelo_nuevo/`
   - **Problema**: Mezcla imágenes sueltas con subcarpetas

2. **modelo_desercion.py** (modelo_base) ⚠️
   - Guarda en: `resultados/modelo_base/`
   - **Problema**: Estructura sin verificar

3. **modelo_desercion_escolar.py** (modelo_base) ⚠️
   - Guarda en: `resultados/modelo_base/`
   - **Problema**: Duplicado, estructura sin verificar

4. **modelo_con_inscrito.py** ❌
   - Genera: 4 modelos (RF, SVM, LR, GB)
   - **Problema CRÍTICO**: Guarda en directorio raíz del proyecto
   - Genera: `matriz_confusion_*.png` y `reporte_*.txt` en modelos/

5. **modelo_con_terminado.py** ❌
   - Genera: 1 modelo (RF)
   - **Problema CRÍTICO**: Guarda en directorio raíz del proyecto
   - Genera: `matriz_confusion_terminado.png` en modelos/

## 🎯 Estructura Ideal

Para cada modelo, TODAS las imágenes deben estar en una carpeta con el nombre del algoritmo:

```
resultados/
└── [nombre_experimento]/
    ├── graficos/
    │   ├── [algoritmo1]/
    │   │   ├── learning_curve.png
    │   │   ├── roc_curve.png
    │   │   ├── precision_recall_curve.png
    │   │   ├── importancia_variables.png
    │   │   └── graficos_intuitivos.png
    │   ├── [algoritmo2]/
    │   │   └── ... (mismo contenido)
    │   └── comparacion_todos_modelos.png  ← Único archivo suelto permitido
    ├── matrices/
    │   ├── [algoritmo1]/
    │   │   └── matriz_confusion.png
    │   └── [algoritmo2]/
    │       └── matriz_confusion.png
    ├── metricas/
    │   ├── comparacion_modelos.csv
    │   └── [algoritmo]/
    │       └── metricas.json
    └── modelos/
        ├── [algoritmo1]_model.pkl
        └── [algoritmo2]_model.pkl
```

## ✅ Imágenes que Debe Generar Cada Modelo

### 1. Matriz de Confusión
- **Ubicación**: `resultados/[experimento]/matrices/[algoritmo]/matriz_confusion.png`
- **Generada por**: Todos los modelos
- **Estado actual**: ❌ En carpeta `matrices/` raíz (modelo_nuevo)

### 2. Curva de Aprendizaje
- **Ubicación**: `resultados/[experimento]/graficos/[algoritmo]/learning_curve.png`
- **Generada por**: Todos los modelos
- **Estado actual**: ❌ En carpeta `graficos/` raíz (modelo_nuevo)

### 3. Curva ROC
- **Ubicación**: `resultados/[experimento]/graficos/[algoritmo]/roc_curve.png`
- **Generada por**: Evaluador (modelos con predict_proba)
- **Estado actual**: ✅ En subcarpetas de graficos/ (generado por evaluador)

### 4. Curva Precision-Recall
- **Ubicación**: `resultados/[experimento]/graficos/[algoritmo]/precision_recall_curve.png`
- **Generada por**: Evaluador (modelos con predict_proba)
- **Estado actual**: ✅ En subcarpetas de graficos/ (generado por evaluador)

### 5. Importancia de Variables
- **Ubicación**: `resultados/[experimento]/graficos/[algoritmo]/importancia_variables.png`
- **Generada por**: RF, DT, GB, AB (modelos tree-based)
- **Estado actual**: ❌ En carpeta `graficos/` raíz (modelo_nuevo)

### 6. Gráficos Intuitivos
- **Ubicación**: `resultados/[experimento]/graficos/[algoritmo]/graficos_intuitivos_*.png`
- **Generada por**: Evaluador (todos los modelos)
- **Estado actual**: ✅ En subcarpetas de graficos/ (generado por evaluador)

### 7. Métricas JSON
- **Ubicación**: `resultados/[experimento]/graficos/[algoritmo]/metricas.json`
- **Generada por**: Evaluador (todos los modelos)
- **Estado actual**: ✅ En subcarpetas de graficos/ (generado por evaluador)

## 🔧 Problemas por Corregir

### Problema 1: Imágenes Sueltas en `modelo_desercion_nuevo.py`

**Líneas problemáticas:**

```python
# Línea ~103: Learning curve guardada en graficos/ raíz
plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'learning_curve_{nombre.lower()}.png'), dpi=300)

# Línea ~208: Matriz de confusión guardada en matrices/ raíz
plt.savefig(os.path.join(RESULTADOS_BASE, 'matrices', f'matriz_confusion_{nombre.lower()}.png'), dpi=300, bbox_inches='tight')

# Línea ~225: Importancia guardada en graficos/ raíz
plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'importancia_{nombre.lower()}.png'), dpi=300)
```

**Solución:**
```python
# Crear subcarpeta para cada modelo
modelo_dir = os.path.join(RESULTADOS_BASE, nombre.lower())
os.makedirs(modelo_dir, exist_ok=True)

# Learning curve
plt.savefig(os.path.join(modelo_dir, 'learning_curve.png'), dpi=300)

# Matriz de confusión
plt.savefig(os.path.join(modelo_dir, 'matriz_confusion.png'), dpi=300, bbox_inches='tight')

# Importancia de variables
plt.savefig(os.path.join(modelo_dir, 'importancia_variables.png'), dpi=300)
```

### Problema 2: `modelo_con_inscrito.py` Guarda en Raíz

**Línea 106:**
```python
plt.savefig(f"matriz_confusion_{nombre.lower()}.png", dpi=300, bbox_inches="tight")
```

**Solución:**
```python
# Definir RESULTADOS_BASE al inicio
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_inscrito')

# Crear estructura de carpetas
os.makedirs(os.path.join(RESULTADOS_BASE, nombre.lower()), exist_ok=True)

# Guardar en subcarpeta del modelo
plt.savefig(os.path.join(RESULTADOS_BASE, nombre.lower(), "matriz_confusion.png"), dpi=300, bbox_inches="tight")
```

### Problema 3: `modelo_con_terminado.py` Guarda en Raíz

**Línea ~67:**
```python
plt.savefig("matriz_confusion_terminado.png", dpi=300, bbox_inches="tight")
```

**Solución:**
```python
# Definir RESULTADOS_BASE al inicio
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_terminado')
os.makedirs(os.path.join(RESULTADOS_BASE, 'randomforest'), exist_ok=True)

# Guardar en subcarpeta
plt.savefig(os.path.join(RESULTADOS_BASE, 'randomforest', "matriz_confusion.png"), dpi=300, bbox_inches="tight")
```

## 📋 Plan de Corrección

### Fase 1: Modificar Scripts ✅ PRIORITARIO

1. **modelo_desercion_nuevo.py**
   - Cambiar todas las rutas de guardado para usar subcarpetas por modelo
   - Mover learning_curve, matriz_confusion, importancia a subcarpetas
   - Mantener comparacion_todos_modelos.png en graficos/ raíz

2. **modelo_con_inscrito.py**
   - Añadir RESULTADOS_BASE apuntando a `resultados/modelo_inscrito/`
   - Crear estructura de subcarpetas por modelo
   - Mover todo a subcarpetas

3. **modelo_con_terminado.py**
   - Añadir RESULTADOS_BASE apuntando a `resultados/modelo_terminado/`
   - Crear subcarpeta `randomforest/`
   - Mover todo a subcarpeta

4. **Verificar modelo_desercion.py y modelo_desercion_escolar.py**
   - Revisar si tienen el mismo problema
   - Aplicar mismas correcciones si es necesario

### Fase 2: Reorganizar Archivos Existentes (Opcional)

Si el usuario desea reorganizar archivos ya generados:
- Mover imágenes sueltas a sus respectivas subcarpetas
- Actualizar README.md de cada carpeta

### Fase 3: Documentar Estructura

- Actualizar documentación con estructura correcta
- Crear script de utilidad para verificar estructura

## 🎯 Resultado Esperado

Después de las correcciones, la estructura será:

```
resultados/
├── modelo_nuevo/
│   ├── adaboost/
│   │   ├── learning_curve.png
│   │   ├── matriz_confusion.png
│   │   ├── importancia_variables.png
│   │   ├── roc_curve.png
│   │   ├── precision_recall_curve.png
│   │   └── metricas.json
│   ├── randomforest/
│   │   └── ... (mismos archivos)
│   ├── ... (resto de modelos)
│   ├── comparacion_todos_modelos.png
│   └── metricas/
│       └── comparacion_modelos.csv
├── modelo_inscrito/
│   ├── randomforest/
│   ├── svm/
│   ├── logisticregression/
│   └── gradientboosting/
└── modelo_terminado/
    └── randomforest/
```

## ✨ Beneficios de la Reorganización

1. **Claridad**: Cada modelo tiene TODAS sus imágenes en un solo lugar
2. **Comparabilidad**: Fácil comparar el mismo gráfico entre modelos
3. **Mantenibilidad**: Fácil encontrar y actualizar imágenes
4. **Escalabilidad**: Agregar nuevos modelos sin desorden
5. **Dashboard**: Frontend puede leer fácilmente por modelo
