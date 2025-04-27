import sqlite3

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

#definimos el minimo de stock para alertar
stock_minimo = 5

#buscamos productos con stock bajo
cursor.execute('SELECT codigo, nombre, cantidad FROM productos WHERE cantidad <= ?', (stock_minimo,))
productos_bajo_stock = cursor.fetchall()

if productos_bajo_stock:
    print("\n🚨 Productos con stock bajo 🚨")
    for producto in productos_bajo_stock:
        print(f"Código: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[2]}")
else:
    print("\n✅ No hay productos con stock bajo.")
 
conn.close()