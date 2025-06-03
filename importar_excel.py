import pandas as pd
import sqlite3

# Especificar la ubicación de la base de datos y el archivo Excel
ruta_db = "C:/Users/Rob Vinz/Documents/Proyectos/productos.db"
archivo_excel = "C:/Users/Rob Vinz/Documents/Proyectos/INVENTARIO RTM134 - SEDE 134 - DIANA DAZA.xlsx"

# Leer el archivo Excel
df = pd.read_excel(archivo_excel)

# Conectar a la base de datos
conn = sqlite3.connect(ruta_db)

# Guardar los datos en una tabla llamada 'inventario'
df.to_sql("inventario", conn, if_exists="replace", index=False)

conn.close()

print("✅ Datos del Excel importados correctamente en la base de datos.")