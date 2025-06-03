import sqlite3

# Especificar la ubicación de la base de datos
ruta_db = "C:/Users/Rob Vinz/Documents/Proyectos/productos.db"

# Conectar a la base de datos
conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()

# Insertar productos en la base de datos
productos = [
    ("123456", "Producto A"),
    ("789101", "Producto B"),
    ("112233", "Producto C"),
]

cursor.executemany("INSERT INTO productos (codigo, nombre) VALUES (?, ?)", productos)
conn.commit()
conn.close()

print("✅ Productos agregados correctamente.")