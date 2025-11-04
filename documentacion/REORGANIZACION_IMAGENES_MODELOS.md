# Reorganización de Imágenes por Modelo

**Fecha:** 21 de octubre de 2025  
**Estado:** ✅ COMPLETADO

## 📋 Resumen Ejecutivo

Se ha reorganizado la estructura de carpetas de todos los modelos para que **cada modelo guarde TODAS sus imágenes en una subcarpeta con su nombre**, facilitando la comparación, el mantenimiento y la lectura desde el dashboard.

## 🎯 Objetivo

**Antes:** Las imágenes estaban mezcladas en carpetas `graficos/` y `matrices/` sin organización clara por modelo.

**Ahora:** Cada modelo tiene su propia carpeta con TODAS sus visualizaciones:
- Matriz de confusión
- Curvas de aprendizaje
- Curvas ROC
- Curvas Precision-Recall
- Importancia de variables
- Gráficos intuitivos
- Métricas JSON

## 📁 Estructura Nueva

### Para `modelo_desercion_nuevo.py`

```
resultados/modelo_nuevo/
├── adaboost/
│   ├── learning_curve.png          ✨ NUEVO
│   ├── matriz_confusion.png        ✨ NUEVO
│   ├── importancia_top15.png       ✨ NUEVO
│   ├── importancia_variables.png   ✅ (del evaluador)
│   ├── roc_curve.png              ✅ (del evaluador)
│   ├── precision_recall_curve.png  ✅ (del evaluador)
│   ├── graficos_intuitivos_*.png   ✅ (del evaluador)
│   └── metricas.json              ✅ (del evaluador)
├── decisiontree/
│   └── ... (mismos archivos)
├── gradientboosting/
│   └── ... (mismos archivos)
├── kneighbors/
│   └── ... (mismos archivos)
├── logisticregression/
│   └── ... (mismos archivos)
├── naivebayes/
│   └── ... (mismos archivos)
├── neuralnetwork/
│   └── ... (mismos archivos)
├── randomforest/
│   └── ... (mismos archivos)
├── svm/
│   └── ... (mismos archivos)
├── comparacion_todos_modelos.png   ✅ (archivo general, correcto en raíz)
└── metricas/
    └── comparacion_modelos.csv     ✅ (archivo general, correcto)
```

### Para `modelo_con_inscrito.py`

```
resultados/modelo_inscrito/          ✨ NUEVA CARPETA
├── randomforest/
│   ├── matriz_confusion.png
│   └── reporte_clasificacion.txt
├── svm/
│   ├── matriz_confusion.png
│   └── reporte_clasificacion.txt
├── logisticregression/
│   ├── matriz_confusion.png
│   └── reporte_clasificacion.txt
└── gradientboosting/
    ├── matriz_confusion.png
    └── reporte_clasificacion.txt
```

### Para `modelo_con_terminado.py`

```
resultados/modelo_terminado/         ✨ NUEVA CARPETA
└── randomforest/
    ├── matriz_confusion.png
    └── reporte_clasificacion.txt
```

## 🔧 Cambios Realizados

### 1. `modelo_desercion_nuevo.py`

#### Cambio 1: Learning Curves
**Antes:**
```python
plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'learning_curve_{nombre_modelo.lower()}.png'), dpi=300)
```

**Ahora:**
```python
# Guardar en subcarpeta del modelo
modelo_dir = os.path.join(RESULTADOS_BASE, nombre_modelo.lower())
os.makedirs(modelo_dir, exist_ok=True)
plt.savefig(os.path.join(modelo_dir, 'learning_curve.png'), dpi=300, bbox_inches='tight')
```

#### Cambio 2: Matrices de Confusión
**Antes:**
```python
plt.savefig(os.path.join(RESULTADOS_BASE, 'matrices', f'matriz_confusion_{nombre.lower()}.png'), dpi=300, bbox_inches='tight')
```

**Ahora:**
```python
# Crear subcarpeta para el modelo
modelo_dir = os.path.join(RESULTADOS_BASE, nombre.lower())
os.makedirs(modelo_dir, exist_ok=True)
plt.savefig(os.path.join(modelo_dir, 'matriz_confusion.png'), dpi=300, bbox_inches='tight')
```

#### Cambio 3: Evaluador
**Antes:**
```python
evaluador_modelo = EvaluadorModelo(
    output_dir=os.path.join(RESULTADOS_BASE, 'graficos', nombre.lower())
)
```

**Ahora:**
```python
evaluador_modelo = EvaluadorModelo(
    output_dir=os.path.join(modelo_dir)  # Ya creada arriba
)
```

#### Cambio 4: Importancia de Variables
**Antes:**
```python
plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'importancia_{nombre.lower()}.png'), dpi=300)
```

**Ahora:**
```python
plt.savefig(os.path.join(modelo_dir, 'importancia_top15.png'), dpi=300)
```

---

### 2. `modelo_con_inscrito.py`

#### Cambio 1: Añadir Configuración de Rutas
**Añadido al inicio del archivo:**
```python
import os

# Definir ruta base de resultados
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_inscrito')

# Asegurar que el directorio de resultados existe
os.makedirs(RESULTADOS_BASE, exist_ok=True)
```

#### Cambio 2: Modificar función `evaluar_modelo()`
**Antes:**
```python
plt.savefig(f"matriz_confusion_{nombre.lower()}.png", dpi=300, bbox_inches="tight")
# ...
with open(f"reporte_{nombre.lower()}.txt", "w") as f:
```

**Ahora:**
```python
# Crear subcarpeta para el modelo
modelo_dir = os.path.join(RESULTADOS_BASE, nombre.lower())
os.makedirs(modelo_dir, exist_ok=True)

plt.savefig(os.path.join(modelo_dir, "matriz_confusion.png"), dpi=300, bbox_inches="tight")
# ...
with open(os.path.join(modelo_dir, "reporte_clasificacion.txt"), "w") as f:
```

---

### 3. `modelo_con_terminado.py`

#### Cambio 1: Añadir Configuración de Rutas
**Añadido al inicio del archivo:**
```python
import os

# Definir ruta base de resultados
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_terminado')

# Crear subcarpeta para el modelo RandomForest
MODELO_DIR = os.path.join(RESULTADOS_BASE, 'randomforest')
os.makedirs(MODELO_DIR, exist_ok=True)
```

#### Cambio 2: Guardar Matriz de Confusión
**Antes:**
```python
plt.savefig("matriz_confusion_terminado.png", dpi=300, bbox_inches="tight")
```

**Ahora:**
```python
plt.savefig(os.path.join(MODELO_DIR, "matriz_confusion.png"), dpi=300, bbox_inches="tight")
print(f"✅ Matriz de confusión guardada en: {MODELO_DIR}/matriz_confusion.png")
```

#### Cambio 3: Guardar Reporte
**Añadido:**
```python
reporte = classification_report(y_test, y_pred)
print("Reporte de clasificación:\n", reporte)

# Guardar reporte en archivo
with open(os.path.join(MODELO_DIR, "reporte_clasificacion.txt"), "w") as f:
    f.write(str(reporte))
print(f"✅ Reporte guardado en: {MODELO_DIR}/reporte_clasificacion.txt")
```

## ✨ Beneficios de la Reorganización

### 1. **Claridad y Organización**
- ✅ Cada modelo tiene TODAS sus visualizaciones en un solo lugar
- ✅ No más archivos sueltos mezclados
- ✅ Fácil de navegar y encontrar resultados

### 2. **Comparabilidad**
- ✅ Comparar la misma métrica entre modelos es trivial
- ✅ Ejemplo: ver todas las matrices de confusión
  ```bash
  ls resultados/modelo_nuevo/*/matriz_confusion.png
  ```

### 3. **Escalabilidad**
- ✅ Agregar nuevos modelos no genera desorden
- ✅ Cada modelo se autocontiene en su carpeta
- ✅ Fácil eliminar un modelo completo si es necesario

### 4. **Mantenibilidad**
- ✅ Scripts más limpios y consistentes
- ✅ Rutas predecibles y documentadas
- ✅ Menos probabilidad de sobrescribir archivos

### 5. **Integración con Dashboard**
- ✅ El frontend puede leer resultados fácilmente
- ✅ Estructura predecible para APIs
- ✅ Filtrado por modelo simplificado

## 🔍 Verificación

Para verificar que la estructura es correcta, ejecuta:

```bash
# Ver estructura de modelo_nuevo
tree resultados/modelo_nuevo -L 2

# Ver estructura de modelo_inscrito
tree resultados/modelo_inscrito

# Ver estructura de modelo_terminado
tree resultados/modelo_terminado
```

### Ejemplo de salida esperada para un modelo:

```
resultados/modelo_nuevo/randomforest/
├── learning_curve.png
├── matriz_confusion.png
├── importancia_top15.png
├── importancia_variables.png
├── roc_curve.png
├── precision_recall_curve.png
├── graficos_intuitivos_comparacion_clases.png
├── graficos_intuitivos_distribucion_predicciones.png
└── metricas.json
```

## 📝 Próximos Pasos

### Opcional: Reorganizar Archivos Existentes

Si deseas reorganizar los archivos que ya fueron generados antes de esta corrección:

```bash
# Script de reorganización (ejemplo para modelo_nuevo)
cd resultados/modelo_nuevo

# Mover learning curves
for modelo in adaboost decisiontree gradientboosting kneighbors logisticregression naivebayes neuralnetwork randomforest svm; do
    mv graficos/learning_curve_${modelo}.png ${modelo}/learning_curve.png 2>/dev/null
done

# Mover matrices de confusión
for modelo in adaboost decisiontree gradientboosting kneighbors logisticregression naivebayes neuralnetwork randomforest svm; do
    mv matrices/matriz_confusion_${modelo}.png ${modelo}/matriz_confusion.png 2>/dev/null
done

# Mover importancias
for modelo in adaboost decisiontree gradientboosting randomforest; do
    mv graficos/importancia_${modelo}.png ${modelo}/importancia_top15.png 2>/dev/null
done
```

### Actualizar README de resultados

Actualizar `/resultados/README.md` con la nueva estructura documentada.

## ✅ Estado Final

- ✅ `modelo_desercion_nuevo.py` - Reorganizado
- ✅ `modelo_con_inscrito.py` - Reorganizado
- ✅ `modelo_con_terminado.py` - Reorganizado
- ⏳ Archivos existentes - Por reorganizar (opcional)
- ⏳ Documentación - Por actualizar

## 🎯 Conclusión

La reorganización está completa y lista para usar. La próxima vez que ejecutes cualquiera de los modelos, las imágenes se guardarán automáticamente en la estructura correcta, facilitando la comparación, el análisis y la presentación de resultados.

**Próxima ejecución:** Todos los resultados estarán perfectamente organizados por modelo. 🎉
