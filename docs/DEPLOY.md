# 🚀 DEPLOY NO RENDER - PASSO A PASSO

## 📋 Pré-requisitos

1. **Conta no GitHub** (gratuita)
2. **Conta no Render** (gratuita) - https://render.com
3. **Repositório Git** do projeto

## 🔧 1. Preparação do Projeto (CONCLUÍDO ✅)

Os seguintes arquivos já foram criados para o deploy:

- ✅ `requirements.txt` - Dependências Python
- ✅ `Procfile` - Comando para executar a aplicação
- ✅ `runtime.txt` - Versão do Python
- ✅ `.gitignore` - Arquivos ignorados pelo Git
- ✅ `app.py` - Modificado para produção

## 📤 2. Enviar Código para o GitHub

### 2.1 Inicializar Git (se ainda não foi feito)

```bash
git init
git add .
git commit -m "Initial commit - Portfolio Flask app"
```

### 2.2 Criar repositório no GitHub

1. Acesse https://github.com
2. Clique em "New repository"
3. Nome: `amiraldo-portfolio`
4. Deixe como **público** (para conta gratuita)
5. NÃO marque "Initialize with README"
6. Clique "Create repository"

### 2.3 Conectar e enviar código

```bash
git remote add origin https://github.com/SEU_USUARIO/amiraldo-portfolio.git
git branch -M main
git push -u origin main
```

## 🌐 3. Deploy no Render

### 3.1 Criar conta no Render

1. Acesse https://render.com
2. Clique "Get Started for Free"
3. Faça login com GitHub

### 3.2 Criar Web Service

1. No dashboard do Render, clique "New +"
2. Selecione "Web Service"
3. Conecte seu repositório GitHub
4. Selecione o repositório `amiraldo-portfolio`

### 3.3 Configurar o serviço

**Configurações básicas:**

- **Name:** `amiraldo-portfolio`
- **Region:** `Oregon (US West)` (mais próximo e gratuito)
- **Branch:** `main`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Configurações avançadas:**

- **Instance Type:** `Free` (gratuito)
- **Auto-Deploy:** `Yes` (deploy automático no push)

### 3.4 Configurar Variáveis de Ambiente

Na seção "Environment Variables", adicione:

```
SECRET_KEY = SUA_CHAVE_SECRETA_SEGURA_AQUI
EMAIL_LOGIN = seu_email@gmail.com
EMAIL_PASSWORD = sua_senha_de_app_gmail
EMAIL_RECEIVER = destino@gmail.com
```

⚠️ **IMPORTANTE:** Use a **senha de app** do Gmail, não a senha normal!

### 3.5 Finalizar Deploy

1. Clique "Create Web Service"
2. Aguarde o build (5-10 minutos)
3. Seu site estará disponível em: `https://amiraldo-portfolio.onrender.com`

## 🔧 4. Configurações Pós-Deploy

### 4.1 Configurar Gmail para envio de emails

1. **Ative a verificação em 2 etapas** na conta Google
2. **Gere uma senha de app:**
   - Google Account → Security → 2-Step Verification
   - App passwords → Mail → Generate
3. **Use essa senha** na variável `EMAIL_PASSWORD`

### 4.2 Testar funcionalidades

- ✅ Navegação entre páginas
- ✅ Formulário de contato
- ✅ Download do CV
- ✅ Responsividade

## 🚨 5. Importante - Limitações do Plano Gratuito

- **Sleep Mode:** Aplicação "dorme" após 15 min sem uso
- **Cold Start:** Primeiro acesso pode ser lento (30s)
- **Banda:** 100GB/mês
- **Build Time:** 500 horas/mês

## 🔄 6. Atualizações Futuras

Para atualizar o site:

```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
```

O Render fará deploy automaticamente! 🎉

## 🆘 7. Solução de Problemas

### Build falhou?

- Verifique se `requirements.txt` está correto
- Confirme se Python 3.11 está especificado em `runtime.txt`

### Aplicação não inicia?

- Verifique se `Procfile` existe e está correto
- Confirme se todas as variáveis de ambiente estão configuradas

### Emails não funcionam?

- Confirme se está usando senha de app do Gmail
- Verifique se as variáveis `EMAIL_*` estão corretas

### Site está lento?

- Normal no plano gratuito após "sleep"
- Considere upgrade para plano pago se necessário

## 📞 Suporte

- **Documentação Render:** https://render.com/docs
- **Status do Render:** https://status.render.com
