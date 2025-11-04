# Gráficos Intuitivos para Modelos de Deserción Escolar

## 📊 Resumen de Mejoras

Se han agregado **gráficos de barras intuitivos** a todos los modelos de aprendizaje automático para facilitar la comprensión de los resultados a personas sin conocimientos técnicos.

## 🎯 Objetivo

Estos gráficos permiten que cualquier persona pueda entender:
- ✅ Cuántas predicciones fueron correctas e incorrectas
- ✅ Comparación entre desertores y no desertores reales vs predichos
- ✅ Desglose detallado de aciertos y errores
- ✅ Efectividad del modelo por categoría

## 🏗️ Arquitectura de la Solución

### ✨ Centralización en `evaluador.py`

**Decisión de diseño**: La función `generar_graficos_intuitivos()` se agregó al `EvaluadorModelo` en lugar de duplicarla en cada archivo de modelo.

**Ventajas**:
1. ✅ **Código centralizado** - Una sola ubicación para mantener
2. ✅ **Reutilizable** - Todos los modelos usan la misma implementación
3. ✅ **Consistencia** - Todos los gráficos se generan de la misma manera
4. ✅ **Mantenibilidad** - Actualizaciones en un solo lugar

### 📁 Estructura de Archivos

```
modelos/
├── evaluador.py                    ← Función generar_graficos_intuitivos()
├── modelo_desercion.py             ← Llama a evaluador.generar_graficos_intuitivos()
├── modelo_desercion_escolar.py     ← Llama a evaluador.generar_graficos_intuitivos()
└── modelo_desercion_nuevo.py       ← Llama a evaluador.generar_graficos_intuitivos()
```

## 📈 Gráficos Generados

Cada modelo genera **4 gráficos intuitivos**:

### 1. **Predicciones Correctas vs Incorrectas**
- 📊 Gráfico de barras simple
- ✅ Verde = Correctas
- ❌ Rojo = Incorrectas
- 📝 Muestra cantidad y porcentaje

**Archivo**: `grafico_predicciones_correctas.png`

### 2. **Comparación: Desertores vs No Desertores**
- 📊 Gráfico de barras agrupadas
- 🔵 Azul = Valores Reales
- 🟠 Naranja = Valores Predichos
- 📝 Compara las dos categorías lado a lado

**Archivo**: `grafico_comparacion_desertores.png`

### 3. **Desglose Detallado de Predicciones**
- 📊 Gráfico de barras con 4 categorías:
  - 🟢 Verdaderos Negativos (No desertores bien clasificados)
  - 🟡 Falsos Positivos (No desertores clasificados como desertores)
  - 🟠 Falsos Negativos (Desertores clasificados como no desertores)
  - 🟢 Verdaderos Positivos (Desertores bien clasificados)
- 📝 Muestra cantidad y porcentaje de cada tipo

**Archivo**: `grafico_desglose_detallado.png`

### 4. **Efectividad por Categoría**
- 📊 Gráfico de barras con porcentajes
- 🔵 Efectividad en No Desertores
- 🔴 Efectividad en Desertores
- 🟣 Efectividad Total
- 📝 Líneas de referencia en 90% y 100%

**Archivo**: `grafico_efectividad_categoria.png`

## 🔧 Uso en el Código

### Opción 1: Automático con `evaluar_modelo()`

```python
evaluador = EvaluadorModelo(output_dir='resultados/modelo_nombre')

# Los gráficos intuitivos se generan automáticamente
evaluador.evaluar_modelo(
    modelo=modelo,
    X_test=X_test,
    y_test=y_test,
    feature_names=X.columns,
    nombre_modelo="RandomForest",
    generar_graficos_intuitivos=True  # Por defecto es True
)
```

### Opción 2: Manual

```python
evaluador = EvaluadorModelo(output_dir='resultados/modelo_nombre')

# Generar solo los gráficos intuitivos
evaluador.generar_graficos_intuitivos(
    y_true=y_test,
    y_pred=y_pred,
    nombre_modelo="RandomForest"
)
```

## 📂 Ubicación de los Archivos

Los gráficos se guardan en la estructura:

```
resultados/
├── modelo_base/
│   └── graficos/
│       ├── randomforest/
│       │   ├── grafico_predicciones_correctas.png
│       │   ├── grafico_comparacion_desertores.png
│       │   ├── grafico_desglose_detallado.png
│       │   ├── grafico_efectividad_categoria.png
│       │   ├── curva_roc.png
│       │   └── curva_precision_recall.png
│       ├── kneighbors/
│       └── ... (otros modelos)
└── modelo_nuevo/
    └── graficos/
        └── ... (misma estructura)
```

## 🎨 Características Visuales

- ✨ **Colores intuitivos**: Verde=Bueno, Rojo=Malo, Azul/Naranja=Comparaciones
- 📏 **Etiquetas claras**: Valores y porcentajes en cada barra
- 🔤 **Títulos descriptivos**: Explicaciones simples sin jerga técnica
- 📐 **Tamaño adecuado**: Gráficos grandes y legibles (alta resolución 300 DPI)
- 🎯 **Líneas de referencia**: Para facilitar la interpretación

## ✅ Modelos Actualizados

- ✅ `modelo_desercion.py`
- ✅ `modelo_desercion_escolar.py`
- ✅ `modelo_desercion_nuevo.py`
- ✅ `evaluador.py`

## 🚀 Próximos Pasos

Para generar los gráficos, ejecuta cualquiera de los modelos:

```bash
# Modelo nuevo (base de datos completa)
python modelo_desercion_nuevo.py

# Modelo base
python modelo_desercion_escolar.py

# Modelo original
python modelo_desercion.py
```

## 📝 Notas Técnicas

- Los gráficos se generan **automáticamente** al evaluar cada modelo
- **No requiere** conocimientos de matrices de confusión
- **Compatible** con todos los algoritmos de ML del proyecto
- **Alta resolución** (300 DPI) lista para publicación web

---

**Fecha de creación**: 20 de octubre de 2025  
**Autor**: Sistema de Evaluación de Modelos  
**Versión**: 1.0
