#!/usr/bin/env python3
"""
Script de teste para o sistema de tratamento de erros
"""

import os
import sys

# Adicionar o diretório raiz ao PYTHONPATH
# tests/unit/test_error_handling.py -> ../../ (raiz do projeto)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    try:
        print("🔍 Testando imports...")
        
        from app import create_app
        print("✅ app.py importado com sucesso")
        
        from app.core.errors.error_handlers import register_error_handlers
        print("✅ error_handlers.py importado com sucesso")
        
        from app.core.errors.logging_config import setup_logging, log_email_attempt
        print("✅ logging_config.py importado com sucesso")
        
        from app.core.security.rate_limiter import rate_limit, get_rate_limit_status
        print("✅ rate_limiter.py importado com sucesso")
        
        from app.core.security.form_validators import FormValidator
        print("✅ form_validators.py importado com sucesso")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao importar módulos: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_form_validation():
    """Testa o sistema de validação de formulários"""
    try:
        print("\n🔍 Testando validação de formulários...")
        
        from app.core.security.form_validators import FormValidator
        
        # Teste com dados válidos
        valid_data = {
            'name': 'João Silva',
            'email': 'joao@exemplo.com',
            'message': 'Esta é uma mensagem de teste válida com mais de 10 caracteres.'
        }
        
        errors = FormValidator.validate_contact_form(valid_data)
        if not errors:
            print("✅ Validação de dados válidos funcionando")
        else:
            print(f"❌ Erro na validação de dados válidos: {errors}")
            return False
        
        # Teste com dados inválidos
        invalid_data = {
            'name': '',
            'email': 'email-invalido',
            'message': 'curto'
        }
        
        errors = FormValidator.validate_contact_form(invalid_data)
        if errors:
            print(f"✅ Validação de dados inválidos funcionando: {len(errors)} erros detectados")
        else:
            print("❌ Validação de dados inválidos não funcionando")
            return False
        
        # Teste de detecção de spam
        spam_message = "Click here to win free money! http://spam.com"
        is_spam, reason = FormValidator.detect_spam_patterns(spam_message)
        if is_spam:
            print(f"✅ Detecção de spam funcionando: {reason}")
        else:
            print("❌ Detecção de spam não funcionando")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar validação: {e}")
        return False

def test_rate_limiter():
    """Testa o sistema de rate limiting"""
    try:
        print("\n🔍 Testando rate limiter...")
        
        from app.core.security.rate_limiter import get_rate_limit_status
        
        # Teste com IP novo
        status = get_rate_limit_status('192.168.1.1')
        if status['requests_in_window'] == 0 and not status['is_limited']:
            print("✅ Rate limiter funcionando para IP novo")
        else:
            print(f"❌ Rate limiter com problema para IP novo: {status}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar rate limiter: {e}")
        return False

def test_app_creation():
    """Testa se a aplicação pode ser criada"""
    try:
        print("\n🔍 Testando criação da aplicação...")
        
        from app import create_app
        import os
        
        # Configura variáveis de ambiente mínimas para teste
        os.environ['SECRET_KEY'] = 'test-secret-key-for-testing'
        os.environ['FLASK_ENV'] = 'testing'
        
        app = create_app('testing')
        
        if app:
            print("✅ Aplicação criada com sucesso")
            print(f"   - Nome: {app.name}")
            print(f"   - Debug: {app.debug}")
            print(f"   - Config: {app.config.get('ENV', 'N/A')}")
            return True
        else:
            print("❌ Erro ao criar aplicação")
            return False
        
    except Exception as e:
        print(f"❌ Erro ao testar criação da aplicação: {e}")
        return False

def main():
    """Executa todos os testes"""
    print("🚀 Iniciando testes do sistema de tratamento de erros...")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Validação de Formulários", test_form_validation),
        ("Rate Limiter", test_rate_limiter),
        ("Criação da Aplicação", test_app_creation),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"\n❌ Teste '{test_name}' falhou")
        except Exception as e:
            print(f"\n❌ Erro no teste '{test_name}': {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Resultados: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! Sistema funcionando corretamente.")
        return True
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
        return False

if __name__ == "__main__":
    main()
