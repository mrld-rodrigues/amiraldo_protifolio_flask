"""
Core Services Package
Serviços essenciais da aplicação
"""

from .keep_alive import start_keep_alive, stop_keep_alive, keep_alive_status

__all__ = ['start_keep_alive', 'stop_keep_alive', 'keep_alive_status']
