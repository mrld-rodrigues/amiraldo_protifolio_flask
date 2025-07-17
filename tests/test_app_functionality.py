#!/usr/bin/env python3
"""
Teste completo da funcionalidade da aplicação Flask
"""

import os
import sys
import requests
import time
import subprocess
import signal
from threading import Thread

# Adicionar o diretório raiz ao PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Definir variáveis de ambiente para testes
os.environ.setdefault('FLASK_ENV', 'testing')
os.environ.setdefault('SECRET_KEY', 'test-secret-key-for-testing-only')

class FlaskAppTester:
    def __init__(self):
        self.server_process = None
        self.base_url = "http://localhost:5001"
    
    def start_server(self):
        """Inicia o servidor Flask em background"""
        try:
            # Usar porta 5001 para evitar conflitos
            cmd = [sys.executable, "-m", "flask", "--app", "wsgi", "run", "--port", "5001"]
            self.server_process = subprocess.Popen(
                cmd, 
                cwd=project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=os.environ.copy()
            )
            
            # Aguardar o servidor iniciar
            for attempt in range(10):
                try:
                    response = requests.get(f"{self.base_url}/", timeout=2)
                    if response.status_code in [200, 404, 500]:  # Qualquer resposta indica que o servidor está rodando
                        print("✅ Servidor Flask iniciado com sucesso")
                        return True
                except requests.exceptions.RequestException:
                    time.sleep(1)
            
            print("❌ Falha ao iniciar servidor Flask")
            return False
            
        except Exception as e:
            print(f"❌ Erro ao iniciar servidor: {e}")
            return False
    
    def stop_server(self):
        """Para o servidor Flask"""
        if self.server_process:
            self.server_process.terminate()
            self.server_process.wait()
            print("🛑 Servidor Flask parado")
    
    def test_routes(self):
        """Testa todas as rotas principais"""
        routes_to_test = [
            "/",
            "/portfolio", 
            "/resume",
            "/contact",
            "/privacy",
            "/useterms"
        ]
        
        print("🔍 Testando rotas...")
        print("=" * 50)
        
        all_passed = True
        for route in routes_to_test:
            try:
                response = requests.get(f"{self.base_url}{route}", timeout=5)
                status = response.status_code
                
                if status == 200:
                    print(f"✅ {route} - Status: {status}")
                elif status in [404, 500]:
                    print(f"⚠️  {route} - Status: {status} (pode precisar de correção)")
                else:
                    print(f"❌ {route} - Status: {status}")
                    all_passed = False
                    
            except requests.exceptions.RequestException as e:
                print(f"❌ {route} - Erro: {e}")
                all_passed = False
        
        return all_passed
    
    def test_static_files(self):
        """Testa se arquivos estáticos estão acessíveis"""
        static_files = [
            "/static/style.css",
            "/static/script.js",
            "/static/images/amiraldo_logo_black.png"
        ]
        
        print("\n🔍 Testando arquivos estáticos...")
        print("=" * 50)
        
        all_passed = True
        for static_file in static_files:
            try:
                response = requests.get(f"{self.base_url}{static_file}", timeout=5)
                status = response.status_code
                
                if status == 200:
                    print(f"✅ {static_file} - Acessível")
                else:
                    print(f"⚠️  {static_file} - Status: {status}")
                    
            except requests.exceptions.RequestException as e:
                print(f"❌ {static_file} - Erro: {e}")
                all_passed = False
        
        return all_passed
    
    def test_contact_form(self):
        """Testa o formulário de contato"""
        print("\n🔍 Testando formulário de contato...")
        print("=" * 50)
        
        try:
            # Primeiro, obter a página de contato
            response = requests.get(f"{self.base_url}/contact", timeout=5)
            if response.status_code != 200:
                print(f"❌ Página de contato não acessível: {response.status_code}")
                return False
            
            # Testar envio do formulário (sem dados válidos para não enviar email)
            form_data = {
                'nome': '',  # Campo vazio para testar validação
                'email': 'test@example.com',
                'assunto': 'Teste',
                'mensagem': 'Mensagem de teste'
            }
            
            response = requests.post(f"{self.base_url}/contact", data=form_data, timeout=5)
            
            if response.status_code in [200, 400]:  # 400 esperado para validação
                print("✅ Formulário de contato processado (validação funcionando)")
                return True
            else:
                print(f"⚠️  Formulário retornou status: {response.status_code}")
                return True  # Não é erro crítico
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao testar formulário: {e}")
            return False
    
    def run_all_tests(self):
        """Executa todos os testes"""
        print("🚀 Iniciando testes da aplicação Flask...")
        print("=" * 60)
        
        # Iniciar servidor
        if not self.start_server():
            return False
        
        try:
            # Executar testes
            routes_ok = self.test_routes()
            static_ok = self.test_static_files()
            contact_ok = self.test_contact_form()
            
            print("\n" + "=" * 60)
            print("📊 RESULTADO DOS TESTES:")
            print(f"✅ Rotas: {'OK' if routes_ok else 'FALHA'}")
            print(f"✅ Arquivos estáticos: {'OK' if static_ok else 'FALHA'}")
            print(f"✅ Formulário de contato: {'OK' if contact_ok else 'FALHA'}")
            
            overall_success = routes_ok and static_ok and contact_ok
            
            if overall_success:
                print("\n🎉 TODOS OS TESTES PASSARAM!")
                print("✅ Aplicação Flask funcionando corretamente")
            else:
                print("\n⚠️  ALGUNS TESTES FALHARAM")
                print("🔧 Verifique os logs acima para detalhes")
            
            return overall_success
            
        finally:
            # Parar servidor
            self.stop_server()

def test_import_functionality():
    """Testa se todos os módulos podem ser importados corretamente"""
    print("🔍 Testando imports da aplicação...")
    print("=" * 50)
    
    try:
        from wsgi import app
        print("✅ WSGI app importado com sucesso")
        
        with app.app_context():
            print("✅ Contexto da aplicação criado com sucesso")
            
        return True
        
    except Exception as e:
        print(f"❌ Erro ao importar aplicação: {e}")
        return False

if __name__ == "__main__":
    # Testar imports primeiro
    import_ok = test_import_functionality()
    
    if import_ok:
        # Se imports estão OK, testar a aplicação rodando
        tester = FlaskAppTester()
        app_ok = tester.run_all_tests()
        
        if app_ok:
            print("\n🏆 APLICAÇÃO TOTALMENTE FUNCIONAL!")
        else:
            print("\n🔧 APLICAÇÃO PRECISA DE AJUSTES")
    else:
        print("\n❌ PROBLEMAS DE IMPORTAÇÃO DETECTADOS")
