# 📊 Resultados de Modelos de Deserción Escolar

## 📁 Estructura de Carpetas

```
resultados/
├── modelo_base/              ← Resultados de modelo_desercion_escolar.py
│   ├── modelos/              ← Archivos .pkl de modelos entrenados
│   ├── matrices/             ← Matrices de confusión (PNG)
│   ├── graficos/             ← Gráficos por modelo
│   │   ├── mlpclassifier/
│   │   │   ├── curva_roc.png
│   │   │   ├── curva_precision_recall.png
│   │   │   ├── grafico_predicciones_correctas.png
│   │   │   ├── grafico_comparacion_desertores.png
│   │   │   ├── grafico_desglose_detallado.png
│   │   │   ├── grafico_efectividad_categoria.png
│   │   │   └── metricas_clasificacion.csv
│   │   └── ... (otros modelos)
│   └── metricas/             ← Métricas comparativas
│
├── modelo_nuevo/             ← Resultados de modelo_desercion_nuevo.py
│   └── (misma estructura que modelo_base/)
│
└── experimentos_antiguos/    ← Resultados históricos (no usar)
    ├── Dataset_Completa_resultados/
    ├── Dataset_Organizada_resultados/
    ├── raiz_antiguos/
    └── carpetas_timestamp/
```

## 🎯 Uso

### Para entrenar modelos:

```bash
cd /Users/alexandervargas/Trabajo_Grado/proyecto_desercion/modelos

# Modelo base (9 algoritmos)
python modelo_desercion_escolar.py

# Modelo nuevo (9 algoritmos con BD completa)
python modelo_desercion_nuevo.py
```

### Para acceder a resultados:

Todos los resultados se guardan automáticamente en:
- `resultados/modelo_base/` - Para modelo_desercion_escolar.py
- `resultados/modelo_nuevo/` - Para modelo_desercion_nuevo.py

## 📊 Tipos de Archivos Generados

Por cada modelo se genera:

1. **Modelo entrenado** (.pkl) - En `modelos/`
2. **Matriz de confusión** (.png) - En `matrices/`
3. **Gráficos técnicos** - En `graficos/[nombre_modelo]/`:
   - Curva ROC
   - Curva Precision-Recall
   - Learning Curve
   - Importancia de características (si aplica)
4. **Gráficos intuitivos** - En `graficos/[nombre_modelo]/`:
   - Predicciones correctas vs incorrectas
   - Comparación desertores vs no desertores
   - Desglose detallado
   - Efectividad por categoría
5. **Métricas** (.csv, .txt) - En `graficos/[nombre_modelo]/`

## 🚫 Carpeta experimentos_antiguos/

Esta carpeta contiene resultados de ejecuciones anteriores del proyecto.
**NO usar estos archivos** - son solo para referencia histórica.

Los modelos actuales siempre guardan en `modelo_base/` o `modelo_nuevo/`.

---

**Última actualización**: 20 de octubre de 2025  
**Ubicación**: `/Users/alexandervargas/Trabajo_Grado/proyecto_desercion/resultados/`
