# Estructura de los archivos

```
/src
  /app
    main.py         # Ventana principal: menú de navegación
    win_home.py     # Ventana 1 - bienvenida con Label/Button/MessageBox
    win_form.py     # Ventana 2 - formulario con validación y guardado a archivo
    win_list.py     # Ventana 3 - Listbox con CRUD básico
    win_table.py    # Ventana 4 - Treeview que muestra datos de sample.csv
    win_canvas.py   # Ventana 5 - Canvas con dibujos básicos
  /core
    helpers.py      # (opcional) funciones utilitarias compartidas
  /data
    sample.csv      # archivo CSV de ejemplo usado por win_table.py
  /tests            # carpeta reservada para pruebas unitarias
/.vscode
  launch.json       # configuración para ejecutar/depurar desde VS Code
/docs
  04_skeleton_5_ventanas_tkinter_equipo.md  # documentación del equipo
```
Esta estructura refleja modularización: cada ventana está en un archivo independiente, la lógica compartida va en `/core`, los datos en `/data`, y la documentación en `/docs`.

# ⚙️ Pasos que realiza el programa al ejecutarse

1. **Inicio desde `main.py`**

   * Se importa `tkinter` y `ttk` (widgets mejorados).
   * También se importan las funciones `open_win_*` de cada subventana.
   * Se crea la **ventana raíz (`Tk`)** con título y tamaño fijo.
   * Dentro de esta ventana, se coloca un `Frame` con botones que sirven de menú.

2. **Navegación a subventanas**

   * Cada botón del menú principal abre una **nueva ventana (`Toplevel`)** mediante la función `open_win_X`.
   * Ejemplo: el botón *"1) Home / Bienvenida"* llama `open_win_home(root)` → se crea otra ventana con etiquetas y un botón que abre un `messagebox`.

3. **Comportamiento de cada subventana:**

   * **win_home.py** → Muestra texto de bienvenida y un botón que abre un cuadro de diálogo (`messagebox.showinfo`).
   * **win_form.py** → Pide nombre y edad, valida que no estén vacíos, y guarda los datos en un archivo elegido con `filedialog.asksaveasfilename`.
   * **win_list.py** → Muestra una lista (`Listbox`) donde se pueden **agregar, eliminar y limpiar** elementos.
   * **win_table.py** → Usa `ttk.Treeview` para mostrar los datos del archivo CSV `data/sample.csv`. Si no existe, avisa con `messagebox.showwarning`.
   * **win_canvas.py** → Dibuja figuras básicas (rectángulo, óvalo, línea y texto) en un `Canvas`.

4. **Uso de utilidades (`helpers.py`)** *(opcional)*

   * Si se requieren validaciones, manejo de rutas o funciones comunes, se colocan aquí para que no se repita código en las subventanas.

5. **Ejecución del ciclo principal**

   * El `main()` de `main.py` termina con `root.mainloop()`, lo que mantiene viva la aplicación hasta que el usuario cierre todas las ventanas.

6. **Opciones de ejecución**

   * Desde terminal:

     ```bash
     python -m src.app.main
     ```
   * Desde VS Code (con `.vscode/launch.json`): elegir la configuración `"Ejecutar main (src.app.main)"` y presionar ▶ o F5.
