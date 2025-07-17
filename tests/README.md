# 🧪 Tests

Testes organizados por tipo:

## 📁 Estrutura

- **`unit/`** - Testes unitários de componentes específicos
- **`integration/`** - Testes de integração e funcionamento geral

## 🔬 Unit Tests

- `test_error_handling.py` - Testa sistema de tratamento de erros
- `test_keep_alive.py` - Testa funcionalidade keep-alive

## 🔗 Integration Tests

- `test_app_functionality.py` - Testa funcionalidades principais da aplicação
- `test_structure.py` - Valida estrutura do projeto
- `test_final.py` - Teste final de integração
- `check_config.py` - Verifica configurações
- `debug_app.py` - Utilitário de debug

## 🔧 Executar Testes

```bash
# Teste específico
python tests/unit/test_error_handling.py

# Teste de estrutura
python tests/integration/test_structure.py

# Teste final completo
python tests/integration/test_final.py
```

## 📋 Todos os Testes

Para executar todos os testes, use o script de validação:

```bash
python scripts/testing/validate_final.py
```
