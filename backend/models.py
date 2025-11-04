from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Inicializar SQLAlchemy
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='user')  # admin, investigador
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        return self.role == 'admin'
        
    def __repr__(self):
        return f'<User {self.username}>'

class ModelResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=False)
    accuracy = db.Column(db.Float)
    precision = db.Column(db.Float)
    recall = db.Column(db.Float)
    f1_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    confusion_matrix_path = db.Column(db.String(255))
    roc_curve_path = db.Column(db.String(255))
    feature_importance_path = db.Column(db.String(255))
    
    def to_dict(self):
        return {
            'nombre_modelo': self.model_name,
            'exactitud': self.accuracy,
            'precision': self.precision,
            'sensibilidad': self.recall,
            'puntaje_f1': self.f1_score,
            'fecha_creacion': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'ruta_matriz_confusion': self.confusion_matrix_path,
            'ruta_curva_roc': self.roc_curve_path,
            'ruta_importancia_caracteristicas': self.feature_importance_path
        }
        
    def __repr__(self):
        return f'<ModelResult {self.model_name}>'
def load_user(id):
    return User.query.get(int(id))