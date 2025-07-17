"""
Handlers de erro personalizados para a aplicação Flask
"""
from flask import render_template, request, jsonify
import logging
import traceback
from datetime import datetime

def register_error_handlers(app):
    """Registra todos os handlers de erro na aplicação"""
    
    @app.errorhandler(404)
    def not_found_error(error):
        """Página não encontrada"""
        app.logger.warning(f'404 Error: {request.url} - IP: {request.remote_addr}')
        
        # Se for uma requisição AJAX, retorna JSON
        if request.is_json or 'application/json' in request.headers.get('Accept', ''):
            return jsonify({
                'error': 'Página não encontrada',
                'status_code': 404
            }), 404
        
        # Renderiza página de erro personalizada
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Erro interno do servidor"""
        # Log detalhado do erro
        app.logger.error(f'500 Error: {str(error)} - URL: {request.url} - IP: {request.remote_addr}')
        app.logger.error(f'Traceback: {traceback.format_exc()}')
        
        # Se for uma requisição AJAX, retorna JSON
        if request.is_json or 'application/json' in request.headers.get('Accept', ''):
            return jsonify({
                'error': 'Erro interno do servidor',
                'status_code': 500
            }), 500
        
        return render_template('errors/500.html'), 500
    
    @app.errorhandler(403)
    def forbidden_error(error):
        """Acesso negado"""
        app.logger.warning(f'403 Error: {request.url} - IP: {request.remote_addr}')
        
        if request.is_json or 'application/json' in request.headers.get('Accept', ''):
            return jsonify({
                'error': 'Acesso negado',
                'status_code': 403
            }), 403
        
        return render_template('errors/403.html'), 403
    
    @app.errorhandler(413)
    def too_large_error(error):
        """Arquivo muito grande"""
        app.logger.warning(f'413 Error: Arquivo muito grande - IP: {request.remote_addr}')
        
        if request.is_json or 'application/json' in request.headers.get('Accept', ''):
            return jsonify({
                'error': 'Arquivo muito grande',
                'status_code': 413
            }), 413
        
        return render_template('errors/413.html'), 413
    
    @app.errorhandler(429)
    def rate_limit_exceeded(error):
        """Rate limit excedido"""
        app.logger.warning(f'429 Error: Rate limit exceeded - IP: {request.remote_addr}')
        
        if request.is_json or 'application/json' in request.headers.get('Accept', ''):
            return jsonify({
                'error': 'Muitas tentativas. Tente novamente mais tarde.',
                'status_code': 429
            }), 429
        
        return render_template('errors/429.html'), 429
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        """Handler genérico para exceções não tratadas"""
        # Log completo do erro
        app.logger.error(f'Unhandled Exception: {str(error)}')
        app.logger.error(f'URL: {request.url}')
        app.logger.error(f'Method: {request.method}')
        app.logger.error(f'IP: {request.remote_addr}')
        app.logger.error(f'User Agent: {request.headers.get("User-Agent")}')
        app.logger.error(f'Traceback: {traceback.format_exc()}')
        
        # Se for desenvolvimento, mostra o erro completo
        if app.config.get('DEBUG'):
            raise error
        
        # Em produção, esconde detalhes do erro
        if request.is_json or 'application/json' in request.headers.get('Accept', ''):
            return jsonify({
                'error': 'Ocorreu um erro inesperado',
                'status_code': 500
            }), 500
        
        return render_template('errors/500.html'), 500
