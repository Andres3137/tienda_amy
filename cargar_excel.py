import pandas as pd
import sqlite3

archivo_excel = 'inventario.xlsx'
df = pd.read_excel(archivo_excel)

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
codigo TEXT UNIQUE,
nombre TEXT,
cantidad INTEGER,
precio_venta REAL,
precio_proveedor REAL
)''')

for _, row in df.iterrows():
    cursor.execute('''
    INSERT OR IGNORE INTO productos (codigo, nombre, cantidad, precio_venta, precio_proveedor)
    VALUES(?, ?, ?, ?, ?)
    ''',(
        row['codigo'],
        row['nombre del producto'],
        row['cantidad'],
        row['precio de venta'],
        row['precio proveedor'] if not pd.isna(row['precio proveedor']) else 0.0
    ))
conn.commit()
conn.close()
print("✅ inventario cargado correctamente en la base de datos.")