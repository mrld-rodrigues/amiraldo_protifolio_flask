"""
Rotas relacionadas ao formulário de contato
"""
from flask import Blueprint, render_template, request, flash, redirect, current_app

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact')
def contact():
    """Página de contato"""
    return render_template('contact.html')

@contact_bp.route('/send', methods=['POST'])
def send():
    """Rota para envio de mensagem automática"""
    from app.core.security.rate_limiter import rate_limit
    from app.core.security.form_validators import FormValidator
    from app.core.email.email_function import send_email, Contato
    from app.core.errors.logging_config import log_email_attempt
    
    # Aplica rate limiting
    try:
        # Simulação simples de rate limiting (em produção usar decorator)
        client_ip = request.remote_addr
        # TODO: Implementar rate limiting aqui se necessário
        
        # Obter dados do formulário
        form_data = {
            'name': request.form.get('name', ''),
            'email': request.form.get('email', ''),
            'message': request.form.get('message', '')
        }
        
        # Log da tentativa de contato
        current_app.logger.info(f'Tentativa de contato - IP: {request.remote_addr} - Email: {form_data["email"]}')
        
        # Sanitizar entradas
        for key in form_data:
            form_data[key] = FormValidator.sanitize_input(form_data[key])
        
        # Validar formulário
        validation_errors = FormValidator.validate_contact_form(form_data)
        
        if validation_errors:
            # Log dos erros de validação
            current_app.logger.warning(f'Erros de validação: {validation_errors} - IP: {request.remote_addr}')
            
            # Exibir primeiro erro encontrado
            for field, errors in validation_errors.items():
                flash(errors[0], 'error')
                break
            
            return redirect('/contact')
        
        # Criar objeto de contato e enviar email
        contato = Contato(form_data['name'], form_data['email'], form_data['message'])
        send_email(contato)
        
        # Log de sucesso com função específica
        log_email_attempt(current_app, contato, success=True)
        flash('Mensagem enviada com sucesso! Obrigado pelo contato.', 'success')
        
    except ValueError as e:
        # Erros de validação
        current_app.logger.warning(f'Erro de validação: {str(e)} - IP: {request.remote_addr}')
        flash('Dados inválidos. Verifique as informações e tente novamente.', 'error')
        
    except Exception as e:
        # Erros gerais - log detalhado mas mensagem genérica para o usuário
        log_email_attempt(current_app, contato if 'contato' in locals() else None, success=False, error_msg=str(e))
        current_app.logger.error(f'Erro ao enviar email: {str(e)} - IP: {request.remote_addr}')
        flash('Ocorreu um erro ao enviar a mensagem. Tente novamente em alguns minutos.', 'error')
    
    return redirect('/contact')
