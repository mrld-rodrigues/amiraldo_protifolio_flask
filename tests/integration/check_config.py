#!/usr/bin/env python3
"""
Script para validar configurações do projeto
"""
import os
import sys
from dotenv import load_dotenv

# Adicionar o diretório raiz ao PYTHONPATH
# tests/integration/check_config.py -> ../../ (raiz do projeto)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def check_config():
    """Verifica se todas as configurações necessárias estão presentes"""
    print("🔍 Verificando configurações...")
    
    # Carrega variáveis de ambiente
    load_dotenv()
    
    # Configurações obrigatórias
    required_vars = [
        'SECRET_KEY',
        'EMAIL_LOGIN', 
        'EMAIL_PASSWORD',
        'EMAIL_RECEIVER'
    ]
    
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
            print(f"❌ {var}: não configurado")
        else:
            # Mascarar valores sensíveis
            if 'PASSWORD' in var or 'SECRET' in var:
                display_value = '*' * len(value)
            else:
                display_value = value
            print(f"✅ {var}: {display_value}")
    
    # Configurações opcionais
    optional_vars = {
        'FLASK_ENV': 'development',
        'PORT': '5000'
    }
    
    print("\n📋 Configurações opcionais:")
    for var, default in optional_vars.items():
        value = os.getenv(var, default)
        print(f"ℹ️  {var}: {value}")
    
    # Resultado final
    if missing_vars:
        print(f"\n❌ Configuração incompleta! Variáveis faltando: {', '.join(missing_vars)}")
        print("💡 Dica: Copie .env.example para .env e configure os valores")
        return False
    else:
        print("\n✅ Todas as configurações necessárias estão presentes!")
        return True

def test_app_import():
    """Testa se a aplicação pode ser importada"""
    print("\n🧪 Testando importação da aplicação...")
    try:
        from app import create_app
        app = create_app('testing')
        print("✅ Aplicação importada com sucesso!")
        print(f"✅ Tipo da app: {type(app)}")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar aplicação: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal"""
    print("🚀 Validador de Configurações - Portfolio Flask\n")
    
    config_ok = check_config()
    app_ok = test_app_import()
    
    if config_ok and app_ok:
        print("\n🎉 Tudo configurado corretamente!")
        print("💡 Para executar: python wsgi.py")
        sys.exit(0)
    else:
        print("\n⚠️ Existem problemas na configuração!")
        print("🔧 Corrija os erros acima antes de continuar")
        sys.exit(1)

if __name__ == "__main__":
    main()
