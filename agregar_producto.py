import sqlite3

conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

#pedir datos al usuario

codigo = input("ingrese el codigo del nuevo producto: ")
nombre = input("ingrese el nombre del producto: ")
cantidad = int(input("ingrese la cantidad inicial: "))
precio_venta = float(input("ingrese el precio de venta: "))
precio_proveedor = float(input("ingrese el precio del proveedor:"))

#insertar datos en la base de datos 

try:
    cursor.execute('''
    INSERT INTO productos (codigo, nombre, cantidad, precio_venta, precio_proveedor)
    VALUES(?, ?, ?, ?, ?)
    ''',(
        codigo,
        nombre,
        cantidad,
        precio_venta,
        precio_proveedor
    ))
    conn.commit()
    print("✅ producto agregado correctamente")
except sqlite3.IntegrityError:
    print("✖️ el codigo ya existe en la base de datos")

conn.close()