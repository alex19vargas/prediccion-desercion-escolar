
# Predicción de Deserción Escolar --> Desertor: 1, No Desertor: 0

# import catboost as cb  # he tenido problemas con la instalación de este modelo
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
RESULTADOS_BASE = os.path.join(os.path.dirname(__file__), '..', 'resultados', 'modelo_base')

# Asegurar que los directorios de resultados existen
os.makedirs(os.path.join(RESULTADOS_BASE, 'matrices'), exist_ok=True)
os.makedirs(os.path.join(RESULTADOS_BASE, 'graficos'), exist_ok=True)
os.makedirs(os.path.join(RESULTADOS_BASE, 'metricas'), exist_ok=True)
os.makedirs(os.path.join(RESULTADOS_BASE, 'modelos'), exist_ok=True)

DATA_PATH = "/Users/alexandervargas/Downloads/DataBase_Completa.xlsx"

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
    
    # Crear variable objetivo basada en inscrito_actual
    df["desertor"] = df["inscrito_actual"].apply(lambda x: 0 if x == 1 else 1)
    
    # Seleccionar variables predictoras (excluyendo inscrito_actual y terminado)
    columnas_a_excluir = ["inscrito_actual", "terminado", "desertor"]  # Excluimos las variables que no deben influir
    X = df.drop(columns=columnas_a_excluir)
    y = df["desertor"]
    
    # Convertir variables categóricas
    X = pd.get_dummies(X, drop_first=True)
    
    # Escalar las variables numéricas
    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    return X, y

def plot_learning_curve(estimator, X, y, nombre):
    
    # Genera y guarda la curva de aprendizaje para un modelo.
    train_sizes = np.linspace(0.1, 1.0, 10)
    train_sizes, train_scores, test_scores = learning_curve(  # type: ignore[misc]
        estimator, X, y, cv=StratifiedKFold(n_splits=5),
        n_jobs=-1, train_sizes=train_sizes, scoring='accuracy',
        return_times=False  # Devuelve solo 3 valores: train_sizes, train_scores, test_scores
    )
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, label='Training score', color='blue')
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, 
                     alpha=0.1, color='blue')
    plt.plot(train_sizes, test_mean, label='Cross-validation score', color='red')
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, 
                     alpha=0.1, color='red')
    
    plt.xlabel('Training Size')
    plt.ylabel('Score')
    plt.title(f'Learning Curve - {nombre}')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'learning_curve_{nombre.lower()}.png'), dpi=300, bbox_inches='tight')
    plt.close()


def optimizar_hiperparametros(modelo, param_grid, X, y, nombre):

    # Realiza búsqueda de grid para optimizar hiperparámetros.
    grid_search = GridSearchCV(
        modelo, param_grid, cv=StratifiedKFold(n_splits=5),
        scoring='accuracy', n_jobs=-1
    )
    grid_search.fit(X, y)
    
    print(f"\n🔧 Mejores parámetros para {nombre}:")
    print(grid_search.best_params_)
    print(f"Mejor score: {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_


def entrenar_y_evaluar_modelo(nombre, config, X_train, y_train, X_test, y_test):
    """
    Entrena un modelo con búsqueda de hiperparámetros y genera métricas de evaluación detalladas.
    
    Args:
        nombre: Nombre del modelo
        config: Diccionario con el modelo base y sus parámetros de búsqueda
        X_train, y_train: Datos de entrenamiento
        X_test, y_test: Datos de prueba
    
    Returns:
        dict: Diccionario con resultados y el modelo optimizado
    """
    print(f"\n🔍 Optimizando {nombre}...")
    
    # Búsqueda de hiperparámetros con validación cruzada estratificada
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    grid_search = GridSearchCV(
        config['model'],
        config['params'],
        cv=cv,
        scoring='roc_auc',
        n_jobs=-1,
        verbose=0
    )
    
    # Entrenar modelo con los mejores parámetros
    grid_search.fit(X_train, y_train)
    mejor_modelo = grid_search.best_estimator_
    
    # Predicciones
    y_pred = mejor_modelo.predict(X_test)
    y_pred_proba = mejor_modelo.predict_proba(X_test)[:, 1]
    
    # Métricas de rendimiento
    cv_scores = cross_val_score(mejor_modelo, X_train, y_train, cv=5, scoring='roc_auc')
    
    # Curva de aprendizaje
    train_sizes, train_scores, valid_scores = learning_curve(  # type: ignore[misc]
        mejor_modelo, X_train, y_train,
        train_sizes=np.linspace(0.1, 1.0, 5),
        cv=5, scoring='roc_auc',
        return_times=False  # Devuelve solo 3 valores
    )
    
    resultados = {
        'modelo': mejor_modelo,
        'mejores_params': grid_search.best_params_,
        'mejor_score': grid_search.best_score_,
        'y_pred': y_pred,
        'y_pred_proba': y_pred_proba,
        'confusion_matrix': confusion_matrix(y_test, y_pred),
        'classification_report': classification_report(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred),
        'avg_precision': average_precision_score(y_test, y_pred_proba),
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'learning_curve': {
            'train_sizes': train_sizes,
            'train_scores': train_scores,
            'valid_scores': valid_scores
        }
    }
    
    return resultados


def graficar_resultados(nombre, resultados, X):
    """
    Genera y guarda visualizaciones detalladas de los resultados del modelo.
    
    Args:
        nombre: Nombre del modelo
        resultados: Diccionario con los resultados del modelo
        X: DataFrame con las variables predictoras
    """
    # 1. Matriz de confusión mejorada
    plt.figure(figsize=(8, 6))
    cm = resultados['confusion_matrix']
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['No Desertor', 'Desertor'],
                yticklabels=['No Desertor', 'Desertor'])
    plt.title(f'Matriz de Confusión - {nombre}')
    plt.ylabel('Real')
    plt.xlabel('Predicho')
    plt.savefig(os.path.join(RESULTADOS_BASE, 'matrices', f'matriz_confusion_{nombre.lower()}.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Importancia de variables (si está disponible)
    if hasattr(resultados['modelo'], 'feature_importances_'):
        importancias = pd.DataFrame({
            'Variable': X.columns,
            'Importancia': resultados['modelo'].feature_importances_
        }).sort_values(by='Importancia', ascending=False)

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Importancia', y='Variable', 
                   data=importancias.head(15), palette='viridis')
        plt.title(f'Variables más importantes - {nombre}')
        plt.xlabel('Importancia')
        plt.ylabel('Variable')
        plt.tight_layout()
        plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'importancia_variables_{nombre.lower()}.png'), dpi=300)
        plt.close()
        
        return importancias

    # 3. Curva de aprendizaje
    plt.figure(figsize=(10, 6))
    train_sizes = resultados['learning_curve']['train_sizes']
    train_scores = resultados['learning_curve']['train_scores']
    valid_scores = resultados['learning_curve']['valid_scores']
    
    plt.plot(train_sizes, train_scores.mean(axis=1), label='Training')
    plt.plot(train_sizes, valid_scores.mean(axis=1), label='Validation')
    plt.fill_between(train_sizes, 
                     train_scores.mean(axis=1) - train_scores.std(axis=1),
                     train_scores.mean(axis=1) + train_scores.std(axis=1), alpha=0.1)
    plt.fill_between(train_sizes, 
                     valid_scores.mean(axis=1) - valid_scores.std(axis=1),
                     valid_scores.mean(axis=1) + valid_scores.std(axis=1), alpha=0.1)
    
    plt.xlabel('Training Examples')
    plt.ylabel('Score (ROC-AUC)')
    plt.title(f'Curva de Aprendizaje - {nombre}')
    plt.legend(loc='best')
    plt.grid(True)
    plt.savefig(os.path.join(RESULTADOS_BASE, 'graficos', f'curva_aprendizaje_{nombre.lower()}.png'), dpi=300, bbox_inches='tight')
    plt.close()

    return None

def main():
    try:
        # 1. Cargar y preparar datos
        print("🔄 Cargando datos...")
        print(f"Intentando leer archivo desde: {DATA_PATH}")
        X, y = cargar_datos(DATA_PATH)
        print("✅ Datos cargados exitosamente")
    except Exception as e:
        print(f"❌ Error al cargar los datos: {str(e)}")
        return
    
    # 2. Escalar variables (importante para SVM y KNN)
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    # 3. Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # 4. Configurar los modelos y sus parámetros de búsqueda
    param_grid = {
        'MLPClassifier': {
            'model': MLPClassifier(random_state=42, max_iter=1000),
            'params': {
                'hidden_layer_sizes': [(50,), (100,), (50, 50)],
                'activation': ['relu', 'tanh'],
                'alpha': [0.0001, 0.001, 0.01]
            }
        },
        'NaiveBayes': {
            'model': GaussianNB(),
            'params': {
                'var_smoothing': [1e-9, 1e-8, 1e-7]
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
        'DecisionTree': {
            'model': DecisionTreeClassifier(random_state=42),
            'params': {
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
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
                'learning_rate': [0.01, 0.1, 1.0]
            }
        },
        'KNeighbors': {
            'model': KNeighborsClassifier(),
            'params': {
                'n_neighbors': [3, 5, 7],
                'weights': ['uniform', 'distance'],
                'p': [1, 2]  # Manhattan or Euclidean
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
        'LogisticRegression': {
            'model': LogisticRegression(random_state=42, max_iter=2000),
            'params': {
                'C': [0.1, 1, 10],
                'penalty': ['l1', 'l2'],
                'solver': ['liblinear', 'saga']
            }
        }
    }
    
    try:
        # 5. Entrenar y evaluar cada modelo
        print("\n✨ Iniciando entrenamiento y evaluación de modelos...")
        resultados = {}
        
        for nombre, config in param_grid.items():
            # Crear evaluador con directorio específico para este modelo
            output_dir = os.path.join('resultados', nombre.lower().replace(' ', '_'))
            evaluador = EvaluadorModelo(output_dir=output_dir)
            try:
                print(f"\n🔄 Entrenando y evaluando {nombre}...")
                
                # Entrenar modelo
                resultados[nombre] = entrenar_y_evaluar_modelo(
                    nombre, config, X_train, y_train, X_test, y_test
                )
                modelo = resultados[nombre]['modelo']
                
                # Obtener predicciones
                y_pred = modelo.predict(X_test)
                try:
                    y_prob = modelo.predict_proba(X_test)[:, 1]
                except:
                    y_prob = y_pred  # Para modelos que no soportan predict_proba
                
                print(f"\n📊 Evaluando modelo {nombre}...")
                # Evaluar el modelo usando el nuevo evaluador
                evaluador.evaluar_modelo(
                    modelo=modelo,
                    X_test=X_test,
                    y_test=y_test,
                    feature_names=X.columns,
                    nombre_modelo=nombre
                )
                
                # Generar gráficos de barras intuitivos (ahora incluido en evaluador)
                print(f"\n📊 Generando gráficos de barras intuitivos para {nombre}...")
                evaluador.generar_graficos_intuitivos(y_test, y_pred, nombre)
                
                print(f"✅ Modelo {nombre} entrenado y evaluado exitosamente")
            except Exception as e:
                print(f"❌ Error al entrenar {nombre}: {str(e)}")
                continue
    except Exception as e:
        print(f"❌ Error general en el entrenamiento: {str(e)}")
        return
        
        # Guardar el modelo entrenado
        joblib.dump(modelo, os.path.join(RESULTADOS_BASE, 'modelos', f'{nombre.lower()}_model.pkl'))
        
        # Evaluar modelo usando el evaluador
        evaluador.evaluar_modelo_completo(
            modelo=modelo,
            X_test=X_test,
            y_test=y_test,
            X_train=X_train,
            y_train=y_train,
            feature_names=X.columns
        )
        
        # Imprimir resultados principales
        print(f"\n📊 Resultados finales para {nombre}:")
        print(f"Mejores parámetros: {resultados[nombre]['mejores_params']}")
        print(f"ROC-AUC: {resultados[nombre]['roc_auc']:.4f}")
        print(f"Precisión promedio: {resultados[nombre]['avg_precision']:.4f}")
        print(f"CV Score (ROC-AUC): {resultados[nombre]['cv_mean']:.4f} ± {resultados[nombre]['cv_std']*2:.4f}")
        print("\nClassification Report:")
        print(resultados[nombre]['classification_report'])

if __name__ == "__main__":
    main()
