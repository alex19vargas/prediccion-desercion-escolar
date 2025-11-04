# Organización del Dashboard por Pestañas

## 📋 Descripción General

Este documento explica la nueva organización del dashboard y cómo se categorizan las imágenes en cada pestaña.

---

## 🎯 Problema Identificado

El dashboard mostraba las siguientes inconsistencias:

- **Métricas del Modelo**: No mostraba nada
- **Gráficos y Curvas**: No mostraba los nuevos gráficos intuitivos, solo curvas
- **Matrices de Confusión**: Funcionaba correctamente
- **Todas las Imágenes**: Mostraba todo mezclado

---

## ✅ Solución Implementada

### Cambios en el Backend (`backend/routes/dashboard_routes.py`)

#### 1. Lectura Directa desde Resultados de Modelos

**ANTES:**
```python
# Leía desde frontend/static/img/
base_dir = os.path.join(current_app.static_folder, 'img')
```

**AHORA:**
```python
# Lee directamente desde resultados/modelo_nuevo/
def get_modelo_base_dir():
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(project_root, 'resultados', MODELO_ACTIVO)
```

**Beneficio:** No necesita sincronización manual. Lee directamente las últimas imágenes generadas.

---

#### 2. Categorización Mejorada de Imágenes

```python
def categorize_image(filename):
    """Categoriza una imagen según su nombre de archivo"""
    filename_lower = filename.lower()
    
    # Matrices de confusión
    if 'matriz' in filename_lower or 'confusion' in filename_lower:
        return 'matrices'
    
    # Curvas y gráficos de aprendizaje
    if any(keyword in filename_lower for keyword in ['learning', 'curva_roc', 'curva_precision', 'roc', 'precision_recall']):
        return 'curvas'
    
    # Gráficos intuitivos
    if any(keyword in filename_lower for keyword in ['grafico_', 'predicciones', 'comparacion', 'desglose', 'efectividad']):
        return 'graficos_intuitivos'
    
    # Importancia de características
    if 'importancia' in filename_lower:
        return 'importancia'
    
    return 'otros'
```

---

#### 3. Métricas Consolidadas por Modelo

```python
@bp.route('/api/metricas')
@login_required
def get_metricas():
    """Obtiene métricas consolidadas de todos los modelos"""
    base_dir = get_modelo_base_dir()
    metricas_por_modelo = {}
    
    for modelo_dir in os.listdir(base_dir):
        modelo_path = os.path.join(base_dir, modelo_dir)
        metricas_file = os.path.join(modelo_path, 'metricas.txt')
        
        if os.path.isdir(modelo_path) and os.path.exists(metricas_file):
            metricas = parse_metricas_file(metricas_file)
            if metricas:
                metricas_por_modelo[modelo_dir] = metricas
    
    return jsonify(metricas_por_modelo)
```

**Función de Parseo:**
```python
def parse_metricas_file(filepath):
    """Extrae métricas del archivo de texto usando regex"""
    # Busca: accuracy, precision, recall, f1_score, roc_auc, avg_precision
    # Ejemplo: accuracy                           0.99      1500
    # Ejemplo: ROC AUC Score: 0.9998
```

---

### Cambios en el Frontend (`frontend/templates/dashboard.html`)

#### 1. Nueva Organización de Pestañas

**ANTES:**
- 📊 Métricas del Modelo
- 📈 Gráficos y Curvas
- 🎯 Matrices de Confusión
- 🖼️ Todas las Imágenes

**AHORA:**
- 📊 **Métricas del Modelo** - Muestra métricas parseadas de `metricas.txt` por cada modelo
- 📈 **Curvas de Aprendizaje** - Learning curves, ROC curves, Precision-Recall curves
- 💡 **Gráficos Intuitivos** - Predicciones, comparaciones, desglose, efectividad
- 🎯 **Matrices de Confusión** - Solo matrices de confusión
- 🖼️ **Todas las Imágenes** - Muestra todas las categorías

---

#### 2. Estadísticas Actualizadas en Cards

```html
<div class="stats-grid">
    <div class="stat-card">
        <h3>Total de Imágenes</h3>
        <div class="value">{{ stats.total_imagenes }}</div>
    </div>
    <div class="stat-card">
        <h3>Curvas de Aprendizaje</h3>
        <div class="value">{{ stats.graficos }}</div>
    </div>
    <div class="stat-card">
        <h3>Matrices de Confusión</h3>
        <div class="value">{{ stats.matrices }}</div>
    </div>
    <div class="stat-card">
        <h3>Gráficos Intuitivos</h3>
        <div class="value">{{ stats.graficos_intuitivos }}</div>
    </div>
</div>
```

---

#### 3. JavaScript - Renderizado por Categorías

```javascript
async function loadImages() {
    const response = await fetch('/api/imagenes');
    const images = await response.json();
    
    // Filtrar por categoría
    const curvas = images.filter(img => img.categoria === 'curvas');
    const graficos_intuitivos = images.filter(img => img.categoria === 'graficos_intuitivos');
    const matrices = images.filter(img => img.categoria === 'matrices');
    
    // Renderizar cada categoría en su contenedor
    renderImages(curvas, 'curvas-container');
    renderImages(graficos_intuitivos, 'graficos-container');
    renderImages(matrices, 'matrices-container');
    renderImages(images, 'todas-container');
}
```

---

#### 4. JavaScript - Métricas por Modelo

```javascript
async function loadMetrics() {
    const response = await fetch('/api/metricas');
    const data = await response.json();
    
    // data = { 
    //   "randomforest": { accuracy: 0.99, precision: 0.99, ... },
    //   "logisticregression": { accuracy: 0.98, ... },
    //   ...
    // }
    
    for (const [modelo, metricas] of Object.entries(data)) {
        // Crear sección por modelo
        const modeloSection = document.createElement('div');
        modeloSection.innerHTML = `<h3>${modelo}</h3>`;
        
        // Agregar cada métrica
        for (const [key, value] of Object.entries(metricas)) {
            // Renderizar: Accuracy: 99.00%
        }
    }
}
```

---

## 📂 Estructura de Archivos

### Resultados del Modelo

```
resultados/modelo_nuevo/
├── randomforest/
│   ├── learning_curve.png              → Curvas
│   ├── curva_roc.png                   → Curvas
│   ├── curva_precision_recall.png      → Curvas
│   ├── matriz_confusion.png            → Matrices
│   ├── grafico_predicciones_correctas.png      → Gráficos Intuitivos
│   ├── grafico_comparacion_desertores.png      → Gráficos Intuitivos
│   ├── grafico_desglose_detallado.png          → Gráficos Intuitivos
│   ├── grafico_efectividad_categoria.png       → Gráficos Intuitivos
│   ├── importancia_top15.png                   → Importancia
│   ├── importancia_caracteristicas.png         → Importancia
│   └── metricas.txt                    → Métricas (parseado)
├── logisticregression/
│   └── ... (misma estructura)
└── ... (otros 7 modelos)
```

---

## 🎨 Categorías de Imágenes

| Categoría | Archivos Incluidos | Pestaña |
|-----------|-------------------|---------|
| **curvas** | `learning_curve.png`, `curva_roc.png`, `curva_precision_recall.png` | 📈 Curvas de Aprendizaje |
| **graficos_intuitivos** | `grafico_predicciones_correctas.png`, `grafico_comparacion_desertores.png`, `grafico_desglose_detallado.png`, `grafico_efectividad_categoria.png` | 💡 Gráficos Intuitivos |
| **matrices** | `matriz_confusion.png` | 🎯 Matrices de Confusión |
| **importancia** | `importancia_top15.png`, `importancia_caracteristicas.png` | 🖼️ Todas las Imágenes |

---

## 🔧 Configuración del Modelo Activo

El modelo activo se configura en `backend/routes/dashboard_routes.py`:

```python
# Línea 10
MODELO_ACTIVO = 'modelo_nuevo'
```

**Opciones disponibles:**
- `modelo_nuevo` - Mejor rendimiento (9 algoritmos)
- `modelo_inscrito` - Basado en variable Inscrito_actual (4 algoritmos)
- `modelo_terminado` - Basado en variable Terminado (1 algoritmo)

---

## 📊 Métricas Mostradas

El dashboard parsea y muestra las siguientes métricas por cada modelo:

| Métrica | Fuente | Formato |
|---------|--------|---------|
| **Accuracy** | `accuracy                           0.99      1500` | 99.00% |
| **Precision** | `weighted avg       0.99      0.98      0.99      1500` (columna 1) | 99.00% |
| **Recall** | `weighted avg       0.99      0.98      0.99      1500` (columna 2) | 98.00% |
| **F1-Score** | `weighted avg       0.99      0.98      0.99      1500` (columna 3) | 99.00% |
| **ROC AUC** | `ROC AUC Score: 0.9998` | 99.98% |
| **Avg Precision** | `Average Precision Score: 0.9990` | 99.90% |

---

## 🚀 Ventajas de la Nueva Implementación

### 1. **Lectura Directa**
- ✅ No necesita `sync_images.py`
- ✅ Siempre muestra las imágenes más recientes
- ✅ Elimina pasos manuales

### 2. **Categorización Inteligente**
- ✅ Separación clara por tipo de visualización
- ✅ Fácil encontrar información específica
- ✅ Mejor experiencia de usuario

### 3. **Métricas Consolidadas**
- ✅ Parsea automáticamente archivos `metricas.txt`
- ✅ Muestra métricas de TODOS los modelos
- ✅ Comparación visual fácil

### 4. **Escalabilidad**
- ✅ Funciona con cualquier número de modelos
- ✅ Detección automática de nuevas carpetas
- ✅ Sin configuración adicional

---

## 🔍 Verificación

### Comprobar que Funciona Correctamente

1. **Iniciar servidor:**
   ```bash
   source .venv/bin/activate
   python run.py
   ```

2. **Abrir navegador:**
   ```
   http://localhost:5000
   ```

3. **Verificar pestañas:**
   - ✅ **Métricas**: Muestra secciones por modelo con 6 métricas cada uno
   - ✅ **Curvas de Aprendizaje**: Muestra 3 curvas por modelo (learning, ROC, PR)
   - ✅ **Gráficos Intuitivos**: Muestra 4 gráficos por modelo
   - ✅ **Matrices**: Muestra 1 matriz por modelo
   - ✅ **Todas**: Muestra todas las imágenes (8-10 por modelo)

4. **Verificar estadísticas:**
   - Total de imágenes: ~81 (9 modelos × 9 archivos PNG promedio)
   - Curvas: ~27 (9 modelos × 3 curvas)
   - Matrices: 9 (1 por modelo)
   - Gráficos Intuitivos: ~36 (9 modelos × 4 gráficos)

---

## 🐛 Troubleshooting

### Problema: "No hay imágenes disponibles"

**Causa:** No se han ejecutado los modelos.

**Solución:**
```bash
cd modelos
python modelo_desercion_nuevo.py
```

---

### Problema: "No hay métricas disponibles"

**Causa:** Archivos `metricas.txt` no existen.

**Solución:** Verificar que cada carpeta de modelo tenga su archivo:
```bash
ls -la resultados/modelo_nuevo/*/metricas.txt
```

---

### Problema: Imágenes rotas o no se cargan

**Causa:** Ruta incorrecta en `get_modelo_base_dir()`.

**Solución:** Verificar la ruta:
```python
base_dir = get_modelo_base_dir()
print(base_dir)  # Debe imprimir: /ruta/proyecto_desercion/resultados/modelo_nuevo
```

---

### Problema: Faltan imágenes en categorías

**Causa:** Función `categorize_image()` no reconoce el nombre.

**Solución:** Agregar palabra clave al mapeo:
```python
def categorize_image(filename):
    if 'mi_nueva_imagen' in filename_lower:
        return 'curvas'  # o la categoría correcta
```

---

## 📝 Próximas Mejoras

### Posibles Extensiones

1. **Filtros por Modelo**
   - Dropdown para seleccionar modelo específico
   - Ver solo imágenes de un modelo a la vez

2. **Comparación Lado a Lado**
   - Mostrar misma métrica de todos los modelos juntos
   - Gráfico de barras comparativo

3. **Exportación de Reportes**
   - Generar PDF con métricas y gráficos
   - Descargar todas las imágenes como ZIP

4. **Gráficos Interactivos**
   - Usar Plotly en lugar de imágenes estáticas
   - Zoom, pan, y tooltips

---

## 📌 Resumen

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| **Fuente de Imágenes** | `frontend/static/img/` (sincronizado manualmente) | `resultados/modelo_nuevo/` (directo) |
| **Categorización** | Genérica (graficos, matrices) | Específica (curvas, intuitivos, matrices) |
| **Métricas** | De base de datos | Parseadas de archivos `metricas.txt` |
| **Pestañas** | 4 pestañas | 5 pestañas (nueva: Gráficos Intuitivos) |
| **Actualización** | Manual (sync_images.py) | Automática (lectura directa) |
| **Modelos Mostrados** | Último sincronizado | Todos los modelos ejecutados |

---

**Última actualización:** 21 de octubre de 2025  
**Responsable:** Sistema de Predicción de Deserción Escolar  
**Versión:** 2.0 - Dashboard Reorganizado
