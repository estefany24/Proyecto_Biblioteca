import sqlite3
from tkinter import messagebox

# Función para insertar un nuevo préstamo en la base de datos
def insertar_prestamo(fecha_prestamo, fecha_entrega, idlibro, idusuario):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar el préstamo
        cursor.execute('''
        INSERT INTO Prestamos (fecha_prestamo, fecha_entrega, idlibro, idusuario)
        VALUES (?, ?, ?, ?)
        ''', (fecha_prestamo, fecha_entrega, idlibro, idusuario))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar el préstamo: {e}")
        return False



# Función para eliminar un préstamo de la base de datos
def eliminar_prestamo(idprestamo):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM Prestamos WHERE idprestamo = ?', (idprestamo,))

        conn.commit()
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al eliminar el préstamo: {e}")
        return False

# Función para actualizar un préstamo en la base de datos
def actualizar_prestamo(idprestamo, fecha_prestamo, fecha_entrega, idlibro, idusuario):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE Prestamos
        SET fecha_prestamo = ?, fecha_entrega = ?, idlibro = ?, idusuario = ?
        WHERE idprestamo = ?
        ''', (fecha_prestamo, fecha_entrega, idlibro, idusuario, idprestamo))

        conn.commit()
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al actualizar el préstamo: {e}")
        return False
    
def buscar_prestamos(idusu):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Prestamos WHERE idusuario LIKE ?
        ''', ('%' + idusu + '%',))  # Utiliza % para buscar coincidencias parciales del título

        prestamo_encontrados = cursor.fetchall()

        conn.close()

        return prestamo_encontrados
    except sqlite3.Error as e:
        print(f"Error al buscar libros por título: {e}")
        return None
    
def obtener_prestamos():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Obtener las categorías
        cursor.execute('SELECT idprestamos, fecha_prestamo, fecha_entrega, idlibro, idusuario FROM Prestamos')
        categorias = cursor.fetchall()

        # Cerrar la conexión
        conn.close()

        return categorias
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los prestamos: {e}")
        return []
