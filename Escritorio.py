import tkinter as tk
import requests

def create_window():
    global window, labelInfo
    window = tk.Tk()
    window.title("Aplicación de Escritorio")
    

    btn_ver_productos = tk.Button(window, text="Ver Productos", command=ver_productos)
    btn_ver_productos.pack(pady=20)

    labelInfo = tk.Label(window, text="", justify="left")
    labelInfo.pack(pady=20)

    window.mainloop()

def ver_productos():
    headers = {"Accept": "application/json"}  # Pide JSON en la respuesta
    response = requests.get("http://127.0.0.1:5000/productos", headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Json:\n")
        print(data)
        productos = data.get("productos", [])
        mostrar_productos(productos)
    else:
        labelInfo.config(text="Error al obtener productos")

def mostrar_productos(productos):
    producto_info = "\n".join(f"{p['nombre']} - ${p['precio']}" for p in productos)
    labelInfo.config(text=producto_info)

create_window()
