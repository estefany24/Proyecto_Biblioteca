import sqlite3
from tkinter import messagebox

# Función para insertar un nuevo libro en la base de datos
def insertar_libro(titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar el libro
        cursor.execute('''
        INSERT INTO Libros (titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar el libro: {e}")
        return False

# Función para eliminar un libro de la base de datos
def eliminar_libro(idlibro):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM Libros WHERE idlibros = ?', (idlibro,))

        conn.commit()
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al eliminar el libro: {e}")
        return False

# Función para actualizar un libro en la base de datos
def actualizar_libro(idlibro, titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE Libros
        SET titulo = ?, edicion = ?, descripcion = ?, categoria_idcategoria = ?, año = ?, nunpaginas = ?
        WHERE idlibro = ?
        ''', (titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas, idlibro))

        conn.commit()
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al actualizar el libro: {e}")
        return False
    

def buscar_libro(titulo):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Libros WHERE titulo LIKE ?
        ''', ('%' + titulo + '%',))  # Utiliza % para buscar coincidencias parciales del título

        libros_encontrados = cursor.fetchall()

        conn.close()

        return libros_encontrados
    except sqlite3.Error as e:
        print(f"Error al buscar libros por título: {e}")
        return None
    
def obtener_libros():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Obtener las categorías
        cursor.execute('SELECT idlibros, titulo, Autores, edicion, descripcion, categoria_idcategoria, año, nunpaginas FROM Libros')
        categorias = cursor.fetchall()

        # Cerrar la conexión
        conn.close()

        return categorias
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener las categorías: {e}")
        return []