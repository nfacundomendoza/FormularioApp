import tkinter as tk
from tkinter import messagebox

def generar_planilla():
    ventana_generar = tk.Toplevel(root)
    ventana_generar.title("Formulario T Cardiólogico")

    # Sección de Datos Generales
    tk.Label(ventana_generar, text="Motivo de Ingreso/Diagnóstico:").grid(row=0, column=0, sticky="w")
    motivo_ingreso = tk.Entry(ventana_generar, width=40)
    motivo_ingreso.grid(row=0, column=1, pady=5)

    # Sección de Checkboxes
    tk.Label(ventana_generar, text="Síntomas:").grid(row=1, column=0, sticky="w")
    dolor_precordial = tk.Checkbutton(ventana_generar, text="Dolor Precordial")
    dolor_precordial.grid(row=1, column=1, sticky="w")

    disnea = tk.Checkbutton(ventana_generar, text="Disnea")
    disnea.grid(row=2, column=1, sticky="w")

    # Sección de Selects (opciones con un Dropdown)
    tk.Label(ventana_generar, text="TA (Tensión Arterial):").grid(row=3, column=0, sticky="w")
    ta_options = ["Normal", "Alta", "Baja"]
    ta_var = tk.StringVar(ventana_generar)
    ta_var.set(ta_options[0])  # default value
    ta_menu = tk.OptionMenu(ventana_generar, ta_var, *ta_options)
    ta_menu.grid(row=3, column=1)

    # Sección de Radio Buttons (opciones exclusivas)
    tk.Label(ventana_generar, text="¿Emergencia Hipertensiva?").grid(row=4, column=0, sticky="w")
    emergencia_hipertensiva = tk.IntVar()
    tk.Radiobutton(ventana_generar, text="Sí", variable=emergencia_hipertensiva, value=1).grid(row=4, column=1, sticky="w")
    tk.Radiobutton(ventana_generar, text="No", variable=emergencia_hipertensiva, value=0).grid(row=4, column=2, sticky="w")

    # Botón para guardar los datos
    def guardar_datos():
        data = motivo_ingreso.get()
        if data:
            messagebox.showinfo("Planilla Generada", f"Planilla generada con los datos: {data}")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar el motivo de ingreso.")
        ventana_generar.destroy()

    btn_guardar = tk.Button(ventana_generar, text="Guardar Planilla", command=guardar_datos)
    btn_guardar.grid(row=5, column=0, columnspan=2, pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario App")
root.geometry("400x400")

# Crear los botones
btn_generar = tk.Button(root, text="Generar Planilla", width=20, command=generar_planilla)
btn_generar.pack(pady=10)

root.mainloop()
