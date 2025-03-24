import tkinter as tk
from tkinter import messagebox
import requests


def create_window():
    global window, labelInfo
    window = tk.Tk()
    window.title("Aplicación de Escritorio")
    centrar_ventana(window, 800, 600)
    window.configure(bg="#11cc8e")  # Fondo de la ventana

    # Contenedor principal para mejor organización
    frame = tk.Frame(window,
                     bg="#11cc8e")
    
    frame.pack(expand=True,
               fill="both",
               padx=20,
               pady=20)

    # Botón estilizado
    btn_ver_productos = tk.Button(
        frame,
        text="Ver Productos",
        command=ver_productos,
        font=("Arial", 14,"bold"),
        fg="#02130d", bg="#069767",
        activebackground="#043d74",
        activeforeground="white",
        relief="ridge",
        bd=3,
        padx=20,
        pady=1
    )
    btn_borrar_productos = tk.Button(
        frame,
        text="Borrar",
        command=borrar_productos,
        font=("Arial", 10, "bold"),
        fg="#02130d", bg="#069767",
        activebackground="#043d74",
        activeforeground="white",
        relief="ridge",
        bd=3, 
        padx=10,
        pady=1
    )
    
    btn_ver_productos.pack()
    
    btn_borrar_productos.pack(pady=3)
    
    texto = "Nombre: Miguel Edad 23 \n" \
    "Nombre: Itzel Edad 22 \n" \
    "Nombre: jessica Edad 24 \n" 
    
    # Etiqueta para mostrar productos
    labelDatos = tk.Label(
        frame,
        text="Datos:",
        font=("Arial", 12),
        fg="#02130d",
        bg="#11cc8e",
        justify="left",
        wraplength=350)
    
    labelLinea = tk.Label(
        frame,
        text="_____________________________________________",
        font=("Arial", 8),
        fg="#02130d",
        bg="#11cc8e",
        justify="left",
        wraplength=350
    )
    
    
    labelInfo = tk.Label(
        frame,
        text="",
        font=("Arial", 12),
        fg="#02130d",
        bg="#11cc8e",
        justify="left",
        wraplength=350,
        relief="ridge",
        bd=0,
        padx=5,
        pady=3
        
    )
    labelDatos.pack()
    labelLinea.pack()
    labelInfo.pack(pady=5)

    window.mainloop()

def borrar_productos():
    labelInfo.config(text="", bd=0)

def ver_productos():
    try:
        headers = {"Accept": "application/json"}  # Pide JSON en la respuesta
        response = requests.get("http://127.0.0.1:5000/productos", headers=headers)

        if response.status_code == 200:
            data = response.json()
            print("Json:\n")
            print(data)
            productos = data.get("productos", [])
            mostrar_productos(productos)
        else:
            labelInfo.config(text="Error al obtener productos",bd=0)
    except:
        messagebox.showerror("Error","No se pudo conectar con el servidor")
        labelInfo.config(text="Error al obtener productos",bd=0)

def mostrar_productos(productos):
    producto_info ="\n".join(f"{p['nombre']} - ${p['precio']}" for p in productos)
    labelInfo.config(text=producto_info, bd=4)

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho - ancho) // 2
    y = (pantalla_alto - alto) // 2
    y = y-50
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

create_window()

