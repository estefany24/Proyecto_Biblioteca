import sqlite3
from tkinter import messagebox

# Función para insertar una nueva relación entre libros y autores en la base de datos
def insertar_libro_autor(libros_idlibros, autores_idautores):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar la relación libro-autor
        cursor.execute('''
        INSERT INTO Libros_Autores (libros_idlibros, autores_idautores)
        VALUES (?, ?)
        ''', (libros_idlibros, autores_idautores))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar la relación libro-autor: {e}")
        return False
