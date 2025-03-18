from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

# Página de productos
@app.route("/productos")
def productos():
    lista_productos = [
        {"nombre": "Laptop", "precio": 15000},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200},
        {"nombre": "Laptop", "precio": 15000},
        {"nombre": "Mouse", "precio": 500},
        {"nombre": "Teclado", "precio": 1200}
    ]
    return render_template("productos.html", productos=lista_productos)

if __name__ == "__main__":
    app.run(debug=True)
