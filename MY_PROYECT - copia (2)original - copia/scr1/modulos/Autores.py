import sqlite3
from tkinter import messagebox

# Función para insertar un nuevo autor en la base de datos
def insertar_autors(nombres, apellidos, dni, nacionalidad):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar el autor
        cursor.execute('''
        INSERT INTO Autoress (nombres, apellidos, dni, nacionalidad)
        VALUES (?, ?, ?, ?)
        ''', (nombres, apellidos, dni, nacionalidad))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar el autor: {e}")
        return False
    
def obtener_autores():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Obtener las categorías
        cursor.execute('SELECT idautor, nombres, apellidos, dni, nacionalidad FROM Autores')
        categorias = cursor.fetchall()

        # Cerrar la conexión
        conn.close()

        return categorias
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los autores: {e}")
        return []

def buscar_autores(titulo):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Autores WHERE titulo LIKE ?
        ''', ('%' + titulo + '%',))  # Utiliza % para buscar coincidencias parciales del título

        libros_encontrados = cursor.fetchall()

        conn.close()

        return libros_encontrados
    except sqlite3.Error as e:
        print(f"Error al buscar el nombre del autor: {e}")
        return None