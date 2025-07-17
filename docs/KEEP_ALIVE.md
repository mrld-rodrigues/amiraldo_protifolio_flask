# Keep-Alive Integration

## Visão Geral

O sistema Keep-Alive foi integrado ao portfólio para manter a aplicação ativa na plataforma Render.com, evitando que ela entre em "sleep mode" após períodos de inatividade.

## Funcionalidades

### 🤖 Keep-Alive Automático

- **Ping periódico**: Envia requisições para o bot keep-alive a cada 8 minutos
- **Auto-recovery**: Tenta novamente em caso de falha
- **Logs detalhados**: Registra todas as operações para monitoramento

### ⚙️ Configuração Flexível

- **Habilitação por ambiente**: Só ativa em produção por padrão
- **Configuração via variáveis de ambiente**
- **Intervalos personalizáveis**

### 📊 Monitoramento

- **Endpoint de health check**: `/health`
- **Status do serviço**: Informa se o keep-alive está funcionando
- **Logs estruturados**: Para debugging e análise

## Configuração

### Variáveis de Ambiente

```bash
# Habilitar/desabilitar keep-alive
KEEP_ALIVE_ENABLED=true

# URL do bot keep-alive
KEEP_ALIVE_BOT_URL=https://keep-alive-bot-tavl.onrender.com/health

# Intervalo entre pings em segundos (padrão: 8 minutos)
KEEP_ALIVE_INTERVAL=480
```

### Configuração no Render.com

1. **Variáveis de Ambiente no Render**:

   ```
   FLASK_ENV=production
   KEEP_ALIVE_ENABLED=true
   KEEP_ALIVE_BOT_URL=https://keep-alive-bot-tavl.onrender.com/health
   ```

2. **Health Check URL**: Configure `/health` como endpoint de health check

## Uso

### Inicialização Automática

O keep-alive é inicializado automaticamente quando:

- `FLASK_ENV=production`
- `KEEP_ALIVE_ENABLED=true`

### Monitoramento

```bash
# Verificar status via endpoint
curl https://seusite.onrender.com/health

# Resposta esperada:
{
  "status": "healthy",
  "timestamp": "2025-07-17T18:30:00",
  "environment": "production",
  "version": "1.0.0",
  "keep_alive": {
    "enabled": true,
    "running": true,
    "interval_minutes": 8
  }
}
```

## Arquitetura

### Localização dos Arquivos

```
app/
├── core/
│   └── services/
│       ├── __init__.py
│       └── keep_alive.py    # 🆕 Serviço keep-alive
├── routes/
│   └── main.py             # Health check endpoint
└── __init__.py             # Integração no factory
```

### Fluxo de Funcionamento

1. **Inicialização**: Ao criar a app em produção
2. **Worker Thread**: Thread daemon em background
3. **Ping Periódico**: Requisições HTTP para o bot
4. **Auto-recovery**: Retry em caso de falha
5. **Logging**: Registro de todas as operações

## Segurança

### Boas Práticas Implementadas

- **Headers personalizados**: Identificação da origem
- **Timeout configurado**: Evita travamentos
- **Thread daemon**: Não bloqueia o shutdown da app
- **Tratamento de exceções**: Handling robusto de erros
- **Logs sem dados sensíveis**: Segurança de informações

### Controles de Acesso

- **Habilitação por ambiente**: Só ativa onde necessário
- **Configuração externa**: Via variáveis de ambiente
- **Graceful shutdown**: Para o serviço adequadamente

## Troubleshooting

### Logs Comuns

```bash
# Sucesso
🤖 Bot keep-alive: SUCCESS (Status: 200)
✅ Bot mantido ativo com sucesso

# Falha temporária
🤖 Bot keep-alive: FAIL (Status: 500)
❌ Falha ao manter bot ativo - tentando novamente em 2min

# Erro de rede
🤖 Bot keep-alive: ERROR - Connection timeout
```

### Verificações

1. **Status do serviço**: `GET /health`
2. **Logs da aplicação**: Verificar mensagens do keep-alive
3. **Variáveis de ambiente**: Confirmar configuração
4. **Conectividade**: Testar acesso ao bot

## Desenvolvimento

### Desabilitação Local

Para desenvolvimento local, o keep-alive é automaticamente desabilitado:

```bash
# .env para desenvolvimento
FLASK_ENV=development
KEEP_ALIVE_ENABLED=false
```

### Testes

```python
# Testar o serviço
from app.core.services import keep_alive_status

status = keep_alive_status()
print(status)
```

## Benefícios

- ✅ **Uptime garantido**: Aplicação sempre disponível
- ✅ **Implementação transparente**: Não afeta funcionalidades
- ✅ **Configuração flexível**: Fácil de ajustar
- ✅ **Monitoramento integrado**: Status em tempo real
- ✅ **Segurança**: Implementação robusta e segura
- ✅ **Performance**: Overhead mínimo na aplicação
