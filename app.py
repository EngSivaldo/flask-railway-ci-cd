# app.py

from flask import Flask, render_template

# Inicializa o objeto Flask
# O nome 'app' é importante, pois será usado pelo Gunicorn/Railway para iniciar
app = Flask(__name__)

# Define a rota principal (/)
@app.route('/')
def home():
    """Renderiza a página inicial."""
    # O Flask procura por 'index.html' na pasta 'templates'
    return render_template('index.html')

# Adiciona uma rota de exemplo para verificar que a aplicação está funcionando
@app.route('/saudacao')
def hello():
    """Retorna uma saudação simples como JSON."""
    return {"mensagem": "Olá, Parceiro de Programação! O Flask está no ar!"}

# Esta condição é usada para rodar o servidor em modo de desenvolvimento local
# O Railway/Gunicorn não usará isso, mas é útil para testes locais
if __name__ == '__main__':
    # Debug=True é bom para desenvolvimento, mas deve ser False em produção
    app.run(debug=True)