
"""
Trabajo de Grado - Predicción de Deserción Escolar
--------------------------------------------------
Este script entrena y compara varios modelos de clasificación para predecir la deserción escolar
usando la variable 'Inscrito_actual' como objetivo.

Definición de la variable objetivo:
----------------------------------
- Inscrito_actual = 1  → Sí se inscribió (No desertó = 0)
- Inscrito_actual = 2  → No se inscribió (Desertó = 1)

El script genera gráficas de matriz de confusión y reportes de clasificación para cada modelo.
"""

# Modelo_con_inscrito.py

import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Configuración global
warnings.filterwarnings("ignore")  # Ignorar warnings para limpieza de salida
DATA_PATH = "/Users/alexandervargas/Downloads/DataBase.xlsx"  # Ruta del archivo de datos

# Definir ruta base de resultados
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_inscrito')

# Asegurar que el directorio de resultados existe
os.makedirs(RESULTADOS_BASE, exist_ok=True)


# 1. Cargar y preparar datos
def cargar_datos(path):
    """
    Carga el dataset desde un archivo Excel y prepara las variables independientes (X)
    y la variable dependiente (y) para el modelo.
    - X2: todas las columnas excepto 'Inscrito_actual' y 'Terminado'
    - y: columna 'Inscrito_actual'
    """
    df = pd.read_excel(path)
    X = df.drop(columns=["Inscrito_actual"])
    X2 = X.drop(columns=["Terminado"])
    y = df["Inscrito_actual"]
    return X2, y


# 2. Dividir datos en entrenamiento y prueba
def dividir_datos(X, y, test_size=0.3, random_state=42):
    """
    Divide los datos en conjuntos de entrenamiento y prueba usando stratificación
    para mantener la proporción de clases.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


# 3. Funciones de entrenamiento de modelos

    # Entrena un modelo RandomForestClassifier
def entrenar_random_forest(X_train, y_train, random_state=42):
    
    modelo = RandomForestClassifier(random_state=random_state)
    modelo.fit(X_train, y_train)
    return modelo

    # Entrena un modelo Support Vector Machine (SVC)
def entrenar_svm(X_train, y_train, random_state=42):
    
    modelo = SVC(random_state=random_state)
    modelo.fit(X_train, y_train)
    return modelo

    #Entrena un modelo de Regresión Logística
def entrenar_logistic_regression(X_train, y_train, random_state=42):
    
    modelo = LogisticRegression(random_state=random_state, max_iter=1000)
    modelo.fit(X_train, y_train)
    return modelo

    #Entrena un modelo Gradient Boosting Classifier
def entrenar_gradient_boosting(X_train, y_train, random_state=42):

    modelo = GradientBoostingClassifier(random_state=random_state)
    modelo.fit(X_train, y_train)
    return modelo


# 4. Evaluación y visualización de resultados
def evaluar_modelo(modelo, X_test, y_test, nombre="RandomForest"):
    """
    Evalúa el modelo entrenado:
    - Calcula y guarda la matriz de confusión como imagen PNG
    - Genera y guarda el reporte de clasificación (precision, recall, f1-score)
    - Imprime la ruta de los archivos generados
    """
    # Crear subcarpeta para el modelo
    modelo_dir = os.path.join(RESULTADOS_BASE, nombre.lower())
    os.makedirs(modelo_dir, exist_ok=True)
    
    y_pred = modelo.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=modelo.classes_, yticklabels=modelo.classes_)
    plt.xlabel("Predicciones")
    plt.ylabel("Valores reales")
    plt.title(f"Matriz de confusión - {nombre}")
    plt.savefig(os.path.join(modelo_dir, "matriz_confusion.png"), dpi=300, bbox_inches="tight")
    plt.close()
    reporte = classification_report(y_test, y_pred)
    with open(os.path.join(modelo_dir, "reporte_clasificacion.txt"), "w") as f:
        f.write(str(reporte))  # type: ignore[arg-type]
    print(f"✅ Resultados guardados en: {modelo_dir}/")
    return reporte


# 5. Ejecución principal del script
def main():
    # Cargar y preparar los datos
    X, y = cargar_datos(DATA_PATH)
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = dividir_datos(X, y)

    # Diccionario de modelos a entrenar
    modelos = {
        "RandomForest": entrenar_random_forest,
        "SVM": entrenar_svm,
        "LogisticRegression": entrenar_logistic_regression,
        "GradientBoosting": entrenar_gradient_boosting
    }

    # Entrenar y evaluar cada modelo
    for nombre, funcion in modelos.items():
        print(f"\nEntrenando y evaluando: {nombre}")
        modelo = funcion(X_train, y_train)
        reporte = evaluar_modelo(modelo, X_test, y_test, nombre=nombre)
        print(reporte)

# Punto de entrada del script
if __name__ == "__main__":
    main()
