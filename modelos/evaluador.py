"""
Evaluador de Modelos de Deserción Escolar
----------------------------------------
Este módulo proporciona una clase para evaluar modelos de manera exhaustiva,
incluyendo métricas de rendimiento y visualizaciones.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_curve, 
    roc_auc_score, precision_recall_curve, average_precision_score
)

class EvaluadorModelo:
    def __init__(self, output_dir=None):
        """
        Inicializa el evaluador.
        
        Args:
            output_dir (str): Directorio donde se guardarán los resultados
        """
        if output_dir is None:
            # Usar directorio 'resultados' en la ubicación actual
            self.output_dir = 'resultados'
        else:
            self.output_dir = output_dir
        
        # Asegurar que el directorio existe
        try:
            os.makedirs(self.output_dir, exist_ok=True)
            print(f"✅ Directorio de resultados creado/verificado: {self.output_dir}")
        except Exception as e:
            print(f"❌ Error al crear directorio de resultados: {str(e)}")
            raise
    
    def _guardar_figura(self, nombre, bbox_inches='tight', dpi=300):
        """Método auxiliar para guardar figuras con manejo de errores."""
        try:
            ruta = os.path.join(self.output_dir, f'{nombre}.png')
            plt.savefig(ruta, bbox_inches=bbox_inches, dpi=dpi)
            print(f"✅ Gráfico guardado: {nombre}.png")
        except Exception as e:
            print(f"❌ Error al guardar {nombre}.png: {str(e)}")
        finally:
            plt.close()
        
    def plot_confusion_matrix(self, y_true, y_pred, titulo='Matriz de Confusión'):
        """
        Genera y guarda la matriz de confusión.
        """
        try:
            plt.figure(figsize=(10, 8))
            cm = confusion_matrix(y_true, y_pred)
            
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title(titulo)
            plt.ylabel('Real')
            plt.xlabel('Predicho')
            
            self._guardar_figura('matriz_confusion')
            
        except Exception as e:
            print(f"❌ Error al generar matriz de confusión: {str(e)}")
            plt.close('all')
        
    def plot_roc_curve(self, y_true, y_prob):
        """
        Genera y guarda la curva ROC.
        """
        try:
            fpr, tpr, _ = roc_curve(y_true, y_prob)
            roc_auc = roc_auc_score(y_true, y_prob)
            
            plt.figure(figsize=(10, 8))
            plt.plot(fpr, tpr, color='darkorange', lw=2, 
                    label=f'ROC curve (AUC = {roc_auc:.2f})')
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('Tasa de Falsos Positivos')
            plt.ylabel('Tasa de Verdaderos Positivos')
            plt.title('Curva ROC')
            plt.legend(loc="lower right")
            plt.grid(True, alpha=0.3)
            
            self._guardar_figura('curva_roc')
            
        except Exception as e:
            print(f"❌ Error al generar curva ROC: {str(e)}")
            plt.close('all')
        
    def plot_precision_recall_curve(self, y_true, y_prob):
        """
        Genera y guarda la curva de Precisión-Recall.
        """
        try:
            precision, recall, _ = precision_recall_curve(y_true, y_prob)
            avg_precision = average_precision_score(y_true, y_prob)
            
            plt.figure(figsize=(10, 8))
            plt.plot(recall, precision, color='blue', lw=2,
                    label=f'P-R curve (AP = {avg_precision:.2f})')
            plt.xlabel('Recall')
            plt.ylabel('Precisión')
            plt.title('Curva Precisión-Recall')
            plt.legend(loc='lower left')
            plt.grid(True, alpha=0.3)
            
            self._guardar_figura('curva_precision_recall')
            
        except Exception as e:
            print(f"❌ Error al generar curva Precisión-Recall: {str(e)}")
            plt.close('all')
        
    def plot_feature_importance(self, modelo, feature_names, top_n=20):
        """
        Genera y guarda el gráfico de importancia de características.
        """
        try:
            if hasattr(modelo, 'feature_importances_'):
                importances = modelo.feature_importances_
            elif hasattr(modelo, 'coef_'):
                importances = np.abs(modelo.coef_[0])
            else:
                print("⚠️ El modelo no proporciona importancia de características")
                return
                
            # Crear DataFrame y ordenar
            importance_df = pd.DataFrame({
                'feature': feature_names,
                'importance': importances
            })
            importance_df = importance_df.sort_values('importance', ascending=False)
            
            # Guardar todas las características en CSV
            importance_df.to_csv(os.path.join(self.output_dir, 'importancia_caracteristicas.csv'), 
                               index=False)
            
            # Plotear top N características
            plt.figure(figsize=(12, 8))
            top_features = importance_df.head(top_n)
            sns.barplot(data=top_features, y='feature', x='importance')
            plt.title(f'Top {top_n} Características más Importantes')
            plt.xlabel('Importancia')
            plt.ylabel('Característica')
            plt.grid(True, alpha=0.3)
            
            self._guardar_figura('importancia_caracteristicas')
            
        except Exception as e:
            print(f"❌ Error al generar gráfico de importancia: {str(e)}")
            plt.close('all')
    
    def guardar_metricas(self, y_true, y_pred, y_prob):
        """
        Guarda todas las métricas en archivos.
        """
        try:
            # Generar reporte de clasificación
            report = classification_report(y_true, y_pred, output_dict=True)
            df_report = pd.DataFrame(report).transpose()
            
            # Calcular métricas adicionales
            roc_auc = roc_auc_score(y_true, y_prob)
            avg_precision = average_precision_score(y_true, y_prob)
            
            # Guardar reporte de clasificación
            df_report.to_csv(os.path.join(self.output_dir, 'metricas_clasificacion.csv'))
            
            # Guardar métricas en formato legible
            with open(os.path.join(self.output_dir, 'metricas.txt'), 'w') as f:
                f.write("=== Reporte de Clasificación ===\n\n")
                f.write(classification_report(y_true, y_pred))
                f.write("\n=== Métricas Adicionales ===\n")
                f.write(f'ROC AUC Score: {roc_auc:.4f}\n')
                f.write(f'Average Precision Score: {avg_precision:.4f}\n')
            
            print("✅ Métricas guardadas exitosamente")
            
        except Exception as e:
            print(f"❌ Error al guardar métricas: {str(e)}")
    
    def generar_graficos_intuitivos(self, y_true, y_pred, nombre_modelo="Modelo"):
        """
        Genera gráficos de barras intuitivos para personas sin conocimiento técnico.
        
        Estos gráficos ayudan a entender los resultados del modelo de manera visual
        y accesible, sin necesidad de conocimientos técnicos sobre matrices de confusión
        o métricas de clasificación.
        
        Args:
            y_true: Valores reales
            y_pred: Valores predichos
            nombre_modelo: Nombre del modelo para los títulos
        """
        try:
            # Convertir a arrays de numpy si son DataFrames o Series
            y_test_array = np.array(y_true).flatten()
            y_pred_array = np.array(y_pred).flatten()
            
            # 1. Gráfico de Predicciones Correctas vs Incorrectas
            correctas = np.sum(y_test_array == y_pred_array)
            incorrectas = np.sum(y_test_array != y_pred_array)
            total = len(y_test_array)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            categorias = ['Predicciones\nCorrectas', 'Predicciones\nIncorrectas']
            valores = [correctas, incorrectas]
            colores = ['#2ecc71', '#e74c3c']
            
            bars = ax.bar(categorias, valores, color=colores, alpha=0.8, edgecolor='black', linewidth=1.5)
            
            # Agregar valores en las barras
            for i, (bar, valor) in enumerate(zip(bars, valores)):
                height = bar.get_height()
                porcentaje = (valor / total) * 100
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{valor}\n({porcentaje:.1f}%)',
                        ha='center', va='bottom', fontsize=14, fontweight='bold')
            
            ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
            ax.set_title(f'Rendimiento del Modelo {nombre_modelo}\nTotal de Estudiantes: {total}', 
                         fontsize=14, fontweight='bold', pad=20)
            ax.set_ylim(0, max(valores) * 1.15)
            plt.tight_layout()
            self._guardar_figura('grafico_predicciones_correctas')
            
            # 2. Comparación Desertores vs No Desertores (Real vs Predicho)
            # Valores reales
            desertores_reales = np.sum(y_test_array == 1)
            no_desertores_reales = np.sum(y_test_array == 0)
            
            # Valores predichos
            desertores_predichos = np.sum(y_pred_array == 1)
            no_desertores_predichos = np.sum(y_pred_array == 0)
            
            fig, ax = plt.subplots(figsize=(12, 7))
            x = np.arange(2)
            width = 0.35
            
            bars1 = ax.bar(x - width/2, [no_desertores_reales, desertores_reales], 
                           width, label='Valores Reales', color='#3498db', alpha=0.8, 
                           edgecolor='black', linewidth=1.5)
            bars2 = ax.bar(x + width/2, [no_desertores_predichos, desertores_predichos], 
                           width, label='Valores Predichos', color='#e67e22', alpha=0.8,
                           edgecolor='black', linewidth=1.5)
            
            # Agregar valores en las barras
            for bars in [bars1, bars2]:
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                            f'{int(height)}',
                            ha='center', va='bottom', fontsize=12, fontweight='bold')
            
            ax.set_xlabel('Categoría', fontsize=12, fontweight='bold')
            ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
            ax.set_title(f'Comparación: Desertores vs No Desertores - {nombre_modelo}', 
                         fontsize=14, fontweight='bold', pad=20)
            ax.set_xticks(x)
            ax.set_xticklabels(['No Desertores', 'Desertores'], fontsize=12)
            ax.legend(fontsize=11)
            ax.set_ylim(0, max(no_desertores_reales, desertores_reales, 
                               no_desertores_predichos, desertores_predichos) * 1.15)
            plt.tight_layout()
            self._guardar_figura('grafico_comparacion_desertores')
            
            # 3. Desglose detallado de aciertos y errores
            cm = confusion_matrix(y_test_array, y_pred_array)
            
            # Verdaderos Negativos, Falsos Positivos, Falsos Negativos, Verdaderos Positivos
            tn, fp, fn, tp = cm.ravel()
            
            fig, ax = plt.subplots(figsize=(14, 8))
            categorias = [
                'Bien Clasificados\nNo Desertores\n(Verdaderos Negativos)',
                'Mal Clasificados\nNo Desertores\n(Falsos Positivos)',
                'Mal Clasificados\nDesertores\n(Falsos Negativos)',
                'Bien Clasificados\nDesertores\n(Verdaderos Positivos)'
            ]
            valores = [tn, fp, fn, tp]
            colores_detallados = ['#27ae60', '#f39c12', '#e67e22', '#2ecc71']
            
            bars = ax.bar(categorias, valores, color=colores_detallados, alpha=0.8, 
                          edgecolor='black', linewidth=1.5)
            
            # Agregar valores y porcentajes en las barras
            for bar, valor in zip(bars, valores):
                height = bar.get_height()
                porcentaje = (valor / total) * 100
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{valor}\n({porcentaje:.1f}%)',
                        ha='center', va='bottom', fontsize=12, fontweight='bold')
            
            ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
            ax.set_title(f'Desglose Detallado de Predicciones - {nombre_modelo}\nTotal: {total} estudiantes', 
                         fontsize=14, fontweight='bold', pad=20)
            ax.set_ylim(0, max(valores) * 1.2)
            plt.xticks(rotation=0, ha='center', fontsize=10)
            plt.tight_layout()
            self._guardar_figura('grafico_desglose_detallado')
            
            # 4. Gráfico de Efectividad por Categoría (Accuracy por grupo)
            accuracy_no_desertores = tn / (tn + fp) if (tn + fp) > 0 else 0
            accuracy_desertores = tp / (tp + fn) if (tp + fn) > 0 else 0
            accuracy_total = (tn + tp) / total
            
            fig, ax = plt.subplots(figsize=(10, 6))
            categorias_efectividad = ['No Desertores', 'Desertores', 'Total']
            valores_efectividad = [accuracy_no_desertores * 100, accuracy_desertores * 100, accuracy_total * 100]
            colores_efectividad = ['#3498db', '#e74c3c', '#9b59b6']
            
            bars = ax.bar(categorias_efectividad, valores_efectividad, color=colores_efectividad, 
                          alpha=0.8, edgecolor='black', linewidth=1.5)
            
            # Agregar valores en las barras
            for bar, valor in zip(bars, valores_efectividad):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{valor:.1f}%',
                        ha='center', va='bottom', fontsize=14, fontweight='bold')
            
            ax.set_ylabel('Precisión (%)', fontsize=12, fontweight='bold')
            ax.set_title(f'Efectividad del Modelo por Categoría - {nombre_modelo}', 
                         fontsize=14, fontweight='bold', pad=20)
            ax.set_ylim(0, 105)
            ax.axhline(y=100, color='green', linestyle='--', alpha=0.3, linewidth=2)
            ax.axhline(y=90, color='orange', linestyle='--', alpha=0.3, linewidth=1)
            plt.tight_layout()
            self._guardar_figura('grafico_efectividad_categoria')
            
            print(f"✅ Gráficos intuitivos generados exitosamente")
            
        except Exception as e:
            print(f"❌ Error al generar gráficos intuitivos: {str(e)}")
            plt.close('all')
    
    def evaluar_modelo(self, modelo, X_test, y_test, feature_names=None, nombre_modelo="", generar_graficos_intuitivos=True):
        """
        Realiza una evaluación completa del modelo.
        
        Args:
            modelo: Modelo entrenado
            X_test: Datos de prueba
            y_test: Etiquetas de prueba
            feature_names: Nombres de las características
            nombre_modelo: Nombre del modelo para personalizar títulos
            generar_graficos_intuitivos: Si True, genera gráficos de barras intuitivos adicionales
        """
        print(f"\n📊 Evaluando modelo{f' {nombre_modelo}' if nombre_modelo else ''}...")
        
        try:
            # Obtener predicciones
            y_pred = modelo.predict(X_test)
            try:
                y_prob = modelo.predict_proba(X_test)[:, 1]
            except:
                print("⚠️ El modelo no soporta predict_proba, usando predicciones directas")
                y_prob = y_pred
            
            # Generar todas las visualizaciones técnicas
            titulo_matriz = f'Matriz de Confusión{f" - {nombre_modelo}" if nombre_modelo else ""}'
            self.plot_confusion_matrix(y_test, y_pred, titulo=titulo_matriz)
            self.plot_roc_curve(y_test, y_prob)
            self.plot_precision_recall_curve(y_test, y_prob)
            
            if feature_names is not None:
                self.plot_feature_importance(modelo, feature_names)
            
            # Guardar métricas
            self.guardar_metricas(y_test, y_pred, y_prob)
            
            # Generar gráficos intuitivos si se solicita
            if generar_graficos_intuitivos:
                print(f"\n📊 Generando gráficos intuitivos...")
                self.generar_graficos_intuitivos(y_test, y_pred, nombre_modelo if nombre_modelo else "Modelo")
            
            print("\n✅ Evaluación completada exitosamente")
            print(f"📁 Resultados guardados en: {self.output_dir}")
            
        except Exception as e:
            print(f"❌ Error durante la evaluación: {str(e)}")