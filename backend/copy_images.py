"""
Script para mover las imágenes generadas por los modelos al directorio de imágenes estáticas
"""

import os
import shutil

# Crear el directorio de imágenes estáticas si no existe
os.makedirs('frontend/static/img', exist_ok=True)

# Directorio donde están los resultados de los modelos
resultados_dir = 'resultados'

# Lista de subdirectorios (uno por cada modelo)
modelos = [
    'mlpclassifier', 'naivebayes', 'randomforest', 'decisiontree', 
    'gradientboosting', 'adaboost', 'kneighbors', 'svm', 'logisticregression'
]

for modelo in modelos:
    modelo_dir = os.path.join(resultados_dir, modelo)
    if os.path.exists(modelo_dir):
        # Buscar todas las imágenes PNG en el directorio del modelo
        for filename in os.listdir(modelo_dir):
            if filename.endswith('.png'):
                # Crear un nuevo nombre que incluya el modelo
                new_filename = f"{modelo}_{filename}"
                src = os.path.join(modelo_dir, filename)
                dst = os.path.join('frontend/static/img', new_filename)
                # Copiar la imagen
                shutil.copy2(src, dst)
                print(f"✅ Copiada imagen: {new_filename}")

print("\n✨ Proceso completado. Imágenes copiadas a frontend/static/img")