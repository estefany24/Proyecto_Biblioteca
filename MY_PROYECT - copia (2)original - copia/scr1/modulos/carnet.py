import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from fpdf import FPDF

class CarnetUniversitario:
    def __init__(self, root):
        self.root = root
        self.root.title("Carnet Universitario")
        self.root.geometry("400x300")

        # Crear frames
        self.frame_datos = tk.Frame(self.root, bg="white")
        self.frame_datos.pack(fill="both", expand=True)

        self.frame_foto = tk.Frame(self.root, bg="white")
        self.frame_foto.pack(fill="both", expand=True)

        # Crear etiquetas y entradas para datos personales
        self.label_nombre = tk.Label(self.frame_datos, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.frame_datos, width=30)
        self.entry_nombre.pack()

        self.label_apellido = tk.Label(self.frame_datos, text="Apellido:")
        self.label_apellido.pack()
        self.entry_apellido = tk.Entry(self.frame_datos, width=30)
        self.entry_apellido.pack()

        self.label_cedula = tk.Label(self.frame_datos, text="Cédula:")
        self.label_cedula.pack()
        self.entry_cedula = tk.Entry(self.frame_datos, width=30)
        self.entry_cedula.pack()

        # Crear botón para seleccionar foto
        self.button_foto = tk.Button(self.frame_foto, text="Seleccionar Foto", command=self.seleccionar_foto)
        self.button_foto.pack()

        # Crear label para mostrar la foto
        self.label_foto = tk.Label(self.frame_foto, image=None)
        self.label_foto.pack()

        # Crear botón para generar el carnet
        self.button_generar_carnet = tk.Button(self.frame_foto, text="Generar Carnet", command=self.generar_carnet)
        self.button_generar_carnet.pack()

    def seleccionar_foto(self):
        # Abrir diálogo para seleccionar archivo
        archivo = filedialog.askopenfilename(title="Seleccionar Foto", filetypes=[("Imagenes", "*.jpg;*.jpeg;*.png")])

        # Mostrar la foto seleccionada
        if archivo:
            self.archivo_foto = archivo
            imagen = Image.open(archivo)
            imagen_reducida = imagen.resize((100, 100), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen_reducida)
            self.label_foto.config(image=imagen_tk)
            self.label_foto.image = imagen_tk

    def generar_carnet(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        cedula = self.entry_cedula.get()

        if not all([nombre, apellido, cedula, hasattr(self, 'archivo_foto')]):
            messagebox.showerror("Error", "Por favor, complete todos los campos y seleccione una foto.")
            return

        # Crear PDF
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not pdf_path:
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="UNIVERSIDAD NACIONAL DEL ALTIPLANO PUNO", ln=True, align='C')
        pdf.cell(200, 10, txt="Carnet Universitario", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Cédula: {cedula}", ln=True, align='L')

        # Añadir la foto al PDF
        pdf.image(self.archivo_foto, x=10, y=60, w=50, h=50)

        pdf.output(pdf_path)
        messagebox.showinfo("Éxito", f"Carnet guardado como {pdf_path}")

root = tk.Tk()
carnet = CarnetUniversitario(root)
root.mainloop()
