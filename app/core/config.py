"""
Configurações da aplicação Flask
Separando configurações de desenvolvimento e produção
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuração base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Email settings
    EMAIL_LOGIN = os.environ.get('EMAIL_LOGIN')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    EMAIL_RECEIVER = os.environ.get('EMAIL_RECEIVER')
    
    # Upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Security headers
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year cache for static files

class DevelopmentConfig(Config):
    """Configuração para desenvolvimento"""
    DEBUG = True
    DEVELOPMENT = True
    
class ProductionConfig(Config):
    """Configuração para produção"""
    DEBUG = False
    DEVELOPMENT = False
    
    # Força HTTPS em produção
    PREFERRED_URL_SCHEME = 'https'
    
    # Security headers mais rigorosos
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

class TestingConfig(Config):
    """Configuração para testes"""
    TESTING = True
    DEBUG = True
    
# Mapeamento de configurações
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Retorna a configuração baseada na variável de ambiente"""
    return config.get(os.environ.get('FLASK_ENV', 'default'), DevelopmentConfig)
