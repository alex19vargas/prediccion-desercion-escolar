#!/usr/bin/env python3
"""
Script de utilidad para gestionar resultados de modelos
"""

import os
import shutil
from datetime import datetime

def listar_resultados():
    """Lista todos los resultados disponibles"""
    resultados_dir = os.path.join(os.path.dirname(__file__), '..', 'resultados')
    
    print("\n📁 ESTRUCTURA DE RESULTADOS")
    print("=" * 80)
    
    for modelo_dir in ['modelo_base', 'modelo_nuevo']:
        path = os.path.join(resultados_dir, modelo_dir)
        if os.path.exists(path):
            print(f"\n📂 {modelo_dir}/")
            
            for subdir in ['modelos', 'graficos', 'metricas', 'matrices']:
                subpath = os.path.join(path, subdir)
                if os.path.exists(subpath):
                    archivos = os.listdir(subpath)
                    count = len([f for f in archivos if not f.startswith('.')])
                    print(f"   ├── {subdir}/ ({count} archivos)")
                else:
                    print(f"   ├── {subdir}/ (vacío)")
    
    print("\n" + "=" * 80)

def limpiar_resultados(modelo='todos'):
    """
    Limpia los resultados de modelos
    Args:
        modelo: 'base', 'nuevo' o 'todos'
    """
    resultados_dir = os.path.join(os.path.dirname(__file__), '..', 'resultados')
    
    modelos_a_limpiar = []
    if modelo == 'todos':
        modelos_a_limpiar = ['modelo_base', 'modelo_nuevo']
    elif modelo == 'base':
        modelos_a_limpiar = ['modelo_base']
    elif modelo == 'nuevo':
        modelos_a_limpiar = ['modelo_nuevo']
    
    for modelo_dir in modelos_a_limpiar:
        path = os.path.join(resultados_dir, modelo_dir)
        if os.path.exists(path):
            print(f"\n🗑️  Limpiando {modelo_dir}...")
            for subdir in ['modelos', 'graficos', 'metricas', 'matrices']:
                subpath = os.path.join(path, subdir)
                if os.path.exists(subpath):
                    for archivo in os.listdir(subpath):
                        if not archivo.startswith('.'):
                            file_path = os.path.join(subpath, archivo)
                            try:
                                os.remove(file_path)
                                print(f"   ✓ Eliminado: {archivo}")
                            except Exception as e:
                                print(f"   ✗ Error al eliminar {archivo}: {e}")
    
    print("\n✅ Limpieza completada")

def archivar_resultados(modelo='nuevo'):
    """
    Archiva los resultados actuales con timestamp
    Args:
        modelo: 'base', 'nuevo' o 'todos'
    """
    resultados_dir = os.path.join(os.path.dirname(__file__), '..', 'resultados')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    modelos_a_archivar = []
    if modelo == 'todos':
        modelos_a_archivar = ['modelo_base', 'modelo_nuevo']
    elif modelo == 'base':
        modelos_a_archivar = ['modelo_base']
    elif modelo == 'nuevo':
        modelos_a_archivar = ['modelo_nuevo']
    
    for modelo_dir in modelos_a_archivar:
        src = os.path.join(resultados_dir, modelo_dir)
        if os.path.exists(src):
            dst = os.path.join(resultados_dir, f'{modelo_dir}_backup_{timestamp}')
            try:
                shutil.copytree(src, dst)
                print(f"✅ Archivado: {modelo_dir} -> {modelo_dir}_backup_{timestamp}")
            except Exception as e:
                print(f"❌ Error al archivar {modelo_dir}: {e}")

def comparar_modelos():
    """Muestra una comparación de los modelos disponibles"""
    import pandas as pd
    
    resultados_dir = os.path.join(os.path.dirname(__file__), '..', 'resultados')
    
    print("\n📊 COMPARACIÓN DE MODELOS")
    print("=" * 80)
    
    for modelo_dir in ['modelo_base', 'modelo_nuevo']:
        csv_path = os.path.join(resultados_dir, modelo_dir, 'metricas', 'comparacion_modelos.csv')
        if os.path.exists(csv_path):
            print(f"\n{modelo_dir.upper()}:")
            df = pd.read_csv(csv_path)
            print(df.to_string(index=False))
        else:
            print(f"\n{modelo_dir.upper()}: No hay resultados disponibles")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("""
Uso: python gestionar_resultados.py [comando] [opciones]

Comandos disponibles:
  listar                  - Lista todos los resultados
  limpiar [modelo]       - Limpia resultados (base|nuevo|todos)
  archivar [modelo]      - Archiva resultados (base|nuevo|todos)
  comparar               - Compara métricas de modelos

Ejemplos:
  python gestionar_resultados.py listar
  python gestionar_resultados.py limpiar nuevo
  python gestionar_resultados.py archivar todos
  python gestionar_resultados.py comparar
        """)
        sys.exit(1)
    
    comando = sys.argv[1]
    
    if comando == 'listar':
        listar_resultados()
    elif comando == 'limpiar':
        modelo = sys.argv[2] if len(sys.argv) > 2 else 'todos'
        limpiar_resultados(modelo)
    elif comando == 'archivar':
        modelo = sys.argv[2] if len(sys.argv) > 2 else 'nuevo'
        archivar_resultados(modelo)
    elif comando == 'comparar':
        comparar_modelos()
    else:
        print(f"❌ Comando desconocido: {comando}")
        sys.exit(1)
