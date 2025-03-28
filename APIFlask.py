from flask import Flask, render_template, jsonify, request
import json

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


#Funciones
@app.route("/productos",methods=["GET"])
def productos():
    # Si la petición es JSON (desde la app de escritorio o AJAX en la web)
    if request.headers.get("Accept") == "application/json" or request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"productos": lista_productos})

    # Si la petición es desde un navegador normal, renderiza la página HTML
    return render_template("productos.html", productos=lista_productos)

@app.route("/productos",methods=["POST"])
def recibir_productos():
    data = request.get_json()
    print(data)
    # Verifica que el JSON contenga la estructura esperada
    if data and "AGG" in data and "producto" in data["AGG"]:
        productos_recibidos = data["AGG"]["producto"]  # Extrae la lista de productos
        lista_productos.extend(productos_recibidos)  # Agrega los productos a la lista
        print(lista_productos)
        return jsonify({"message": "Producto agregado", "productos": lista_productos})

    return jsonify({"error": "Formato JSON inválido"}), 400 

if __name__ == "__main__":
    app.run(debug=True)
