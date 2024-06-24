import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from fpdf import FPDF
from tkinter import messagebox ,ttk,Menu,Entry,Button
from scr1.modulos import categorias
from scr1.modulos import Autores
from scr1.modulos import libros
from scr1.modulos import Libros_Autores
from scr1.modulos import prestamos
from scr1.modulos import Roles  # Importar el módulo de roles
from scr1.modulos import usuarios 
from scr1.modulos.carnetuniversitario import CarnetUniversitariosss

class BibliotecaBibli:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca")
        self.master.geometry("800x600")

        # Crear la barra de menú
        self.crear_menu()
        self.mostrar_prestamos()

    def crear_menu(self):
        menubar = Menu(self.master)
        
        # Menú Prestamos
        prestamos_menu = Menu(menubar, tearoff=0)
        prestamos_menu.add_command(label="Ver prestamos", command=self.mostrar_prestamos)
        prestamos_menu.add_command(label="Ver todo", command=self.mostrar_todos_prestamos)
        menubar.add_cascade(label="Prestamos", menu=prestamos_menu)

        # Menú Libros
        libros_menu = Menu(menubar, tearoff=0)
        libros_menu.add_command(label="Ver libros", command=self.mostrar_libros)
        libros_menu.add_command(label="Ver todo", command=self.mostrar_todos_libros)
        menubar.add_cascade(label="Libros", menu=libros_menu)

        # Menú Categorías
        categorias_menu = Menu(menubar, tearoff=0)
        categorias_menu.add_command(label="Ver Todo", command=self.mostrar_todas_categorias)
        categorias_menu.add_command(label="Ver", command=self.mostrar_categorias)
        menubar.add_cascade(label="Categorías", menu=categorias_menu)

        # Menú Autores
        autores_menu = Menu(menubar, tearoff=0)
        autores_menu.add_command(label="Ver Autores", command=self.mostrar_autores)
        autores_menu.add_command(label="Ver todo", command=self.mostrar_todos_autores)
        menubar.add_cascade(label="Autores", menu=autores_menu)

        self.master.config(menu=menubar)

    def mostrar_prestamos(self):
        self.limpiar_pantalla()
        self.crear_barra_busqueda_prestamos()
        self.crear_area_resultado_prestamo()

    def mostrar_todos_prestamos(self):
        self.limpiar_pantalla()
        self.crear_area_resultado_prestamo()
        self.mostrar_datos_prestamos()

    def mostrar_libros(self):
        self.limpiar_pantalla()
        self.crear_barra_busqueda_libro()
        self.crear_area_resultado_libro()
        self.mostrar_datos_libros()

    def mostrar_todos_libros(self):
        self.limpiar_pantalla()
        self.crear_area_resultado_libro()
        self.mostrar_datos_libros()

    def mostrar_todas_categorias(self):
        self.limpiar_pantalla()
        self.crear_area_categorias()
        self.mostrar_datos_categorias()

    def mostrar_categorias(self):
        self.limpiar_pantalla()
        self.crear_area_categorias()
        categoria_seleccionada = self.categorias_combobox.get()

        categorias_text = ''
        for categoria in categorias.obtener_categorias():
            if categoria[1] == categoria_seleccionada:
                categorias_text += f"ID: {categoria[0]}, Categoria: {categoria[1]}, Ubicacion: {categoria[2]}\n"

        self.categorias_text.delete('1.0', tk.END)
        self.categorias_text.insert(tk.END, categorias_text)

    def mostrar_autores(self):
        self.limpiar_pantalla()
        self.crear_barra_busqueda_autor()
        self.crear_area_resultado_autor()
        self.mostrar_datos_autores()

    def mostrar_todos_autores(self):
        self.limpiar_pantalla()
        self.crear_area_resultado_autor()
        self.mostrar_datos_autores()

    def limpiar_pantalla(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

    def crear_barra_busqueda_prestamos(self):
        search_frame = tk.Frame(self.master)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT, padx=5)
        
        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        
        search_button = ttk.Button(search_frame, text="Buscar", command=self.realizar_busqueda_prestamo)
        search_button.pack(side=tk.LEFT, padx=5)

    def crear_area_resultado_prestamo(self):
        self.resultados_frame = tk.Frame(self.master)
        self.resultados_frame.pack(pady=10)

        self.tree = ttk.Treeview(self.resultados_frame, columns=('ID', 'Usuario', 'Libro', 'Fecha Prestamo', 'Fecha Devolucion'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Usuario', text='Usuario')
        self.tree.heading('Libro', text='Libro')
        self.tree.heading('Fecha Prestamo', text='Fecha Prestamo')
        self.tree.heading('Fecha Devolucion', text='Fecha Devolucion')
        self.tree.pack(fill=tk.BOTH, expand=True)

    def crear_barra_busqueda_libro(self):
        search_frame = tk.Frame(self.master)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT, padx=5)
        
        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        
        search_button = ttk.Button(search_frame, text="Buscar", command=self.realizar_busqueda_libro)
        search_button.pack(side=tk.LEFT, padx=5)


        #Agregamos un nuevo boton para agregar un libro
        boton_agregar= ttk.Button(search_frame,text="Agregar",command=self.agregar_libro)
        boton_agregar.pack(side=tk.LEFT,padx=5)

    def agregar_libro(self):

        libro_window = tk.Toplevel(self.master)
        libro_window.title("Agregar Libro")

        tk.Label(libro_window, text="Título").grid(row=0, column=0)
        tk.Label(libro_window, text="Autor").grid(row=1, column=0)
        tk.Label(libro_window,text="Edicion").grid(row=2,column=0)
        tk.Label(libro_window,text="Descripcion").grid(row=3,column=0)
        tk.Label(libro_window, text="Categoría").grid(row=4, column=0)
        tk.Label(libro_window,text="Año").grid(row=5,column=0)
        tk.Label(libro_window,text="Numero de paginas").grid(row=6,column=0)


        titulo_entry = tk.Entry(libro_window)
        autores = Autores.obtener_autores()
        edicion_entry=tk.Entry(libro_window)
        descripcion_entry=tk.Entry(libro_window)
        catego= categorias.obtener_categorias()
        ano_entry=tk.Entry(libro_window)
        numpaginas_entry=tk.Entry(libro_window)

        autores_var = tk.StringVar(libro_window)
        categorias_var = tk.StringVar(libro_window)

        autores_menu = tk.OptionMenu(libro_window, autores_var, *[f"{autor[0]}" for autor in autores])
        categorias_menu = tk.OptionMenu(libro_window, categorias_var, *[f"{categori[0]}" for categori in catego])

        titulo_entry.grid(row=0, column=1)
        autores_menu.grid(row=1, column=1)
        edicion_entry.grid(row=2,column=1)
        descripcion_entry.grid(row=3,column=1)
        categorias_menu.grid(row=4, column=1)
        ano_entry.grid(row=5,column=1)
        numpaginas_entry.grid(row=6,column=1)

        save_button = ttk.Button(libro_window, text="Guardar", command=lambda: self.guardar_libro(titulo_entry, autores_var, edicion_entry, descripcion_entry, categorias_var, ano_entry, numpaginas_entry))
        save_button.grid(row=7, column=0, columnspan=2, pady=10)

    def guardar_libro(self, titulo_entry, autores_var, edicion_entry, descripcion_entry, categorias_var, ano_entry, numpaginas_entry):
        # Obtener los valores de los campos de entrada
        titulo = titulo_entry.get()
        autor = autores_var.get()
        edicion = edicion_entry.get()
        descripcion = descripcion_entry.get()
        categoria = categorias_var.get()
        ano = ano_entry.get()
        numpaginas = numpaginas_entry.get()

        # Verificar que todos los campos estén llenos
        if not (titulo and autor and edicion and descripcion and categoria and ano and numpaginas):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        # Guardar el libro en la base de datos
        resultado = libros.insertar_libro(titulo, autor, edicion, descripcion, categoria, ano, numpaginas)
        
        if resultado:
            messagebox.showinfo("Éxito", "Libro agregado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo agregar el libro")

    def crear_area_resultado_libro(self):
        self.resultados_frame = tk.Frame(self.master)
        self.resultados_frame.pack(pady=10)

        self.tree = ttk.Treeview(self.resultados_frame, columns=('ID', 'Titulo', 'Autor', 'Genero', 'Año'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Titulo', text='Titulo')
        self.tree.heading('Autor', text='Autor')
        self.tree.heading('Genero', text='Genero')
        self.tree.heading('Año', text='Año')
        self.tree.pack(fill=tk.BOTH, expand=True)

    def crear_barra_busqueda_autor(self):
        search_frame = tk.Frame(self.master)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT, padx=5)

        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        search_button = ttk.Button(search_frame, text="Buscar", command=self.realizar_busqueda_autor)
        search_button.pack(side=tk.LEFT, padx=5)

    def crear_area_resultado_autor(self):
        self.resultados_frame = tk.Frame(self.master)
        self.resultados_frame.pack(pady=10)

        self.tree = ttk.Treeview(self.resultados_frame, columns=('ID', 'Nombre', 'Nacionalidad'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Nacionalidad', text='Nacionalidad')
        self.tree.pack(fill=tk.BOTH, expand=True)

    def crear_area_categorias(self):
        categorias_frame = tk.Frame(self.master)
        categorias_frame.pack(pady=10)

        tk.Label(categorias_frame, text="Categorías:").pack(side=tk.LEFT, padx=5)

        # Obtener las categorías desde la base de datos
        categorias_list = [categoria[1] for categoria in categorias.obtener_categorias()]
        
        # Crear el Combobox para las categorías
        self.categorias_combobox = ttk.Combobox(categorias_frame, values=categorias_list, width=40)
        self.categorias_combobox.pack(side=tk.LEFT, padx=5)
        self.categorias_combobox.current(0)  # Seleccionar el primer elemento por defecto

        # Botón para actualizar resultados al seleccionar una categoría
        ver_button = ttk.Button(categorias_frame, text="Ver", command=self.mostrar_categorias)
        ver_button.pack(side=tk.LEFT, padx=5)

        # Crear el área de texto para mostrar las categorías
        self.categorias_text = tk.Text(self.master, height=10, width=80)
        self.categorias_text.pack(pady=10)

    def mostrar_datos_prestamos(self):
        resultados = prestamos.obtener_prestamos()
        for row in self.tree.get_children():
            self.tree.delete(row)

        for resultado in resultados:
            self.tree.insert('', tk.END, values=resultado)

    def mostrar_datos_libros(self):
        resultados = libros.obtener_libros()
        #for row in self.tree.get_children():
            #self.tree.delete(row)

        for resultado in resultados:
            self.tree.insert('', tk.END, values=resultado)

    def mostrar_datos_autores(self):
        resultados = Autores.obtener_autores()
        for row in self.tree.get_children():
            self.tree.delete(row)

        for resultado in resultados:
            self.tree.insert('', tk.END, values=resultado)

    def mostrar_datos_categorias(self):
        categorias_text = ''
        for categoria in categorias.obtener_categorias():
            categorias_text += f"ID: {categoria[0]}, Categoria: {categoria[1]}, Ubicacion: {categoria[2]}\n"

        self.categorias_text.delete('1.0', tk.END)
        self.categorias_text.insert(tk.END, categorias_text)

    def realizar_busqueda_libro(self):
        termino_busqueda = self.search_entry.get()
        if not termino_busqueda:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un término de búsqueda")
            return

        resultados = libros.buscar_libro(termino_busqueda)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for resultado in resultados:
            self.tree.insert('', tk.END, values=resultado)
    
    def realizar_busqueda_prestamo(self):
        idusu = self.search_entry.get()
        if not idusu:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un término de búsqueda")
            return

        resultados = prestamos.buscar_prestamos(idusu)
        for row in self.tree.get_children():
            self.tree.delete(row)
 
        for resultado in resultados:
            self.tree.insert('', tk.END, values=resultado)

    def realizar_busqueda_autor(self):
        termino_busqueda = self.search_entry.get()
        if not termino_busqueda:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un término de búsqueda")
            return

        resultados = Autores.buscar_autores(termino_busqueda)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for resultado in resultados:
            self.tree.insert('', tk.END, values=resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaBibli(root)
    root.mainloop()
