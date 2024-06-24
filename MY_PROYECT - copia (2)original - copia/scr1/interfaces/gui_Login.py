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

class VentanaLogin(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.usuario_autenticado = False  # Atributo para verificar si el usuario está autenticado
        self.title("Inicio de Sesión")
        self.geometry("300x300")

        tk.Label(self, text="DNI:").pack(pady=5)
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.contrasena_entry = tk.Entry(self, show="*")
        self.contrasena_entry.pack(pady=5)

        tk.Label(self, text="Rol:").pack(pady=5)
        self.rol_combobox = ttk.Combobox(self)
        self.rol_combobox.pack(pady=5)

        tk.Button(self, text="Iniciar Sesión", command=self.verificar_usuario).pack(pady=20)
        self.cargar_roles()

    def cargar_roles(self):
        # Conectar a la base de datos y obtener los roles
        
        # Actualizar la lista desplegable con los roles obtenidos
        self.rol_combobox['values'] = [rol[1] for rol in Roles.mostrar_roles()]

    def verificar_usuario(self):
        dni = self.usuario_entry.get()
        password = self.contrasena_entry.get()
        rol= self.rol_combobox.get()
        rol2=0
        self.rol_verificar= rol
        if(type(rol)==str):
            if(rol=='estudiante'):
                rol2=1
            elif(rol=='bibliotecologo'):
                rol2=2
            elif(rol=='admin'):
                rol2=3
        if verificar_usuario(dni, password,rol2):  # Usar la función importada para verificar
            self.usuario_autenticado = True
            self.destroy()  # Cierra la ventana de inicio de sesión
        else:
            messagebox.showwarning("Advertencia", "Usuario, contraseña o rol son incorrectos")