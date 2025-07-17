"""
Rate limiting simples para proteger contra spam
"""
from datetime import datetime, timedelta
from functools import wraps
from flask import request, abort, current_app
import logging

# Cache simples em memória para rate limiting
request_cache = {}

def cleanup_cache():
    """Remove entradas antigas do cache"""
    now = datetime.now()
    expired_keys = [
        ip for ip, data in request_cache.items() 
        if now - data['last_request'] > timedelta(hours=1)
    ]
    for key in expired_keys:
        del request_cache[key]

def rate_limit(max_requests=5, window_minutes=15, per_hour=10):
    """
    Decorator para rate limiting
    
    Args:
        max_requests: Máximo de requests por janela
        window_minutes: Tamanho da janela em minutos
        per_hour: Máximo de requests por hora
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Limpa cache periodicamente
            cleanup_cache()
            
            client_ip = request.remote_addr
            now = datetime.now()
            
            # Inicializa dados do IP se não existir
            if client_ip not in request_cache:
                request_cache[client_ip] = {
                    'requests': [],
                    'last_request': now,
                    'hourly_count': 0,
                    'hourly_reset': now + timedelta(hours=1)
                }
            
            ip_data = request_cache[client_ip]
            
            # Reset contador por hora
            if now > ip_data['hourly_reset']:
                ip_data['hourly_count'] = 0
                ip_data['hourly_reset'] = now + timedelta(hours=1)
            
            # Verifica limite por hora
            if ip_data['hourly_count'] >= per_hour:
                current_app.logger.warning(f'Rate limit exceeded (hourly): {client_ip}')
                abort(429)  # Too Many Requests
            
            # Remove requests antigas da janela
            window_start = now - timedelta(minutes=window_minutes)
            ip_data['requests'] = [
                req_time for req_time in ip_data['requests'] 
                if req_time > window_start
            ]
            
            # Verifica limite da janela
            if len(ip_data['requests']) >= max_requests:
                current_app.logger.warning(f'Rate limit exceeded (window): {client_ip}')
                abort(429)
            
            # Registra a request atual
            ip_data['requests'].append(now)
            ip_data['last_request'] = now
            ip_data['hourly_count'] += 1
            
            current_app.logger.info(f'Rate limit check passed: {client_ip} ({len(ip_data["requests"])}/{max_requests})')
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def get_rate_limit_status(ip_address):
    """Retorna o status atual do rate limiting para um IP"""
    if ip_address not in request_cache:
        return {
            'requests_in_window': 0,
            'hourly_requests': 0,
            'is_limited': False
        }
    
    ip_data = request_cache[ip_address]
    now = datetime.now()
    
    # Conta requests na janela atual
    window_start = now - timedelta(minutes=15)
    window_requests = len([
        req_time for req_time in ip_data['requests'] 
        if req_time > window_start
    ])
    
    return {
        'requests_in_window': window_requests,
        'hourly_requests': ip_data['hourly_count'],
        'is_limited': window_requests >= 5 or ip_data['hourly_count'] >= 10
    }
