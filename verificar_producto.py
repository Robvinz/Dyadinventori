import sqlite3

# Especificar la ubicación de la base de datos
ruta_db = "C:/Users/Rob Vinz/Documents/Proyectos/productos.db"

# Conectar a la base de datos
conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()

# Función para verificar si un código está en la base de datos
def verificar_producto():
    codigo = input("🔍 Ingrese el código de producto a buscar: ")
    cursor.execute("SELECT nombre FROM productos WHERE codigo=?", (codigo,))
    resultado = cursor.fetchone()
    
    if resultado:
        print(f"✅ Producto encontrado: {resultado[0]}")
    else:
        print("❌ Código no registrado en la base de datos.")

# Ejecutar la función de verificación
verificar_producto()

# Cerrar la conexión
conn.close()