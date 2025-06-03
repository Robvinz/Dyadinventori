import sqlite3

# Especificar la ubicación de la base de datos en la carpeta Proyectos de Rob Vinz
ruta_db = "C:/Users/Rob Vinz/Documents/Proyectos/productos.db"

# Conectar a la base de datos (si no existe, se crea automáticamente)
conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()

# Crear la tabla de productos si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE NOT NULL,
        nombre TEXT NOT NULL
    )
""")

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print(f"✅ Base de datos creada en: {ruta_db}")