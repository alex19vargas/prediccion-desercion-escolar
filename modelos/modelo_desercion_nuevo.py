# Predicción de Deserción Escolar

import os
import warnings

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from evaluador import EvaluadorModelo
from sklearn.ensemble import (AdaBoostClassifier, GradientBoostingClassifier,
                              RandomForestClassifier)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (average_precision_score, classification_report,
                             confusion_matrix, precision_recall_curve,
                             roc_auc_score, roc_curve)
from sklearn.model_selection import (GridSearchCV, StratifiedKFold,
                                     cross_val_score, learning_curve,
                                     train_test_split)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Configuración global
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')

# Definir ruta base de resultados
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_nuevo')

# Asegurar que los directorios de resultados existen
os.makedirs(os.path.join(RESULTADOS_BASE, 'matrices'), exist_ok=True)
os.makedirs(os.path.join(RESULTADOS_BASE, 'graficos'), exist_ok=True)
os.makedirs(os.path.join(RESULTADOS_BASE, 'metricas'), exist_ok=True)
os.makedirs(os.path.join(RESULTADOS_BASE, 'modelos'), exist_ok=True)

DATA_PATH = "/Users/alexandervargas/Downloads/DesercionEscolarCompleta.xlsx"

def cargar_datos(path):
    """
    Carga y prepara los datos para el modelo.
    Returns:
        X (DataFrame): Variables predictoras
        y (Series): Variable objetivo (Desertor)
    """
    df = pd.read_excel(path)
    
    # Mostrar las columnas disponibles
    print("\nColumnas en el dataset:")
    print(df.columns.tolist())
    
    # Seleccionar variables predictoras (excluyendo School y Dropped_Out)
    columnas_a_excluir = ["School", "Dropped_Out"]
    X = df.drop(columns=columnas_a_excluir)
    y = df["Dropped_Out"]
    
    print("\n📊 Distribución de la variable objetivo:")
    print(y.value_counts(normalize=True))
    
    # Convertir variables categóricas
    X = pd.get_dummies(X, drop_first=True)
    
    # Escalar las variables numéricas
    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    return X, y

def plot_learning_curve(estimator, X, y, nombre_modelo):
    """
    Genera y guarda la curva de aprendizaje del modelo.
    """
    train_sizes, train_scores, val_scores = learning_curve(  # type: ignore[misc]
        estimator, X, y, cv=5, n_jobs=-1,
        train_sizes=np.linspace(0.1, 1.0, 10),
        scoring='accuracy',
        return_times=False  # Devuelve solo 3 valores: train_sizes, train_scores, val_scores
    )
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, label='Entrenamiento', marker='o')
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1)
    plt.plot(train_sizes, val_mean, label='Validación', marker='s')
    plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.1)
    plt.xlabel('Tamaño del conjunto de entrenamiento')
    plt.ylabel('Score')
    plt.title(f'Curva de Aprendizaje - {nombre_modelo}')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Guardar en subcarpeta del modelo
    modelo_dir = os.path.join(RESULTADOS_BASE, nombre_modelo.lower())
    os.makedirs(modelo_dir, exist_ok=True)
    plt.savefig(os.path.join(modelo_dir, 'learning_curve.png'), dpi=300, bbox_inches='tight')
    plt.close()


def optimizar_hiperparametros(modelo, param_grid, X, y, nombre):
    """
    Realiza búsqueda de grid para optimizar hiperparámetros.
    """
    grid_search = GridSearchCV(
        modelo, param_grid, cv=StratifiedKFold(n_splits=5),
        scoring='accuracy', n_jobs=-1
    )
    grid_search.fit(X, y)
    
    print(f"\n🔧 Mejores parámetros para {nombre}:")
    print(grid_search.best_params_)
    print(f"Mejor score: {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_

def main():
    try:
        # 1. Cargar y preparar datos
        print("🔄 Cargando datos...")
        print(f"Intentando leer archivo desde: {DATA_PATH}")
        X, y = cargar_datos(DATA_PATH)
        print("✅ Datos cargados exitosamente")
        
        # 2. Escalar variables (importante para SVM y KNN)
        scaler = StandardScaler()
        X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
        
        # 3. Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.3, random_state=42, stratify=y
        )
        
        # 4. Configurar los modelos y sus parámetros de búsqueda
        modelos = {
            'LogisticRegression': {
                'model': LogisticRegression(random_state=42, max_iter=1000),
                'params': {
                    'C': [0.1, 1, 10],
                    'penalty': ['l1', 'l2'],
                    'solver': ['liblinear']
                }
            },
            'DecisionTree': {
                'model': DecisionTreeClassifier(random_state=42),
                'params': {
                    'max_depth': [None, 10, 20],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                }
            },
            'RandomForest': {
                'model': RandomForestClassifier(random_state=42),
                'params': {
                    'n_estimators': [100, 200],
                    'max_depth': [None, 10, 20],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2]
                }
            },
            'GradientBoosting': {
                'model': GradientBoostingClassifier(random_state=42),
                'params': {
                    'n_estimators': [100, 200],
                    'learning_rate': [0.01, 0.1],
                    'max_depth': [3, 5]
                }
            },
            'AdaBoost': {
                'model': AdaBoostClassifier(random_state=42),
                'params': {
                    'n_estimators': [50, 100],
                    'learning_rate': [0.5, 1.0]
                }
            },
            'KNeighbors': {
                'model': KNeighborsClassifier(),
                'params': {
                    'n_neighbors': [3, 5, 7],
                    'weights': ['uniform', 'distance'],
                    'metric': ['euclidean', 'manhattan']
                }
            },
            'SVM': {
                'model': SVC(random_state=42, probability=True),
                'params': {
                    'C': [0.1, 1, 10],
                    'kernel': ['rbf', 'linear'],
                    'gamma': ['scale', 'auto']
                }
            },
            'NeuralNetwork': {
                'model': MLPClassifier(random_state=42, max_iter=1000),
                'params': {
                    'hidden_layer_sizes': [(50,), (100,), (50, 50)],
                    'activation': ['relu', 'tanh'],
                    'alpha': [0.0001, 0.001]
                }
            },
            'NaiveBayes': {
                'model': GaussianNB(),
                'params': {
                    'var_smoothing': [1e-9, 1e-8, 1e-7]
                }
            }
        }
        
        # 5. Entrenar y evaluar cada modelo
        print("\n✨ Iniciando entrenamiento y evaluación de modelos...")
        
        # Diccionario para almacenar resultados de todos los modelos
        resultados_comparativos = []
        
        for nombre, config in modelos.items():
            print(f"\n🔄 Entrenando {nombre}...")
            try:
                # Optimizar hiperparámetros
                mejor_modelo = optimizar_hiperparametros(
                    config['model'], config['params'],
                    X_train, y_train, nombre
                )
                
                # Evaluar en conjunto de prueba
                y_pred = mejor_modelo.predict(X_test)
                
                # Calcular métricas
                from sklearn.metrics import (accuracy_score, f1_score,
                                             precision_score, recall_score)
                accuracy = accuracy_score(y_test, y_pred)
                precision = precision_score(y_test, y_pred, average='weighted')
                recall = recall_score(y_test, y_pred, average='weighted')
                f1 = f1_score(y_test, y_pred, average='weighted')
                
                # Guardar resultados para comparación
                resultados_comparativos.append({
                    'Modelo': nombre,
                    'Accuracy': accuracy,
                    'Precision': precision,
                    'Recall': recall,
                    'F1-Score': f1
                })
                
                print(f"\n📊 Resultados para {nombre}:")
                print("\nMatriz de Confusión:")
                cm = confusion_matrix(y_test, y_pred)
                print(cm)
                print("\nReporte de Clasificación:")
                print(classification_report(y_test, y_pred))
                
                # Crear subcarpeta para el modelo
                modelo_dir = os.path.join(RESULTADOS_BASE, nombre.lower())
                os.makedirs(modelo_dir, exist_ok=True)
                
                # Guardar matriz de confusión como imagen
                plt.figure(figsize=(8, 6))
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                           xticklabels=['No Desertor', 'Desertor'],
                           yticklabels=['No Desertor', 'Desertor'])
                plt.title(f'Matriz de Confusión - {nombre}')
                plt.ylabel('Valor Real')
                plt.xlabel('Predicción')
                plt.tight_layout()
                plt.savefig(os.path.join(modelo_dir, 'matriz_confusion.png'), dpi=300, bbox_inches='tight')
                plt.close()
                
                # Usar evaluador para gráficos adicionales (ROC, Precision-Recall)
                print(f"\n📈 Generando gráficos adicionales para {nombre}...")
                evaluador_modelo = EvaluadorModelo(
                    output_dir=os.path.join(modelo_dir)
                )
                
                # Obtener probabilidades si el modelo las soporta
                try:
                    y_prob = mejor_modelo.predict_proba(X_test)[:, 1]
                except:
                    print(f"⚠️  {nombre} no soporta predict_proba, usando predicciones binarias")
                    y_prob = y_pred
                
                # Generar curvas ROC y Precision-Recall
                evaluador_modelo.plot_roc_curve(y_test, y_prob)
                evaluador_modelo.plot_precision_recall_curve(y_test, y_prob)
                evaluador_modelo.guardar_metricas(y_test, y_pred, y_prob)
                
                # Generar gráficos de barras intuitivos (ahora incluido en evaluador)
                print(f"\n📊 Generando gráficos de barras intuitivos para {nombre}...")
                evaluador_modelo.generar_graficos_intuitivos(y_test, y_pred, nombre)
                
                # Generar curva de aprendizaje
                plot_learning_curve(mejor_modelo, X_train, y_train, nombre)
                
                # Guardar modelo
                joblib.dump(mejor_modelo, os.path.join(RESULTADOS_BASE, 'modelos', f'{nombre.lower()}_model.pkl'))
                
                # Graficar importancia de variables si está disponible
                if hasattr(mejor_modelo, 'feature_importances_'):
                    importancias = pd.DataFrame({
                        'Variable': X.columns,
                        'Importancia': mejor_modelo.feature_importances_
                    }).sort_values('Importancia', ascending=False)
                    
                    plt.figure(figsize=(12, 6))
                    sns.barplot(x='Importancia', y='Variable', data=importancias.head(15))
                    plt.title(f'Variables más importantes - {nombre}')
                    plt.tight_layout()
                    plt.savefig(os.path.join(modelo_dir, 'importancia_top15.png'), dpi=300)
                    plt.close()
                    
                    # Usar evaluador para guardar importancia de características (top 20)
                    evaluador_modelo.plot_feature_importance(mejor_modelo, X.columns, top_n=20)
                
            except Exception as e:
                print(f"❌ Error al entrenar {nombre}: {str(e)}")
                continue
        
        # 6. Mostrar tabla comparativa de resultados
        if resultados_comparativos:
            print("\n" + "="*80)
            print("📊 TABLA COMPARATIVA DE TODOS LOS MODELOS")
            print("="*80)
            df_resultados = pd.DataFrame(resultados_comparativos)
            df_resultados = df_resultados.sort_values('Accuracy', ascending=False)
            print(df_resultados.to_string(index=False))
            
            # Guardar resultados en CSV
            csv_path = os.path.join(RESULTADOS_BASE, 'metricas', 'comparacion_modelos.csv')
            df_resultados.to_csv(csv_path, index=False)
            print(f"\n💾 Resultados guardados en: {csv_path}")
            
            # Crear gráfico comparativo
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            
            metricas = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
            for idx, metrica in enumerate(metricas):
                ax = axes[idx // 2, idx % 2]
                df_sorted = df_resultados.sort_values(metrica, ascending=True)
                ax.barh(df_sorted['Modelo'], df_sorted[metrica])
                ax.set_xlabel(metrica)
                ax.set_title(f'Comparación de {metrica}')
                ax.set_xlim([0.85, 1.0])
                
                # Agregar valores en las barras
                for i, v in enumerate(df_sorted[metrica]):
                    ax.text(v, i, f' {v:.4f}', va='center')
            
            plt.tight_layout()
            grafico_path = os.path.join(RESULTADOS_BASE, 'graficos', 'comparacion_todos_modelos.png')
            plt.savefig(grafico_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"📈 Gráfico comparativo guardado en: {grafico_path}")
            
            print("\n🏆 Mejor modelo según Accuracy: " + df_resultados.iloc[0]['Modelo'])
        
        print("\n✅ Proceso completado exitosamente")
        
    except Exception as e:
        print(f"❌ Error general: {str(e)}")

if __name__ == "__main__":
    main()