import sqlite3

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

#pedir codigo del producto a actualizar
codigo = input("ingrese el codigo del producto que desea actualizar: ")

#busca el producto en la base de datos
cursor.execute('SELECT * FROM productos WHERE codigo = ?', (codigo,))
producto = cursor.fetchone()

if producto:
    print(f"\nProducto encontrado: {producto[2]} (Cantidad actual: {producto[3]}, Precio Venta actual: {producto[4]})\n")

    nueva_cantidad = input("ingrese la nueva cantidad (deje vacio si no desea cambiar): ")
    nuevo_precio = input("ingrese el nuevo precio de venta (deje vacio si no desea cambiar): ")
#solo actualiza si el usuario ingresa un valor

    if nueva_cantidad:
        cursor.execute('UPDATE productos SET cantidad = ? WHERE codigo = ?', (int(nueva_cantidad), codigo))
    if nuevo_precio:
        cursor.execute('UPDATE productos SET precio_venta = ? WHERE codigo = ?', (float(nuevo_precio), codigo))
    
    conn.commit()
else:
    print("✖️ producto no encontrado. ")

    conn.close()