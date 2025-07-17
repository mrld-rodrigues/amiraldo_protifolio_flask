#!/usr/bin/env python3
"""
Teste do sistema Keep-Alive
"""

import os
import sys

# Adicionar o diretório raiz ao PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_keep_alive_service():
    """Testa o serviço keep-alive"""
    print("🔍 TESTANDO SERVIÇO KEEP-ALIVE")
    print("=" * 50)
    
    try:
        # Importar o serviço
        from app.core.services.keep_alive import KeepAliveService, get_keep_alive_service
        print("✅ Serviço keep-alive importado com sucesso")
        
        # Criar instância para teste (desabilitada)
        os.environ['KEEP_ALIVE_ENABLED'] = 'false'
        service = KeepAliveService()
        print("✅ Instância do serviço criada")
        
        # Testar status
        status = service.status()
        print(f"✅ Status obtido: {status}")
        
        # Testar funções de conveniência
        from app.core.services import start_keep_alive, stop_keep_alive, keep_alive_status
        print("✅ Funções de conveniência importadas")
        
        # Testar status global
        global_status = keep_alive_status()
        print(f"✅ Status global: {global_status}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_health_endpoint():
    """Testa o endpoint de health check"""
    print("\n🔍 TESTANDO ENDPOINT HEALTH CHECK")
    print("=" * 50)
    
    try:
        # Configurar ambiente de teste
        os.environ['SECRET_KEY'] = 'test-key-for-health-check'
        os.environ['FLASK_ENV'] = 'testing'
        os.environ['KEEP_ALIVE_ENABLED'] = 'false'
        
        from app import create_app
        app = create_app('testing')
        
        with app.test_client() as client:
            response = client.get('/health')
            
            print(f"✅ Status code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.get_json()
                print(f"✅ Response data: {data}")
                
                # Verificar campos obrigatórios
                required_fields = ['status', 'timestamp', 'environment', 'version']
                for field in required_fields:
                    if field in data:
                        print(f"✅ Campo '{field}' presente: {data[field]}")
                    else:
                        print(f"❌ Campo '{field}' ausente")
                        return False
                
                return True
            else:
                print(f"❌ Status code inesperado: {response.status_code}")
                return False
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_production_mode():
    """Testa modo de produção (sem iniciar o keep-alive real)"""
    print("\n🔍 TESTANDO MODO PRODUÇÃO (SIMULADO)")
    print("=" * 50)
    
    try:
        # Simular produção mas com keep-alive desabilitado
        os.environ['SECRET_KEY'] = 'test-key-for-production'
        os.environ['FLASK_ENV'] = 'production'
        os.environ['KEEP_ALIVE_ENABLED'] = 'false'
        
        from app import create_app
        app = create_app('production')
        
        with app.test_client() as client:
            # Testar health check em modo produção
            response = client.get('/health')
            
            if response.status_code == 200:
                data = response.get_json()
                print(f"✅ Health check em produção: {data['status']}")
                print(f"✅ Ambiente: {data['environment']}")
                
                if 'keep_alive' in data:
                    print(f"✅ Status keep-alive: {data['keep_alive']}")
                
                return True
            else:
                print(f"❌ Health check falhou: {response.status_code}")
                return False
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Executa todos os testes"""
    print("🚀 TESTES DO SISTEMA KEEP-ALIVE")
    print("=" * 60)
    
    tests = [
        ("Serviço Keep-Alive", test_keep_alive_service),
        ("Health Check Endpoint", test_health_endpoint),
        ("Modo Produção", test_production_mode)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📍 {test_name}")
        if test_func():
            passed += 1
            print(f"✅ {test_name}: PASSOU")
        else:
            print(f"❌ {test_name}: FALHOU")
    
    print("\n" + "=" * 60)
    print(f"📊 RESULTADO: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 TODOS OS TESTES DO KEEP-ALIVE PASSARAM!")
        print("✅ Sistema keep-alive pronto para produção")
        return True
    else:
        print("⚠️  ALGUNS TESTES FALHARAM")
        print("🔧 Revise a implementação do keep-alive")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
