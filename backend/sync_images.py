"""
Script para sincronizar las imágenes del modelo seleccionado al directorio estático del frontend
=================================================================================================

⚠️ CONFIGURACIÓN IMPORTANTE - CAMBIAR AQUÍ SI SE ELIGE OTRO MODELO ⚠️

Este script copia las imágenes desde la carpeta de resultados del modelo activo
al directorio frontend/static/img/ para que sean accesibles desde la interfaz web.

INSTRUCCIONES PARA CAMBIAR DE MODELO EN EL FUTURO:
--------------------------------------------------
1. Identifica el nuevo modelo mejor (ej: si modelo_inscrito funciona mejor)
2. Cambia la variable MODELO_ACTIVO abajo (línea 24)
3. Ejecuta este script: python backend/sync_images.py
4. Reinicia el servidor Flask

Ejemplo de cambios:
- Para usar modelo_nuevo:       MODELO_ACTIVO = 'modelo_nuevo'
- Para usar modelo_inscrito:    MODELO_ACTIVO = 'modelo_inscrito'
- Para usar modelo_terminado:   MODELO_ACTIVO = 'modelo_terminado'
- Para usar modelo_base:        MODELO_ACTIVO = 'modelo_base'
"""

import os
import shutil
from pathlib import Path

# ╔═══════════════════════════════════════════════════════════════════╗
# ║  🎯 CONFIGURACIÓN DEL MODELO ACTIVO - CAMBIAR AQUÍ               ║
# ╚═══════════════════════════════════════════════════════════════════╝

MODELO_ACTIVO = 'modelo_nuevo'  # ← CAMBIAR ESTA LÍNEA PARA USAR OTRO MODELO

# ═══════════════════════════════════════════════════════════════════════

def sync_images():
    """
    Sincroniza las imágenes del modelo activo al directorio estático.
    """
    # Rutas base
    proyecto_dir = Path(__file__).parent.parent
    resultados_dir = proyecto_dir / 'resultados' / MODELO_ACTIVO
    static_img_dir = proyecto_dir / 'frontend' / 'static' / 'img'
    
    # Verificar que el modelo existe
    if not resultados_dir.exists():
        print(f"❌ ERROR: La carpeta {resultados_dir} no existe.")
        print(f"   Modelos disponibles en resultados/:")
        resultados_base = proyecto_dir / 'resultados'
        if resultados_base.exists():
            for item in resultados_base.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    print(f"   - {item.name}")
        return False
    
    # Crear directorio de destino si no existe
    static_img_dir.mkdir(parents=True, exist_ok=True)
    
    # Limpiar imágenes antiguas (opcional - comentar si no se desea)
    print(f"\n🧹 Limpiando imágenes antiguas de {static_img_dir}...")
    for old_file in static_img_dir.glob('*.png'):
        old_file.unlink()
        print(f"   🗑️  Eliminado: {old_file.name}")
    
    print(f"\n📊 Sincronizando imágenes desde: {MODELO_ACTIVO}")
    print(f"📁 Directorio fuente: {resultados_dir}")
    print(f"📂 Directorio destino: {static_img_dir}\n")
    
    imagenes_copiadas = 0
    estructura_detectada = "nueva"  # nueva o antigua
    
    # Detectar si es estructura nueva (carpetas por modelo) o antigua (graficos/matrices)
    carpetas_modelo = [d for d in resultados_dir.iterdir() 
                       if d.is_dir() 
                       and not d.name.startswith('.') 
                       and d.name not in ['graficos', 'matrices', 'metricas', 'modelos']]
    
    tiene_graficos_matrices = (resultados_dir / 'graficos').exists() or (resultados_dir / 'matrices').exists()
    
    if carpetas_modelo and not tiene_graficos_matrices:
        # ESTRUCTURA NUEVA: Cada modelo en su carpeta
        estructura_detectada = "nueva"
        print(f"✨ Estructura nueva detectada (carpetas por modelo)\n")
        
        for modelo_subdir in carpetas_modelo:
            modelo_nombre = modelo_subdir.name
            
            # Buscar todas las imágenes en la subcarpeta del modelo
            imagenes = list(modelo_subdir.glob('*.png'))
            
            if imagenes:
                print(f"📦 {modelo_nombre}: {len(imagenes)} imagen(es)")
                
                for imagen in imagenes:
                    # Crear nombre con prefijo del modelo
                    # Ejemplo: randomforest_matriz_confusion.png
                    nuevo_nombre = f"{modelo_nombre}_{imagen.name}"
                    destino = static_img_dir / nuevo_nombre
                    
                    shutil.copy2(imagen, destino)
                    print(f"   ✅ {imagen.name}")
                    imagenes_copiadas += 1
        
        # Copiar imágenes generales en raíz (comparaciones, etc.)
        print(f"\n📊 Imágenes generales:")
        for imagen in resultados_dir.glob('*.png'):
            destino = static_img_dir / imagen.name
            shutil.copy2(imagen, destino)
            print(f"   ✅ {imagen.name}")
            imagenes_copiadas += 1
    
    else:
        # ESTRUCTURA ANTIGUA: graficos/ y matrices/
        estructura_detectada = "antigua"
        print(f"⚙️  Estructura antigua detectada (carpetas graficos/matrices)\n")
        
        # Copiar desde subcarpetas graficos, matrices, metricas
        categorias = {
            'graficos': '📈',
            'matrices': '🎯',
            'metricas': '📊'
        }
        
        for categoria, icono in categorias.items():
            subdir = resultados_dir / categoria
            if subdir.exists():
                imagenes = list(subdir.glob('*.png'))
                if imagenes:
                    print(f"{icono} {categoria.capitalize()}: {len(imagenes)} imagen(es)")
                    
                    for imagen in imagenes:
                        # Mantener nombre original o agregar prefijo según preferencia
                        destino = static_img_dir / imagen.name
                        shutil.copy2(imagen, destino)
                        print(f"   ✅ {imagen.name}")
                        imagenes_copiadas += 1
        
        # Copiar subcarpetas dentro de graficos (si existen)
        graficos_dir = resultados_dir / 'graficos'
        if graficos_dir.exists():
            print(f"\n📂 Subcarpetas de gráficos:")
            for modelo_subdir in graficos_dir.iterdir():
                if modelo_subdir.is_dir() and not modelo_subdir.name.startswith('.'):
                    imagenes = list(modelo_subdir.glob('*.png'))
                    if imagenes:
                        print(f"   📦 {modelo_subdir.name}: {len(imagenes)} imagen(es)")
                        for imagen in imagenes:
                            nuevo_nombre = f"{modelo_subdir.name}_{imagen.name}"
                            destino = static_img_dir / nuevo_nombre
                            shutil.copy2(imagen, destino)
                            imagenes_copiadas += 1
        
        # Copiar imágenes en raíz
        print(f"\n📊 Imágenes en raíz:")
        for imagen in resultados_dir.glob('*.png'):
            destino = static_img_dir / imagen.name
            shutil.copy2(imagen, destino)
            print(f"   ✅ {imagen.name}")
            imagenes_copiadas += 1
    
    print(f"\n{'='*70}")
    print(f"✨ SINCRONIZACIÓN COMPLETADA")
    print(f"{'='*70}")
    print(f"📊 Modelo activo: {MODELO_ACTIVO}")
    print(f"🏗️  Estructura: {estructura_detectada.upper()}")
    print(f"📸 Imágenes copiadas: {imagenes_copiadas}")
    print(f"📂 Ubicación: {static_img_dir}")
    print(f"{'='*70}\n")
    
    if imagenes_copiadas == 0:
        print(f"⚠️  ADVERTENCIA: No se encontraron imágenes para copiar.")
        print(f"   Verifica que el modelo haya generado resultados.")
    else:
        print(f"💡 NOTA: Para ver la estructura NUEVA con carpetas por modelo:")
        print(f"   1. Ejecuta cualquier modelo (ej: modelo_desercion_nuevo.py)")
        print(f"   2. Las nuevas imágenes se guardarán en carpetas por algoritmo")
        print(f"   3. Vuelve a ejecutar este script para sincronizar")
    
    return True

def listar_modelos_disponibles():
    """
    Lista todos los modelos disponibles en la carpeta resultados.
    """
    proyecto_dir = Path(__file__).parent.parent
    resultados_dir = proyecto_dir / 'resultados'
    
    if not resultados_dir.exists():
        print("❌ La carpeta 'resultados' no existe.")
        return
    
    print("\n📊 MODELOS DISPONIBLES:")
    print("=" * 70)
    
    for modelo_dir in sorted(resultados_dir.iterdir()):
        if modelo_dir.is_dir() and not modelo_dir.name.startswith('.'):
            # Contar subcarpetas (algoritmos)
            algoritmos = [d for d in modelo_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
            
            # Contar imágenes totales
            imagenes = list(modelo_dir.rglob('*.png'))
            
            # Marcar el modelo activo
            activo = "✅ ACTIVO" if modelo_dir.name == MODELO_ACTIVO else ""
            
            print(f"\n📁 {modelo_dir.name} {activo}")
            print(f"   - Algoritmos: {len(algoritmos)}")
            print(f"   - Imágenes: {len(imagenes)}")
            
            if algoritmos:
                print(f"   - Modelos: {', '.join([a.name for a in algoritmos[:5]])}")
                if len(algoritmos) > 5:
                    print(f"              ...y {len(algoritmos) - 5} más")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║" + " " * 20 + "SINCRONIZADOR DE IMÁGENES" + " " * 23 + "║")
    print("╚" + "═" * 68 + "╝\n")
    
    # Mostrar modelos disponibles
    listar_modelos_disponibles()
    
    # Sincronizar imágenes
    print("\n" + "─" * 70)
    sync_images()
    
    print("\n💡 RECUERDA:")
    print("   - Reinicia el servidor Flask para ver los cambios")
    print("   - Las imágenes ahora están disponibles en /static/img/")
    print("   - Para cambiar de modelo, edita la variable MODELO_ACTIVO en este script\n")
