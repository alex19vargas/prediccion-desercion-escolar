import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app import create_app, db
from backend.models import User

def init_db():
    app = create_app()
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        
        # Crear usuario administrador si no existe
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
        
        # Crear usuario docente si no existe
        if not User.query.filter_by(username='docente').first():
            docente = User(username='docente')
            docente.set_password('docente123')
            db.session.add(docente)
        
        db.session.commit()
        print("✅ Base de datos inicializada y usuarios creados")

if __name__ == '__main__':
    init_db()