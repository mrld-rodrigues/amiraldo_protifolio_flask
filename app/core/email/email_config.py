import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configurações de email
login = os.getenv('EMAIL_LOGIN')
senha = os.getenv('EMAIL_PASSWORD')
email_receiver = os.getenv('EMAIL_RECEIVER')

# Validação básica
if not all([login, senha, email_receiver]):
    print("⚠️ AVISO: Configurações de email não encontradas!")
    print("Configure as variáveis EMAIL_LOGIN, EMAIL_PASSWORD e EMAIL_RECEIVER")
