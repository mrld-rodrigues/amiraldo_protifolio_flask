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

**Solução implementada (ATUAL):**

- Adicionado `app = create_app()` no final de `app/__init__.py`
- Agora `from app import app` funciona corretamente
- Render pode usar `gunicorn app:app` como esperado
- Criado `render.yaml` para configuração explícita

**Solução alternativa (BACKUP):**

- Criado `application.py` na raiz como ponto de entrada limpo
- Pode usar `gunicorn application:app` se necessário

## 💡 Uso

### Configuração atual (recomendada):

```
web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --max-requests 1000
```

### Configuração com render.yaml:

```yaml
services:
  - type: web
    startCommand: gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

### Para usar uma alternativa:

1. Copie o conteúdo de `Procfile.alternatives` desejado
2. Substitua no `Procfile` principal
3. Faça novo deploy

## ⚠️ Importante

- Adicionado `app = create_app()` em `app/__init__.py` para compatibilidade
- `render.yaml` fornece configuração explícita para Render
- `application.py` existe como backup se necessário
- Teste localmente antes do deploy
