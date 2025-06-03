import sqlite3
import tkinter as tk
from tkinter import ttk

class InventoryApp:
    def __init__(self, root):
        # Configuración inicial de la ventana y ruta a la base de datos.
        self.root = root
        self.root.title("Lista de Productos")
        self.ruta_db = "C:/Users/Rob Vinz/Documents/Proyectos/productos.db"
        # Llama a la configuración de la interfaz.
        self.setup_ui()

    def setup_ui(self):
        """Configura todos los widgets de la interfaz."""
        # Campo para ingresar el código del producto.
        self.entrada = tk.Entry(self.root)
        self.entrada.pack(pady=5)

        # Botón para verificar el código.
        self.boton_verificar = tk.Button(self.root, text="Verificar Código", command=self.verificar_codigo)
        self.boton_verificar.pack(pady=5)

        # Etiqueta de estado para mostrar mensajes.
        self.etiqueta = tk.Label(self.root, text="🔍 Ingrese un código", bg="gray")
        self.etiqueta.pack(fill="both", expand=True, pady=5)

        # Treeview para mostrar la lista de productos.
        self.tabla = ttk.Treeview(self.root, columns=("Código", "Nombre"), show="headings")
        self.tabla.heading("Código", text="Código")
        self.tabla.heading("Nombre", text="Nombre")

        # Definir estilos para el Treeview.
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        style.map("Treeview", background=[("selected", "lightgreen")])
        self.tabla.tag_configure("encontrado", background="lightgreen")

        self.tabla.pack(pady=5, fill="both", expand=True)

        # Botón para cargar productos desde la base de datos.
        self.boton_cargar = tk.Button(self.root, text="Cargar Productos", command=self.cargar_productos)
        self.boton_cargar.pack(pady=5)

    def cargar_productos(self):
        """Carga la lista de productos desde la base de datos en el Treeview."""
        # Conectar a la base de datos y extraer los productos.
        conn = sqlite3.connect(self.ruta_db)
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre FROM productos")
        productos = cursor.fetchall()
        conn.close()

        # Limpiar la tabla antes de cargar datos nuevos.
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar cada producto en la tabla.
        for producto in productos:
            self.tabla.insert("", "end", values=producto)

    def verificar_codigo(self):
        """Verifica si el código ingresado corresponde a un producto en la base de datos."""
        codigo_ingresado = self.entrada.get().strip()
        conn = sqlite3.connect(self.ruta_db)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM productos WHERE codigo=?", (codigo_ingresado,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            # Producto encontrado: actualiza la etiqueta de estado y resalta la fila.
            self.etiqueta.config(bg="green", text=f"✅ Producto encontrado: {resultado[0]}")
            for item in self.tabla.get_children():
                if self.tabla.item(item, "values")[0] == codigo_ingresado:
                    self.tabla.item(item, tags=("encontrado",))
        else:
            # Producto no encontrado: notifica al usuario.
            self.etiqueta.config(bg="red", text="❌ Código no registrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()