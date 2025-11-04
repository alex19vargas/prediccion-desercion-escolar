from flask import Flask
from flask_login import LoginManager
from backend.models import db
from backend.config import Config

def create_app():
    app = Flask(__name__, 
                template_folder='../frontend/templates',
                static_folder='../frontend/static')
    
    app.config.from_object(Config)
    
    # Inicializar SQLAlchemy
    db.init_app(app)
    
    # Configurar Login Manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Importar y registrar modelos aquí para evitar importaciones circulares
    from backend.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Registrar blueprints
    from backend.routes import auth_routes, dashboard_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(dashboard_routes.bp)
    
    # Crear todas las tablas e inicializar usuarios
    with app.app_context():
        db.create_all()
        
        # Crear usuarios predeterminados si no existen
        if User.query.count() == 0:
            print("⚙️  Inicializando usuarios predeterminados...")
            admin = User(username='admin', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            
            docente = User(username='docente', role='docente')
            docente.set_password('docente123')
            db.session.add(docente)
            
            db.session.commit()
            print("✅ Usuarios creados exitosamente")
    
    return app