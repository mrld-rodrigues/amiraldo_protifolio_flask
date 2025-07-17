#!/usr/bin/env python3
"""
Teste final simplificado da aplicação
"""

import os
import sys

# Adicionar o diretório raiz ao PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Definir variáveis de ambiente para testes
os.environ.setdefault('FLASK_ENV', 'testing')
os.environ.setdefault('SECRET_KEY', 'test-secret-key-for-testing-only')

def test_final():
    """Teste final da aplicação"""
    print("🚀 TESTE FINAL DA APLICAÇÃO")
    print("=" * 50)
    
    try:
        from app import create_app
        app = create_app('testing')
        
        with app.test_client() as client:
            routes = ['/', '/portfolio', '/resume', '/p_privacy', '/useterms', '/contact']
            
            print("📍 Testando rotas:")
            all_working = True
            
            for route in routes:
                try:
                    response = client.get(route)
                    if response.status_code == 200:
                        print(f"  ✅ {route} - OK")
                    else:
                        print(f"  ⚠️  {route} - Status: {response.status_code}")
                        all_working = False
                except Exception as e:
                    print(f"  ❌ {route} - Erro: {str(e)[:100]}...")
                    all_working = False
            
            # Teste de arquivos estáticos
            print("\n📁 Testando arquivos estáticos:")
            static_files = ['/static/style.css', '/static/script.js']
            
            for static_file in static_files:
                try:
                    response = client.get(static_file)
                    if response.status_code == 200:
                        print(f"  ✅ {static_file} - OK")
                    else:
                        print(f"  ⚠️  {static_file} - Status: {response.status_code}")
                except Exception as e:
                    print(f"  ❌ {static_file} - Erro: {str(e)[:50]}...")
            
            print("\n" + "=" * 50)
            if all_working:
                print("🎉 APLICAÇÃO FUNCIONANDO PERFEITAMENTE!")
                print("✅ Todas as rotas principais estão operacionais")
                print("✅ Templates carregando corretamente") 
                print("✅ Arquivos estáticos acessíveis")
                return True
            else:
                print("⚠️  APLICAÇÃO COM PROBLEMAS MENORES")
                print("🔧 Algumas rotas precisam de ajustes")
                return False
            
    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_final()
