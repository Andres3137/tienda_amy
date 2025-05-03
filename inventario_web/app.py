from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = '../tienda.db'  # Asegúrate de que esta ruta sea correcta

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

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

if __name__ == "__main__":
    app.run(debug=True)