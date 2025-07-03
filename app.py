from flask import Flask, flash, render_template, redirect, request, send_from_directory
from control.email_function import send_email, Contato
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


"""
 Rotas para as páginas
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/p_privacy')
def privacy():
    return render_template('p_privacy.html')

@app.route('/useterms')
def useterms():
    return render_template('useterms.html')



"""
 Rota para o envio da mensagem automática
"""

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']        
        contato = Contato(nome, email, mensagem)        
        try:
            send_email(contato)
            flash('Message sent successfully!')
        except Exception as e:
            flash(f'Error sending message: {str(e)}')
    return redirect('/')

"""
 Rota para o download do arquivo CV.pdf
"""

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/download', filename)



if __name__ == '__main__':
    app.run(debug=True)
