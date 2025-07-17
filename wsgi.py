"""
Portfolio Amiraldo Rodrigues - Aplicação Flask
Ponto de entrada principal da aplicação para Gunicorn
"""
import os
import sys

# Adicionar o diretório atual ao path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from app import create_app
    # Criar a instância da aplicação para o Gunicorn
    app = create_app()
    print("✅ Aplicação Flask criada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao criar aplicação: {e}")
    raise

if __name__ == '__main__':
    # Detecta o ambiente
    env = os.environ.get('FLASK_ENV', 'development')
    
    if env == 'production':
        # Produção: usa configurações do Render
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        # Desenvolvimento: modo debug local
        app.run(debug=True)
