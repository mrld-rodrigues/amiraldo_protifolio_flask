# 🚀 Deploy Files

Esta pasta contém arquivos alternativos para deploy e configuração.

## 📁 Arquivos

- **`main.py`** - Ponto de entrada alternativo para deploy
- **`run.py`** - Script para execução em desenvolvimento
- **`flask_app.py`** - Ponto de entrada sem conflitos (alternativo ao app.py)
- **`Procfile.alternatives`** - Configurações alternativas do Procfile para diferentes cenários

## 🔧 Solução para Conflito app:app

**Problema identificado:** Render tentava usar `gunicorn app:app` e encontrava a pasta `app/` ao invés de um arquivo `app.py`, causando o erro:

```
AttributeError: module 'app' has no attribute 'app'
```

**Solução implementada:**

- Criado `application.py` na raiz como ponto de entrada limpo
- Atualizado `Procfile` para usar `gunicorn application:app`
- Este arquivo evita conflitos com a pasta `app/`

## 💡 Uso

### Configuração atual (recomendada):

```
web: gunicorn application:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --max-requests 1000
```

### Para usar uma alternativa:

1. Copie o conteúdo de `Procfile.alternatives` desejado
2. Substitua no `Procfile` principal
3. Faça novo deploy

## ⚠️ Importante

- O `application.py` na raiz resolve conflitos de nomenclatura
- Mantenha sempre uma das opções do Procfile ativa
- Teste localmente antes do deploy
