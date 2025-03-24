from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
# Variables 
lista_productos = [
        {"nombre": "Laptop", "precio": 15000},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Miguel", "precio": 8000},
        {"nombre": "Teclado", "precio": 1200}
    ]
# Página principal
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/productos",methods=["GET"])
def productos():
    # Si la petición es JSON (desde la app de escritorio o AJAX en la web)
    if request.headers.get("Accept") == "application/json" or request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"productos": lista_productos})

    # Si la petición es desde un navegador normal, renderiza la página HTML
    return render_template("productos.html", productos=lista_productos)

if __name__ == "__main__":
    app.run(debug=True)
