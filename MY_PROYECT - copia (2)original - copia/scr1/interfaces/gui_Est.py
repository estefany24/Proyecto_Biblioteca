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

class BibliotecaEst:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca - Estudiante")
        self.master.geometry("400x300")
        tk.Label(self.master, text="Bienvenido Estudiante").pack(pady=20)