# Portfolio Amiraldo Rodrigues

Portfolio pessoal desenvolvido em Flask com funcionalidades de contato por email.

## 🚀 Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Bootstrap 5
- **Email:** SMTP (Gmail)
- **Gerenciamento de Ambiente:** python-dotenv

## 📋 Pré-requisitos

- Python 3.7+
- Conta Gmail com senha de app configurada

## 🔧 Instalação

1. **Clone o repositório**

   ```bash
   git clone <url-do-repositorio>
   cd amiraldo_protifólio
   ```

2. **Crie um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**

   Crie um arquivo `.env` na raiz do projeto:

   ```env
   SECRET_KEY=sua_chave_secreta_aqui
   EMAIL_LOGIN=seu_email@gmail.com
   EMAIL_PASSWORD=sua_senha_de_app_gmail
   EMAIL_RECEIVER=email_destino@gmail.com
   ```

5. **Execute a aplicação**

   ```bash
   python app.py
   ```

6. **Acesse no navegador**
   ```
   http://127.0.0.1:5000
   ```

## 📁 Estrutura do Projeto

```
amiraldo_protifólio/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências do projeto
├── .env                  # Variáveis de ambiente (criar)
├── .gitignore           # Arquivos ignorados pelo Git
├── control/             # Módulos de controle
│   ├── __init__.py
│   ├── email_config.py  # Configurações de email
│   └── email_function.py # Funções de envio de email
├── static/              # Arquivos estáticos
│   ├── css/            # Estilos CSS
│   ├── js/             # Scripts JavaScript
│   ├── images/         # Imagens
│   ├── fonts/          # Fontes
│   └── download/       # Arquivos para download
└── templates/           # Templates HTML
    ├── index.html      # Página inicial
    ├── portfolio.html  # Portfólio
    ├── resume.html     # Currículo
    ├── contact.html    # Contato
    ├── p_privacy.html  # Política de Privacidade
    └── useterms.html   # Termos de Uso
```

## 📧 Configuração do Email

Para o funcionamento do formulário de contato:

1. **Ative a verificação em 2 etapas** na sua conta Google
2. **Gere uma senha de app** para o Gmail
3. **Configure as variáveis** no arquivo `.env`

## 🛠️ Desenvolvimento

Para desenvolvimento local:

```bash
# Modo debug (recarregamento automático)
python app.py
```

A aplicação será executada em modo debug por padrão.

## 📝 Funcionalidades

- ✅ Página inicial responsiva
- ✅ Portfólio de projetos
- ✅ Currículo detalhado
- ✅ Formulário de contato funcional
- ✅ Download de CV em PDF
- ✅ Design responsivo
- ✅ Animações CSS
- ✅ **Sistema robusto de tratamento de erros**
- ✅ **Rate limiting contra spam**
- ✅ **Validação avançada de formulários**
- ✅ **Logs estruturados para monitoramento**
- ✅ **Headers de segurança**

## 🔒 Segurança e Monitoramento

### Sistema de Tratamento de Erros

- **Páginas de erro personalizadas**: 404, 500, 403, 413, 429
- **Logging estruturado**: Console (dev) e arquivo rotativo (prod)
- **Rate limiting**: Proteção contra spam no formulário de contato
- **Validação robusta**: Email, nome, mensagem + detecção de spam
- **Headers de segurança**: XSS, CSRF, Content-Type proteções

### Logs e Monitoramento

```bash
# Logs de desenvolvimento (console)
FLASK_ENV=development python app.py

# Logs de produção (arquivo)
FLASK_ENV=production python app.py
# Logs salvos em: logs/portfolio.log
```

### Testes

Execute os testes do sistema:

```bash
python test_error_handling.py
```

Para mais detalhes, consulte: `ERROR_HANDLING_SUMMARY.md`

## 📄 Licença

Este projeto é pessoal e todos os direitos são reservados a Amiraldo Rodrigues.
