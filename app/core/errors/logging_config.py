"""
Configuração de logging para a aplicação
"""
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

def setup_logging(app):
    """Configura o sistema de logging da aplicação"""
    
    if not app.debug and not app.testing:
        # Configuração para produção
        
        # Cria diretório de logs se não existir
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        # Handler para arquivo com rotação
        file_handler = RotatingFileHandler(
            'logs/portfolio.log', 
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        
        # Formato detalhado para logs
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        
        # Log de inicialização
        app.logger.setLevel(logging.INFO)
        app.logger.info('Portfolio application startup')
        
    else:
        # Configuração para desenvolvimento
        # Logs mais simples no console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        console_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(console_handler)
        app.logger.setLevel(logging.DEBUG)

def log_email_attempt(app, contato, success=True, error_msg=None):
    """Log específico para tentativas de envio de email"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if success:
        app.logger.info(f'Email sent successfully - From: {contato.email} - Name: {contato.nome} - Time: {timestamp}')
    else:
        app.logger.error(f'Email failed - From: {contato.email} - Name: {contato.nome} - Error: {error_msg} - Time: {timestamp}')

def log_security_event(app, event_type, details):
    """Log para eventos de segurança"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app.logger.warning(f'SECURITY EVENT - Type: {event_type} - Details: {details} - Time: {timestamp}')
