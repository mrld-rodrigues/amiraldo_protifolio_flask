#!/bin/bash

# Script para preparar e fazer deploy no Render
echo "🚀 Preparando projeto para deploy no Render..."

# Verifica se estamos em um repositório Git
if [ ! -d ".git" ]; then
    echo "📦 Inicializando repositório Git..."
    git init
fi

# Adiciona todos os arquivos
echo "📄 Adicionando arquivos ao Git..."
git add .

# Pergunta por uma mensagem de commit
read -p "📝 Digite a mensagem do commit: " commit_message
if [ -z "$commit_message" ]; then
    commit_message="Deploy: Atualizações do portfolio"
fi

# Faz o commit
echo "💾 Fazendo commit..."
git commit -m "$commit_message"

# Verifica se remote origin existe
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Configure o remote do GitHub:"
    read -p "Cole a URL do seu repositório GitHub: " repo_url
    git remote add origin "$repo_url"
fi

# Envia para o GitHub
echo "📤 Enviando para o GitHub..."
git push -u origin main

echo "✅ Código enviado para o GitHub!"
echo ""
echo "🌐 Próximos passos:"
echo "1. Acesse https://render.com"
echo "2. Crie um Web Service"
echo "3. Conecte seu repositório GitHub"
echo "4. Configure as variáveis de ambiente"
echo "5. Faça o deploy!"
echo ""
echo "📖 Consulte DEPLOY.md para instruções detalhadas"
