from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = '../tienda.db'  

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return "bienvenido a la tienda web"

@app.route('/productos')
def listar_productos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, precio_venta, cantidad FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return render_template('productos.html', productos=productos)

@app.route('/producto/<int:id>')
def detalle_producto(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, codigo, nombre, cantidad, precio_venta, precio_proveedor FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    conn.close()
    if producto:
        return render_template('detalle_producto.html', producto=producto)
    else:
        return render_template('error_producto.html', mensaje="producto no encontrado")

if __name__ == "__main__":
    app.run(debug=True)