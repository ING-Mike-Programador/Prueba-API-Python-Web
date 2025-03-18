from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Página principal
@app.route("/")
def home():
    return render_template("index.html")
# Página de productos (devuelve una lista de productos en JSON)
@app.route("/productos", methods=["GET"])
def productos():
    lista_productos = [
        {"nombre": "Laptop", "precio": 15000},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200}
    ]
    return jsonify(lista_productos)


if __name__ == "__main__":
    app.run(debug=True)
