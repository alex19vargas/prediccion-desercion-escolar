import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Clave secreta para sesiones y tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-desarrollo-cambiar-en-produccion'
    
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de sesión
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SESSION_PROTECTION = 'strong'
    
    # Configuración de Flask-Login
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
    REMEMBER_COOKIE_SECURE = False  # Cambiar a True en producción con HTTPS
    REMEMBER_COOKIE_HTTPONLY = True