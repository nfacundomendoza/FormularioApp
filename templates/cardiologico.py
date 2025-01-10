import tkinter as tk
from utils.json_utils import guardar_formulario, cargar_formulario

def generar_cardiologico(ventana_padre):
    # Cargar los datos guardados si existen, o usar datos vacíos
    datos = cargar_formulario()
    if datos is None:
        datos = {
            "nombre_paciente": "",
            "motivo_ingreso": "",
            "diagnostico": "",
            "sintomas": {},
            "examen_fisico": {},
            "laboratorio": {}
        }

    # Crear la ventana del formulario
    ventana = tk.Toplevel(ventana_padre)
    ventana.title("Formulario Cardiológico")

    # Título con el nombre del paciente
    tk.Label(ventana, text="Nombre del Paciente:").grid(row=0, column=0, sticky="w")
    nombre_paciente = tk.Entry(ventana, width=40)
    nombre_paciente.insert(0, datos["nombre_paciente"])
    nombre_paciente.grid(row=0, column=1, pady=5)

    # Motivo de Ingreso/Diagnóstico
    tk.Label(ventana, text="Motivo de Ingreso/Diagnóstico:").grid(row=1, column=0, sticky="w")
    motivo_ingreso = tk.Entry(ventana, width=40)
    motivo_ingreso.insert(0, datos["motivo_ingreso"])
    motivo_ingreso.grid(row=1, column=1, pady=5)

    # Checkboxes de síntomas
    tk.Label(ventana, text="Síntomas:").grid(row=2, column=0, sticky="w")
    dolor_precordial = tk.Checkbutton(ventana, text="Dolor Precordial")
    dolor_precordial.grid(row=2, column=1, sticky="w")
    if datos["sintomas"].get("dolor_precordial", False):
        dolor_precordial.select()

    # Más síntomas (puedes agregar más checkboxes aquí de acuerdo a tu necesidad)
    # Ejemplo: SCASEST, SCACEST, Insuficiencia Cardíaca Descompensada, etc.
    scase = tk.Checkbutton(ventana, text="SCASEST")
    scase.grid(row=3, column=1, sticky="w")
    if datos["sintomas"].get("scase", False):
        scase.select()

    # Guardar los datos
    def guardar_datos():
        datos["nombre_paciente"] = nombre_paciente.get()
        datos["motivo_ingreso"] = motivo_ingreso.get()
        # Guardar todos los checkboxes y demás campos aquí
        guardar_formulario(datos)
        ventana.destroy()

    # Botón para guardar
    btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
    btn_guardar.grid(row=10, column=0, columnspan=2, pady=10)

    # Botón para volver
    btn_volver = tk.Button(ventana, text="Volver", command=ventana.destroy)
    btn_volver.grid(row=11, column=0, columnspan=2, pady=10)
