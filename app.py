# Importando a biblioteca do Flask para fazer um site dinâmico
from flask import Flask, render_template

# Criando um objeto do servidor
app = Flask(__name__)

# Definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

# Parte principal do programa em Python
if __name__ == '__main__':
    app.run(debug=True)