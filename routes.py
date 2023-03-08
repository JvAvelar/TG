from TirodeGuerra import app, database
from flask import render_template


lista_usuarios = ['SubTenente Farias', 'Cabo Lucas', 'Cabo Wilhiam']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/localidade')
def contato():
    return render_template('localidade.html')

@app.route('/postos')
def usuarios():
    return render_template('postos.html', lista_usuarios=lista_usuarios)
