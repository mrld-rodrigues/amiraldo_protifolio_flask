#!/bin/bash

# Script de setup para desenvolvimento
# Execute: chmod +x setup.sh && ./setup.sh

echo "🚀 Configurando ambiente de desenvolvimento..."

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale Python 3.7+ primeiro."
    exit 1
fi

# Cria ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativa ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source venv/bin/activate

# Atualiza pip
echo "⬆️ Atualizando pip..."
pip install --upgrade pip

# Instala dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# Verifica se .env existe
if [ ! -f ".env" ]; then
    echo "⚠️ Arquivo .env não encontrado!"
    echo "📝 Criando template .env..."
    cat > .env << EOF
# Flask Configuration
SECRET_KEY=sua_chave_secreta_muito_segura_aqui

# Email Configuration
EMAIL_LOGIN=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app_gmail
EMAIL_RECEIVER=destino@gmail.com
EOF
    echo "✏️ Por favor, edite o arquivo .env com suas configurações reais"
fi

echo "✅ Setup concluído!"
echo "🎯 Para executar a aplicação:"
echo "   source venv/bin/activate"
echo "   python app.py"
