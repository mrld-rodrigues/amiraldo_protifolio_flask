"""
Ponto de entrada compatível para Render.com
Redireciona para o wsgi.py principal
"""

# Importar a aplicação do ponto de entrada principal
from wsgi import app

# Para compatibilidade com diferentes configurações de deploy
application = app

# Se executado diretamente
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
