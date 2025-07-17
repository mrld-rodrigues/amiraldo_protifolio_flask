import smtplib
import ssl
from email.message import EmailMessage
from app.core.email.email_config import login, senha, email_receiver
import logging

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
        
    def __str__(self):
        return f"Contato(nome='{self.nome}', email='{self.email}')"

def send_email(contato):
    """
    Envia email de contato com tratamento de erros aprimorado
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Validação básica
        if not all([login, senha, email_receiver]):
            raise ValueError("Configurações de email não estão completas")
        
        if not contato.nome or not contato.email or not contato.mensagem:
            raise ValueError("Dados do contato incompletos")
        
        # Criação da mensagem
        msg = EmailMessage()
        msg['Subject'] = f'Client Contact - {contato.nome}'
        msg['From'] = login
        msg['To'] = email_receiver   
        
        body = f"""
Nova mensagem de contato do portfolio:

Nome: {contato.nome}
Email: {contato.email}
Mensagem:
{contato.mensagem}

---
Enviado automaticamente pelo sistema de contato do portfolio.
        """
        msg.set_content(body)
        
        # Log da tentativa
        logger.info(f"Tentando enviar email de contato: {contato}")
        
        # Envio do email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(login, senha)
            smtp.send_message(msg)
            
        # Log de sucesso
        logger.info(f"Email enviado com sucesso para {contato.email}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"Erro de autenticação SMTP: {e}")
        raise Exception("Erro de autenticação do email. Verifique as credenciais.")
        
    except smtplib.SMTPRecipientsRefused as e:
        logger.error(f"Email do destinatário recusado: {e}")
        raise Exception("Email do destinatário inválido.")
        
    except smtplib.SMTPException as e:
        logger.error(f"Erro SMTP: {e}")
        raise Exception("Erro no servidor de email. Tente novamente.")
        
    except ssl.SSLError as e:
        logger.error(f"Erro SSL: {e}")
        raise Exception("Erro de conexão segura. Tente novamente.")
        
    except Exception as e:
        logger.error(f"Erro inesperado ao enviar email: {e}")
        raise Exception("Erro inesperado. Tente novamente mais tarde.")
