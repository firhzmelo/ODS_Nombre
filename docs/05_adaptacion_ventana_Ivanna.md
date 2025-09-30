# Avances applicación 
## Win_Talleres
Se cambiaron los botones de texto para poder mandar al usuario a una página de internet que le de más información o un tutoríal para hacer diferentes acciónes por el clima. El ususario también puede elegir en caso de que no quiera hacer actividades vistuales hemos puesto un link directo a la página del municipio donde pueden consultar más información para ir dentro de la ciudad, se planea revisar si se puede agregar otro tipo de set de tips 


<img width="491" height="386" alt="image" src="https://github.com/user-attachments/assets/f9ec486a-6b38-4e49-85e0-8db20f72b872" />


# Código 

´´´
#Importación de librerias 
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Home / Bienvenida")
    win.geometry("400x300")
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text="Talleres", font=("Segoe UI", 11, "bold")).pack(pady=(0, 8))
    ttk.Button(frm, text="Tutorial huerto vertical",
               command=lambda:webbrowser.open("https://www.youtube.com/watch?v=IEX7D8wxkm4")).pack()
    ttk.Button(frm, text="Taller de composta",
               command=lambda:webbrowser.open("https://educacion.mma.gob.cl/educacion-ambiental-en-tu-casa/compostaje/")).pack()
    ttk.Button(frm, text="Tutorial papel reciclado",
               command=lambda:webbrowser.open("https://youtu.be/kjkry2AkcPQ?si=dt_3K-GP22iAtmzg")).pack()
    ttk.Button(frm, text="Talleres precenciales en León, Guanajuato",
               command=lambda:webbrowser.open("https://www.leon.gob.mx/medioambiente/articulo.php?a=312")).pack()
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8)

´´´
