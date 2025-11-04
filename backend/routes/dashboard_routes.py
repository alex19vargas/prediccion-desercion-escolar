import json
import os
import re
from datetime import datetime

import pandas as pd
from flask import (Blueprint, current_app, jsonify, render_template,
                   send_from_directory)
from flask_login import current_user, login_required

from backend.models import ModelResult

bp = Blueprint('dashboard', __name__)

# Configuración del modelo activo
MODELO_ACTIVO = 'modelo_balanceado'

@bp.route('/')
@bp.route('/dashboard')
@login_required
def index():
    stats = {
        'total_imagenes': len(get_all_images()),
        'curvas': len([img for img in get_all_images() if img['categoria'] == 'curvas']),
        'matrices': len([img for img in get_all_images() if img['categoria'] == 'matrices']),
        'graficos_intuitivos': len([img for img in get_all_images() if img['categoria'] == 'graficos_intuitivos']),
        'ultima_actualizacion': datetime.now().strftime('%d/%m/%Y %H:%M')
    }
    return render_template('dashboard.html', username=current_user.username, stats=stats)

@bp.route('/api/metricas')
@login_required
def get_metricas():
    """Obtiene métricas consolidadas de todos los modelos"""
    base_dir = get_modelo_base_dir()
    metricas_por_modelo = {}
    
    if not os.path.exists(base_dir):
        return jsonify({'error': 'No hay métricas disponibles. Ejecuta los modelos primero.'})
    
    # Recorrer todas las carpetas de modelos
    for modelo_dir in os.listdir(base_dir):
        modelo_path = os.path.join(base_dir, modelo_dir)
        metricas_file = os.path.join(modelo_path, 'metricas.txt')
        
        if os.path.isdir(modelo_path) and os.path.exists(metricas_file):
            metricas = parse_metricas_file(metricas_file)
            if metricas:
                metricas_por_modelo[modelo_dir] = metricas
    
    if not metricas_por_modelo:
        return jsonify({'error': 'No se encontraron archivos de métricas'})
    
    return jsonify(metricas_por_modelo)

@bp.route('/api/imagenes')
@login_required
def get_imagenes():
    return jsonify(get_all_images())

@bp.route('/resultados/<path:filename>')
@login_required
def serve_resultado_image(filename):
    """Sirve imágenes desde la carpeta de resultados"""
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    resultados_dir = os.path.join(project_root, 'resultados')
    return send_from_directory(resultados_dir, filename)

def get_modelo_base_dir():
    """Retorna el directorio base del modelo activo"""
    # Subir desde backend/ a proyecto_desercion/, luego a resultados/
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(project_root, 'resultados', MODELO_ACTIVO)

def parse_metricas_file(filepath):
    """Extrae métricas del archivo de texto"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metricas = {}
        
        # Buscar accuracy
        accuracy_match = re.search(r'accuracy\s+(\d+\.\d+)', content)
        if accuracy_match:
            metricas['accuracy'] = float(accuracy_match.group(1))
        
        # Buscar weighted avg (precision, recall, f1-score)
        weighted_match = re.search(r'weighted avg\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)', content)
        if weighted_match:
            metricas['precision'] = float(weighted_match.group(1))
            metricas['recall'] = float(weighted_match.group(2))
            metricas['f1_score'] = float(weighted_match.group(3))
        
        # Buscar ROC AUC
        roc_match = re.search(r'ROC AUC Score:\s*(\d+\.\d+)', content)
        if roc_match:
            metricas['roc_auc'] = float(roc_match.group(1))
        
        # Buscar Average Precision
        ap_match = re.search(r'Average Precision Score:\s*(\d+\.\d+)', content)
        if ap_match:
            metricas['avg_precision'] = float(ap_match.group(1))
        
        return metricas
    except Exception as e:
        print(f"Error parseando métricas de {filepath}: {e}")
        return None

def get_all_images():
    """Obtiene todas las imágenes de los modelos con categorización mejorada"""
    base_dir = get_modelo_base_dir()
    result_images = []
    
    if not os.path.exists(base_dir):
        return result_images
    
    # Recorrer todas las carpetas de modelos
    for modelo_dir in os.listdir(base_dir):
        modelo_path = os.path.join(base_dir, modelo_dir)
        
        # Solo procesar directorios (ignorar archivos sueltos)
        if not os.path.isdir(modelo_path):
            continue
        
        # Listar archivos PNG en la carpeta del modelo
        for filename in os.listdir(modelo_path):
            if filename.endswith('.png'):
                # Categorizar según el nombre del archivo
                categoria = categorize_image(filename)
                
                # Nombre amigable para mostrar
                nombre_display = format_display_name(modelo_dir, filename)
                
                result_images.append({
                    'nombre': nombre_display,
                    'filename': filename,
                    'modelo': modelo_dir,
                    'url': f'/resultados/{MODELO_ACTIVO}/{modelo_dir}/{filename}',
                    'categoria': categoria
                })
    
    return result_images

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

def format_display_name(modelo_dir, filename):
    """Formatea el nombre para mostrar en la interfaz"""
    # Limpiar nombre del modelo
    modelo_clean = modelo_dir.replace('_', ' ').title()
    
    # Limpiar nombre del archivo
    nombre_archivo = filename.replace('.png', '').replace('_', ' ').title()
    
    return f"{modelo_clean} - {nombre_archivo}"

@bp.route('/api/estudiantes-riesgo')
@login_required
def get_estudiantes_riesgo():
    """
    Obtiene datos simulados de estudiantes en riesgo usando el dataset balanceado.
    En una implementación real, esto consultaría la base de datos de estudiantes
    y aplicaría el modelo de predicción a cada uno.
    """
    try:
        # Cargar dataset balanceado
        import numpy as np
        data_path = "/Users/alexandervargas/Downloads/datos_balanceados_75_25.xlsx"
        
        if not os.path.exists(data_path):
            # Si no existe el archivo, generar datos simulados
            return jsonify(generate_simulated_students())
        
        # Leer el dataset
        df = pd.read_excel(data_path)
        
        # Filtrar solo los estudiantes que son desertores (True)
        estudiantes_riesgo = df[df['Dropped_Out'] == True].copy()
        
        # Tomar una muestra aleatoria de 50 estudiantes
        if len(estudiantes_riesgo) > 50:
            estudiantes_riesgo = estudiantes_riesgo.sample(n=50, random_state=42)
        
        # Generar probabilidades simuladas (alto riesgo: 75-95%)
        np.random.seed(42)
        estudiantes_riesgo['probabilidad'] = np.random.uniform(75, 95, len(estudiantes_riesgo))
        
        # Factores de riesgo basados en las variables del dataset
        factores_posibles = {
            'bajo_rendimiento': 'Bajo rendimiento académico',
            'ausentismo': 'Ausentismo frecuente',
            'economico': 'Dificultades económicas',
            'edad': 'Edad fuera del rango típico',
            'genero': 'Factor de género',
            'inscrito': 'Problemas con inscripción',
            'terminado': 'Cursos sin terminar'
        }
        
        # Acciones sugeridas
        acciones = [
            'Entrevista urgente con padres/tutores',
            'Apoyo psicopedagógico inmediato',
            'Evaluación de becas o ayudas',
            'Tutoría académica personalizada',
            'Seguimiento semanal intensivo',
            'Derivación a trabajador social',
            'Plan de recuperación académica',
            'Intervención familiar programada'
        ]
        
        # Construir respuesta
        resultados = []
        for idx, (index, row) in enumerate(estudiantes_riesgo.iterrows(), 1):
            # Determinar nivel de riesgo basado en probabilidad
            prob = row['probabilidad']
            if prob >= 85:
                nivel = 'alto'
            elif prob >= 70:
                nivel = 'medio'
            else:
                nivel = 'bajo'
            
            # Seleccionar factores aleatorios
            num_factores = np.random.randint(1, 3)
            factores_seleccionados = np.random.choice(list(factores_posibles.values()), 
                                                      size=num_factores, 
                                                      replace=False)
            
            # Seleccionar acción sugerida
            accion = np.random.choice(acciones)
            
            resultados.append({
                'id': f'EST-{str(index).zfill(4)}',
                'nivel_riesgo': nivel,
                'probabilidad': round(prob, 1),
                'factores': ', '.join(factores_seleccionados),
                'accion_sugerida': accion
            })
        
        # Ordenar por probabilidad descendente
        resultados.sort(key=lambda x: x['probabilidad'], reverse=True)
        
        return jsonify({
            'total': len(resultados),
            'riesgo_alto': len([e for e in resultados if e['nivel_riesgo'] == 'alto']),
            'riesgo_medio': len([e for e in resultados if e['nivel_riesgo'] == 'medio']),
            'riesgo_bajo': len([e for e in resultados if e['nivel_riesgo'] == 'bajo']),
            'estudiantes': resultados
        })
        
    except Exception as e:
        print(f"Error cargando estudiantes en riesgo: {e}")
        return jsonify(generate_simulated_students())

def generate_simulated_students():
    """Genera datos simulados de estudiantes en riesgo"""
    import numpy as np
    
    np.random.seed(42)
    
    factores = [
        'Bajo rendimiento académico',
        'Ausentismo frecuente',
        'Dificultades económicas',
        'Problemas familiares',
        'Dificultades de aprendizaje',
        'Cambio de residencia',
        'Problemas de salud'
    ]
    
    acciones = [
        'Entrevista urgente con padres/tutores',
        'Apoyo psicopedagógico inmediato',
        'Evaluación de becas o ayudas',
        'Tutoría académica personalizada',
        'Seguimiento semanal intensivo',
        'Derivación a trabajador social',
        'Plan de recuperación académica'
    ]
    
    estudiantes = []
    total_estudiantes = 150
    
    for i in range(1, total_estudiantes + 1):
        prob = np.random.uniform(70, 95)
        
        if prob >= 85:
            nivel = 'alto'
        elif prob >= 70:
            nivel = 'medio'
        else:
            nivel = 'bajo'
        
        num_factores = np.random.randint(1, 3)
        factores_seleccionados = np.random.choice(factores, size=num_factores, replace=False)
        accion = np.random.choice(acciones)
        
        estudiantes.append({
            'id': f'EST-{str(i).zfill(4)}',
            'nivel_riesgo': nivel,
            'probabilidad': round(prob, 1),
            'factores': ', '.join(factores_seleccionados),
            'accion_sugerida': accion
        })
    
    estudiantes.sort(key=lambda x: x['probabilidad'], reverse=True)
    
    return {
        'total': len(estudiantes),
        'riesgo_alto': len([e for e in estudiantes if e['nivel_riesgo'] == 'alto']),
        'riesgo_medio': len([e for e in estudiantes if e['nivel_riesgo'] == 'medio']),
        'riesgo_bajo': len([e for e in estudiantes if e['nivel_riesgo'] == 'bajo']),
        'estudiantes': estudiantes
    }