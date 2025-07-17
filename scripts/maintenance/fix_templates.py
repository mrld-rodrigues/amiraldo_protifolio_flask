#!/usr/bin/env python3
"""
Script para corrigir os url_for nos templates para usar blueprints
"""

import os
import re

def fix_url_for_in_file(filepath):
    """Corrige url_for em um arquivo específico"""
    
    # Mapeamento de endpoints antigos para novos (com blueprint)
    url_mappings = {
        "url_for('home')": "url_for('main.home')",
        "url_for('resume')": "url_for('main.resume')",
        "url_for('portfolio')": "url_for('main.portfolio')",
        "url_for('privacy')": "url_for('main.privacy')",
        "url_for('useterms')": "url_for('main.useterms')",
        "url_for('contact')": "url_for('contact.contact')",  # Este é do blueprint contact
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        for old_pattern, new_pattern in url_mappings.items():
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                changes_made += content.count(new_pattern) - original_content.count(new_pattern)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {os.path.basename(filepath)} - {changes_made} correções feitas")
            return True
        else:
            print(f"⚪ {os.path.basename(filepath)} - Nenhuma alteração necessária")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao processar {filepath}: {e}")
        return False

def fix_all_templates():
    """Corrige todos os templates na pasta app/templates"""
    
    templates_dir = "/home/mrldrodor/Documentos/mrld_projetos/amiraldo_protifólio/app/templates"
    
    print("🔧 Corrigindo url_for nos templates...")
    print("=" * 50)
    
    if not os.path.exists(templates_dir):
        print(f"❌ Pasta de templates não encontrada: {templates_dir}")
        return False
    
    template_files = []
    for file in os.listdir(templates_dir):
        if file.endswith('.html'):
            template_files.append(os.path.join(templates_dir, file))
    
    if not template_files:
        print("❌ Nenhum arquivo HTML encontrado")
        return False
    
    total_fixed = 0
    for template_file in template_files:
        if fix_url_for_in_file(template_file):
            total_fixed += 1
    
    print("=" * 50)
    print(f"🎯 {total_fixed} arquivos corrigidos de {len(template_files)} arquivos processados")
    
    return True

if __name__ == "__main__":
    fix_all_templates()
