from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='app/views/templates', static_folder='app/views/static')

CUPCAKES = [
    {"id": 1, "nome": "Cupcake de Chocolate Supremo", "preco": 12.50, "descricao": "Massa de cacau 70% com recheio de brigadeiro gourmet.", "imagem": "chocolate.jpg"},
    {"id": 2, "nome": "Cupcake Red Velvet", "preco": 14.00, "descricao": "Massa aveludada tradicional com recheio de cream cheese.", "imagem": "redvelvet.jpg"},
    {"id": 3, "nome": "Cupcake de Baunilha com Morango", "preco": 11.00, "descricao": "Massa leve de baunilha com geleia artesanal de morango.", "imagem": "morango.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html', cupcakes=CUPCAKES)

@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(CUPCAKES), 200

if __name__ == '__main__':
    app.run(debug=True)