'''
Trabajo de Grado - Predicción de Deserción Escolar
Modelo basado en la variable 'Terminado'

Descripción:
------------
Este script utiliza la columna 'Terminado' como variable objetivo para
predecir la deserción escolar. Se define que:
- Terminado = 1  → No desertó (0)
- Terminado = 2  → Desertó (1)
'''
# ==========================
# modelo_con_terminado.py
# ==========================

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Definir ruta base de resultados
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_terminado')

# Crear subcarpeta para el modelo RandomForest
MODELO_DIR = os.path.join(RESULTADOS_BASE, 'randomforest')
os.makedirs(MODELO_DIR, exist_ok=True)

# ==========================
# 1. Cargar la base de datos
# ==========================
df = pd.read_excel("Base_datos_original.xlsx")

# ==========================
# 2. Definir X e y
# ==========================
X = df.drop(columns=["Terminado"])  # Variables independientes
y = df["Terminado"]                 # Variable dependiente

# ==========================
# 3. Separar en entrenamiento y prueba
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ==========================
# 4. Entrenar modelo
# ==========================
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# ==========================
# 5. Predicciones
# ==========================
y_pred = modelo.predict(X_test)

# ==========================
# 6. Matriz de confusión
# ==========================
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=modelo.classes_.tolist(),  # type: ignore[arg-type]
            yticklabels=modelo.classes_.tolist())  # type: ignore[arg-type]
plt.xlabel("Predicciones")
plt.ylabel("Valores reales")
plt.title("Matriz de confusión - Modelo Terminado")

# Mostrar en pantalla
plt.show()

# Guardar imagen en la carpeta del modelo
plt.savefig(os.path.join(MODELO_DIR, "matriz_confusion.png"), dpi=300, bbox_inches="tight")
print(f"✅ Matriz de confusión guardada en: {MODELO_DIR}/matriz_confusion.png")

# ==========================
# 7. Reporte
# ==========================
reporte = classification_report(y_test, y_pred)
print("Reporte de clasificación:\n", reporte)

# Guardar reporte en archivo
with open(os.path.join(MODELO_DIR, "reporte_clasificacion.txt"), "w") as f:
    f.write(str(reporte))
print(f"✅ Reporte guardado en: {MODELO_DIR}/reporte_clasificacion.txt")
