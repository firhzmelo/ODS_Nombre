import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_data():
    """
    Conecta con la API de Open-Meteo y obtiene temperaturas horarias
    de León, Gto (últimas 24 horas).
    Devuelve dos listas: horas y temperaturas.
    """
    try:
        url = (
           "https://api.open-meteo.com/v1/forecast?latitude=59.9127&longitude=10.7461&hourly=precipitation_probability&timezone=auto&forecast_days=1" 
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        fecha_hora = data["hourly"]["time"]
        horas = []
        for h in fecha_hora:
            horas.append(h[-5:])
        precipitation_prob = data["hourly"]["precipitation_probability"]

        return horas, precipitation_prob
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\\n{e}")
        return [], []


def create_line_chart(horas, prob):
    """Gráfica de línea."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(horas, prob, linestyle="-", marker="o", markersize=3)
    ax.set_title("Probabilidad de precipitación en Oslo (línea)")
    ax.set_xlabel("Hora")
    ax.set_ylabel("%")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def create_bar_chart(horas, prob):
    """Gráfica de barras."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(horas, prob)
    ax.set_title("Probabilidad de precipitación en Oslo (barras)")
    ax.set_xlabel("Hora")
    ax.set_ylabel("%")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig

def create_disp_chart(horas, prob):
    """Gráfica de barras."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.scatter(horas, prob)
    ax.set_title("Probabilidad de precipitación en Oslo (barras)")
    ax.set_xlabel("Hora")
    ax.set_ylabel("%")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig

def mostrar_graficas(frm, horas, temps):
    """Inserta las tres gráficas en el frame de la ventana tkinter."""
    # Línea
    fig1 = create_line_chart(horas, temps)
    canvas1 = FigureCanvasTkAgg(fig1, master=frm)
    canvas1.draw()
    canvas1.get_tk_widget().pack(pady=10, fill="x")

    # Barras
    fig2 = create_bar_chart(horas, temps)
    canvas2 = FigureCanvasTkAgg(fig2, master=frm)
    canvas2.draw()
    canvas2.get_tk_widget().pack(pady=10, fill="x")

    # Dispersión
    fig3 = create_disp_chart(horas, temps)
    canvas3 = FigureCanvasTkAgg(fig3, master=frm)
    canvas3.draw()
    canvas3.get_tk_widget().pack(pady=10, fill="x")
    


def open_win_canvas(parent: tk.Tk):
    """
    Crea la ventana secundaria con gráficas de la API.
    """
    win = tk.Toplevel(parent)
    win.title("Canvas con API (Open-Meteo) y gráficas")
    win.geometry("960x1000")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    # Botón para cargar datos y graficar
    def cargar():
        horas, temps = fetch_data()
        if horas and temps:
            mostrar_graficas(frm, horas, temps)

    ttk.Button(frm, text="Cargar y mostrar gráficas", command=cargar).pack(pady=10)


# Para pruebas independientes (opcional)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()