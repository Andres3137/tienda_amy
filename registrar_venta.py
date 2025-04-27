import sqlite3

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

#pregunta al  usuario

codigo_producto = input("ingrese el codigo del producto vendido: ")

#buca el producto en la base de datoss

cursor.execute('SELECT nombre,cantidad  FROM productos WHERE codigo = ?', (codigo_producto,))
resultado = cursor.fetchone()

if resultado:
    nombre_producto, cantidad_actual = resultado
    print(f"\nProducto encontrado: {nombre_producto}")
    print(f"cantidad disponible: {cantidad_actual}\n")

    cantidad_vendida = int(input("ingrese la cantidad vendida: "))

    if cantidad_vendida > cantidad_actual:
        print("✖️ no hay suficiente stock para esta venta ")
    else:
        nueva_cantidad = cantidad_actual - cantidad_vendida
        cursor.execute('UPDATE productos SET cantidad = ? WHERE codigo = ?', (nueva_cantidad, codigo_producto))
        conn.commit()
        print("✅ venta registrada correctamente")
else:
    print("✖️ producto no encontrado")

conn.close()