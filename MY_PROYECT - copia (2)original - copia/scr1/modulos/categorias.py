import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para insertar una nueva categoría en la base de datos
def insertar_categoria(nombre_categoria, ubicacion):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar la categoría
        cursor.execute('''
        INSERT INTO Categorias (nombre_categoria, ubicacion)
        VALUES (?, ?)
        ''', (nombre_categoria, ubicacion))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        messagebox.showinfo("Éxito", "Categoría insertada correctamente.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar la categoría: {e}")

def actualizar_categoria(id_categoria, nombre_categoria, ubicacion):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Actualizar la categoría
        cursor.execute('''
        UPDATE Categorias
        SET nombre_categoria = ?, ubicacion = ?
        WHERE idcategoria = ?
        ''', (nombre_categoria, ubicacion, id_categoria))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al actualizar la categoría: {e}")
        return False

# Función para eliminar una categoría por su ID
def eliminar_categoria(id_categoria):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Eliminar la categoría
        cursor.execute('DELETE FROM Categorias WHERE idcategoria = ?', (id_categoria,))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        messagebox.showinfo("Éxito", "Categoría eliminada correctamente.")
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al eliminar la categoría: {e}")
        return False

def obtener_categorias():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Obtener las categorías
        cursor.execute('SELECT idcategoria, nombre_categoria, ubicacion FROM Categorias')
        categorias = cursor.fetchall()

        # Cerrar la conexión
        conn.close()

        return categorias
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener las categorías: {e}")
        return []
    


def obtener_categoria_por_id(id_categoria):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()
        cursor.execute('SELECT idcategoria, nombre_categoria, ubicacion FROM Categorias WHERE idcategoria = ?', (id_categoria,))
        categoria = cursor.fetchone()
        conn.close()
        return categoria
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener la categoría: {e}")
        return None
    
def buscar_categoria_por_nombre(nombre):
    conn = sqlite3.connect('ABIBLIOTECA.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias WHERE nombre_categoria LIKE ?", ('%' + nombre + '%',))
    categorias = cursor.fetchall()
    conn.close()
    return categorias