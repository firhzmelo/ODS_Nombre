def leer_usuario(usuario):
    import os
    from core.classes import User
    lista_archivos = os.listdir()
    if usuario in lista_archivos:
        archivo = open(usuario, "r")
    else:
        return -1

    x = archivo.read().splitlines()
    y = User(x[0], x[1], x[2])
    return y
