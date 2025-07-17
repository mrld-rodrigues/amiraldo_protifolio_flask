# 🔧 Correção: Conflito de Nomes app.py vs app/

## 🐛 Problema Identificado

O arquivo `app.py` criado na raiz estava entrando em conflito com a pasta `app/` do projeto:

```
amiraldo_portifólio/
├── app.py          ← Arquivo conflitante
├── app/            ← Pasta do projeto
│   ├── __init__.py
│   └── ...
```

**Erro observado:**

```
AttributeError: module 'app' has no attribute 'app'
```

## 🔍 Causa do Problema

Quando o Python tentava importar `app`, ele importava a **pasta** `app/` como módulo em vez do **arquivo** `app.py`. Isso acontece porque:

1. Python prioriza pastas com `__init__.py` sobre arquivos `.py`
2. O Render tentava executar `gunicorn app:app`
3. Resultado: importava `app/` (pasta) mas procurava `app.app` (atributo)

## ✅ Solução Aplicada

1. **Renomeado** `app.py` → `flask_app.py`
2. **Atualizado** imports e configurações
3. **Testado** funcionamento correto

## 📝 Arquivos Atualizados

- ✅ `app.py` → `flask_app.py` (renomeado e melhorado)
- ✅ `Procfile.alternatives` (nova opção adicionada)
- ✅ `scripts/test_deploy.py` (teste atualizado)

## 🚀 Resultado

Agora temos múltiplas opções funcionais para deploy:

1. **`wsgi.py`** (principal, atual no Procfile)
2. **`main.py`** (alternativo)
3. **`flask_app.py`** (sem conflitos)
4. **`run.py`** (desenvolvimento)

## 🧪 Validação

```bash
python scripts/test_deploy.py
```

**Resultado:** ✅ 4/4 testes passaram

## 📋 Próximos Passos

1. Fazer novo deploy no Render
2. Se ainda houver problemas, usar alternativas do `Procfile.alternatives`
3. Validar funcionamento em produção
