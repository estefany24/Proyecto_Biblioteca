import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para insertar un nuevo rol en la base de datos
def insertar_rol(nombre_rol):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar el rol
        cursor.execute('''
        INSERT INTO Roles (nombre_rol)
        VALUES (?)''', (nombre_rol,))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        messagebox.showinfo("Éxito", "Rol insertado correctamente.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar el rol: {e}")

# Ejemplo de uso
# insertar_rol("Administrador")  # Llamada a la función para insertar un rol
# Función para eliminar un rol de la base de datos
def eliminar_rol(id_rol):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Eliminar el rol
        cursor.execute('''
        DELETE FROM Roles
        WHERE id_rol = ?''', (id_rol,))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        messagebox.showinfo("Éxito", "Rol eliminado correctamente.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al eliminar el rol: {e}")

# Función para actualizar un rol en la base de datos
def actualizar_rol(id_rol, nuevo_nombre_rol):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Actualizar el rol
        cursor.execute('''
        UPDATE Roles
        SET nombre_rol = ?
        WHERE id_rol = ?''', (nuevo_nombre_rol, id_rol))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        messagebox.showinfo("Éxito", "Rol actualizado correctamente.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al actualizar el rol: {e}")

def mostrar_roles():
        # Conectar a la base de datos y obtener los roles
        conn = sqlite3.connect('ABIBLIOTECA.db')
        c = conn.cursor()
        c.execute('SELECT idrol, nombre_rol FROM Roles')  # Suponiendo que 'roles' es la tabla que contiene los roles
        roles = c.fetchall()
        conn.close()

        return roles
