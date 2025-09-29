# Ventana Home/Menú Principal
La ventana de Home va a servir de referencia a nuestros usuarios para navegar entre las diferentes funcionalidades de la aplicación. Incluye los botones que van a redirigir a los apartados de "Metas", "Progreso", "Talleres" y "Tips", así como un mensaje de bienvenida personalizado que se mostrará como "Hola, [nombre]".

<img width="423" height="343" alt="image" src="https://github.com/user-attachments/assets/4ee4564f-2d80-4919-8d63-0fc20b3c65ba" />

Lista de cambios aplicados a la ventana:
- Se modificó el título por el mensaje de bienvenida personalizado.
- Se añadieron más botones con la finalidad de poder redirigir al usuario a las ventanas de las funcionalidades.

Estos cambios son la base para que la experiencia del usuario dentro de la app sea la más cómoda y entendible posible. También es importante ya que representa la primera interacción que tiene el usuario con las funcionalidades que ofrece la app y, por consiguiente, con el objetivo del ODS 13.

#Código

import tkinter as tk
from tkinter import ttk, messagebox

def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Home / Bienvenida")
    win.geometry("360x220")
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)
    ttk.Label(frm, text="'Hola, ___________'", font=("Segoe UI", 11, "bold")).pack(pady=(0, 8))
    ttk.Button(frm, text="Metas",
               command=lambda: messagebox.showinfo("Info", "¡Equipo listo!")).pack()
    ttk.Button(frm, text="Progreso",
               command=lambda: messagebox.showinfo("Info", "¡Equipo listo!")).pack()
    ttk.Button(frm, text="Talleres",
               command=lambda: messagebox.showinfo("Info", "¡Equipo listo!")).pack()
    ttk.Button(frm, text="Tips",
               command=lambda: messagebox.showinfo("Info", "¡Equipo listo!")).pack()
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack()
