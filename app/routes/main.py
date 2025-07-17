"""
Rotas principais da aplicação
"""
from flask import Blueprint, render_template, send_from_directory, abort
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Página inicial"""
    return render_template('index.html')

@main_bp.route('/resume')
def resume():
    """Página de currículo"""
    return render_template('resume.html')

@main_bp.route('/portfolio')
def portfolio():
    """Página de portfólio"""
    return render_template('portfolio.html')

@main_bp.route('/p_privacy')
def privacy():
    """Página de privacidade"""
    return render_template('p_privacy.html')

@main_bp.route('/useterms')
def useterms():
    """Página de termos de uso"""
    return render_template('useterms.html')

@main_bp.route('/download/<filename>')
def download_file(filename):
    """Rota para download de arquivos com validação de segurança"""
    from flask import current_app, request
    
    try:
        # Log da tentativa de download
        current_app.logger.info(f'Download request: {filename} - IP: {request.remote_addr}')
        
        # Validação básica do nome do arquivo
        if not filename or '..' in filename or '/' in filename or '\\' in filename:
            current_app.logger.warning(f'Tentativa de download suspeita: {filename} - IP: {request.remote_addr}')
            abort(403)
        
        # Lista de arquivos permitidos para download
        allowed_files = ['cv.pdf']  # Adicione outros arquivos conforme necessário
        
        if filename not in allowed_files:
            current_app.logger.warning(f'Arquivo não permitido para download: {filename} - IP: {request.remote_addr}')
            abort(404)
        
        # Verificar se o arquivo existe
        file_path = os.path.join(current_app.static_folder, 'download', filename)
        if not os.path.exists(file_path):
            current_app.logger.error(f'Arquivo não encontrado: {file_path}')
            abort(404)
        
        # Log de sucesso
        current_app.logger.info(f'Download autorizado: {filename} - IP: {request.remote_addr}')
        return send_from_directory('static/download', filename, as_attachment=True)
        
    except Exception as e:
        current_app.logger.error(f'Erro no download: {str(e)} - Arquivo: {filename} - IP: {request.remote_addr}')
        abort(500)

@main_bp.route('/health')
def health_check():
    """Endpoint de health check para monitoramento"""
    from flask import jsonify, current_app
    from datetime import datetime
    import os
    
    try:
        # Verificar status dos serviços
        status = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'environment': os.environ.get('FLASK_ENV', 'unknown'),
            'version': '1.0.0'
        }
        
        # Verificar keep-alive em produção
        if os.environ.get('FLASK_ENV') == 'production':
            try:
                from app.core.services import keep_alive_status
                status['keep_alive'] = keep_alive_status()
            except Exception as e:
                current_app.logger.warning(f'Erro ao verificar keep-alive: {e}')
                status['keep_alive'] = {'error': str(e)}
        
        return jsonify(status), 200
        
    except Exception as e:
        current_app.logger.error(f'Erro no health check: {e}')
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500
