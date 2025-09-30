import tkinter as tk
from tkinter import ttk
from leer_usuario import leer_usuario

def emergente(titulo, mensaje, elim):
    global win
    win = tk.Toplevel(root)
    win.title(titulo)
    win.geometry("150x150")

    tk.Label(win, text=mensaje).pack()
    if elim:
        tk.Button(win, text="Ok", command=lambda: root.destroy()).pack()
    else:
        tk.Button(win, text="Ok", command=lambda: win.destroy()).pack()

def has_cuenta(usuario, nombre, clave, clave2):
    import os

    if usuario.strip() == "" or nombre.strip() == "" or clave == "" or clave2 == "":
        emergente("Datos vacios","Hay campos vacios,\nrellena e intenta de nuevo", 0)
    elif clave != clave2:
        emergente("Contraseña no coincide","La contraseña no coincide,\n intente de nuevo", 0)
    elif leer_usuario(usuario) != -1:
        emergente("Usuario repetido","El usuario ya existe", 0)
    else:
        archivo = open(usuario, "w")
        archivo.write(usuario + '\n')
        archivo.write(nombre + '\n')
        archivo.write(clave)
        archivo.close()
        emergente("Registro exitoso", "El registro se conlcuyo\n de forma exitosa", 1)
        

def crea_cuenta(logIn):
    global root
    root = tk.Toplevel(logIn)
    root.title("Crea tu cuenta")
    root.geometry("350x350")

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Crea una cuenta", font=("Segoe UI",16, "bold")).pack(pady = 10)

    usuario = tk.StringVar()
    nombre = tk.StringVar()
    clave = tk.StringVar()
    clave2 = tk.StringVar()

    ttk.Label(frame, text="Usuario").pack(fill='x')
    ttk.Entry(frame, textvariable=usuario).pack(fill='x')
    ttk.Label(frame, text="Nombre").pack(fill='x')
    ttk.Entry(frame, textvariable=nombre).pack(fill="x")
    ttk.Label(frame, text="Contraseña").pack(fill='x')
    ttk.Entry(frame, textvariable=clave, show='*').pack(fill='x')
    ttk.Label(frame, text="Repite Contraseña").pack(fill='x')
    ttk.Entry(frame, textvariable=clave2, show='*').pack(fill='x')

    ttk.Button(frame, text="Crear", command=lambda: has_cuenta(usuario.get(), nombre.get(), clave.get(), clave2.get())).pack()
    root.mainloop()