import sqlite3

def mostrar_tablas():
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Consultar las tablas en la base de datos
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()

        # Mostrar las tablas encontradas
        if tablas:
            print("Las tablas en la base de datos son:")
            for tabla in tablas:
                print(tabla[0])  # Imprimir el nombre de la tabla

        else:
            print("No se encontraron tablas en la base de datos.")

        # Cerrar la conexión
        conn.close()

    except sqlite3.Error as e:
        print(f"Error SQLite: {e}")

# Llamar a la función para mostrar las tablas
mostrar_tablas()
