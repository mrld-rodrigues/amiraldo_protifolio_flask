@echo off
REM Script de setup para desenvolvimento no Windows
REM Execute: setup.bat

echo 🚀 Configurando ambiente de desenvolvimento...

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado. Instale Python 3.7+ primeiro.
    pause
    exit /b 1
)

REM Cria ambiente virtual se não existir
if not exist "venv" (
    echo 📦 Criando ambiente virtual...
    python -m venv venv
)

REM Ativa ambiente virtual
echo 🔄 Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Atualiza pip
echo ⬆️ Atualizando pip...
python -m pip install --upgrade pip

REM Instala dependências
echo 📚 Instalando dependências...
pip install -r requirements.txt

REM Verifica se .env existe
if not exist ".env" (
    echo ⚠️ Arquivo .env não encontrado!
    echo 📝 Criando template .env...
    (
        echo # Flask Configuration
        echo SECRET_KEY=sua_chave_secreta_muito_segura_aqui
        echo.
        echo # Email Configuration
        echo EMAIL_LOGIN=seu_email@gmail.com
        echo EMAIL_PASSWORD=sua_senha_de_app_gmail
        echo EMAIL_RECEIVER=destino@gmail.com
    ) > .env
    echo ✏️ Por favor, edite o arquivo .env com suas configurações reais
)

echo ✅ Setup concluído!
echo 🎯 Para executar a aplicação:
echo    venv\Scripts\activate
echo    python app.py
pause
