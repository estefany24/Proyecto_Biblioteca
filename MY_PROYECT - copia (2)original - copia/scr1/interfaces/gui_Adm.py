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

        # Opción del menú Categorías
        self.menu_categorias = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Categorías", menu=self.menu_categorias)
        self.menu_categorias.add_command(label="Agregar Categoría", command=self.abrir_ventana_categoria)
        self.menu_categorias.add_command(label="Ver Categorías", command=self.ver_categorias)

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

    def ver_categorias(self):
        try:
            # Limpiar las filas existentes en el Treeview
            self.tree.delete(*self.tree.get_children())

            # Obtener las categorías desde la base de datos
            categorias_data = categorias.obtener_categorias()

            # Agregar las categorías al Treeview
            for categoria in categorias_data:
                id_categoria = categoria[0]
                nombre_categoria = categoria[1]
                ubicacion = categoria[2]
                self.tree.insert('', 'end', values=(id_categoria, nombre_categoria, ubicacion))

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener las categorías: {e}")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
