from flask import Flask, flash, render_template, redirect, request, send_from_directory, abort
from control.email_function import send_email, Contato
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')

    @app.route('/')
    def home():
        """Página inicial"""
        return render_template('index.html')

    @app.route('/resume')
    def resume():
        """Página de currículo"""
        return render_template('resume.html')

    @app.route('/portfolio')
    def portfolio():
        """Página de portfólio"""
        return render_template('portfolio.html')

    @app.route('/contact')
    def contact():
        """Página de contato"""
        return render_template('contact.html')

    @app.route('/p_privacy')
    def privacy():
        """Página de privacidade"""
        return render_template('p_privacy.html')

    @app.route('/useterms')
    def useterms():
        """Página de termos de uso"""
        return render_template('useterms.html')

    @app.route('/send', methods=['POST'])
    def send():
        """Rota para envio de mensagem automática"""
        nome = request.form.get('name')
        email = request.form.get('email')
        mensagem = request.form.get('message')
        if not nome or not email or not mensagem:
            flash('Todos os campos são obrigatórios.')
            return redirect('/')
        contato = Contato(nome, email, mensagem)
        try:
            send_email(contato)
            flash('Message sent successfully!')
        except Exception as e:
            flash(f'Error sending message: {str(e)}')
        return redirect('/')

    @app.route('/download/<filename>')
    def download_file(filename):
        """Rota para download de arquivos"""
        file_path = os.path.join('static/download', filename)
        if not os.path.exists(file_path):
            abort(404)
        return send_from_directory('static/download', filename)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
