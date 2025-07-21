"""
Keep-Alive Integration for Render.com
Sistema para manter serviços ativos na plataforma Render
"""

import threading
import time
import requests
import logging
import os
from datetime import datetime
from typing import Optional

class KeepAliveService:
    """
    Serviço para manter aplicações ativas no Render.com
    """
    
    def __init__(self, bot_url: str = None, interval: int = None):
        """
        Inicializa o serviço keep-alive
        
        Args:
            bot_url: URL do bot keep-alive (padrão via env var)
            interval: Intervalo entre pings em segundos (padrão: 8 minutos)
        """
        self.bot_url = bot_url or os.environ.get(
            'KEEP_ALIVE_BOT_URL', 
            'https://keep-alive-bot-tavl.onrender.com'
        )
        self.interval = interval or int(os.environ.get('KEEP_ALIVE_INTERVAL', 8 * 60))
        self.enabled = os.environ.get('KEEP_ALIVE_ENABLED', 'true').lower() == 'true'
        self.headers = {
            "User-Agent": "Amiraldo-Portfolio-KeepAlive/1.0",
            "X-Source": "amiraldo-portfolio"
        }
        self.is_running = False
        self.thread: Optional[threading.Thread] = None
        
        # Configurar logger específico
        self.logger = logging.getLogger('keep_alive')
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)
            
        # Log de inicialização para diagnóstico
        self.logger.info(f"KeepAlive inicializado:")
        self.logger.info(f"  - URL: {self.bot_url}")
        self.logger.info(f"  - Intervalo: {self.interval}s ({self.interval//60}min)")
        self.logger.info(f"  - Habilitado: {self.enabled}")
        print(f"[KeepAlive] Configurado - URL: {self.bot_url}, Intervalo: {self.interval}s")
    
    def ping_bot(self) -> bool:
        """
        Envia ping para o bot keep-alive
        
        Returns:
            bool: True se sucesso, False caso contrário
        """
        try:
            response = requests.get(
                self.bot_url, 
                headers=self.headers, 
                timeout=30
            )
            
            if response.status_code == 200:
                self.logger.info(f"🤖 Bot keep-alive: SUCCESS (Status: {response.status_code})")
                return True
            else:
                self.logger.warning(f"🤖 Bot keep-alive: FAIL (Status: {response.status_code})")
                return False
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"🤖 Bot keep-alive: ERROR - {e}")
            return False
        except Exception as e:
            self.logger.error(f"🤖 Bot keep-alive: UNEXPECTED ERROR - {e}")
            return False
    
    def _worker(self):
        """
        Worker thread que executa os pings periodicamente
        """
        self.logger.info("🚀 Iniciando Keep-Alive Worker")
        ping_count = 0
        
        while self.is_running:
            ping_count += 1
            self.logger.info(f"🔄 Ping #{ping_count} para o Keep-Alive Bot")
            
            success = self.ping_bot()
            
            if success:
                self.logger.info("✅ Bot mantido ativo com sucesso")
                # Aguarda o intervalo normal
                self.logger.info(f"⏱️ Próximo ping em {self.interval//60} minutos")
                
                # Sleep com verificação de parada
                for _ in range(self.interval):
                    if not self.is_running:
                        break
                    time.sleep(1)
            else:
                self.logger.error("❌ Falha ao manter bot ativo - tentando novamente em 2min")
                # Sleep menor em caso de erro
                for _ in range(120):  # 2 minutos
                    if not self.is_running:
                        break
                    time.sleep(1)
    
    def start(self):
        """
        Inicia o serviço keep-alive
        """
        self.logger.info("🔧 Tentando iniciar serviço Keep-Alive...")
        print("[KeepAlive] Tentando iniciar serviço...")
        
        if not self.enabled:
            self.logger.info("🚫 Keep-Alive desabilitado via configuração")
            print("[KeepAlive] DESABILITADO - variável KEEP_ALIVE_ENABLED=false")
            return
        
        if self.is_running:
            self.logger.warning("⚠️ Keep-Alive já está rodando")
            print("[KeepAlive] JÁ ESTÁ RODANDO")
            return
        
        self.logger.info("🚀 Iniciando Keep-Alive Worker...")
        print(f"[KeepAlive] INICIANDO - URL: {self.bot_url}")
        
        self.is_running = True
        self.thread = threading.Thread(target=self._worker, daemon=True)
        self.thread.start()
        
        self.logger.info("🎯 Keep-Alive Worker iniciado em background")
        print("[KeepAlive] ✅ WORKER INICIADO EM BACKGROUND")
        
        # Faz um ping imediato para testar
        self.logger.info("🧪 Testando conexão imediata com bot...")
        success = self.ping_bot()
        if success:
            self.logger.info("✅ Teste inicial bem-sucedido")
            print("[KeepAlive] ✅ TESTE INICIAL OK")
        else:
            self.logger.error("❌ Teste inicial falhou")
            print("[KeepAlive] ❌ TESTE INICIAL FALHOU")
    
    def stop(self):
        """
        Para o serviço keep-alive
        """
        if not self.is_running:
            return
        
        self.logger.info("🛑 Parando Keep-Alive Worker")
        self.is_running = False
        
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=5)
        
        self.logger.info("✅ Keep-Alive Worker parado")
    
    def status(self) -> dict:
        """
        Retorna o status do serviço
        
        Returns:
            dict: Status do serviço
        """
        return {
            'enabled': self.enabled,
            'running': self.is_running,
            'bot_url': self.bot_url,
            'interval_minutes': self.interval // 60,
            'thread_alive': self.thread.is_alive() if self.thread else False
        }

# Instância global do serviço
_keep_alive_service = None

def get_keep_alive_service() -> KeepAliveService:
    """
    Retorna a instância global do serviço keep-alive
    """
    global _keep_alive_service
    if _keep_alive_service is None:
        _keep_alive_service = KeepAliveService()
    return _keep_alive_service

def start_keep_alive():
    """
    Função de conveniência para iniciar o keep-alive
    """
    service = get_keep_alive_service()
    service.start()

def stop_keep_alive():
    """
    Função de conveniência para parar o keep-alive
    """
    service = get_keep_alive_service()
    service.stop()

def keep_alive_status() -> dict:
    """
    Função de conveniência para obter o status
    """
    service = get_keep_alive_service()
    return service.status()
