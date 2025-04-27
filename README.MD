# 🛒 Sistema de Inventario - Tienda Física de Alimentos

## 📚 Descripción
Sistema completo de gestión de inventario y ventas para una tienda física de alimentos, desarrollado en Python con base de datos SQLite.

El sistema permite:
- Cargar productos desde un archivo Excel.
- Consultar el inventario completo.
- Registrar ventas descontando la cantidad disponible
- Agregar nuevos productos al inventario.
- Actualizar precios y cantidades de productos existentes.
- Generar alertas automáticas de stock bajo.

---

## 🚀 Funcionalidades
- **Carga inicial** del inventario desde un archivo `inventario.xlsx`.
- **Consulta general** de todos los productos disponibles.
- **Búsqueda específica** por código de producto.
- **Registro de ventas**: descuenta automáticamente de la cantidad disponible .
- **Adición de productos** nuevos manualmente.
- **Actualización** de precios de venta y cantidades.
- **Alerta de stock bajo** para productos con pocas unidades.

---

## 🛠️ Tecnologías utilizadas
- **Lenguaje**: Python 3
- **Base de datos**: SQLite3
- **Librerías**:
  - `pandas` (para leer Excel)
  - `openpyxl` (para soporte de archivos `.xlsx`)

---

## 📂 Estructura del proyecto
tienda_amy/ 
├── agregar_producto.py 
├── alerta_stock.py 
├── actualizar_producto.py
├── cargar_excel.py 
├── consultar_productos.py 
├── inventario.xlsx 
├── registrar_venta.py 
├── tienda.db 
└── README.md


---

## 📋 Cómo ejecutar el proyecto

1. Instalar dependencias si es necesario:
   ```bash
   pip install pandas openpyxl
2.Ejecutar  la carga de inventario:
    py cargar_excel.py
3.utilizar los demas scripts  segun sea necesario Consultar productos: 

-Consultar productos:py consultar_productos.py

-Registrar una venta: py registrar_venta.py

-Agregar producto: py agregar_producto.py

-Actualizar producto: py actualizar_producto.py

-Alerta de stock bajo: py alerta_stock.py


👨‍💻 Autor
Desarrollado por Andres felipe Ramos Orjuela como parte de un proyecto de automatización y mejora de inventarios.
