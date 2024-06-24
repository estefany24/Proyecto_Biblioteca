import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from scr1.modulos import categorias

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca App")
        self.root.geometry("800x600")

        # Crear el menú principal
        self.menu_principal = tk.Menu(root)
        root.config(menu=self.menu_principal)
<<<<<<< HEAD
        
  


=======
>>>>>>> 5caf6712a4be06cd8dce0b697cd6b8dff6901102

        # Opción del menú Categorías
        self.menu_categorias = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Categorías", menu=self.menu_categorias)
        self.menu_categorias.add_command(label="Agregar Categoría", command=self.abrir_ventana_categoria)
        self.menu_categorias.add_command(label="Ver Categorías", command=self.ver_categorias)
<<<<<<< HEAD
        #self.menu_categorias.add_command(label="Eliminar Categorías", command=self.abrir_ventana_eliminar_categoria)
        #self.menu_categorias.add_command(label="actualizar Categorías", command=self.abrir_ventana_actualizar_categoria)
        #self.menu_categorias.add_command(label="actualizar actegoria",command=self.actualizar_lista_categorias)
        
        # Crear Frame para Treeview y botones
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')

        # Crear Treeview
        self.tree = ttk.Treeview(self.frame, columns=('ID', 'Categoría', 'Ubicación'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Ubicación', text='Ubicación')
        self.tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Scrollbar para Treeview
        self.tree_scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.grid(row=0, column=2, sticky='ns')

        # Crear Canvas para botones de acción
        self.canvas = tk.Canvas(self.frame)
        self.canvas.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

        # Scrollbar para Canvas
        self.canvas_scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.canvas_scroll.set)
        self.canvas_scroll.grid(row=0, column=4, sticky='ns')

        self.frame_buttons = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        self.root.bind('<Configure>', self.on_frame_configure)

        


       

        # Etiquetas y campos de entrada para categorías (inicialmente ocultos)
        self.label_nombre_categoria = tk.Label(root, text="Nombre de la categoría:")
        self.nombre_categoria_entry = tk.Entry(root)
        self.label_ubicacion = tk.Label(root, text="Ubicación de la categoría:")
        self.ubicacion_entry = tk.Entry(root)
        self.btn_agregar_categoria = tk.Button(root, text="Agregar Categoría", command=self.agregar_categoria)
        
                # Etiquetas y campos de entrada para categorías (inicialmente ocultos)
        #self.label_id_categoria = tk.Label(root, text="ID de la categoría:")
        #self.id_categoria_entry = tk.Entry(root)
        #self.btn_eliminar_categoria = tk.Button(root, text="Eliminar Categoría", command=self.eliminar_categoria)

        # Etiquetas y campos de entrada para actualizar categoría (inicialmente ocultos)
        self.label_id_categoria_actualizar = tk.Label(root, text="ID de la categoría:")
        self.id_categoria_actualizar_entry = tk.Entry(root)
        self.label_nombre_categoria_actualizar = tk.Label(root, text="Nuevo nombre de la categoría:")
        self.nombre_categoria_actualizar_entry = tk.Entry(root)
        self.label_ubicacion_actualizar = tk.Label(root, text="Nueva ubicación de la categoría:")
        self.ubicacion_actualizar_entry = tk.Entry(root)
        #self.btn_actualizar_categoria = tk.Button(root, text="Actualizar Categoría", command=self.actualizar_categoria)

        # Área de texto para mostrar las categorías (inicialmente oculta)
        #self.text_area = tk.Text(root, height=20, width=50)
       # self.text_area.grid(row=10, columnspan=2, padx=10, pady=10)
       # self.text_area.grid_remove()  # Ocultar inicialmente
                # Mostrar el encabezado de columnas

       
         

    
=======

        # Crear Frame para Treeview y botones
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Frame superior para buscar y agregar
        self.frame_superior = tk.Frame(self.frame)
        self.frame_superior.grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        # Campo de entrada para búsqueda con ancho mayor
        self.buscar_entry = tk.Entry(self.frame_superior, width=80)  # Establece el ancho deseado aquí
        self.buscar_entry.grid(row=0, column=0, padx=10)

        # Botón de búsqueda
        self.btn_buscar = tk.Button(self.frame_superior, text="Buscar", command=self.buscar_categoria)
        self.btn_buscar.grid(row=0, column=1, padx=10)

        # Botón de agregar
        self.btn_agregar_categoria = tk.Button(self.frame_superior, text="Agregar", command=self.abrir_ventana_categoria)
        self.btn_agregar_categoria.grid(row=0, column=2, padx=10)
        
        # Crear Treeview
        self.tree = ttk.Treeview(self.frame, columns=('ID', 'Categoría', 'Ubicación'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Ubicación', text='Ubicación')
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        # Scrollbar para Treeview
        self.tree_scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.grid(row=1, column=3, sticky='ns')

        # Crear menú contextual
        self.menu_contextual = tk.Menu(self.root, tearoff=0)
        self.menu_contextual.add_command(label="Eliminar", command=self.eliminar_categoria_contextual)
        self.menu_contextual.add_command(label="Actualizar", command=self.abrir_ventana_actualizar_categoria_contextual)
>>>>>>> 5caf6712a4be06cd8dce0b697cd6b8dff6901102

        # Asociar evento de clic derecho al Treeview
        self.tree.bind("<Button-3>", self.mostrar_menu_contextual)

        self.selected_item = None  # Para guardar el elemento seleccionado en el menú contextual
        self.ver_categorias()

    def abrir_ventana_categoria(self):
        # Crear una nueva ventana para agregar categoría
        self.ventana_agregar_categoria = tk.Toplevel(self.root)
        self.ventana_agregar_categoria.title("Agregar Categoría")

        tk.Label(self.ventana_agregar_categoria, text="Nombre de la categoría:").pack(pady=5)
        self.nombre_categoria_entry = tk.Entry(self.ventana_agregar_categoria)
        self.nombre_categoria_entry.pack(pady=5)

        tk.Label(self.ventana_agregar_categoria, text="Ubicación de la categoría:").pack(pady=5)
        self.ubicacion_entry = tk.Entry(self.ventana_agregar_categoria)
        self.ubicacion_entry.pack(pady=5)

        tk.Button(self.ventana_agregar_categoria, text="Agregar", command=self.agregar_categoria).pack(pady=10)

    def agregar_categoria(self):
        nombre = self.nombre_categoria_entry.get()
        ubicacion = self.ubicacion_entry.get()

        if nombre and ubicacion:
            categorias.insertar_categoria(nombre, ubicacion)
            self.ventana_agregar_categoria.destroy()
            self.ver_categorias()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def ver_categorias(self):
        try:
<<<<<<< HEAD
            # Crear el Treeview si aún no existe
            if not hasattr(self, 'tree'):
                self.tree = ttk.Treeview(self.root, columns=('ID', 'Categoría', 'Ubicación', 'Acciones'), show='headings')
                self.tree.heading('ID', text='ID')
                self.tree.heading('Categoría', text='Categoría')
                self.tree.heading('Ubicación', text='Ubicación')
                self.tree.heading('Acciones', text='Acciones')
                self.tree.grid(row=10, columnspan=2, padx=10, pady=10, sticky='nsew')

            # Limpiar las filas existentes en el Treeview
            self.tree.delete(*self.tree.get_children())

=======
            # Limpiar las filas existentes en el Treeview
            self.tree.delete(*self.tree.get_children())

>>>>>>> 5caf6712a4be06cd8dce0b697cd6b8dff6901102
            # Obtener las categorías desde la base de datos
            categorias_data = categorias.obtener_categorias()

            # Agregar las categorías al Treeview
            for categoria in categorias_data:
                id_categoria = categoria[0]
                nombre_categoria = categoria[1]
                ubicacion = categoria[2]
<<<<<<< HEAD
                self.tree.insert('', 'end', values=(id_categoria, nombre_categoria, ubicacion, ''))

                # Añadir botones de acción a cada fila
                eliminar_btn = tk.Button(self.frame_buttons, text='Eliminar', command=lambda id_categoria=id_categoria: self.eliminar_categoria(id_categoria))
                actualizar_btn = tk.Button(self.frame_buttons, text='Actualizar', command=lambda id_categoria=id_categoria: self.abrir_ventana_actualizar_categoria(id_categoria))
                eliminar_btn.grid(row=id_categoria, column=0, padx=5, pady=5)
                actualizar_btn.grid(row=id_categoria, column=1, padx=5, pady=5)

            # Ajustar las columnas al contenido
            for col in ('ID', 'Categoría', 'Ubicación', 'Acciones'):
                self.tree.column(col, width=tk.font.Font().measure(col))
=======
                self.tree.insert('', 'end', values=(id_categoria, nombre_categoria, ubicacion))
>>>>>>> 5caf6712a4be06cd8dce0b697cd6b8dff6901102

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener las categorías: {e}")

<<<<<<< HEAD
    def abrir_ventana_actualizar_categoria(self, id_categoria):
        # Crear una nueva ventana
        self.ventana_actualizar_categoria = tk.Toplevel(self.root)
        self.ventana_actualizar_categoria.title("Actualizar Categoría")
        
        # Obtener la categoría a actualizar
        categoria = categorias.obtener_categoria_por_id(id_categoria)

        # Crear etiquetas y campos de entrada para la nueva ventana
        tk.Label(self.ventana_actualizar_categoria, text="Nuevo nombre de la categoría:").pack()
        nombre_categoria_entry = tk.Entry(self.ventana_actualizar_categoria)
        nombre_categoria_entry.insert(0, categoria[1])  # Mostrar el nombre actual de la categoría
        nombre_categoria_entry.pack()

        tk.Label(self.ventana_actualizar_categoria, text="Nueva ubicación de la categoría:").pack()
        ubicacion_categoria_entry = tk.Entry(self.ventana_actualizar_categoria)
        ubicacion_categoria_entry.insert(0, categoria[2])  # Mostrar la ubicación actual de la categoría
        ubicacion_categoria_entry.pack()

=======
    def mostrar_menu_contextual(self, event):
        # Obtener el elemento sobre el que se hizo clic
        item = self.tree.identify_row(event.y)
        if item:
            self.selected_item = item
            self.menu_contextual.post(event.x_root, event.y_root)

    def eliminar_categoria_contextual(self):
        if self.selected_item:
            id_categoria = self.tree.item(self.selected_item)['values'][0]
            self.eliminar_categoria(id_categoria)

    def abrir_ventana_actualizar_categoria_contextual(self):
        if self.selected_item:
            id_categoria = self.tree.item(self.selected_item)['values'][0]
            self.abrir_ventana_actualizar_categoria(id_categoria)

    def abrir_ventana_actualizar_categoria(self, id_categoria):
        # Crear una nueva ventana
        self.ventana_actualizar_categoria = tk.Toplevel(self.root)
        self.ventana_actualizar_categoria.title("Actualizar Categoría")

        # Obtener la categoría a actualizar
        categoria = categorias.obtener_categoria_por_id(id_categoria)

        # Crear etiquetas y campos de entrada para la nueva ventana
        tk.Label(self.ventana_actualizar_categoria, text="Nuevo nombre de la categoría:").pack()
        nombre_categoria_entry = tk.Entry(self.ventana_actualizar_categoria)
        nombre_categoria_entry.insert(0, categoria[1])  # Mostrar el nombre actual de la categoría
        nombre_categoria_entry.pack()

        tk.Label(self.ventana_actualizar_categoria, text="Nueva ubicación de la categoría:").pack()
        ubicacion_categoria_entry = tk.Entry(self.ventana_actualizar_categoria)
        ubicacion_categoria_entry.insert(0, categoria[2])  # Mostrar la ubicación actual de la categoría
        ubicacion_categoria_entry.pack()

>>>>>>> 5caf6712a4be06cd8dce0b697cd6b8dff6901102
        # Función para actualizar la categoría
        def actualizar():
            nuevo_nombre = nombre_categoria_entry.get()
            nueva_ubicacion = ubicacion_categoria_entry.get()
            if nuevo_nombre and nueva_ubicacion:
                if categorias.actualizar_categoria(id_categoria, nuevo_nombre, nueva_ubicacion):
                    messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
                    self.ventana_actualizar_categoria.destroy()  # Cerrar la ventana después de la actualización
                    self.ver_categorias()  # Actualizar la vista de categorías en la ventana principal
                else:
                    messagebox.showerror("Error", "No se pudo actualizar la categoría.")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        # Botón para actualizar la categoría
        tk.Button(self.ventana_actualizar_categoria, text="Actualizar", command=actualizar).pack()

    def eliminar_categoria(self, id_categoria):
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro que quiere eliminar esta categoría?")
        if confirmar:
            if categorias.eliminar_categoria(id_categoria):
                messagebox.showinfo("Éxito", "Categoría eliminada correctamente.")
                self.ver_categorias()
            else:
                messagebox.showerror("Error", "No se pudo eliminar la categoría.")

<<<<<<< HEAD







    

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
=======
    def buscar_categoria(self):
        query = self.buscar_entry.get()
        if query:
            categorias_data = categorias.buscar_categoria_por_nombre(query)
            self.tree.delete(*self.tree.get_children())
            for categoria in categorias_data:
                id_categoria = categoria[0]
                nombre_categoria = categoria[1]
                ubicacion = categoria[2]
                self.tree.insert('', 'end', values=(id_categoria, nombre_categoria, ubicacion))
        else:
            self.ver_categorias()

>>>>>>> 5caf6712a4be06cd8dce0b697cd6b8dff6901102
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
