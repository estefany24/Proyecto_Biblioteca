import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from fpdf import FPDF
import sqlite3

class CarnetUniversitariosss:
    def __init__(self, root):
        self.root = root
        self.root.title("Generar Carnet Universitario")
        self.root.geometry("400x500")

        self.label_dni = tk.Label(self.root, text="Ingrese DNI:")
        self.label_dni.pack()

        self.entry_dni = tk.Entry(self.root)
        self.entry_dni.pack()

        self.button_buscar_usuario = tk.Button(self.root, text="Buscar Usuario", command=self.buscar_usuario)
        self.button_buscar_usuario.pack()

        self.label_resultados = tk.Label(self.root, text="")
        self.label_resultados.pack()

        self.archivo_foto = None  # Para almacenar la ruta de la foto seleccionada
        self.label_foto = tk.Label(self.root, text="Foto:")
        self.label_foto.pack()

        self.button_seleccionar_foto = tk.Button(self.root, text="Seleccionar Foto", command=self.seleccionar_foto)
        self.button_seleccionar_foto.pack()

        self.button_generar_carnet = tk.Button(self.root, text="Generar Carnet", command=self.generar_carnet, state=tk.DISABLED)
        self.button_generar_carnet.pack()

    def buscar_usuario(self):
        dni = self.entry_dni.get()

        if not dni:
            messagebox.showerror("Error", "Por favor, ingrese un DNI.")
            return

        usuario = obtener_usuario_por_dni(dni)

        if not usuario:
            messagebox.showerror("Error", "No se encontró un usuario con el DNI especificado.")
            return

        self.mostrar_resultados(usuario)

    def mostrar_resultados(self, usuario):
        self.label_resultados.config(text=f"Nombre: {usuario[2]} {usuario[3]}\n"  # usuario[1] para nombres, usuario[2] para apellidos, etc.
                                      f"DNI: {usuario[1]}\n"
                                      f"Dirección: {usuario[5]}\n"
                                      f"Celular: {usuario[6]}\n"
                                      f"Rol: {usuario[7]}\n")

        self.usuario = usuario  # Guardamos el usuario actual para usarlo al generar el carnet
        self.button_generar_carnet.config(state=tk.NORMAL)

    def seleccionar_foto(self):
        archivo = filedialog.askopenfilename(title="Seleccionar Foto", filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png")])
        if archivo:
            self.archivo_foto = archivo
            self.mostrar_foto()

    def mostrar_foto(self):
        if self.archivo_foto:
            imagen = Image.open(self.archivo_foto)
            imagen = imagen.resize((100, 100), Image.ANTIALIAS)
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.label_foto.config(image=imagen_tk)
            self.label_foto.image = imagen_tk

    def generar_carnet(self):
        if not self.usuario:
            messagebox.showerror("Error", "Primero debe buscar un usuario.")
            return

        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
        if not pdf_path:
            return

        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(200, 10, txt="Universidad Nacional", ln=True, align='C')
            pdf.cell(200, 10, txt="Carnet Universitario", ln=True, align='C')
            pdf.cell(200, 10, txt=f"Nombre: {self.usuario[2]} {self.usuario[3]}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"DNI: {self.usuario[1]}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Dirección: {self.usuario[5]}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Celular: {self.usuario[6]}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Rol: {self.usuario[7]}", ln=True, align='L')

            if self.archivo_foto:
                pdf.image(self.archivo_foto, x=150, y=20, w=40)

            pdf.output(pdf_path)
            messagebox.showinfo("Éxito", f"Carnet generado correctamente: {pdf_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el carnet: {e}")

def obtener_usuario_por_dni(dni):
    try:
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuarios WHERE dni = ?', (dni,))
        usuario = cursor.fetchone()
        conn.close()
        return usuario
    except sqlite3.Error as e:
        print(f"Error al obtener usuario por DNI: {e}")
        return None

# Esta parte del código solo se ejecutará si ejecutamos carnetuniversitario.py directamente
if __name__ == "__main__":
    root = tk.Tk()
    app = CarnetUniversitariosss(root)
    root.mainloop()
