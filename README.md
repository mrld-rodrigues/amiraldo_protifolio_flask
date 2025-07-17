# 🎨 Portfólio Amiraldo Rodrigues

> **Portfolio profissional desenvolvido com Flask - Totalmente padronizado e otimizado para produção**

## ✨ Características

- 🎯 **Design Responsivo**: Adaptável a todos os dispositivos
- 🚀 **Performance Otimizada**: Carregamento rápido e eficiente
- 🔒 **Segurança Robusta**: Rate limiting, validações e proteções
- 🤖 **Keep-Alive System**: Uptime garantido no Render.com
- 📧 **Sistema de Contato**: Formulário funcional com validações
- 📊 **Monitoramento**: Health checks e logs estruturados
- 🎨 **UX Profissional**: Tratamento elegante de erros

## 🏗️ Estrutura do Projeto

```
amiraldo_portfolio/
├── wsgi.py                     # Ponto de entrada principal
├── requirements.txt            # Dependências Python
├── runtime.txt                # Versão Python para deploy
├── Procfile                   # Configuração Render/Heroku
├── .env.example               # Variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Este arquivo
├── app/                       # 🎯 Aplicação Flask
│   ├── __init__.py           #   Factory da aplicação
│   ├── routes/               #   📍 Rotas organizadas
│   │   ├── main.py          #     Rotas principais
│   │   └── contact.py       #     Sistema de contato
│   ├── core/                 #   🔧 Funcionalidades essenciais
│   │   ├── config.py        #     Configurações por ambiente
│   │   ├── email/           #     Sistema de email
│   │   ├── security/        #     Segurança e validações
│   │   ├── errors/          #     Tratamento de erros
│   │   └── services/        #     🆕 Keep-alive e serviços
│   ├── static/              #   📁 Arquivos estáticos
│   └── templates/           #   🎨 Templates HTML
├── docs/                      # 📚 Documentação
│   ├── DEPLOY.md             #   Guia de deploy
│   ├── KEEP_ALIVE.md         #   Sistema keep-alive
│   └── MELHORIAS_IMPLEMENTADAS.md  # Melhorias completas
├── scripts/                   # 🔧 Scripts de automação
│   ├── setup.sh             #   Setup Linux/Mac
│   ├── setup.bat            #   Setup Windows
│   └── deploy.sh            #   Deploy automatizado
└── tests/                     # 🧪 Testes automatizados
    ├── test_structure.py     #   Teste da estrutura
    ├── test_final.py         #   Teste final completo
    └── test_keep_alive.py    #   Teste do keep-alive
```

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask 3.1+ (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5
- **Email**: SMTP (Gmail) com validações
- **Deploy**: Render.com / Heroku
- **Monitoramento**: Health checks integrados
- **Keep-Alive**: Sistema automático para uptime

## 📋 Pré-requisitos

- Python 3.11+
- Conta Gmail com senha de app configurada
- Git para versionamento

## 🚀 Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone <url-do-repositorio>
cd amiraldo_protifólio
```

### 2. Configuração Automática (Recomendado)

**Linux/Mac:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

**Windows:**
```batch
scripts/setup.bat
```

### 3. Configuração Manual

**Criar ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

**Instalar dependências:**
```bash
pip install -r requirements.txt
```

**Configurar variáveis de ambiente:**
```bash
cp .env.example .env
# Edite o .env com suas configurações
```

### 4. Configurações Obrigatórias

Edite o arquivo `.env` com suas informações:

```bash
# Aplicação
SECRET_KEY=sua_chave_secreta_muito_forte_aqui
FLASK_ENV=development

# Email
EMAIL_LOGIN=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app_do_gmail
EMAIL_RECEIVER=email_destino@gmail.com

# Keep-Alive (para produção)
KEEP_ALIVE_ENABLED=true
KEEP_ALIVE_BOT_URL=https://keep-alive-bot-tavl.onrender.com/health
```

## 🏃‍♂️ Executando a Aplicação

### Desenvolvimento Local

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Executar aplicação
python wsgi.py
```

A aplicação estará disponível em: `http://localhost:5000`

### Usando Flask CLI

```bash
flask --app wsgi run --debug
```

## 🧪 Testes

### Executar Todos os Testes

```bash
# Teste da estrutura
python tests/test_structure.py

# Teste completo da aplicação
python tests/test_final.py

# Teste do sistema keep-alive
python tests/test_keep_alive.py
```

### Verificar Health Check

```bash
curl http://localhost:5000/health
```

## 🚀 Deploy em Produção

### Render.com (Recomendado)

1. **Criar novo Web Service no Render**
2. **Conectar repositório GitHub**
3. **Configurar variáveis de ambiente:**
   - `SECRET_KEY`
   - `EMAIL_LOGIN`
   - `EMAIL_PASSWORD`
   - `EMAIL_RECEIVER`
   - `KEEP_ALIVE_ENABLED=true`

4. **Deploy automático**: O Render detectará automaticamente as configurações

### Script de Deploy

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

## 📊 Monitoramento

### Endpoints Disponíveis

- **Home**: `/`
- **Portfolio**: `/portfolio`
- **Resume**: `/resume`
- **Contact**: `/contact`
- **Privacy**: `/p_privacy`
- **Terms**: `/useterms`
- **Health Check**: `/health` 🆕
- **Download CV**: `/download/cv.pdf`

### Health Check

O endpoint `/health` retorna informações sobre:
- Status da aplicação
- Ambiente de execução
- Status do keep-alive
- Timestamp da verificação

```json
{
  "status": "healthy",
  "environment": "production",
  "version": "1.0.0",
  "timestamp": "2025-07-17T18:30:00",
  "keep_alive": {
    "enabled": true,
    "running": true,
    "interval_minutes": 8
  }
}
```

## 🔒 Segurança Implementada

- ✅ **Rate Limiting**: Proteção contra spam
- ✅ **Validação de Formulários**: Entrada sanitizada
- ✅ **Headers de Segurança**: XSS, CSRF, etc.
- ✅ **Whitelist de Downloads**: Arquivos permitidos
- ✅ **Logs de Auditoria**: Monitoramento de atividades
- ✅ **Configuração Segura**: Sem dados sensíveis no código

## 🎨 Funcionalidades

### 📧 Sistema de Contato
- Formulário com validações robustas
- Envio via SMTP (Gmail)
- Rate limiting anti-spam
- Feedback visual para o usuário

### 📄 Download de CV
- Download seguro com whitelist
- Logs de todas as tentativas
- Validação de nomes de arquivo

### 🤖 Keep-Alive System
- Mantém aplicação ativa no Render
- Configuração flexível
- Monitoramento em tempo real
- Auto-recovery em falhas

## 📚 Documentação Adicional

- **[Guia de Deploy](docs/DEPLOY.md)**: Instruções detalhadas de deploy
- **[Keep-Alive System](docs/KEEP_ALIVE.md)**: Documentação do sistema
- **[Melhorias Implementadas](docs/MELHORIAS_IMPLEMENTADAS.md)**: Changelog completo

## 🆘 Troubleshooting

### Problemas Comuns

**Erro de Email:**
- Verifique se a senha de app do Gmail está correta
- Confirme se a autenticação em duas etapas está ativada

**Erro 500 em Produção:**
- Verifique os logs: `heroku logs --tail` ou logs do Render
- Confirme se todas as variáveis de ambiente estão configuradas

**Keep-Alive não funcionando:**
- Verifique se `KEEP_ALIVE_ENABLED=true`
- Confirme a URL do bot keep-alive
- Verifique logs no endpoint `/health`

### Logs e Debug

```bash
# Verificar logs da aplicação
tail -f logs/app.log

# Health check local
curl http://localhost:5000/health

# Testar keep-alive
python tests/test_keep_alive.py
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Amiraldo Rodrigues**
- Portfolio: [Seu Portfolio URL]
- LinkedIn: [Seu LinkedIn]
- Email: [Seu Email]

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**
