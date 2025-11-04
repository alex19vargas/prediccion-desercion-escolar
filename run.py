# Script principal para iniciar la aplicación web
import os
from backend.app import create_app

# Crear instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Configuración para desarrollo local
    print("\n" + "="*70)
    print("SISTEMA DE PREDICCIÓN DE DESERCIÓN ESCOLAR")
    print("="*70)
    print("\n📊 Iniciando servidor web...")
    print("\n🌐 Accede a la aplicación en:")
    print("   • Local:    http://localhost:5000")
    print("   • Red:      http://0.0.0.0:5000")
    print("\n🔐 Credenciales de acceso:")
    print("   Admin:      admin / admin123")
    print("   Docente:    docente / docente123")
    print("\n⚠️  Presiona CTRL+C para detener el servidor")
    print("="*70 + "\n")
    
    # Obtener configuración desde variables de entorno
    debug_mode = os.environ.get('FLASK_DEBUG', 'True') == 'True'
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    
    app.run(debug=debug_mode, host=host, port=port)