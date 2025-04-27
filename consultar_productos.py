import sqlite3

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

#consulta los productos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()

#muestra los productos

for producto in productos:
    print(f"ID: {producto[0]} | codigo: {producto[1]} | nombre: {producto[2]} | cantidad: {producto[3]} | precio venta: {producto[4]} | precio proveedor: {producto[5]}")

buscar = input("\n¿Desea buscar un producto específico? (si/no): ").lower()

if buscar == 'si':
    codigo_buscar = input("ingrese el codigo del producto a buscar: ")

    cursor.execute('SELECT * FROM productos WHERE codigo = ?',(codigo_buscar,))
    producto_especifico = cursor.fetchone()

    if producto_especifico:
        print("\n📦 Producto encontrado:")
        print(f"Código: {producto_especifico[1]}")
        print(f"Nombre: {producto_especifico[2]}")
        print(f"Cantidad disponible: {producto_especifico[3]}")
        print(f"Precio de venta: {producto_especifico[4]}")
        print(f"Precio del proveedor: {producto_especifico[5]}")
    else:
        print("❌ producto no encontrado")


conn.close()
