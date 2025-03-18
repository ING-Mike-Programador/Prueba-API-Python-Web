import tkinter as tk
import requests
Lista = []
labelInfo = ""
# Crear la ventana de la aplicación de escritorio
def create_window():
    global window, labelInfo
    window = tk.Tk()
    window.title("Aplicación de Escritorio")

    # Botón para ver productos
    btn_ver_productos = tk.Button(window, text="Ver Productos", command=ver_productos)
    btn_ver_productos.pack(pady=20)
    labelInfo = tk.Label(window, text="")
    labelInfo.pack(pady=20)
    window.mainloop()

def ver_productos():
    # Solicitar los productos a la API
    response = requests.get("http://127.0.0.1:5000/productos")
    
    if response.status_code == 200:
        productos = response.json()  # Convierte la respuesta a formato JSON
        mostrar_productos(productos)
    else:
        print("Error al obtener productos")

def mostrar_productos(productos):
    # Mostrar los productos en la ventana
    labelInfo.config(text="")    
    producto_info = ""
    for producto in productos:
        producto_info += f"{producto['nombre']} - ${producto['precio']}\n"
    labelInfo.config(text=producto_info)    
    


# Ejecutar la interfaz gráfica
create_window()
