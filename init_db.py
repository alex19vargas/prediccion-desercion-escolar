from backend.app import create_app, db
from backend.models import User

app = create_app()

with app.app_context():
    db.create_all()
    
    # Crear usuarios predeterminados si no existen
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
    
    if not User.query.filter_by(username='docente').first():
        docente = User(username='docente', role='docente')
        docente.set_password('docente123')
        db.session.add(docente)
    
    db.session.commit()
    
print("✅ Base de datos inicializada exitosamente")