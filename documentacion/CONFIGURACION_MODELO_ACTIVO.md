# Configuración del Modelo Activo en la Interfaz Web

**Fecha:** 21 de octubre de 2025  
**Estado:** ✅ CONFIGURADO - modelo_nuevo

## 🎯 Resumen Ejecutivo

La interfaz web está configurada para mostrar las imágenes y resultados del modelo **`modelo_nuevo`**, que ha sido identificado como el modelo con mejor rendimiento.

## 📍 Dónde Cambiar el Modelo Activo

### Archivo Principal: `backend/sync_images.py`

**Ubicación:** `/Users/alexandervargas/Trabajo_Grado/proyecto_desercion/backend/sync_images.py`

**Línea a modificar:** Línea 28

```python
# ╔═══════════════════════════════════════════════════════════════════╗
# ║  🎯 CONFIGURACIÓN DEL MODELO ACTIVO - CAMBIAR AQUÍ               ║
# ╚═══════════════════════════════════════════════════════════════════╝

MODELO_ACTIVO = 'modelo_nuevo'  # ← CAMBIAR ESTA LÍNEA PARA USAR OTRO MODELO
```

### Modelos Disponibles

```python
# Opciones disponibles (según carpetas en resultados/):
MODELO_ACTIVO = 'modelo_nuevo'      # ✅ ACTUAL - Mejor rendimiento
MODELO_ACTIVO = 'modelo_inscrito'   # Basado en variable Inscrito_actual
MODELO_ACTIVO = 'modelo_terminado'  # Basado en variable Terminado
MODELO_ACTIVO = 'modelo_base'       # Modelo base original
```

## 🔄 Proceso para Cambiar de Modelo

### Paso 1: Identificar el Nuevo Mejor Modelo

Ejecuta tus modelos y compara métricas:

```bash
# Ejecutar modelo y ver resultados
cd modelos/
python modelo_desercion_nuevo.py

# Ver comparación de métricas
cat resultados/modelo_nuevo/metricas/comparacion_modelos.csv
```

### Paso 2: Modificar la Configuración

Edita `backend/sync_images.py`:

```python
# Cambiar de:
MODELO_ACTIVO = 'modelo_nuevo'

# A (ejemplo):
MODELO_ACTIVO = 'modelo_inscrito'
```

### Paso 3: Sincronizar Imágenes

Ejecuta el script de sincronización:

```bash
cd /Users/alexandervargas/Trabajo_Grado/proyecto_desercion
python backend/sync_images.py
```

**Salida esperada:**
```
╔════════════════════════════════════════════════════════════════════╗
║                    SINCRONIZADOR DE IMÁGENES                       ║
╚════════════════════════════════════════════════════════════════════╝

📊 MODELOS DISPONIBLES:
...
📁 modelo_inscrito ✅ ACTIVO
...

✨ SINCRONIZACIÓN COMPLETADA
📊 Modelo activo: modelo_inscrito
📸 Imágenes copiadas: X
```

### Paso 4: Reiniciar el Servidor

```bash
# Si el servidor está corriendo, detenerlo (Ctrl+C)
# Luego reiniciar:
python run.py
```

### Paso 5: Verificar en el Dashboard

1. Abre tu navegador en `http://localhost:5000`
2. Inicia sesión
3. Verifica que las imágenes corresponden al nuevo modelo

## 📁 Estructura de Carpetas

### Estructura Nueva (Recomendada)

Después de ejecutar los modelos con las correcciones aplicadas:

```
resultados/
└── modelo_nuevo/
    ├── adaboost/
    │   ├── learning_curve.png
    │   ├── matriz_confusion.png
    │   ├── importancia_top15.png
    │   ├── importancia_variables.png
    │   ├── roc_curve.png
    │   ├── precision_recall_curve.png
    │   └── metricas.json
    ├── randomforest/
    │   └── ... (mismos archivos)
    ├── ... (otros 7 modelos)
    └── comparacion_todos_modelos.png
```

El script `sync_images.py` copiará automáticamente:
- Todas las imágenes de cada subcarpeta de modelo
- Agregará prefijo del modelo: `randomforest_matriz_confusion.png`

### Estructura Antigua (Actual en modelo_nuevo)

```
resultados/
└── modelo_nuevo/
    ├── graficos/
    │   ├── learning_curve_*.png
    │   ├── importancia_*.png
    │   ├── adaboost/
    │   ├── randomforest/
    │   └── ... (subcarpetas con ROC, PR)
    ├── matrices/
    │   └── matriz_confusion_*.png
    └── metricas/
        └── comparacion_modelos.csv
```

El script detecta automáticamente qué estructura usa cada modelo.

## 🔍 Verificación del Modelo Activo

### Ver qué modelo está activo:

```bash
python backend/sync_images.py
```

Busca la línea: `📁 modelo_nuevo ✅ ACTIVO`

### Ver qué imágenes están en el frontend:

```bash
ls -lh frontend/static/img/*.png | wc -l
```

### Ver estructura del modelo activo:

```bash
tree resultados/modelo_nuevo -L 2
```

## 📊 Tipos de Imágenes Sincronizadas

El script copia todas las imágenes `.png` encontradas en el modelo activo:

| Tipo de Imagen | Nombre Original | Nombre en Frontend |
|----------------|-----------------|-------------------|
| Matriz de Confusión | `matriz_confusion.png` | `modelo_matriz_confusion.png` |
| Curva de Aprendizaje | `learning_curve.png` | `modelo_learning_curve.png` |
| Curva ROC | `roc_curve.png` | `modelo_roc_curve.png` |
| Precision-Recall | `precision_recall_curve.png` | `modelo_precision_recall_curve.png` |
| Importancia Variables | `importancia_variables.png` | `modelo_importancia_variables.png` |
| Gráficos Intuitivos | `graficos_intuitivos_*.png` | `modelo_graficos_intuitivos_*.png` |
| Comparación General | `comparacion_todos_modelos.png` | `comparacion_todos_modelos.png` |

## 🚀 Ejemplo Completo de Cambio

**Escenario:** Descubres que `modelo_inscrito` tiene mejor accuracy que `modelo_nuevo`.

### 1. Editar configuración

```bash
code backend/sync_images.py
```

Cambiar línea 28:
```python
MODELO_ACTIVO = 'modelo_inscrito'  # Cambio de modelo_nuevo a modelo_inscrito
```

### 2. Sincronizar

```bash
python backend/sync_images.py
```

Salida:
```
📁 modelo_inscrito ✅ ACTIVO
...
📸 Imágenes copiadas: 42
```

### 3. Reiniciar servidor

```bash
# Terminal donde corre Flask:
Ctrl+C
python run.py
```

### 4. Verificar en navegador

- Abre `http://localhost:5000/dashboard`
- Las nuevas matrices e imágenes deben aparecer
- Verifica que corresponden al nuevo modelo

## 📝 Notas Importantes

### Limpieza Automática

El script **elimina las imágenes antiguas** antes de copiar las nuevas:

```python
# Limpiar imágenes antiguas (opcional - comentar si no se desea)
for old_file in static_img_dir.glob('*.png'):
    old_file.unlink()
```

Si NO quieres que se eliminen, comenta estas líneas en `sync_images.py`.

### Caché del Navegador

Después de cambiar el modelo, es posible que necesites:
1. **Refrescar el navegador:** `Ctrl+F5` (Windows) o `Cmd+Shift+R` (Mac)
2. **Limpiar caché:** En la configuración del navegador

### Estructura Mixta

El script soporta **ambas estructuras** automáticamente:
- ✅ Estructura NUEVA: Carpetas por modelo
- ✅ Estructura ANTIGUA: Carpetas graficos/matrices

## 🔧 Troubleshooting

### Problema: No se copian imágenes

**Solución:**
```bash
# Verificar que el modelo existe
ls -la resultados/modelo_nuevo/

# Verificar permisos
chmod -R 755 resultados/modelo_nuevo/

# Ver qué detecta el script
python backend/sync_images.py
```

### Problema: Imágenes no aparecen en el dashboard

**Solución:**
```bash
# Verificar que se copiaron
ls -lh frontend/static/img/*.png

# Reiniciar servidor
pkill -f "python run.py"
python run.py

# Limpiar caché del navegador
```

### Problema: Quiero usar modelo personalizado

**Solución:**

1. Crea tu carpeta en `resultados/mi_modelo_custom/`
2. Genera imágenes dentro siguiendo la estructura
3. Edita `sync_images.py`:
   ```python
   MODELO_ACTIVO = 'mi_modelo_custom'
   ```
4. Ejecuta el script

## 📚 Archivos Relacionados

- **`backend/sync_images.py`** - Script de sincronización (PRINCIPAL)
- **`backend/routes/dashboard_routes.py`** - Lee imágenes de frontend/static/img/
- **`frontend/templates/dashboard.html`** - Muestra las imágenes
- **`modelos/modelo_desercion_nuevo.py`** - Genera resultados para modelo_nuevo
- **`modelos/modelo_con_inscrito.py`** - Genera resultados para modelo_inscrito
- **`modelos/modelo_con_terminado.py`** - Genera resultados para modelo_terminado

## ✅ Checklist de Cambio de Modelo

- [ ] Ejecutar el nuevo modelo y verificar que genera resultados
- [ ] Comparar métricas con modelo actual
- [ ] Decidir si el nuevo modelo es mejor
- [ ] Editar `backend/sync_images.py` línea 28
- [ ] Ejecutar `python backend/sync_images.py`
- [ ] Verificar que se copiaron imágenes (debe mostrar cantidad > 0)
- [ ] Reiniciar servidor Flask
- [ ] Abrir dashboard en navegador
- [ ] Verificar que imágenes corresponden al nuevo modelo
- [ ] Limpiar caché del navegador si es necesario
- [ ] Documentar el cambio (fecha, razón, métricas)

## 🎯 Modelo Actual

**Modelo activo:** `modelo_nuevo`  
**Fecha de configuración:** 21 de octubre de 2025  
**Razón:** Mejor rendimiento general en métricas de clasificación  
**Algoritmos incluidos:** 9 (LR, DT, RF, GB, AB, KNN, SVM, NN, NB)  
**Total imágenes:** 81

---

**Última actualización:** 21 de octubre de 2025  
**Responsable:** Sistema de predicción de deserción escolar
