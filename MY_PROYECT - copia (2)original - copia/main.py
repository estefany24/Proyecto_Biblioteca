import tkinter as tk
from scr1.interfaces.gui_Adm import BibliotecaApp
from scr1.interfaces.gui_Login import VentanaLogin
from scr1.interfaces.gui_Bibli import BibliotecaBibli
from scr1.interfaces.gui_Est import BibliotecaEst

def iniciar_aplicacion():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal temporalmente

    ventana_login = VentanaLogin(root)
    root.wait_window(ventana_login)  # Espera a que se cierre la ventana de inicio de sesin

    if ventana_login.usuario_autenticado:
        rol_seleccionado = ventana_login.rol_verificar
        if rol_seleccionado == 'admin':
            # Abrir la aplicación para el rol de administrador
            root_admin = tk.Toplevel(root)
            admin_app = BibliotecaApp(root_admin)  # Ajusta según la aplicación de administrador
            root_admin.mainloop()
        elif rol_seleccionado =='bibliotecologo':
            #abrir biblioteca para bibliotecologo
            root_bibli = tk.Toplevel(root)
            bibli_app = BibliotecaBibli(root_bibli) # Ajusta según la aplicación de administrador
            root_bibli.mainloop()
        elif rol_seleccionado=='estudiante':
            root_est = tk.Toplevel(root)
            est_app = BibliotecaEst(root_est)  # Ajusta según la aplicación de administrador
            root_est.mainloop()
        else:
            root.destroy()  # Si el inicio de sesin no es exitoso, cierra la aplicacin

if __name__ == "__main__":
    iniciar_aplicacion()
    
    