"""
Ponto de entrada compatível para deploy
Evita conflitos com a pasta app/ do projeto
"""
import os
import sys

# Adicionar o diretório atual ao path para garantir imports corretos
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    # Importa a aplicação do wsgi.py
    from wsgi import app
    
    # Para compatibilidade total com diferentes serviços de deploy
    application = app
    flask_app = app
    portfolio_app = app
    
    print("✅ flask_app.py: Aplicação carregada com sucesso!")
    
except Exception as e:
    print(f"❌ Erro ao carregar aplicação em flask_app.py: {e}")
    raise

if __name__ == '__main__':
    # Para execução direta
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando aplicação na porta {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
