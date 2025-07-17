#!/usr/bin/env python3
"""
Script de teste para verificar a nova estrutura organizacional
"""

import os
import sys

# Adicionar o diretório raiz ao PYTHONPATH
# tests/integration/test_structure.py -> ../../ (raiz do projeto)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Definir variáveis de ambiente para testes
os.environ.setdefault('FLASK_ENV', 'testing')
os.environ.setdefault('SECRET_KEY', 'test-secret-key-for-testing-only')

def test_structure():
    """Testa se a nova estrutura está funcionando"""
    import os
    
    print("🔍 Testando nova estrutura do projeto...")
    print("=" * 60)
    
    # Testa se consegue importar a aplicação
    try:
        from app import create_app
        print("✅ Factory da aplicação importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar factory: {e}")
        return False
    
    # Testa se consegue criar a aplicação
    try:
        app = create_app('testing')
        print("✅ Aplicação criada com sucesso")
    except Exception as e:
        print(f"❌ Erro ao criar aplicação: {e}")
        return False
    
    # Testa blueprints
    try:
        from app.routes.main import main_bp
        from app.routes.contact import contact_bp
        print("✅ Blueprints importados com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar blueprints: {e}")
        return False
    
    # Testa módulos core
    try:
        from app.core.config import get_config
        from app.core.email.email_function import Contato
        from app.core.security.form_validators import FormValidator
        from app.core.errors.error_handlers import register_error_handlers
        print("✅ Módulos core importados com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar módulos core: {e}")
        return False
    
    # Verifica estrutura de arquivos
    expected_files = [
        'app/__init__.py',
        'app/routes/main.py',
        'app/routes/contact.py',
        'app/core/config.py',
        'app/core/email/email_function.py',
        'app/core/security/form_validators.py',
        'app/core/errors/error_handlers.py',
        'app/static',
        'app/templates',
        'docs/',
        'scripts/',
        'tests/'
    ]
    
    missing_files = []
    for file_path in expected_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Arquivos/pastas faltando: {missing_files}")
        return False
    else:
        print("✅ Estrutura de arquivos correta")
    
    print("\n" + "=" * 60)
    print("🎉 Nova estrutura funcionando perfeitamente!")
    return True

def show_new_structure():
    """Mostra a nova estrutura do projeto"""
    print("\n📁 Nova Estrutura do Projeto:")
    print("=" * 60)
    
    structure = """
amiraldo_portfolio/
├── app.py                     # Ponto de entrada principal
├── requirements.txt           # Dependências
├── runtime.txt               # Versão Python
├── Procfile                  # Deploy
├── .env.example              # Exemplo de variáveis
├── .gitignore               # Git ignore
├── README.md                # Documentação principal
├── app/                     # 🆕 Aplicação organizada
│   ├── __init__.py          # Factory da aplicação
│   ├── routes/              # 🆕 Rotas organizadas
│   │   ├── __init__.py
│   │   ├── main.py          # Rotas principais
│   │   └── contact.py       # Rotas de contato
│   ├── core/                # 🆕 Funcionalidades core
│   │   ├── __init__.py
│   │   ├── config.py        # Configurações
│   │   ├── email/           # 🆕 Sistema de email
│   │   │   ├── __init__.py
│   │   │   ├── email_config.py
│   │   │   └── email_function.py
│   │   ├── security/        # 🆕 Segurança e validação
│   │   │   ├── __init__.py
│   │   │   ├── form_validators.py
│   │   │   └── rate_limiter.py
│   │   └── errors/          # 🆕 Tratamento de erros
│   │       ├── __init__.py
│   │       ├── error_handlers.py
│   │       └── logging_config.py
│   ├── static/              # Arquivos estáticos
│   └── templates/           # Templates HTML
├── docs/                    # 🆕 Documentação
│   ├── ERROR_HANDLING_SUMMARY.md
│   └── DEPLOY.md
├── scripts/                 # 🆕 Scripts de setup/deploy
│   ├── setup.sh
│   ├── setup.bat
│   └── deploy.sh
└── tests/                   # 🆕 Testes
    ├── test_error_handling.py
    └── check_config.py
    """
    
    print(structure)
    
    print("\n🎯 Benefícios da Nova Estrutura:")
    print("✅ Organização clara por responsabilidade")
    print("✅ Código modular e reutilizável")
    print("✅ Fácil manutenção e expansão")
    print("✅ Padrão profissional Flask")
    print("✅ Separação de concerns")
    print("✅ Blueprints para escalabilidade")

if __name__ == "__main__":
    show_new_structure()
    print("\n")
    test_structure()
