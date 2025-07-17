"""
Ponto de entrada alternativo para o Render.com
Este arquivo garante que a aplicação seja encontrada corretamente
"""
import os
import sys

# Adicionar o diretório atual ao Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Importar a aplicação do wsgi.py
from wsgi import app

# Exportar a aplicação para o Gunicorn
application = app

if __name__ == '__main__':
    # Para execução direta
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
