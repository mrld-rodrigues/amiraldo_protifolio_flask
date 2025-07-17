#!/usr/bin/env python3
"""
Script para testar a configuração de deploy
Simula o que o Gunicorn/Render fará
"""
import os
import sys
import subprocess

# Adicionar o diretório raiz ao PYTHONPATH
# scripts/testing/test_deploy.py -> ../../ (raiz do projeto)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_wsgi_import():
    """Testa se o wsgi.py pode ser importado"""
    try:
        print("🔍 Testando importação do wsgi.py...")
        import wsgi
        print(f"✅ wsgi.py importado com sucesso!")
        print(f"✅ Tipo da app: {type(wsgi.app)}")
        print(f"✅ Nome da app: {wsgi.app.name}")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar wsgi.py: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_flask_app_import():
    """Testa se o flask_app.py pode ser importado"""
    try:
        print("\n🔍 Testando importação do deploy/flask_app.py...")
        from deploy import flask_app
        print(f"✅ deploy/flask_app.py importado com sucesso!")
        print(f"✅ Tipo da app: {type(flask_app.app)}")
        print(f"✅ Tipo da application: {type(flask_app.application)}")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar deploy/flask_app.py: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_gunicorn_command():
    """Testa se o comando do Gunicorn funciona"""
    try:
        print("\n🔍 Testando comando do Gunicorn...")
        # Simula o que o Render fará com PYTHONPATH correto
        cmd = f"PYTHONPATH={project_root} python -c \"import wsgi; print('Gunicorn pode importar:', type(wsgi.app))\""
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Comando do Gunicorn funcionará!")
            print(f"✅ Output: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ Comando do Gunicorn falhou: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Erro ao testar Gunicorn: {e}")
        return False

def test_app_routes():
    """Testa se as rotas da aplicação estão funcionando"""
    try:
        print("\n🔍 Testando rotas da aplicação...")
        import wsgi
        app = wsgi.app
        
        with app.test_client() as client:
            # Testa rota principal
            response = client.get('/')
            print(f"✅ Rota '/': Status {response.status_code}")
            
            # Testa rota de saúde
            response = client.get('/health')
            print(f"✅ Rota '/health': Status {response.status_code}")
            
            # Testa rota de contato
            response = client.get('/contact')
            print(f"✅ Rota '/contact': Status {response.status_code}")
            
        return True
    except Exception as e:
        print(f"❌ Erro ao testar rotas: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Iniciando testes de deploy...\n")
    
    # Adicionar diretório atual ao path
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    os.chdir(current_dir)
    
    tests = [
        test_wsgi_import,
        test_flask_app_import,
        test_gunicorn_command,
        test_app_routes
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print("-" * 50)
    
    print(f"\n📊 Resultados: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! Deploy deve funcionar.")
        return True
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
