#!/usr/bin/env python3
"""
Teste rápido para identificar problemas na aplicação
"""

import os
import sys
import traceback

# Adicionar o diretório raiz ao PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Definir variáveis de ambiente básicas
os.environ.setdefault('SECRET_KEY', 'test-secret-key-for-debugging')
os.environ.setdefault('FLASK_ENV', 'development')

def test_basic_import():
    """Testa imports básicos"""
    print("🔍 Testando imports básicos...")
    
    try:
        from app import create_app
        print("✅ Factory importado")
        
        app = create_app()
        print("✅ App criado")
        
        return app
    except Exception as e:
        print(f"❌ Erro: {e}")
        traceback.print_exc()
        return None

def test_routes_with_client(app):
    """Testa rotas usando test_client"""
    print("\n🔍 Testando rotas com test_client...")
    
    routes_to_test = ['/', '/portfolio', '/resume', '/p_privacy', '/useterms']
    
    with app.test_client() as client:
        for route in routes_to_test:
            try:
                response = client.get(route)
                print(f"📍 {route} - Status: {response.status_code}")
                
                if response.status_code == 500:
                    print(f"   ❌ Erro 500 em {route}")
                    # Tentar obter mais detalhes do erro
                    data = response.get_data(as_text=True)
                    if 'TemplateNotFound' in data:
                        print(f"   📄 Template não encontrado")
                    elif 'jinja2' in data.lower():
                        print(f"   🎨 Erro no template Jinja2")
                    else:
                        print(f"   🐛 Outro erro: {data[:200]}...")
                        
            except Exception as e:
                print(f"   ❌ Exceção em {route}: {e}")

def test_template_paths(app):
    """Verifica se os templates existem"""
    print("\n🔍 Verificando templates...")
    
    template_folder = app.template_folder
    print(f"📁 Template folder: {template_folder}")
    
    expected_templates = ['index.html', 'portfolio.html', 'resume.html', 'p_privacy.html', 'useterms.html']
    
    for template in expected_templates:
        template_path = os.path.join(template_folder, template)
        if os.path.exists(template_path):
            print(f"✅ {template} existe")
        else:
            print(f"❌ {template} NÃO existe em {template_path}")

def test_static_paths(app):
    """Verifica se os arquivos static existem"""
    print("\n🔍 Verificando arquivos static...")
    
    static_folder = app.static_folder
    print(f"📁 Static folder: {static_folder}")
    
    important_static_files = [
        'style.css',
        'bootstrap/css/bootstrap.css',
        'images/amiraldo_logo_black.png'
    ]
    
    for static_file in important_static_files:
        static_path = os.path.join(static_folder, static_file)
        if os.path.exists(static_path):
            print(f"✅ {static_file} existe")
        else:
            print(f"❌ {static_file} NÃO existe em {static_path}")

if __name__ == "__main__":
    print("🚀 DIAGNÓSTICO RÁPIDO DA APLICAÇÃO")
    print("=" * 60)
    
    app = test_basic_import()
    
    if app:
        test_template_paths(app)
        test_static_paths(app)
        test_routes_with_client(app)
        
        print("\n" + "=" * 60)
        print("🎯 DIAGNÓSTICO CONCLUÍDO")
    else:
        print("\n❌ FALHA NA CRIAÇÃO DA APLICAÇÃO")
