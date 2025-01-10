import os
from flask import Flask, flash, json, render_template, redirect, request, url_for
from forms.formulario_cardiologico import FormularioCardiologico  # Importa el formulario


app = Flask(__name__)
app.secret_key = 'secretkey'  # Clave secreta necesaria para las sesiones de Flask-WTF

def crear_carpetas():
    # Ruta para la carpeta principal y las subcarpetas
    carpeta_principal = 'saved_forms'
    subcarpeta_cardiologico = os.path.join(carpeta_principal, 'formularios_cardiologicos')
    subcarpeta_politraumatizado = os.path.join(carpeta_principal, 'formularios_politraumatizados')
    
    # Verificar si la carpeta principal existe, si no la crea
    if not os.path.exists(carpeta_principal):
        os.makedirs(carpeta_principal)
        print(f"Carpeta creada: {carpeta_principal}")
    
    # Verificar si la subcarpeta de cardiología existe, si no la crea
    if not os.path.exists(subcarpeta_cardiologico):
        os.makedirs(subcarpeta_cardiologico)
        print(f"Subcarpeta creada: {subcarpeta_cardiologico}")
    
    # Verificar si la subcarpeta de politraumatizado existe, si no la crea
    if not os.path.exists(subcarpeta_politraumatizado):
        os.makedirs(subcarpeta_politraumatizado)
        print(f"Subcarpeta creada: {subcarpeta_politraumatizado}")


# Llamar a la función de creación de carpetas al iniciar la aplicación
crear_carpetas()

@app.route('/')
def home():
    """
    Ruta principal de la aplicación.
    Renderiza la página de inicio.
    """
    return render_template('index.html')

@app.route('/generar_planilla')
def generar_planilla():
    """
    Ruta para generar una nueva planilla.
    Renderiza la página de selección de guía (Cardiológico o Politraumatizado).
    """
    return render_template('seleccionar_guia.html')

@app.route('/guia_t_cardiologico', methods=['GET', 'POST'])
def guia_t_cardiologico():
    """
    Ruta para mostrar el formulario de la guía T Cardiológica.
    Si el formulario es enviado y válido, guarda los datos en un archivo JSON.
    """
    form = FormularioCardiologico()

    if form.validate_on_submit():  # Si el formulario se envía y es válido
        try:
            # Crear un diccionario con los datos del formulario
            formulario_data = {
                'nombre_paciente': form.nombre_paciente.data,
                'motivo_ingreso_diag': form.motivo_ingreso_diag.data,
                'dolor_precordial': form.dolor_precordial.data,
                'scaest': form.scaest.data,
                'scacest': form.scacest.data,
                'insuficiencia_cardiaca': form.insuficiencia_cardiaca.data,
                'pericarditis': form.pericarditis.data,
                'emergencia_hipertensiva': form.emergencia_hipertensiva.data,
                'sincop': form.sincop.data,
                'shock': form.shock.data,
                'tep': form.tep.data,
                'arritmia': form.arritmia.data,
                'antecedentes': form.antecedentes.data,
                'disnea': form.disnea.data,
                'dolor_precordial_tipico': form.dolor_precordial_tipico.data,
                'hta': form.hta.data,
                'mareos': form.mareos.data,
                'palpitaciones': form.palpitaciones.data,
                'taquicardia': form.taquicardia.data,
                'bradicardia': form.bradicardia.data,
                'hipotension_shock': form.hipotension_shock.data,
                'cianosis': form.cianosis.data,
                'respiratorio': form.respiratorio.data,
                'mecanica_ventilatoria': form.mecanica_ventilatoria.data,
                'buena_entrada_aire': form.buena_entrada_aire.data,
                'hipoventilacion_der': form.hipoventilacion_der.data,
                'hipoventilacion_izq': form.hipoventilacion_izq.data,
                'roncus': form.roncus.data,
                'sibilancias': form.sibilancias.data,
                'rales': form.rales.data,
                'arm': form.arm.data,
                'ta': form.ta.data,
                'tam': form.tam.data,
                'pvc': form.pvc.data,
                'fc': form.fc.data,
                'relleno_capilar': form.relleno_capilar.data,
                'soplos': form.soplos.data,
                'ingurgitacion_yugular': form.ingurgitacion_yugular.data,
                'edemas': form.edemas.data,
                'pulsos_regulares': form.pulsos_regulares.data,
                'pulsos_irregulares': form.pulsos_irregulares.data,
                'fallo_bomba': form.fallo_bomba.data,
                'killip_kimball': form.killip_kimball.data,
                'derrame_pericardico': form.derrame_pericardico.data,
                'aceptable_perf_periferica': form.aceptable_perf_periferica.data,
                'shock2': form.shock2.data,
                'inotropicos': form.inotropicos.data,
                'abdomen': form.abdomen.data,
                'rha': form.rha.data,
                'diuresis': form.diuresis.data,
                'sonda_vesical': form.sonda_vesical.data,
                'bajo_sedoanalgesia': form.bajo_sedoanalgesia.data,
                'glasgow': form.glasgow.data,
                'pupilas': form.pupilas.data,
                'foco_motor': form.foco_motor.data,
                'enzimas': form.enzimas.data,
                'rx_torax': form.rx_torax.data,
                'ecg': form.ecg.data,
                'ecocardiograma': form.ecocardiograma.data
            }

            # Crear el nombre del archivo
            filename = f"{form.nombre_paciente.data.replace(' ', '_').lower()}_cardiologico.json"
            filepath = os.path.join('saved_forms/formularios_cardiologicos', filename)

            # Guardar los datos en un archivo JSON
            with open(filepath, 'w') as json_file:
                json.dump(formulario_data, json_file, indent=4)

            # Mensaje de éxito
            flash('Formulario guardado correctamente.', 'success')

        except Exception as e:
            # Si ocurre algún error, mostrar el mensaje de error
            flash(f'Error al guardar el formulario: {str(e)}', 'danger')

        # Redirigir después de guardar el formulario
        return redirect(url_for('guia_t_cardiologico'))

    # Si el formulario no es válido o es un GET
    return render_template('formulario_cardiologico.html', form=form)

@app.route('/guia_t_politraumatizado')
def guia_t_politraumatizado():
    """
    Ruta para mostrar el formulario de la guía T Politraumatizado.
    Aún no implementado.
    """
    # Lógica para 'GUIA T POLITRAUMATIZADO'
    return "Formulario GUIA T POLITRAUMATIZADO"

@app.route('/seleccionar_planilla', methods=['GET', 'POST'])
def seleccionar_planilla():
    tipo_planilla = ""
    archivos = []
    buscar_nombre = ""

    if request.method == 'POST':
        tipo_planilla = request.form.get('tipo_planilla')
        buscar_nombre = request.form.get('buscar_nombre', '').lower()  # Convertir a minúsculas para una búsqueda insensible a mayúsculas
        
        # Asegurarse de que el tipo tiene la "s" al final"
        tipo_planilla = tipo_planilla + 's'

        # Verificar que los valores coincidan con las carpetas correctas
        if tipo_planilla == 'cardiologicos':
            folder_path = 'saved_forms/formularios_cardiologicos'  # Cambié esto para que sea 'formularios_cardiologicos'
        elif tipo_planilla == 'politraumatizados':
            folder_path = 'saved_forms/formularios_politraumatizados'  # Asegurando que coincida con la carpeta de politraumatizados
        else:
            tipo_planilla = None

        # Listar los archivos en la carpeta seleccionada
        if tipo_planilla:
            try:
                archivos = [f for f in os.listdir(folder_path) if f.endswith('.json')]

                # Filtrar archivos por nombre, si se especifica un término de búsqueda
                if buscar_nombre:
                    archivos = [f for f in archivos if buscar_nombre in f.lower()]

            except FileNotFoundError:
                archivos = []  # Si no se encuentran archivos, la lista estará vacía

    return render_template('seleccionar_planilla.html', tipo_planilla=tipo_planilla, archivos=archivos, buscar_nombre=buscar_nombre)



@app.route('/ver_detalle_planilla/<tipo>/<archivo>', methods=['GET'])
def ver_detalle_planilla(tipo, archivo):
    """
    Ruta para ver los detalles de una planilla guardada.
    Dependiendo del tipo de planilla (Cardiológico o Politraumatizado), se renderiza una plantilla específica.
    """
    # Asegurarse de que el tipo tiene la "s" al final si es "cardiologico"
    tipo = tipo + 's' if tipo == 'cardiologico' else tipo

    # Construir la ruta completa al archivo usando os.path.join()
    folder_path = os.path.join('saved_forms', f'formularios_{tipo}')
    file_path = os.path.join(folder_path, archivo)  # Ruta completa
    
    print(f"Ruta del archivo: {file_path}")  # Imprimir la ruta para depurar

    try:
        # Intentamos abrir el archivo y cargarlo como JSON
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}"

    # Dependiendo del tipo de planilla, renderizamos una plantilla diferente
    if tipo == 'cardiologicos':
        return render_template('detalle_cardiologico.html', planilla=planilla_data)
    elif tipo == 'politraumatizados':
        return render_template('detalle_politraumatizado.html', planilla=planilla_data)
    else:
        return "Tipo de planilla no válido"




if __name__ == '__main__':
    app.run(debug=True)
