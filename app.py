"""
Compatibilidade com Render.com
Este arquivo garante que a aplicação seja encontrada independente da configuração
"""
# Importa a aplicação do wsgi.py
from wsgi import app

# Para compatibilidade total
application = app

# Exporta para diferentes convenções
flask_app = app
portfolio_app = app

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
