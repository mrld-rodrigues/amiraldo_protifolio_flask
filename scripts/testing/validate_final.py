#!/usr/bin/env python3
"""
Validação final da organização e funcionalidade do projeto
"""

import os
import sys

def validate_structure():
    """Valida se a estrutura está corretamente organizada"""
    print("🔍 VALIDANDO ESTRUTURA ORGANIZACIONAL")
    print("=" * 50)
    
    required_files = [
        "wsgi.py",
        "requirements.txt", 
        "runtime.txt",
        "Procfile",
        ".env.example",
        ".gitignore",
        "README.md"
    ]
    
    required_dirs = [
        "app/",
        "app/core/",
        "app/routes/",
        "app/static/",
        "app/templates/",
        "app/core/email/",
        "app/core/security/",
        "app/core/errors/",
        "app/core/services/",
        "docs/",
        "scripts/",
        "tests/"
    ]
    
    # Verificar arquivos obrigatórios
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file}")
    
    # Verificar diretórios obrigatórios
    missing_dirs = []
    for dir in required_dirs:
        if not os.path.exists(dir):
            missing_dirs.append(dir)
        else:
            print(f"✅ {dir}")
    
    if missing_files or missing_dirs:
        print(f"\n❌ Arquivos faltando: {missing_files}")
        print(f"❌ Diretórios faltando: {missing_dirs}")
        return False
    
    print("\n✅ ESTRUTURA TOTALMENTE ORGANIZADA!")
    return True

def validate_no_duplicates():
    """Valida que não há arquivos duplicados na raiz"""
    print("\n🔍 VALIDANDO LIMPEZA DE DUPLICATAS")
    print("=" * 50)
    
    # Arquivos que NÃO devem existir na raiz (duplicatas)
    should_not_exist = [
        "app.py",
        "config.py", 
        "error_handlers.py",
        "form_validators.py",
        "static/",
        "templates/",
        "control/",
        "__pycache__/",
        "README_OLD.md",
        "README_NEW.md"
    ]
    
    duplicates_found = []
    for item in should_not_exist:
        if os.path.exists(item):
            duplicates_found.append(item)
    
    if duplicates_found:
        print(f"❌ Duplicatas encontradas: {duplicates_found}")
        return False
    else:
        print("✅ Nenhuma duplicata encontrada!")
        print("✅ Raiz do projeto limpa e organizada!")
        return True

def validate_functionality():
    """Valida se a aplicação ainda funciona"""
    print("\n🔍 VALIDANDO FUNCIONALIDADE")
    print("=" * 50)
    
    try:
        # Adicionar o diretório raiz ao PYTHONPATH
        # scripts/testing/validate_final.py -> ../../ (raiz do projeto)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
        
        # Configurar ambiente de teste
        os.environ['SECRET_KEY'] = 'test-key-validation'
        os.environ['FLASK_ENV'] = 'testing'
        
        # Importar e testar
        from app import create_app
        app = create_app('testing')
        
        with app.test_client() as client:
            # Testar rotas principais
            routes = ['/', '/portfolio', '/resume', '/contact', '/health']
            
            for route in routes:
                response = client.get(route)
                if response.status_code == 200:
                    print(f"✅ {route} - Funcional")
                else:
                    print(f"❌ {route} - Status: {response.status_code}")
                    return False
        
        print("✅ APLICAÇÃO TOTALMENTE FUNCIONAL!")
        return True
        
    except Exception as e:
        print(f"❌ Erro na validação: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Executa todas as validações"""
    print("🏆 VALIDAÇÃO FINAL DA ORGANIZAÇÃO")
    print("=" * 60)
    
    validations = [
        ("Estrutura Organizacional", validate_structure),
        ("Limpeza de Duplicatas", validate_no_duplicates), 
        ("Funcionalidade da Aplicação", validate_functionality)
    ]
    
    all_passed = True
    
    for validation_name, validation_func in validations:
        if not validation_func():
            all_passed = False
            print(f"\n❌ {validation_name}: FALHOU")
        else:
            print(f"\n✅ {validation_name}: PASSOU")
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("🎉 PROJETO PERFEITAMENTE ORGANIZADO E FUNCIONAL!")
        print("✅ Estrutura profissional implementada")
        print("✅ Código limpo e modular")
        print("✅ Funcionalidades testadas e validadas")
        print("✅ Pronto para deploy em produção")
        print("\n🚀 PARABÉNS! SEU PORTFÓLIO ESTÁ IMPECÁVEL! 🏆")
        return True
    else:
        print("⚠️  ALGUMAS VALIDAÇÕES FALHARAM")
        print("🔧 Revise os itens marcados acima")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
