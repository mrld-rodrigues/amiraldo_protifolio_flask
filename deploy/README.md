# 🚀 Deploy Files

Esta pasta contém arquivos alternativos para deploy e configuração:

## 📁 Arquivos

- **`main.py`** - Ponto de entrada alternativo para deploy
- **`run.py`** - Script para execução em desenvolvimento  
- **`flask_app.py`** - Ponto de entrada sem conflitos (alternativo ao app.py)
- **`Procfile.alternatives`** - Configurações alternativas do Procfile para diferentes cenários

## 🔧 Uso

Estes arquivos são usados como fallback caso o `wsgi.py` principal apresente problemas no deploy.

### Para usar uma alternativa:

1. Copie o conteúdo de `Procfile.alternatives` desejado
2. Substitua no `Procfile` principal
3. Faça novo deploy

## ⚠️ Importante

Mantenha sempre o `wsgi.py` na raiz como ponto de entrada principal.
