import sqlite3
import tkinter as tk

# Especificar la ubicación de la base de datos
ruta_db = "C:/Users/Rob Vinz/Documents/Proyectos/productos.db"

# Función para verificar si un código está en la base de datos
def verificar_producto():
    codigo = entrada.get()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM productos WHERE codigo=?", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        etiqueta.config(bg="green", text=f"✅ Producto encontrado: {resultado[0]}")
    else:
        etiqueta.config(bg="red", text="❌ Código no registrado.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Verificación de Productos")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Verificar Código", command=verificar_producto)
boton.pack()

etiqueta = tk.Label(ventana, text="🔍 Ingrese un código", bg="gray")
etiqueta.pack(fill="both", expand=True)

ventana.mainloop()