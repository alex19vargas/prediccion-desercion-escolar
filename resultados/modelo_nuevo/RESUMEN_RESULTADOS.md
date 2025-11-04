# 📊 Resumen de Resultados - Modelo Nuevo

**Fecha de generación:** 18 de octubre de 2025  
**Base de datos:** DesercionEscolarCompleta.xlsx (5000 registros, 34 columnas)  
**Distribución:** 84.44% No Desertores, 15.56% Desertores

---

## 🎯 Modelos Entrenados (9 Total)

### 🥇 Modelos con Rendimiento Perfecto (100% Accuracy)

1. **KNeighbors**
   - Accuracy: 100.00%
   - Precision: 100.00%
   - Recall: 100.00%
   - F1-Score: 100.00%
   - Mejor configuración: n_neighbors=3, weights='distance', metric='euclidean'
   - ✅ 0 Falsos Positivos, 0 Falsos Negativos

2. **SVM (Support Vector Machine)**
   - Accuracy: 100.00%
   - Precision: 100.00%
   - Recall: 100.00%
   - F1-Score: 100.00%
   - Mejor configuración: C=10, kernel='rbf', gamma='scale'
   - ✅ 0 Falsos Positivos, 0 Falsos Negativos

3. **Neural Network (MLP)**
   - Accuracy: 100.00%
   - Precision: 100.00%
   - Recall: 100.00%
   - F1-Score: 100.00%
   - Mejor configuración: hidden_layers=(50,50), activation='tanh', alpha=0.0001
   - ✅ 0 Falsos Positivos, 0 Falsos Negativos

---

### 🥈 Modelos con Excelente Rendimiento (>99%)

4. **Random Forest**
   - Accuracy: 99.27%
   - Precision: 99.26%
   - Recall: 99.27%
   - F1-Score: 99.26%
   - Mejor configuración: n_estimators=100, max_depth=None, min_samples_split=2
   - Errores: 3 FP, 8 FN

5. **Gradient Boosting**
   - Accuracy: 99.13%
   - Precision: 99.13%
   - Recall: 99.13%
   - F1-Score: 99.13%
   - Mejor configuración: n_estimators=200, learning_rate=0.1, max_depth=5
   - Errores: 5 FP, 8 FN

6. **Decision Tree**
   - Accuracy: 99.07%
   - Precision: 99.06%
   - Recall: 99.07%
   - F1-Score: 99.06%
   - Mejor configuración: max_depth=None, min_samples_split=2, min_samples_leaf=1
   - Errores: 5 FP, 9 FN

---

### 🥉 Modelos con Muy Buen Rendimiento (~99%)

7. **Logistic Regression**
   - Accuracy: 98.87%
   - Precision: 98.87%
   - Recall: 98.87%
   - F1-Score: 98.87%
   - Mejor configuración: C=10, penalty='l1', solver='liblinear'
   - Errores: 9 FP, 8 FN

8. **AdaBoost**
   - Accuracy: 98.80%
   - Precision: 98.80%
   - Recall: 98.80%
   - F1-Score: 98.80%
   - Mejor configuración: n_estimators=50, learning_rate=0.5
   - Errores: 10 FP, 8 FN

---

### ⚠️ Modelo con Rendimiento Moderado

9. **Naive Bayes**
   - Accuracy: 87.73%
   - Precision: 91.34%
   - Recall: 87.73%
   - F1-Score: 88.75%
   - Mejor configuración: var_smoothing=1e-09
   - Errores: 158 FP, 26 FN
   - **Nota:** Aunque tiene menor accuracy, detecta bien los casos de deserción (recall=89% para desertores)

---

## 📁 Archivos Generados

### Carpeta: `resultados/modelo_nuevo/`

#### 📦 Modelos Entrenados (9 archivos .pkl)
- `logisticregression_model.pkl` (1.1 KB)
- `decisiontree_model.pkl` (6.7 KB)
- `randomforest_model.pkl` (956 KB)
- `gradientboosting_model.pkl` (1.0 MB)
- `adaboost_model.pkl` (29 KB)
- `kneighbors_model.pkl` (1.1 MB)
- `svm_model.pkl` (94 KB)
- `neuralnetwork_model.pkl` (153 KB)
- `naivebayes_model.pkl` (1.9 KB)

#### 📊 Matrices de Confusión (9 imágenes PNG)
- Una por cada modelo mostrando: Verdaderos Positivos, Falsos Positivos, Verdaderos Negativos, Falsos Negativos

#### 📈 Gráficos de Rendimiento (14 imágenes PNG)
- **Curvas de Aprendizaje (9):** Muestran cómo mejora el modelo con más datos
- **Importancia de Variables (4):** Para RandomForest, GradientBoosting, DecisionTree, AdaBoost
- **Comparación General (1):** Gráfico de barras comparando todos los modelos

#### 📋 Métricas (1 archivo CSV)
- `comparacion_modelos.csv`: Tabla con Accuracy, Precision, Recall y F1-Score de todos los modelos

---

## 🎓 Interpretación de Resultados

### Variables Más Importantes (según Random Forest):
1. **Final_Grade** - Calificación final
2. **Grade_2** - Calificación del segundo período
3. **Grade_1** - Calificación del primer período
4. **Number_of_Absences** - Número de ausencias
5. **Number_of_Failures** - Número de reprobaciones

### Recomendación de Modelo para Producción:
Aunque **KNeighbors, SVM y Neural Network** tienen 100% de precisión, recomiendo usar **Random Forest** o **Gradient Boosting** porque:
- ✅ Rendimiento excelente (>99%)
- ✅ Más robustos ante nuevos datos
- ✅ Proporcionan importancia de variables
- ✅ Menos propensos a sobreajuste
- ✅ Más interpretables

### Uso del Modelo:
```python
import joblib
import pandas as pd

# Cargar el modelo
modelo = joblib.load('resultados/modelo_nuevo/modelos/randomforest_model.pkl')

# Preparar datos nuevos (deben tener las mismas columnas que el entrenamiento)
X_nuevo = pd.DataFrame(...)

# Hacer predicciones
predicciones = modelo.predict(X_nuevo)
probabilidades = modelo.predict_proba(X_nuevo)

# 0 = No Desertor, 1 = Desertor
```

---

## 📝 Notas Técnicas

- **División de datos:** 70% entrenamiento, 30% prueba
- **Validación cruzada:** StratifiedKFold con 5 splits
- **Optimización:** GridSearchCV para encontrar mejores hiperparámetros
- **Escalado:** StandardScaler aplicado a todas las variables
- **Variables categóricas:** Convertidas con pd.get_dummies()

---

## 🔄 Próximos Pasos

1. ✅ Comparar con `modelo_base` (base de datos original)
2. ⏳ Validar con datos reales del siguiente semestre
3. ⏳ Implementar sistema de alertas tempranas
4. ⏳ Integrar con aplicación web
5. ⏳ Crear dashboard interactivo
