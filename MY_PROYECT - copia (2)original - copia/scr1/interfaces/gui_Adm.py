import tkinter as tk
import sqlite3
import sys
import os
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from fpdf import FPDF
from tkinter import messagebox ,ttk
from scr1.modulos import categorias
from scr1.modulos import Autores
from scr1.modulos import libros
from scr1.modulos import Libros_Autores
from scr1.modulos import prestamos
from scr1.modulos import Roles  # Importar el módulo de roles
from scr1.modulos import usuarios 
from scr1.modulos.usuarios import verificar_usuario
from scr1.modulos.carnetuniversitario import CarnetUniversitariosss

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),)))

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca App")
        self.root.geometry("800x600") 

        # Crear el menú principal
        self.menu_principal = tk.Menu(root)
        root.config(menu=self.menu_principal)
        '''
   # Opción del menú Libros
        self.menu_libros = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Libros", menu=self.menu_libros)
        self.menu_libros.add_command(label="Buscar Libro", command=self.abrir_ventana_buscar_libro)
          # Widgets para buscar libros
        self.label_buscar_libro = tk.Label(root, text="Buscar libro por título:")
        self.buscar_libro_entry = tk.Entry(root)
        self.btn_buscar_libro = tk.Button(root, text="Buscar", command=self.buscar_libro)

        # Etiquetas para mostrar información del libro encontrado
        self.label_info_libro = tk.Label(root, text="Información del Libro Encontrado:")
        self.label_titulo_encontrado = tk.Label(root, text="")
        self.label_edicion_encontrada = tk.Label(root, text="")
        self.label_descripcion_encontrada = tk.Label(root, text="")
        # Puedes agregar más etiquetas según los atributos del libro que desees mostrar

        # Ubicación de los widgets en la interfaz (row y column)
        self.label_buscar_libro.grid(row=0, column=0, padx=10, pady=10)
        self.buscar_libro_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_buscar_libro.grid(row=1, columnspan=2, padx=10, pady=10)

        self.label_info_libro.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        self.label_titulo_encontrado.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.label_edicion_encontrada.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        self.label_descripcion_encontrada.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        # Ajusta las ubicaciones según necesites para mostrar más atributos del libro
        '''
    




        # Opción del menú Categorías
        self.menu_categorias = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Categorías", menu=self.menu_categorias)
        self.menu_categorias.add_command(label="Agregar Categoría", command=self.abrir_ventana_categoria)
        self.menu_categorias.add_command(label="Ver Categorías", command=self.ver_categorias)
        self.menu_categorias.add_command(label="Eliminar Categorías", command=self.abrir_ventana_eliminar_categoria)
        self.menu_categorias.add_command(label="actualizar Categorías", command=self.abrir_ventana_actualizar_categoria)
        #self.menu_categorias.add_command(label="actualizar actegoria",command=self.actualizar_lista_categorias)
        

        # Opción del menú Autores
        self.menu_autores = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Autores", menu=self.menu_autores)
        self.menu_autores.add_command(label="Agregar Autor", command=self.abrir_ventana_autor)
        self.menu_autores.add_command(label="Ver Autores", command=self.ver_autores)
        self.menu_autores.add_command(label="Eliminar Autor", command=self.abrir_ventana_eliminar_autor)
        self.menu_autores.add_command(label="Actualizar Autor", command=self.abrir_ventana_actualizar_autor)

        # Opción del menú Libros
        self.menu_libros = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Libros", menu=self.menu_libros)
        self.menu_libros.add_command(label="Agregar Libro", command=self.abrir_ventana_libro)
        self.menu_libros.add_command(label="Ver libros", command=self.ver_libros)
        self.menu_libros.add_command(label="Eliminar Libro", command=self.abrir_ventana_eliminar_libro)
        self.menu_libros.add_command(label="Actualizar Libro", command=self.abrir_ventana_actualizar_libro)

        # Opción del menú Libros_Autores
        self.menu_libros_autores = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Libros_Autores", menu=self.menu_libros_autores)
        self.menu_libros_autores.add_command(label="Agregar Relación Libro-Autor", command=self.abrir_ventana_libro_autor)
        self.menu_libros_autores.add_command(label="Ver informacion completa", command=self.ver_libros_autores)

        # Opción del menú Prestamos
        self.menu_prestamos = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Prestamos", menu=self.menu_prestamos)
        self.menu_prestamos.add_command(label="Agregar Préstamo", command=self.abrir_ventana_prestamo)
        self.menu_prestamos.add_command(label="Ver prestamos", command=self.ver_prestamos)
        self.menu_prestamos.add_command(label="Eliminar Préstamo", command=self.abrir_ventana_eliminar_prestamo)
        self.menu_prestamos.add_command(label="Actualizar Préstamo", command=self.abrir_ventana_actualizar_prestamo)

         # Opción del menú Roles
        self.menu_roles = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Roles", menu=self.menu_roles)
        self.menu_roles.add_command(label="Agregar Rol", command=self.abrir_ventana_rol)
        self.menu_roles.add_command(label="Ver prestamos", command=self.ver_roles)
        self.menu_roles.add_command(label="Eliminar Rol", command=self.abrir_ventana_eliminar_rol)
        self.menu_roles.add_command(label="Actualizar Rol", command=self.abrir_ventana_actualizar_rol)

        # Opción del menú Usuarios


        self.menu_usuarios = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Usuarios", menu=self.menu_usuarios)
        self.menu_usuarios.add_command(label="Agregar Usuario", command=self.abrir_ventana_usuario)
        self.menu_usuarios.add_command(label="Ver usuarios", command=self.ver_usuarios)
        self.menu_usuarios.add_command(label="Eliminar Usuario", command=self.abrir_ventana_eliminar_usuario)
        self.menu_usuarios.add_command(label="Actualizar Usuario", command=self.abrir_ventana_actualizar_usuario)
        self.menu_usuarios.add_command(label="Generar Carnet", command=self.abrir_ventana_carnet) 
        # Crear una instancia de CarnetUniversitario para utilizarla más adelante
        #self.carnet_universitario_app = carnetuniversitario(self.root)

        # Etiquetas y campos de entrada para categorías (inicialmente ocultos)
        self.label_nombre_categoria = tk.Label(root, text="Nombre de la categoría:")
        self.nombre_categoria_entry = tk.Entry(root)
        self.label_ubicacion = tk.Label(root, text="Ubicación de la categoría:")
        self.ubicacion_entry = tk.Entry(root)
        self.btn_agregar_categoria = tk.Button(root, text="Agregar Categoría", command=self.agregar_categoria)
        
                # Etiquetas y campos de entrada para categorías (inicialmente ocultos)
        self.label_id_categoria = tk.Label(root, text="ID de la categoría:")
        self.id_categoria_entry = tk.Entry(root)
        self.btn_eliminar_categoria = tk.Button(root, text="Eliminar Categoría", command=self.eliminar_categoria)

        # Etiquetas y campos de entrada para actualizar categoría (inicialmente ocultos)
        self.label_id_categoria_actualizar = tk.Label(root, text="ID de la categoría:")
        self.id_categoria_actualizar_entry = tk.Entry(root)
        self.label_nombre_categoria_actualizar = tk.Label(root, text="Nuevo nombre de la categoría:")
        self.nombre_categoria_actualizar_entry = tk.Entry(root)
        self.label_ubicacion_actualizar = tk.Label(root, text="Nueva ubicación de la categoría:")
        self.ubicacion_actualizar_entry = tk.Entry(root)
        self.btn_actualizar_categoria = tk.Button(root, text="Actualizar Categoría", command=self.actualizar_categoria)

        # Área de texto para mostrar las categorías (inicialmente oculta)
        self.text_area = tk.Text(root, height=20, width=50)
        self.text_area.grid(row=10, columnspan=2, padx=10, pady=10)
        self.text_area.grid_remove()  # Ocultar inicialmente
                # Mostrar el encabezado de columnas

        # Etiquetas y campos de entrada para autores (inicialmente ocultos)
        self.label_nombres = tk.Label(root, text="Nombres del autor:")
        self.nombres_entry = tk.Entry(root)
        self.label_apellidos = tk.Label(root, text="Apellidos del autor:")
        self.apellidos_entry = tk.Entry(root)
        self.label_dni = tk.Label(root, text="DNI del autor:")
        self.dni_entry = tk.Entry(root)
        self.label_nacionalidad = tk.Label(root, text="Nacionalidad del autor:")
        self.nacionalidad_entry = tk.Entry(root)
        self.btn_agregar_autor = tk.Button(root, text="Agregar Autor", command=self.agregar_autor)

        # Widgets para eliminar autores (inicialmente ocultos)
        self.label_id_autor = tk.Label(root, text="ID del autor:")
        self.id_autor_entry = tk.Entry(root)
        self.btn_eliminar_autor = tk.Button(root, text="Eliminar Autor", command=self.eliminar_autor)

        # Widgets para actualizar autores (inicialmente ocultos)
        self.label_id_autor_actualizar = tk.Label(root, text="ID del autor:")
        self.id_autor_actualizar_entry = tk.Entry(root)
        self.label_nombres_autor_actualizar = tk.Label(root, text="Nuevos nombres del autor:")
        self.nombres_autor_actualizar_entry = tk.Entry(root)
        self.label_apellidos_actualizar = tk.Label(root, text="Nuevos apellidos:")
        self.apellidos_actualizar_entry = tk.Entry(root)
        self.label_dni_actualizar = tk.Label(root, text="Nuevo DNI:")
        self.dni_actualizar_entry = tk.Entry(root)
        self.label_nacionalidad_actualizar = tk.Label(root, text="Nueva nacionalidad:")
        self.nacionalidad_actualizar_entry = tk.Entry(root)
        self.btn_actualizar_autor = tk.Button(root, text="Actualizar Autor", command=self.actualizar_autor)

        # Etiquetas y campos de entrada para libros (inicialmente ocultos)
        self.label_titulo = tk.Label(root, text="Título del libro:")
        self.titulo_entry = tk.Entry(root)
        self.label_edicion = tk.Label(root, text="Edición del libro:")
        self.edicion_entry = tk.Entry(root)
        self.label_descripcion = tk.Label(root, text="Descripción del libro:")
        self.descripcion_entry = tk.Entry(root)
        self.label_categoria_idcategoria = tk.Label(root, text="ID de la Categoría:")
        self.categoria_idcategoria_entry = tk.Entry(root)
        self.label_año = tk.Label(root, text="Año del libro:")
        self.año_entry = tk.Entry(root)
        self.label_nunpaginas = tk.Label(root, text="Número de páginas:")
        self.nunpaginas_entry = tk.Entry(root)
        self.btn_agregar_libro = tk.Button(root, text="Agregar Libro", command=self.agregar_libro)

 # Widgets para eliminar libros (inicialmente ocultos)
        self.label_id_libro = tk.Label(root, text="ID del libro:")
        self.id_libro_entry = tk.Entry(root)
        self.btn_eliminar_libro = tk.Button(root, text="Eliminar Libro", command=self.eliminar_libro)

        # Widgets para actualizar libros (inicialmente ocultos)
        self.label_id_libro_actualizar = tk.Label(root, text="ID del libro:")
        self.id_libro_actualizar_entry = tk.Entry(root)
        self.label_titulo_libro_actualizar = tk.Label(root, text="Nuevo título del libro:")
        self.titulo_libro_actualizar_entry = tk.Entry(root)
        self.label_edicion_actualizar = tk.Label(root, text="Nueva edición:")
        self.edicion_actualizar_entry = tk.Entry(root)
        self.label_descripcion_actualizar = tk.Label(root, text="Nueva descripción:")
        self.descripcion_actualizar_entry = tk.Entry(root)
        self.label_categoria_idcategoria_actualizar = tk.Label(root, text="Nuevo ID de la categoría:")
        self.categoria_idcategoria_actualizar_entry = tk.Entry(root)
        self.label_año_actualizar = tk.Label(root, text="Nuevo año:")
        self.año_actualizar_entry = tk.Entry(root)
        self.label_num_paginas_actualizar = tk.Label(root, text="Nuevo número de páginas:")
        self.num_paginas_actualizar_entry = tk.Entry(root)
        self.btn_actualizar_libro = tk.Button(root, text="Actualizar Libro", command=self.actualizar_libro)

        # Etiquetas y campos de entrada para libros_autores (inicialmente ocultos)
        self.label_libros_idlibros = tk.Label(root, text="ID del Libro:")
        self.libros_idlibros_entry = tk.Entry(root)
        self.label_autores_idautores = tk.Label(root, text="ID del Autor:")
        self.autores_idautores_entry = tk.Entry(root)
        self.btn_agregar_libro_autor = tk.Button(root, text="Agregar Relación Libro-Autor", command=self.agregar_libro_autor)

        # Etiquetas y campos de entrada para prestamos (inicialmente ocultos)
        self.label_fecha_prestamo = tk.Label(root, text="Fecha de préstamo:")
        self.fecha_prestamo_entry = tk.Entry(root)
        self.label_fecha_entrega = tk.Label(root, text="Fecha de entrega:")
        self.fecha_entrega_entry = tk.Entry(root)
        self.label_idlibro = tk.Label(root, text="ID del Libro:")
        self.idlibro_entry = tk.Entry(root)
        self.label_idusuario = tk.Label(root, text="ID del Usuario:")
        self.idusuario_entry = tk.Entry(root)
        self.btn_agregar_prestamo = tk.Button(root, text="Agregar Préstamo", command=self.agregar_prestamo)

         # Widgets para eliminar préstamos (inicialmente ocultos)
        self.label_id_prestamo_eliminar = tk.Label(root, text="ID del Préstamo:")
        self.id_prestamo_eliminar_entry = tk.Entry(root)
        self.btn_eliminar_prestamo = tk.Button(root, text="Eliminar Préstamo", command=self.eliminar_prestamo)

        # Widgets para actualizar préstamos (inicialmente ocultos)
        self.label_id_prestamo_actualizar = tk.Label(root, text="ID del Préstamo:")
        self.id_prestamo_actualizar_entry = tk.Entry(root)
        self.label_fecha_prestamo_actualizar = tk.Label(root, text="Nueva Fecha de Préstamo:")
        self.fecha_prestamo_actualizar_entry = tk.Entry(root)
        self.label_fecha_entrega_actualizar = tk.Label(root, text="Nueva Fecha de Entrega:")
        self.fecha_entrega_actualizar_entry = tk.Entry(root)
        self.label_idlibro_actualizar = tk.Label(root, text="Nuevo ID del Libro:")
        self.idlibro_actualizar_entry = tk.Entry(root)
        self.label_idusuario_actualizar = tk.Label(root, text="Nuevo ID del Usuario:")
        self.idusuario_actualizar_entry = tk.Entry(root)
        self.btn_actualizar_prestamo = tk.Button(root, text="Actualizar Préstamo", command=self.actualizar_prestamo)

        # Etiquetas y campos de entrada para roles (inicialmente ocultos)
        self.label_nombre_rol = tk.Label(root, text="Nombre del rol:")
        self.nombre_rol_entry = tk.Entry(root)
        self.btn_agregar_rol = tk.Button(root, text="Agregar Rol", command=self.agregar_rol)

        # Widgets para eliminar roles (inicialmente ocultos)
        self.label_id_rol_eliminar = tk.Label(root, text="ID del Rol:")
        self.id_rol_eliminar_entry = tk.Entry(root)
        self.btn_eliminar_rol = tk.Button(root, text="Eliminar Rol", command=self.eliminar_rol)

        # Widgets para actualizar roles (inicialmente ocultos)
        self.label_id_rol_actualizar = tk.Label(root, text="ID del Rol:")
        self.id_rol_actualizar_entry = tk.Entry(root)
        self.label_nuevo_nombre_rol = tk.Label(root, text="Nuevo Nombre del Rol:")
        self.nuevo_nombre_rol_entry = tk.Entry(root)
        self.btn_actualizar_rol = tk.Button(root, text="Actualizar Rol", command=self.actualizar_rol)

        # Etiquetas y campos de entrada para usuarios (inicialmente ocultos)
        self.label_dni = tk.Label(root, text="DNI del usuario:")
        self.dni_entry = tk.Entry(root)
        self.label_nombres = tk.Label(root, text="Nombres del usuario:")
        self.nombres_entry = tk.Entry(root)
        self.label_apellidos = tk.Label(root, text="Apellidos del usuario:")
        self.apellidos_entry = tk.Entry(root)
        self.label_password = tk.Label(root, text="Password del usuario:")
        self.password_entry = tk.Entry(root, show="*")  # Campo de entrada para password oculto
        self.label_direccion = tk.Label(root, text="Dirección del usuario:")
        self.direccion_entry = tk.Entry(root)
        self.label_celular = tk.Label(root, text="Celular del usuario:")
        self.celular_entry = tk.Entry(root)
        self.label_rol = tk.Label(root, text="Rol del usuario:")
        self.rol_entry = tk.Entry(root)
        self.btn_agregar_usuario = tk.Button(root, text="Agregar Usuario", command=self.agregar_usuario)

         # Widgets para eliminar usuarios (inicialmente ocultos)
        self.label_id_usuario_eliminar = tk.Label(root, text="ID del Usuario:")
        self.id_usuario_eliminar_entry = tk.Entry(root)
        self.btn_eliminar_usuario = tk.Button(root, text="Eliminar Usuario", command=self.eliminar_usuario)

        # Widgets para actualizar usuarios (inicialmente ocultos)
        self.label_id_usuario_actualizar = tk.Label(root, text="ID del Usuario:")
        self.id_usuario_actualizar_entry = tk.Entry(root)
        self.label_dni_usuario_actualizar = tk.Label(root, text="Nuevo DNI:")
        self.dni_usuario_actualizar_entry = tk.Entry(root)
        self.label_nombres_usuario_actualizar = tk.Label(root, text="Nuevos Nombres:")
        self.nombres_usuario_actualizar_entry = tk.Entry(root)
        self.label_apellidos_usuario_actualizar = tk.Label(root, text="Nuevos Apellidos:")
        self.apellidos_usuario_actualizar_entry = tk.Entry(root)
        self.label_password_usuario_actualizar = tk.Label(root, text="Nuevo Password:")
        self.password_usuario_actualizar_entry = tk.Entry(root)
        self.label_direccion_usuario_actualizar = tk.Label(root, text="Nueva Dirección:")
        self.direccion_usuario_actualizar_entry = tk.Entry(root)
        self.label_celular_usuario_actualizar = tk.Label(root, text="Nuevo Celular:")
        self.celular_usuario_actualizar_entry = tk.Entry(root)
        self.label_roles_usuario_actualizar = tk.Label(root, text="Nuevos Roles:")
        self.roles_usuario_actualizar_entry = tk.Entry(root)
        self.btn_actualizar_usuario = tk.Button(root, text="Actualizar Usuario", command=self.actualizar_usuario)
        pass
        
       
         

    def abrir_ventana_buscar_libro(self):
        self.ocultar_widgets()
        # Mostrar los widgets para buscar libro
        self.label_buscar_libro.grid(row=0, column=0, padx=10, pady=10)
        self.buscar_libro_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_buscar_libro.grid(row=1, columnspan=2, padx=10, pady=10)

        

    def buscar_libro(self):
        titulo = self.buscar_libro_entry.get()

        if titulo:
            libros_encontrados = libros.buscar_libro(titulo)

            if libros_encontrados:
                primer_libro = libros_encontrados[0]  # Tomamos el primer libro encontrado

                self.label_titulo_encontrado.config(text=f"Título: {primer_libro[1]}")
                self.label_edicion_encontrada.config(text=f"Edición: {primer_libro[2]}")
                self.label_descripcion_encontrada.config(text=f"Descripción: {primer_libro[3]}")
                # Actualiza otras etiquetas según los atributos del libro

                # Mostrar widgets de información del libro encontrado
                self.label_info_libro.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
                self.label_titulo_encontrado.grid(row=4, column=0, padx=10, pady=5, sticky='w')
                self.label_edicion_encontrada.grid(row=5, column=0, padx=10, pady=5, sticky='w')
                self.label_descripcion_encontrada.grid(row=6, column=0, padx=10, pady=5, sticky='w')
            else:
                messagebox.showinfo("Información", "No se encontraron libros con ese título.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un título para buscar.")

    def limpiar_campos(self):
        self.buscar_libro_entry.delete(0, tk.END)
        self.label_titulo_encontrado.config(text="")
        self.label_edicion_encontrada.config(text="")
        self.label_descripcion_encontrada.config(text="")
        # Limpia otras etiquetas según los atributos del libr



    def abrir_ventana_categoria(self):
        self.ocultar_widgets()
        self.label_nombre_categoria.grid(row=0, column=0, padx=10, pady=10)
        self.nombre_categoria_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_ubicacion.grid(row=1, column=0, padx=10, pady=10)
        self.ubicacion_entry.grid(row=1, column=1, padx=10, pady=10)
        self.btn_agregar_categoria.grid(row=2, columnspan=2, padx=10, pady=10)

    def agregar_categoria(self):
        nombre = self.nombre_categoria_entry.get()
        ubicacion = self.ubicacion_entry.get()

        if nombre and ubicacion:
            if categorias.insertar_categoria(nombre, ubicacion):
                messagebox.showinfo("Éxito", "Categoría agregada correctamente.")
                self.nombre_categoria_entry.delete(0, tk.END)
                self.ubicacion_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar la categoría.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    def crear_text_area(self):
        # Crear el área de texto si aún no existe
        if not self.text_area:
            self.text_area = tk.Text(self.root, height=50, width=100)
            self.text_area.grid(row=10, columnspan=2, padx=10, pady=10)

    def destruir_text_area(self):
        # Destruir el área de texto si existe
        if self.text_area:
            self.text_area.destroy()
            self.text_area = None  # Establecer a None para indicar que no existe

    def ver_categorias(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto
            
            encabezado = "ID\tCategoría\t Ubicación\n"
            self.text_area.insert(tk.END, encabezado)
        #self.text_area.insert(tk.END, "-"*60 + "\n")  # Línea separadora
            # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

            # Obtener las categorías
            cursor.execute('SELECT idcategoria, nombre_categoria, ubicacion FROM Categorias')
            categorias = cursor.fetchall()
            # Cerrar la conexión
            conn.close()
            # Agregar las categorías al área de texto
            if categorias:
                for categoria in categorias:
                    self.text_area.insert(tk.END, f"{categoria[0]}\t {categoria[1]}\t  {categoria[2]}\n")
            else:
                self.text_area.insert(tk.END, "No hay categorías disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener las categorías: {e}")

    def abrir_ventana_eliminar_categoria(self):
        
        self.label_id_categoria.grid(row=0, column=0, padx=10, pady=10)
        self.id_categoria_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_eliminar_categoria.grid(row=1, columnspan=2, padx=10, pady=10)

    def eliminar_categoria(self):
        id_categoria = self.id_categoria_entry.get()

        if id_categoria:
            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar la categoría con ID {id_categoria}?"):
                if categorias.eliminar_categoria(id_categoria):
                    messagebox.showinfo("Éxito", "Categoría eliminada correctamente.")
                    self.actualizar_lista_categorias()
                    self.id_categoria_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar la categoría.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de categoría.")

    def abrir_ventana_actualizar_categoria(self):
        self.ocultar_widgets()
        self.label_id_categoria_actualizar.grid(row=0, column=0, padx=10, pady=10)
        self.id_categoria_actualizar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_nombre_categoria_actualizar.grid(row=1, column=0, padx=10, pady=10)
        self.nombre_categoria_actualizar_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_ubicacion_actualizar.grid(row=2, column=0, padx=10, pady=10)
        self.ubicacion_actualizar_entry.grid(row=2, column=1, padx=10, pady=10)
        self.btn_actualizar_categoria.grid(row=3, columnspan=2, padx=10, pady=10)

    def actualizar_categoria(self):
        id_categoria = self.id_categoria_actualizar_entry.get()
        nuevo_nombre = self.nombre_categoria_actualizar_entry.get()
        nueva_ubicacion = self.ubicacion_actualizar_entry.get()

        if id_categoria and nuevo_nombre and nueva_ubicacion:
            if messagebox.askyesno("Confirmar actualización", f"¿Estás seguro de actualizar la categoría con ID {id_categoria}?"):
                if categorias.actualizar_categoria(id_categoria, nuevo_nombre, nueva_ubicacion):
                    messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
                    self.actualizar_lista_categorias()
                    self.id_categoria_actualizar_entry.delete(0, tk.END)
                    self.nombre_categoria_actualizar_entry.delete(0, tk.END)
                    self.ubicacion_actualizar_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "No se pudo actualizar la categoría.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def abrir_ventana_autor(self):
        self.ocultar_widgets()
        self.label_nombres.grid(row=0, column=0, padx=10, pady=10)
        self.nombres_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_apellidos.grid(row=1, column=0, padx=10, pady=10)
        self.apellidos_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_dni.grid(row=2, column=0, padx=10, pady=10)
        self.dni_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_nacionalidad.grid(row=3, column=0, padx=10, pady=10)
        self.nacionalidad_entry.grid(row=3, column=1, padx=10, pady=10)
        self.btn_agregar_autor.grid(row=4, columnspan=2, padx=10, pady=10)

    def agregar_autor(self):
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        dni = self.dni_entry.get()
        nacionalidad = self.nacionalidad_entry.get()

        if nombres and apellidos and dni and nacionalidad:
            if Autores.insertar_autors(nombres, apellidos, dni, nacionalidad):
                messagebox.showinfo("Éxito", "Autor agregado correctamente.")
                self.nombres_entry.delete(0, tk.END)
                self.apellidos_entry.delete(0, tk.END)
                self.dni_entry.delete(0, tk.END)
                self.nacionalidad_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar el autor.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    def ver_autores(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto
           
            encabezado = "ID\tNombres\tApellidos\tDNI\tNacionalidad\n"
            self.text_area.insert(tk.END, encabezado)

        # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

        # Obtener los autores
            cursor.execute('SELECT idautor, nombres, apellidos, dni, nacionalidad FROM Autoress')
            autores = cursor.fetchall()

        # Cerrar la conexión
            conn.close()

        # Limpiar el área de texto antes de agregar nuevos autores
            self.text_area.delete('3.0', tk.END)

        # Agregar los autores al área de texto
            if autores:
                for autor in autores:
                   self.text_area.insert(tk.END, f"{autor[0]}\t{autor[1]}\t{autor[2]}\t{autor[3]}\t{autor[4]}\n")
            else:
                self.text_area.insert(tk.END, "No hay autores disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener los autores: {e}")

    def abrir_ventana_eliminar_autor(self):
        self.ocultar_widgets()
        self.label_id_autor.grid(row=0, column=0, padx=10, pady=10)
        self.id_autor_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_eliminar_autor.grid(row=1, columnspan=2, padx=10, pady=10)

    def eliminar_autor(self):
        id_autor = self.id_autor_entry.get()

        if id_autor:
            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el autor con ID {id_autor}?"):
                if Autores.eliminar_autor(id_autor):
                    messagebox.showinfo("Éxito", "Autor eliminado correctamente.")
                    self.id_autor_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el autor.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de autor.")

    def abrir_ventana_actualizar_autor(self):
        self.ocultar_widgets()
        self.label_id_autor_actualizar.grid(row=0, column=0, padx=10, pady=10)
        self.id_autor_actualizar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_nombres_autor_actualizar.grid(row=1, column=0, padx=10, pady=10)
        self.nombres_autor_actualizar_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_apellidos_actualizar.grid(row=2, column=0, padx=10, pady=10)
        self.apellidos_actualizar_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_dni_actualizar.grid(row=3, column=0, padx=10, pady=10)
        self.dni_actualizar_entry.grid(row=3, column=1, padx=10, pady=10)
        self.label_nacionalidad_actualizar.grid(row=4, column=0, padx=10, pady=10)
        self.nacionalidad_actualizar_entry.grid(row=4, column=1, padx=10, pady=10)
        self.btn_actualizar_autor.grid(row=5, columnspan=2, padx=10, pady=10)

    def actualizar_autor(self):
        id_autor = self.id_autor_actualizar_entry.get()
        nuevos_nombres = self.nombres_autor_actualizar_entry.get()
        nuevos_apellidos = self.apellidos_actualizar_entry.get()
        nuevo_dni = self.dni_actualizar_entry.get()
        nueva_nacionalidad = self.nacionalidad_actualizar_entry.get()

        if id_autor and nuevos_nombres and nuevos_apellidos and nuevo_dni and nueva_nacionalidad:
            if messagebox.askyesno("Confirmar actualización", f"¿Estás seguro de actualizar el autor con ID {id_autor}?"):
                if Autores.actualizar_autor(id_autor, nuevos_nombres, nuevos_apellidos, nuevo_dni, nueva_nacionalidad):
                    messagebox.showinfo("Éxito", "Autor actualizado correctamente.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el autor.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")


    def abrir_ventana_eliminar_libro(self):
        self.ocultar_widgets()
        self.label_id_libro.grid(row=0, column=0, padx=10, pady=10)
        self.id_libro_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_eliminar_libro.grid(row=1, columnspan=2, padx=10, pady=10)

    def eliminar_libro(self):
        id_libro = self.id_libro_entry.get()

        if id_libro:
            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el libro con ID {id_libro}?"):
                if libros.eliminar_libro(id_libro):
                    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
                    self.id_libro_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el libro.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de libro.")

    def abrir_ventana_actualizar_libro(self):
        self.ocultar_widgets()
        self.label_id_libro_actualizar.grid(row=0, column=0, padx=10, pady=10)
        self.id_libro_actualizar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_titulo_libro_actualizar.grid(row=1, column=0, padx=10, pady=10)
        self.titulo_libro_actualizar_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_edicion_actualizar.grid(row=2, column=0, padx=10, pady=10)
        self.edicion_actualizar_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_descripcion_actualizar.grid(row=3, column=0, padx=10, pady=10)
        self.descripcion_actualizar_entry.grid(row=3, column=1, padx=10, pady=10)
        self.label_categoria_idcategoria_actualizar.grid(row=4, column=0, padx=10, pady=10)
        self.categoria_idcategoria_actualizar_entry.grid(row=4, column=1, padx=10, pady=10)
        self.label_año_actualizar.grid(row=5, column=0, padx=10, pady=10)
        self.año_actualizar_entry.grid(row=5, column=1, padx=10, pady=10)
        self.label_num_paginas_actualizar.grid(row=6, column=0, padx=10, pady=10)
        self.num_paginas_actualizar_entry.grid(row=6, column=1, padx=10, pady=10)
        self.btn_actualizar_libro.grid(row=7, columnspan=2, padx=10, pady=10)

    def actualizar_libro(self):
        id_libro = self.id_libro_actualizar_entry.get()
        nuevo_titulo = self.titulo_libro_actualizar_entry.get()
        nueva_edicion = self.edicion_actualizar_entry.get()
        nueva_descripcion = self.descripcion_actualizar_entry.get()
        nueva_categoria_idcategoria = self.categoria_idcategoria_actualizar_entry.get()
        nuevo_año = self.año_actualizar_entry.get()
        nuevo_num_paginas = self.num_paginas_actualizar_entry.get()

        if id_libro and nuevo_titulo and nueva_edicion and nueva_descripcion and nueva_categoria_idcategoria and nuevo_año and nuevo_num_paginas:
            if messagebox.askyesno("Confirmar actualización", f"¿Estás seguro de actualizar el libro con ID {id_libro}?"):
                if libros.actualizar_libro(id_libro, nuevo_titulo, nueva_edicion, nueva_descripcion, nueva_categoria_idcategoria, nuevo_año, nuevo_num_paginas):
                    messagebox.showinfo("Éxito", "Libro actualizado correctamente.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el libro.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def abrir_ventana_libro(self):
        self.ocultar_widgets()
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10)
        self.titulo_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_edicion.grid(row=1, column=0, padx=10, pady=10)
        self.edicion_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_descripcion.grid(row=2, column=0, padx=10, pady=10)
        self.descripcion_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_categoria_idcategoria.grid(row=3, column=0, padx=10, pady=10)
        self.categoria_idcategoria_entry.grid(row=3, column=1, padx=10, pady=10)
        self.label_año.grid(row=4, column=0, padx=10, pady=10)
        self.año_entry.grid(row=4, column=1, padx=10, pady=10)
        self.label_nunpaginas.grid(row=5, column=0, padx=10, pady=10)
        self.nunpaginas_entry.grid(row=5, column=1, padx=10, pady=10)
        self.btn_agregar_libro.grid(row=6, columnspan=2, padx=10, pady=10)

    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        edicion = self.edicion_entry.get()
        descripcion = self.descripcion_entry.get()
        categoria_idcategoria = self.categoria_idcategoria_entry.get()
        año = self.año_entry.get()
        nunpaginas = self.nunpaginas_entry.get()

        if titulo and edicion and descripcion and categoria_idcategoria and año and nunpaginas:
            if libros.insertar_libro(titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas):
                messagebox.showinfo("Éxito", "Libro agregado correctamente.")
                self.titulo_entry.delete(0, tk.END)
                self.edicion_entry.delete(0, tk.END)
                self.descripcion_entry.delete(0, tk.END)
                self.categoria_idcategoria_entry.delete(0, tk.END)
                self.año_entry.delete(0, tk.END)
                self.nunpaginas_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar el libro.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def abrir_ventana_libro_autor(self):
        self.ocultar_widgets()
        self.label_libros_idlibros.grid(row=0, column=0, padx=10, pady=10)
        self.libros_idlibros_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_autores_idautores.grid(row=1, column=0, padx=10, pady=10)
        self.autores_idautores_entry.grid(row=1, column=1, padx=10, pady=10)
        self.btn_agregar_libro_autor.grid(row=2, columnspan=2, padx=10, pady=10)

    def ver_libros(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto

            encabezado = "ID\tTítulo   \tEdición  \tDescripción  \tCategoría  \tAño  \tNúm.  Páginas\n"
            self.text_area.insert(tk.END, encabezado)

            # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

            # Obtener los libros
            cursor.execute('SELECT idlibros, titulo, edicion, descripcion, categoria_idcategoria, año, nunpaginas FROM Libros')
            libros = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            # Limpiar el área de texto antes de agregar nuevos libros
            self.text_area.delete('3.0', tk.END)

            # Agregar los libros al área de texto
            if libros:
                for libro in libros:
                    self.text_area.insert(tk.END, f"{libro[0]}     \t{libro[1]}    \t{libro[2]}         \t{libro[3]}         \t{libro[4]}          \t{libro[5]}     \t{libro[6]}\n")
            else:
                self.text_area.insert(tk.END, "No hay libros disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener los libros: {e}")

    def agregar_libro_autor(self):
        libros_idlibros = self.libros_idlibros_entry.get()
        autores_idautores = self.autores_idautores_entry.get()

        if libros_idlibros and autores_idautores:
            if Libros_Autores.insertar_libro_autor(libros_idlibros, autores_idautores):
                messagebox.showinfo("Éxito", "Relación Libro-Autor agregada correctamente.")
                self.libros_idlibros_entry.delete(0, tk.END)
                self.autores_idautores_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar la relación Libro-Autor.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    
    def ver_libros_autores(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto

            encabezado = "ID Libro\tID Autor\n"
            self.text_area.insert(tk.END, encabezado)

            # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

            # Obtener las relaciones entre libros y autores
            cursor.execute('SELECT libros_idlibros, autores_idautores FROM Libros_Autores')
            libros_autores = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            # Limpiar el área de texto antes de agregar nuevas relaciones
            self.text_area.delete('3.0', tk.END)

            # Agregar las relaciones al área de texto
            if libros_autores:
                for relacion in libros_autores:
                    self.text_area.insert(tk.END, f"{relacion[0]}\t{relacion[1]}\n")
            else:
                self.text_area.insert(tk.END, "No hay relaciones disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener las relaciones: {e}")


    def abrir_ventana_prestamo(self):
        self.ocultar_widgets()
        self.label_fecha_prestamo.grid(row=0, column=0, padx=10, pady=10)
        self.fecha_prestamo_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_fecha_entrega.grid(row=1, column=0, padx=10, pady=10)
        self.fecha_entrega_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_idlibro.grid(row=2, column=0, padx=10, pady=10)
        self.idlibro_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_idusuario.grid(row=3, column=0, padx=10, pady=10)
        self.idusuario_entry.grid(row=3, column=1, padx=10, pady=10)
        self.btn_agregar_prestamo.grid(row=4, columnspan=2, padx=10, pady=10)

    def agregar_prestamo(self):
        fecha_prestamo = self.fecha_prestamo_entry.get()
        fecha_entrega = self.fecha_entrega_entry.get()
        idlibro = self.idlibro_entry.get()
        idusuario = self.idusuario_entry.get()

        if fecha_prestamo and fecha_entrega and idlibro and idusuario:
            if prestamos.insertar_prestamo(fecha_prestamo, fecha_entrega, idlibro, idusuario):
                messagebox.showinfo("Éxito", "Préstamo agregado correctamente.")
                self.fecha_prestamo_entry.delete(0, tk.END)
                self.fecha_entrega_entry.delete(0, tk.END)
                self.idlibro_entry.delete(0, tk.END)
                self.idusuario_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar el préstamo.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def ver_prestamos(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto

            encabezado = "ID\tFecha Préstamo\tFecha Entrega\tID Libro\tID Usuario\n"
            self.text_area.insert(tk.END, encabezado)

            # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

            # Obtener los préstamos
            cursor.execute('SELECT idprestamos, fecha_prestamo, fecha_entrega, idlibro, idusuario FROM Prestamos')
            prestamos = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            # Limpiar el área de texto antes de agregar nuevos préstamos
            self.text_area.delete('3.0', tk.END)

            # Agregar los préstamos al área de texto
            if prestamos:
                for prestamo in prestamos:
                    self.text_area.insert(tk.END, f"{prestamo[0]}\t{prestamo[1]}\t      {prestamo[2]}\t      {prestamo[3]}\t        {prestamo[4]}\n")
            else:
                self.text_area.insert(tk.END, "No hay préstamos disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener los préstamos: {e}")           

    def abrir_ventana_eliminar_prestamo(self):
        self.ocultar_widgets()
        self.label_id_prestamo_eliminar.grid(row=0, column=0, padx=10, pady=10)
        self.id_prestamo_eliminar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_eliminar_prestamo.grid(row=1, columnspan=2, padx=10, pady=10)

    def eliminar_prestamo(self):
        id_prestamo = self.id_prestamo_eliminar_entry.get()

        if id_prestamo:
            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el préstamo con ID {id_prestamo}?"):
                if prestamos.eliminar_prestamo(id_prestamo):
                    messagebox.showinfo("Éxito", "Préstamo eliminado correctamente.")
                    self.id_prestamo_eliminar_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el préstamo.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de préstamo.")

    def abrir_ventana_actualizar_prestamo(self):
        self.ocultar_widgets()
        self.label_id_prestamo_actualizar.grid(row=0, column=0, padx=10, pady=10)
        self.id_prestamo_actualizar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_fecha_prestamo_actualizar.grid(row=1, column=0, padx=10, pady=10)
        self.fecha_prestamo_actualizar_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_fecha_entrega_actualizar.grid(row=2, column=0, padx=10, pady=10)
        self.fecha_entrega_actualizar_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_idlibro_actualizar.grid(row=3, column=0, padx=10, pady=10)
        self.idlibro_actualizar_entry.grid(row=3, column=1, padx=10, pady=10)
        self.label_idusuario_actualizar.grid(row=4, column=0, padx=10, pady=10)
        self.idusuario_actualizar_entry.grid(row=4, column=1, padx=10, pady=10)
        self.btn_actualizar_prestamo.grid(row=5, columnspan=2, padx=10, pady=10)

    def actualizar_prestamo(self):
        id_prestamo = self.id_prestamo_actualizar_entry.get()
        nueva_fecha_prestamo = self.fecha_prestamo_actualizar_entry.get()
        nueva_fecha_entrega = self.fecha_entrega_actualizar_entry.get()
        nuevo_idlibro = self.idlibro_actualizar_entry.get()
        nuevo_idusuario = self.idusuario_actualizar_entry.get()

        if id_prestamo and nueva_fecha_prestamo and nueva_fecha_entrega and nuevo_idlibro and nuevo_idusuario:
            if messagebox.askyesno("Confirmar actualización", f"¿Estás seguro de actualizar el préstamo con ID {id_prestamo}?"):
                if prestamos.actualizar_prestamo(id_prestamo, nueva_fecha_prestamo, nueva_fecha_entrega, nuevo_idlibro, nuevo_idusuario):
                    messagebox.showinfo("Éxito", "Préstamo actualizado correctamente.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el préstamo.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def abrir_ventana_rol(self):
        self.ocultar_widgets()
        self.label_nombre_rol.grid(row=0, column=0, padx=10, pady=10)
        self.nombre_rol_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_agregar_rol.grid(row=1, columnspan=2, padx=10, pady=10)

    def agregar_rol(self):
        nombre_rol = self.nombre_rol_entry.get()

        if nombre_rol:
            if Roles.insertar_rol(nombre_rol):
                messagebox.showinfo("Éxito", "Rol agregado correctamente.")
                self.nombre_rol_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar el rol.")
        else:
            messagebox.showwarning("Advertencia", "El nombre del rol es obligatorio.")

    def ver_roles(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto

            encabezado = "ID Rol\tNombre del Rol\n"
            self.text_area.insert(tk.END, encabezado)

            # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

            # Obtener los roles
            cursor.execute('SELECT idrol, nombre_rol FROM Roles')
            roles = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            # Limpiar el área de texto antes de agregar nuevos roles
            self.text_area.delete('3.0', tk.END)

            # Agregar los roles al área de texto
            if roles:
                for rol in roles:
                    self.text_area.insert(tk.END, f"{rol[0]}\t{rol[1]}\n")
            else:
                self.text_area.insert(tk.END, "No hay roles disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener los roles: {e}")

    def abrir_ventana_eliminar_rol(self):
        self.ocultar_widgets()
        self.label_id_rol_eliminar.grid(row=0, column=0, padx=10, pady=10)
        self.id_rol_eliminar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_eliminar_rol.grid(row=1, columnspan=2, padx=10, pady=10)

    def eliminar_rol(self):
        id_rol = self.id_rol_eliminar_entry.get()
        if id_rol:
            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el rol con ID {id_rol}?"):
                Roles.eliminar_rol(id_rol)
                self.id_rol_eliminar_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de rol.")

    def abrir_ventana_actualizar_rol(self):
        self.ocultar_widgets()
        self.label_id_rol_actualizar.grid(row=0, column=0, padx=10, pady=10)
        self.id_rol_actualizar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_nuevo_nombre_rol.grid(row=1, column=0, padx=10, pady=10)
        self.nuevo_nombre_rol_entry.grid(row=1, column=1, padx=10, pady=10)
        self.btn_actualizar_rol.grid(row=2, columnspan=2, padx=10, pady=10)

    def actualizar_rol(self):
        id_rol = self.id_rol_actualizar_entry.get()
        nuevo_nombre_rol = self.nuevo_nombre_rol_entry.get()
        if id_rol and nuevo_nombre_rol:
            if messagebox.askyesno("Confirmar actualización", f"¿Estás seguro de actualizar el rol con ID {id_rol}?"):
                Roles.actualizar_rol(id_rol, nuevo_nombre_rol)
                self.id_rol_actualizar_entry.delete(0, tk.END)
                self.nuevo_nombre_rol_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def abrir_ventana_usuario(self):
        self.ocultar_widgets()
        self.label_dni.grid(row=0, column=0, padx=10, pady=10)
        self.dni_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_nombres.grid(row=1, column=0, padx=10, pady=10)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_apellidos.grid(row=2, column=0, padx=10, pady=10)
        self.apellidos_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_password.grid(row=3, column=0, padx=10, pady=10)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)
        self.label_direccion.grid(row=4, column=0, padx=10, pady=10)
        self.direccion_entry.grid(row=4, column=1, padx=10, pady=10)
        self.label_celular.grid(row=5, column=0, padx=10, pady=10)
        self.celular_entry.grid(row=5, column=1, padx=10, pady=10)
        self.label_rol.grid(row=6, column=0, padx=10, pady=10)
        self.rol_entry.grid(row=6, column=1, padx=10, pady=10)
        self.btn_agregar_usuario.grid(row=7, columnspan=2, padx=10, pady=10)

    def agregar_usuario(self):
        dni = self.dni_entry.get()
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        password = self.password_entry.get()
        direccion = self.direccion_entry.get()
        celular = self.celular_entry.get()
        rol = self.rol_entry.get()

        if dni and nombres and apellidos and password and direccion and celular and rol:
            if usuarios.insertar_usuario(dni, nombres, apellidos, password, direccion, celular, rol):
                messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
                self.dni_entry.delete(0, tk.END)
                self.nombres_entry.delete(0, tk.END)
                self.apellidos_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.direccion_entry.delete(0, tk.END)
                self.celular_entry.delete(0, tk.END)
                self.rol_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No se pudo agregar el usuario.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def ver_usuarios(self):
        try:
            self.destruir_text_area()  # Destruir el área de texto actual
            self.crear_text_area()  # Crear un nuevo área de texto

            encabezado = "ID\tDNI\tNombres\tApellidos\tDirección\t    Celular \tRoles\n"
            self.text_area.insert(tk.END, encabezado)

            # Conexión a la base de datos
            conn = sqlite3.connect('ABIBLIOTECA.db')
            cursor = conn.cursor()

            # Obtener los usuarios con sus roles
            
            cursor.execute('SELECT idUsuarios, dni, nombres, apellidos, direccion, celular, roles FROM Usuarios')
            usuarios = cursor.fetchall()

            # Cerrar la conexión
            conn.close()

            # Limpiar el área de texto antes de agregar nuevos usuarios
            self.text_area.delete('3.0', tk.END)

            # Agregar los usuarios al área de texto
            if usuarios:
                for usuario in usuarios:
                    self.text_area.insert(tk.END, f"{usuario[0]}\t{usuario[1]}\t{usuario[2]}\t {usuario[3]}\t  {usuario[4]}\t     {usuario[5]}\t     {usuario[6]}\n")
            else:
                self.text_area.insert(tk.END, "No hay usuarios disponibles.\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener los usuarios: {e}")
    
    def abrir_ventana_eliminar_usuario(self):
        self.ocultar_widgets()
        self.label_id_usuario_eliminar.grid(row=0, column=0, padx=10, pady=10)
        self.id_usuario_eliminar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.btn_eliminar_usuario.grid(row=1, columnspan=2, padx=10, pady=10)

    def eliminar_usuario(self):
        id_usuario = self.id_usuario_eliminar_entry.get()
        if id_usuario:
            if messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el usuario con ID {id_usuario}?"):
                if usuarios.eliminar_usuario(id_usuario):
                    messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                    self.id_usuario_eliminar_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el usuario.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de usuario.")

    def abrir_ventana_actualizar_usuario(self):
        self.ocultar_widgets()
        self.label_id_usuario_actualizar.grid(row=0, column=0, padx=10, pady=10)
        self.id_usuario_actualizar_entry.grid(row=0, column=1, padx=10, pady=10)
        self.label_dni_usuario_actualizar.grid(row=1, column=0, padx=10, pady=10)
        self.dni_usuario_actualizar_entry.grid(row=1, column=1, padx=10, pady=10)
        self.label_nombres_usuario_actualizar.grid(row=2, column=0, padx=10, pady=10)
        self.nombres_usuario_actualizar_entry.grid(row=2, column=1, padx=10, pady=10)
        self.label_apellidos_usuario_actualizar.grid(row=3, column=0, padx=10, pady=10)
        self.apellidos_usuario_actualizar_entry.grid(row=3, column=1, padx=10, pady=10)
        self.label_password_usuario_actualizar.grid(row=4, column=0, padx=10, pady=10)
        self.password_usuario_actualizar_entry.grid(row=4, column=1, padx=10, pady=10)
        self.label_direccion_usuario_actualizar.grid(row=5, column=0, padx=10, pady=10)
        self.direccion_usuario_actualizar_entry.grid(row=5, column=1, padx=10, pady=10)
        self.label_celular_usuario_actualizar.grid(row=6, column=0, padx=10, pady=10)
        self.celular_usuario_actualizar_entry.grid(row=6, column=1, padx=10, pady=10)
        self.label_roles_usuario_actualizar.grid(row=7, column=0, padx=10, pady=10)
        self.roles_usuario_actualizar_entry.grid(row=7, column=1, padx=10, pady=10)
        self.btn_actualizar_usuario.grid(row=8, columnspan=2, padx=10, pady=10)

    def actualizar_usuario(self):
        id_usuario = self.id_usuario_actualizar_entry.get()
        dni = self.dni_usuario_actualizar_entry.get()
        nombres = self.nombres_usuario_actualizar_entry.get()
        apellidos = self.apellidos_usuario_actualizar_entry.get()
        password = self.password_usuario_actualizar_entry.get()
        direccion = self.direccion_usuario_actualizar_entry.get()
        celular = self.celular_usuario_actualizar_entry.get()
        roles = self.roles_usuario_actualizar_entry.get()

        if id_usuario and dni and nombres and apellidos and password and direccion and celular and roles:
            if messagebox.askyesno("Confirmar actualización", f"¿Estás seguro de actualizar el usuario con ID {id_usuario}?"):
                if usuarios.actualizar_usuario(id_usuario, dni, nombres, apellidos, password, direccion, celular, roles):
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el usuario.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    

       
    def abrir_ventana_carnet(self):
        # Lógica para abrir la ventana de carnet universitario
        carnet_universitario_window = tk.Toplevel(self.root)
        CarnetUniversitariosss(carnet_universitario_window)
    

    

    def ocultar_widgets(self):
        '''# Ocultar widgets de información del libro encontrado
        self.label_info_libro.grid_forget()
        self.label_titulo_encontrado.grid_forget()
        self.label_edicion_encontrada.grid_forget()
        self.label_descripcion_encontrada.grid_forget()
        # Ocultar widgets de categorías
        self.label_nombre_categoria.grid_forget()
        self.nombre_categoria_entry.grid_forget()
        self.label_ubicacion.grid_forget()
        self.ubicacion_entry.grid_forget()
        self.btn_agregar_categoria.grid_forget()
        self.text_area.grid(row=3, columnspan=2, padx=10, pady=10)
        '''
        # Ocultar widgets de autores
        self.label_nombres.grid_forget()
        self.nombres_entry.grid_forget()
        self.label_apellidos.grid_forget()
        self.apellidos_entry.grid_forget()
        self.label_dni.grid_forget()
        self.dni_entry.grid_forget()
        self.label_nacionalidad.grid_forget()
        self.nacionalidad_entry.grid_forget()
        self.btn_agregar_autor.grid_forget()

        # Ocultar widgets de libros
        self.label_titulo.grid_forget()
        self.titulo_entry.grid_forget()
        self.label_edicion.grid_forget()
        self.edicion_entry.grid_forget()
        self.label_descripcion.grid_forget()
        self.descripcion_entry.grid_forget()
        self.label_categoria_idcategoria.grid_forget()
        self.categoria_idcategoria_entry.grid_forget()
        self.label_año.grid_forget()
        self.año_entry.grid_forget()
        self.label_nunpaginas.grid_forget()
        self.nunpaginas_entry.grid_forget()
        self.btn_agregar_libro.grid_forget()

        # Ocultar widgets de libros_autores
        self.label_libros_idlibros.grid_forget()
        self.libros_idlibros_entry.grid_forget()
        self.label_autores_idautores.grid_forget()
        self.autores_idautores_entry.grid_forget()
        self.btn_agregar_libro_autor.grid_forget()

        # Ocultar widgets de prestamos
        self.label_fecha_prestamo.grid_forget()
        self.fecha_prestamo_entry.grid_forget()
        self.label_fecha_entrega.grid_forget()
        self.fecha_entrega_entry.grid_forget()
        self.label_idlibro.grid_forget()
        self.idlibro_entry.grid_forget()
        self.label_idusuario.grid_forget()
        self.idusuario_entry.grid_forget()
        self.btn_agregar_prestamo.grid_forget()

         # Ocultar widgets de roles
        self.label_nombre_rol.grid_forget()
        self.nombre_rol_entry.grid_forget()
        self.btn_agregar_rol.grid_forget()
    
        # Ocultar widgets de usuarios
        self.label_dni.grid_forget()
        self.dni_entry.grid_forget()
        self.label_nombres.grid_forget()
        self.nombres_entry.grid_forget()
        self.label_apellidos.grid_forget()
        self.apellidos_entry.grid_forget()
        self.label_password.grid_forget()
        self.password_entry.grid_forget()
        self.label_direccion.grid_forget()
        self.direccion_entry.grid_forget()
        self.label_celular.grid_forget()
        self.celular_entry.grid_forget()
        self.label_rol.grid_forget()
        self.rol_entry.grid_forget()
        self.btn_agregar_usuario.grid_forget()
        
        self.text_area.grid_remove()
      
         # Ocultar widgets relacionados con categorías
        self.label_id_categoria.grid_forget()
        self.id_categoria_entry.grid_forget()
        self.btn_eliminar_categoria.grid_forget()

        self.label_id_categoria_actualizar.grid_forget()
        self.id_categoria_actualizar_entry.grid_forget()
        self.label_nombre_categoria_actualizar.grid_forget()
        self.nombre_categoria_actualizar_entry.grid_forget()
        self.label_ubicacion_actualizar.grid_forget()
        self.ubicacion_actualizar_entry.grid_forget()
        self.btn_actualizar_categoria.grid_forget()

        

        # Ocultar widgets relacionados con autores
        self.label_id_autor.grid_forget()
        self.id_autor_entry.grid_forget()
        self.btn_eliminar_autor.grid_forget()

        self.label_id_libro_actualizar.grid_forget()
        self.id_libro_actualizar_entry.grid_forget()
        self.label_titulo_libro_actualizar.grid_forget()
        self.titulo_libro_actualizar_entry.grid_forget()
        self.label_edicion_actualizar.grid_forget()
        self.edicion_actualizar_entry.grid_forget()
        self.label_descripcion_actualizar.grid_forget()
        self.descripcion_actualizar_entry.grid_forget()
        self.label_categoria_idcategoria_actualizar.grid_forget()
        self.categoria_idcategoria_actualizar_entry.grid_forget()
        self.label_año_actualizar.grid_forget()
        self.año_actualizar_entry.grid_forget()
        self.label_num_paginas_actualizar.grid_forget()
        self.num_paginas_actualizar_entry.grid_forget()
        self.btn_actualizar_libro.grid_forget()



        


        # Ocultar widgets de eliminar libro
        
        self.label_id_libro.grid_forget()
        self.id_libro_entry.grid_forget()
        self.btn_eliminar_libro.grid_forget()
        

        self.label_id_libro_actualizar.grid_forget()
        self.id_libro_actualizar_entry.grid_forget()
        self.label_titulo_libro_actualizar.grid_forget()
        self.titulo_libro_actualizar_entry.grid_forget()
        self.label_edicion_actualizar.grid_forget()
        self.edicion_actualizar_entry.grid_forget()
        self.label_descripcion_actualizar.grid_forget()
        self.descripcion_actualizar_entry.grid_forget()
        self.label_categoria_idcategoria_actualizar.grid_forget()
        self.categoria_idcategoria_actualizar_entry.grid_forget()
        self.label_año_actualizar.grid_forget()
        self.año_actualizar_entry.grid_forget()
        self.label_num_paginas_actualizar.grid_forget()
        self.num_paginas_actualizar_entry.grid_forget()
        self.btn_actualizar_libro.grid_forget()


       

         # Ocultar widgets de eliminar préstamos
        self.label_id_prestamo_eliminar.grid_forget()
        self.id_prestamo_eliminar_entry.grid_forget()
        self.btn_eliminar_prestamo.grid_forget()

        # Ocultar widgets de actualizar préstamos
        self.label_id_prestamo_actualizar.grid_forget()
        self.id_prestamo_actualizar_entry.grid_forget()
        self.label_fecha_prestamo_actualizar.grid_forget()
        self.fecha_prestamo_actualizar_entry.grid_forget()
        self.label_fecha_entrega_actualizar.grid_forget()
        self.fecha_entrega_actualizar_entry.grid_forget()
        self.label_idlibro_actualizar.grid_forget()
        self.idlibro_actualizar_entry.grid_forget()
        self.label_idusuario_actualizar.grid_forget()
        self.idusuario_actualizar_entry.grid_forget()
        self.btn_actualizar_prestamo.grid_forget()
        
         # Ocultar widgets de eliminar roles
        self.label_id_rol_eliminar.grid_forget()
        self.id_rol_eliminar_entry.grid_forget()
        self.btn_eliminar_rol.grid_forget()

        # Ocultar widgets de actualizar roles
        self.label_id_rol_actualizar.grid_forget()
        self.id_rol_actualizar_entry.grid_forget()
        self.label_nuevo_nombre_rol.grid_forget()
        self.nuevo_nombre_rol_entry.grid_forget()
        self.btn_actualizar_rol.grid_forget()
# Ocultar widgets de eliminar usuarios
        self.label_id_usuario_eliminar.grid_forget()
        self.id_usuario_eliminar_entry.grid_forget()
        self.btn_eliminar_usuario.grid_forget()

        # Ocultar widgets de actualizar usuarios
        self.label_id_usuario_actualizar.grid_forget()
        self.id_usuario_actualizar_entry.grid_forget()
        self.label_dni_usuario_actualizar.grid_forget()
        self.dni_usuario_actualizar_entry.grid_forget()
        self.label_nombres_usuario_actualizar.grid_forget()
        self.nombres_usuario_actualizar_entry.grid_forget()
        self.label_apellidos_usuario_actualizar.grid_forget()
        self.apellidos_usuario_actualizar_entry.grid_forget()
        self.label_password_usuario_actualizar.grid_forget()
        self.password_usuario_actualizar_entry.grid_forget()
        self.label_direccion_usuario_actualizar.grid_forget()
        self.direccion_usuario_actualizar_entry.grid_forget()
        self.label_celular_usuario_actualizar.grid_forget()
        self.celular_usuario_actualizar_entry.grid_forget()
        self.label_roles_usuario_actualizar.grid_forget()
        self.roles_usuario_actualizar_entry.grid_forget()
        self.btn_actualizar_usuario.grid_forget()


    def limpiar_campos_libros(self):
        # Limpiar todos los campos de entrada relacionados con libros
        for entry in (self.titulo_entry, self.edicion_entry, self.descripcion_entry, self.categoria_idcategoria_entry,
                      self.año_entry, self.nunpaginas_entry, self.id_libro_entry, self.id_libro_actualizar_entry,
                       self.edicion_actualizar_entry, self.descripcion_actualizar_entry,
                      self.categoria_idcategoria_actualizar_entry, self.año_actualizar_entry):
            entry.delete(0, tk.END)

    def limpiar_campos(self):
        for entry in ( self.apellidos_entry, self.dni_entry, self.nacionalidad_entry,
                      self.id_autor_entry, self.id_autor_actualizar_entry, self.nombres_autor_actualizar_entry,
                      self.apellidos_actualizar_entry, self.dni_actualizar_entry, self.nacionalidad_actualizar_entry):
            entry.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()












