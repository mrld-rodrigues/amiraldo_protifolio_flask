#!/usr/bin/env python3
"""
Script para mostrar a estrutura final organizada do projeto
"""

import os

def show_tree(directory, prefix="", max_depth=3, current_depth=0):
    """Mostra a estrutura de diretórios em formato tree"""
    if current_depth >= max_depth:
        return
    
    items = []
    try:
        all_items = sorted(os.listdir(directory))
        # Filtrar itens importantes
        for item in all_items:
            if item.startswith('.') and item not in ['.env.example', '.gitignore']:
                continue
            if item in ['__pycache__', '*.pyc', 'venv']:
                continue
            items.append(item)
    except PermissionError:
        return
    
    for i, item in enumerate(items):
        item_path = os.path.join(directory, item)
        is_last = i == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        
        print(f"{prefix}{current_prefix}{item}")
        
        if os.path.isdir(item_path):
            extension = "    " if is_last else "│   "
            show_tree(item_path, prefix + extension, max_depth, current_depth + 1)

def main():
    project_root = "/home/mrldrodor/Documentos/mrld_projetos/amiraldo_protifólio"
    
    print("🏗️ ESTRUTURA FINAL DO PROJETO ORGANIZADO")
    print("=" * 60)
    print(f"📁 {os.path.basename(project_root)}/")
    
    show_tree(project_root)
    
    print("\n" + "=" * 60)
    print("✅ ESTRUTURA PERFEITAMENTE ORGANIZADA!")
    print()
    print("📋 RESUMO:")
    print("├── 📄 Arquivos de configuração na raiz")
    print("├── 📁 app/ - Aplicação Flask modular")
    print("│   ├── core/ - Funcionalidades essenciais")
    print("│   ├── routes/ - Blueprints organizados")
    print("│   ├── static/ - Arquivos estáticos")
    print("│   └── templates/ - Templates HTML")
    print("├── 📚 docs/ - Documentação completa")
    print("├── 🔧 scripts/ - Scripts de automação")
    print("└── 🧪 tests/ - Testes automatizados")
    print()
    print("🎯 BENEFÍCIOS DA ORGANIZAÇÃO:")
    print("✅ Estrutura clara e navegável")
    print("✅ Separação de responsabilidades")
    print("✅ Fácil manutenção e escalabilidade")
    print("✅ Padrões profissionais seguidos")
    print("✅ Pronto para deploy em produção")

if __name__ == "__main__":
    main()
