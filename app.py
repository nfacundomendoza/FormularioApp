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
                'scasest': form.scasest.data,  
                'scacest': form.scacest.data,
                'insuficiencia_cardiaca_descompensada': form.insuficiencia_cardiaca_descompensada.data,  
                'pericarditis': form.pericarditis.data,
                'emergencia_hipertensiva': form.emergencia_hipertensiva.data,
                'sincope': form.sincope.data,  
                'shock': form.shock.data,
                'tep': form.tep.data,
                'arritmia': form.arritmia.data,
                'antecedentes': form.antecedentes.data,
                'enfermedad_actual': form.enfermedad_actual.data,
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
                'buena_entrada_aire_bilateral': form.buena_entrada_aire_bilateral.data,  
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
                'aceptable_perf_periferica': form.aceptable_perfusion_periferica.data, 
                'shock_2': form.shock_2.data,  
                'inotropicos': form.inotropicos.data,
                'abdomen': form.abdomen.data,
                'blando_depresible_indoloro': form.blando_depresible_indoloro.data,
                'rha': form.rha.data,
                'diuresis': form.diuresis.data,
                'sonda_vesical': form.sonda_vesical.data,
                'bajo_sedoanalgesia': form.bajo_sedoanalgesia.data,
                'glasgow': form.glasgow.data,
                'pupilas': form.pupilas.data,
                'foco_motor': form.foco_motor.data,
                'laboratorio': form.laboratorio.data,
                'ecg': form.ecg.data,
                'ecocardiograma': form.ecocardiograma.data
            }

            # Crear el nombre del archivo y asegurarse de que no tenga caracteres inválidos
            filename = f"{form.nombre_paciente.data.replace(' ', '_').lower()}.json"
            directory = 'saved_forms/formularios_cardiologicos'
            if not os.path.exists(directory):
                os.makedirs(directory)  # Crear el directorio si no existe

            filepath = os.path.join(directory, filename)

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
        buscar_nombre = request.form.get('buscar_nombre', '').lower() 
      

        # Verificar que los valores coincidan con las carpetas correctas
        if tipo_planilla == 'cardiologico':
            folder_path = 'saved_forms/formularios_cardiologicos'  
        elif tipo_planilla == 'politraumatizado':
            folder_path = 'saved_forms/formularios_politraumatizados' 
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


@app.route('/detalle_cardiologico/<archivo>', methods=['GET'])
def detalle_cardiologico(archivo):
    """
    Ruta para ver los detalles de una planilla cardiológica guardada.
    """
    # Construir la ruta completa al archivo usando os.path.join()
    folder_path = 'saved_forms/formularios_cardiologicos'
    file_path = os.path.join(folder_path, archivo)  # Ruta completa
    
    print(f"Ruta del archivo: {file_path}")  # Imprimir la ruta para depurar

    try:
        # Intentamos abrir el archivo y cargarlo como JSON
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

    # Renderizamos la plantilla específica para cardiológico
    return render_template('detalle_cardiologico.html', planilla=planilla_data, archivo=archivo)

@app.route('/detalle_politraumatizado/<archivo>', methods=['GET'])
def detalle_politraumatizado(archivo):
    """
    Ruta para ver los detalles de una planilla politraumatizado guardada.
    """
    # Construir la ruta completa al archivo usando os.path.join()
    folder_path = 'saved_forms/formularios_politraumatizados'
    file_path = os.path.join(folder_path, archivo)  # Ruta completa
    
    print(f"Ruta del archivo: {file_path}")  # Imprimir la ruta para depurar

    try:
        # Intentamos abrir el archivo y cargarlo como JSON
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

    # Renderizamos la plantilla específica para politraumatizado
    return render_template('detalle_politraumatizado.html', planilla=planilla_data, archivo=archivo)

@app.route('/editar_cardiologico/<archivo>', methods=['GET', 'POST'])
def editar_cardiologico(archivo):
    """
    Ruta para editar un formulario cardiológico existente.
    Los datos se cargan desde un archivo JSON y se usan para inicializar el formulario.
    """
    folder_path = os.path.join('saved_forms', 'formularios_cardiologicos')
    file_path = os.path.join(folder_path, archivo)

    print(f"URL accedida: {request.url}")
    print(f"Path del archivo: {file_path}")

    try:
        # Cargar los datos del archivo JSON
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

    # Crear el formulario e inicializarlo con los datos cargados
    form = FormularioCardiologico(data=planilla_data)

    if form.validate_on_submit():  # Si el formulario es enviado y válido
        try:
            # Crear un diccionario con los datos del formulario
            formulario_data = {
                'nombre_paciente': form.nombre_paciente.data,
                'motivo_ingreso_diag': form.motivo_ingreso_diag.data,
                'dolor_precordial': form.dolor_precordial.data,
                'scasest': form.scasest.data,
                'scacest': form.scacest.data,
                'insuficiencia_cardiaca_descompensada': form.insuficiencia_cardiaca_descompensada.data,
                'pericarditis': form.pericarditis.data,
                'emergencia_hipertensiva': form.emergencia_hipertensiva.data,
                'sincope': form.sincope.data,
                'shock': form.shock.data,
                'tep': form.tep.data,
                'arritmia': form.arritmia.data,
                'antecedentes': form.antecedentes.data,
                'enfermedad_actual': form.enfermedad_actual.data,
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
                'buena_entrada_aire_bilateral': form.buena_entrada_aire_bilateral.data,
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
                'shock_2': form.shock_2.data,
                'inotropicos': form.inotropicos.data,
                'abdomen': form.abdomen.data,
                'blando_depresible_indoloro': form.blando_depresible_indoloro.data,
                'rha': form.rha.data,
                'diuresis': form.diuresis.data,
                'sonda_vesical': form.sonda_vesical.data,
                'bajo_sedoanalgesia': form.bajo_sedoanalgesia.data,
                'glasgow': form.glasgow.data,
                'pupilas': form.pupilas.data,
                'foco_motor': form.foco_motor.data,
                'laboratorio': form.laboratorio.data,
                'ecg': form.ecg.data,
                'ecocardiograma': form.ecocardiograma.data
            }

            # Guardar los datos actualizados en el archivo JSON
            with open(file_path, 'w') as file:
                json.dump(formulario_data, file, indent=4)

            # Mensaje de éxito
            flash('Formulario actualizado correctamente.', 'success')

        except Exception as e:
            flash(f'Error al guardar el formulario: {str(e)}', 'danger')

        # Redirigir después de guardar el formulario
        return redirect(url_for('detalle_cardiologico', archivo=archivo))

    # Si el formulario no es válido o es un GET
    return render_template('editar_cardiologico.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)
