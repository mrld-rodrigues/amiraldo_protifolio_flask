"""
Portfolio Flask Application Factory
"""
from flask import Flask
import os

def create_app(config_name=None):
    """Factory para criar a aplicação Flask"""
    import os
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    
    app = Flask(__name__, 
                static_folder=static_dir,
                template_folder=template_dir)
    
    # Carrega configuração
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    from app.core.config import get_config
    config_class = get_config()
    app.config.from_object(config_class)
    
    # Configuração de segurança básica
    app.secret_key = app.config['SECRET_KEY']
    
    # Configura logging
    from app.core.errors.logging_config import setup_logging
    setup_logging(app)
    
    # Registra handlers de erro
    from app.core.errors.error_handlers import register_error_handlers
    register_error_handlers(app)
    
    # Headers de segurança básicos
    @app.after_request
    def add_security_headers(response):
        """Adiciona headers de segurança às respostas"""
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response
    
    # Middleware para log de requisições
    @app.before_request
    def log_request_info():
        """Log básico de requisições"""
        from flask import request
        if not app.debug:
            app.logger.info(f'Request: {request.method} {request.url} - IP: {request.remote_addr}')
    
    # Limite de tamanho de upload
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    
    # Registra blueprints
    from app.routes.main import main_bp
    from app.routes.contact import contact_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(contact_bp)
    
    return app
