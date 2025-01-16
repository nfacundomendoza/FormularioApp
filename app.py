from datetime import datetime, time
from math import ceil
import os
from flask import Flask, flash, json, render_template, redirect, request, url_for
from forms.formulario_cardiologico import FormularioCardiologico 
from forms.formulario_politraumatizado import FormularioPolitraumatizado

app = Flask(__name__)
app.secret_key = 'secretkey'

def crear_carpetas():
    """
    Función para crear las carpetas necesarias para guardar los formularios.
    """

    carpeta_principal = 'saved_forms'
    subcarpeta_cardiologico = os.path.join(carpeta_principal, 'formularios_cardiologicos')
    subcarpeta_politraumatizado = os.path.join(carpeta_principal, 'formularios_politraumatizados')
    
    if not os.path.exists(carpeta_principal):
        os.makedirs(carpeta_principal)
        print(f"Carpeta creada: {carpeta_principal}")
    
    if not os.path.exists(subcarpeta_cardiologico):
        os.makedirs(subcarpeta_cardiologico)
        print(f"Subcarpeta creada: {subcarpeta_cardiologico}")
    
    if not os.path.exists(subcarpeta_politraumatizado):
        os.makedirs(subcarpeta_politraumatizado)
        print(f"Subcarpeta creada: {subcarpeta_politraumatizado}")

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
   
    if form.validate_on_submit():  
        try:
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
                'examen_fisico': form.examen_fisico.data,
                'signos_vitales': form.signos_vitales.data,
                'respiratorio': form.respiratorio.data,
                'mecanica_ventilatoria': form.mecanica_ventilatoria.data,
                'buena_entrada_aire_bilateral': form.buena_entrada_aire_bilateral.data,  
                'hipoventilacion_der': form.hipoventilacion_der.data,
                'hipoventilacion_izq': form.hipoventilacion_izq.data,
                'roncus': form.roncus.data,
                'sibilancias': form.sibilancias.data,
                'rales': form.rales.data,
                'arm': form.arm.data,
                'cardiovascular': form.cardiovascular.data,
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
                'aceptable_perfusion_periferica': form.aceptable_perfusion_periferica.data, 
                'shock_2': form.shock_2.data,  
                'inotropicos': form.inotropicos.data,
                'abdomen': form.abdomen.data,
                'blando_depresible_indoloro': form.blando_depresible_indoloro.data,
                'rha': form.rha.data,
                'diuresis': form.diuresis.data,
                'sonda_vesical': form.sonda_vesical.data,
                'neurologico': form.neurologico.data,
                'bajo_sedoanalgesia': form.bajo_sedoanalgesia.data,
                'glasgow': form.glasgow.data,
                'pupilas': form.pupilas.data,
                'foco_motor': form.foco_motor.data,
                'laboratorio': form.laboratorio.data,
                'ecg': form.ecg.data,
                'ecocardiograma': form.ecocardiograma.data
            }

            filename = f"{form.nombre_paciente.data.replace(' ', '_').lower()}.json"
            directory = 'saved_forms/formularios_cardiologicos'
            if not os.path.exists(directory):
                os.makedirs(directory)  

            filepath = os.path.join(directory, filename)

            with open(filepath, 'w') as json_file:
                json.dump(formulario_data, json_file, indent=4)

            flash('Formulario guardado correctamente.', 'success')

        except Exception as e:
            flash(f'Error al guardar el formulario: {str(e)}', 'danger')

        return redirect(url_for('detalle_cardiologico', archivo=filename))

    return render_template('formulario_cardiologico.html', form=form)

@app.route('/guia_t_politraumatizado', methods=['GET', 'POST'])
def guia_t_politraumatizado():
    """
    Ruta para mostrar el formulario de la guía T Politraumatizado.
    Aún no implementado.
    """
    form = FormularioPolitraumatizado()

    if form.validate_on_submit(): 
        try:
            formulario_data = {
            'nombre_paciente': form.nombre_paciente.data,
            'sexo': form.sexo.data,
            'fecha_evento': form.fecha_evento.data.strftime('%d/%m/%Y'),
            'hora': form.hora.data.strftime('%H:%M') if form.hora.data else '',
            'tipo_evento': form.tipo_evento.data,
            'estado_general': form.estado_general.data,
            'temperatura': form.temperatura.data,
            'palidez': form.palidez.data,
            'cianosis': form.cianosis.data,
            'edemas': form.edemas.data,
            'lesiones_piel_partes_blandas': form.lesiones_piel_partes_blandas.data,
            'respiratorio': form.respiratorio.data,
            'trauma_torax_cerrado': form.trauma_torax_cerrado.data,
            'fracturas_costales': form.fracturas_costales.data,
            'contusiones': form.contusiones.data,
            'arm': form.arm.data,
            'sato2': form.sato2.data,
            'pafi': form.pafi.data,
            'buena_entrada_aire_bilateral': form.buena_entrada_aire_bilateral.data,
            'fr': form.fr.data,
            'hipoventilacion_derecha': form.hipoventilacion_derecha.data,
            'hipoventilacion_izquierda': form.hipoventilacion_izquierda.data,
            'neumotorax': form.neumotorax.data,
            'hemotorax': form.hemotorax.data,
            'tap': form.tap.data,
            'circulatorio': form.circulatorio.data,
            'ta': form.ta.data,
            'tam': form.tam.data,
            'pvc': form.pvc.data,
            'fc': form.fc.data,
            'relleno_capilar': form.relleno_capilar.data,
            'hemorragia_externa_activa': form.hemorragia_externa_activa.data,
            'sospecha_hemorragia_interna': form.sospecha_hemorragia_interna.data,
            'fallo_de_bomba': form.fallo_de_bomba.data,
            'derrame_pericardico': form.derrame_pericardico.data,
            'aceptable_perfusion_periferica': form.aceptable_perfusion_periferica.data,
            'shock': form.shock.data,
            'inotropicos': form.inotropicos.data,
            'requerimiento_de_transfusion': form.requerimiento_de_transfusion.data,
            'abdomen': form.abdomen.data,
            'trauma_abdominal_cerrado': form.trauma_abdominal_cerrado.data,
            'trauma_abdominal_abierto': form.trauma_abdominal_abierto.data,
            'blando_depresible_indoloro': form.blando_depresible_indoloro.data,
            'rha': form.rha.data,
            'distendido': form.distendido.data,
            'sng': form.sng.data,
            'alim_enteral': form.alim_enteral.data,
            'intervencion_quirurgica': form.intervencion_quirurgica.data,
            'detalle_intervencion': form.detalle_intervencion.data,
            'drenajes': form.drenajes.data,
            'diuresis': form.diuresis.data,
            'sonda_vesical': form.sonda_vesical.data,
            'funcion_neurologica': form.funcion_neurologica.data,
            'tec': form.tec.data,
            'trauma_columna': form.trauma_columna.data,
            'bajo_sedanalgesia': form.bajo_sedanalgesia.data,
            'glasgow': form.glasgow.data,
            'pupilas': form.pupilas.data,
            'foco_motor': form.foco_motor.data,
            'pic': form.pic.data,
            'collar_cervical': form.collar_cervical.data,
            'inmovilizacion_tabla': form.inmovilizacion_tabla.data,
            'lesion_traumatologica': form.lesion_traumatologica.data,
            'rts': form.rts.data,
            'imagenes': form.imagenes.data,
            'laboratorio': form.laboratorio.data,
            'interconsultas': form.interconsultas.data,
            'pronostico': form.pronostico.data,
            'apache_ii': form.apache_ii.data,
            'sofa': form.sofa.data
        }

            filename = f"{form.nombre_paciente.data.replace(' ', '_').lower()}.json"
            directory = 'saved_forms/formularios_politraumatizados'
            if not os.path.exists(directory):
                os.makedirs(directory)  

            filepath = os.path.join(directory, filename)

            with open(filepath, 'w') as json_file:
                json.dump(formulario_data, json_file, indent=4)

            flash('Formulario guardado correctamente.', 'success')

        except Exception as e:
            flash(f'Error al guardar el formulario: {str(e)}', 'danger')

        return redirect(url_for('detalle_politraumatizado', archivo=filename))

    return render_template('formulario_politraumatizado.html', form=form)

@app.route('/seleccionar_planilla', methods=['GET', 'POST'])
def seleccionar_planilla():
    tipo_planilla = request.args.get('tipo_planilla', '') 
    archivos = [] 
    buscar_nombre = request.args.get('buscar_nombre', '').lower()  
    page = int(request.args.get('page', 1))  # Página actual
    per_page = 10  # Archivos por página

    if request.method == 'POST':
        tipo_planilla = request.form.get('tipo_planilla')
        buscar_nombre = request.form.get('buscar_nombre', '').lower() 

    if tipo_planilla:
        if tipo_planilla == 'cardiologico':
            folder_path = 'saved_forms/formularios_cardiologicos'  
        elif tipo_planilla == 'politraumatizado':
            folder_path = 'saved_forms/formularios_politraumatizados' 
        else:
            tipo_planilla = None

        if tipo_planilla:
            try:
                archivos = [f for f in os.listdir(folder_path) if f.endswith('.json')]
                if buscar_nombre:
                    archivos = [f for f in archivos if buscar_nombre in f.lower()]
                archivos = sorted(archivos, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)
            except FileNotFoundError:
                archivos = [] 

    # Paginación
    total_archivos = len(archivos)
    total_paginas = ceil(total_archivos / per_page)
    archivos_paginados = archivos[(page - 1) * per_page : page * per_page]

    return render_template(
        'seleccionar_planilla.html', 
        tipo_planilla=tipo_planilla, 
        archivos=archivos_paginados, 
        buscar_nombre=buscar_nombre,
        page=page,
        total_paginas=total_paginas
    )
@app.route('/eliminar_archivo/<archivo>/<tipo_planilla>', methods=['POST'])
def eliminar_archivo(archivo, tipo_planilla):
    """ 
    Ruta para eliminar un archivo JSON de una planilla guardada.
    """
    if tipo_planilla == 'cardiologico':
        carpeta = 'saved_forms/formularios_cardiologicos'
    elif tipo_planilla == 'politraumatizado':
        carpeta = 'saved_forms/formularios_politraumatizados'
    else:
        flash('Tipo de planilla no válido.', 'danger')
        return redirect(url_for('home'))

    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta, archivo)

    # Verificar si el archivo existe y eliminarlo
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
        flash(f'Planilla {archivo} eliminada correctamente.', 'success')
    else:
        flash(f'El archivo {archivo} no se encuentra en la carpeta {carpeta}.', 'danger')

    return redirect(url_for('seleccionar_planilla',tipo_planilla=tipo_planilla))


@app.route('/detalle_cardiologico/<archivo>', methods=['GET'])
def detalle_cardiologico(archivo):
    """
    Ruta para ver los detalles de una planilla cardiológica guardada.
    """
    folder_path = 'saved_forms/formularios_cardiologicos'
    file_path = os.path.join(folder_path, archivo)  
    try:
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

    return render_template('detalle_cardiologico.html', planilla=planilla_data, archivo=archivo)

@app.route('/detalle_politraumatizado/<archivo>', methods=['GET'])
def detalle_politraumatizado(archivo):
    """
    Ruta para ver los detalles de una planilla politraumatizado guardada.
    """
    folder_path = 'saved_forms/formularios_politraumatizados'
    file_path = os.path.join(folder_path, archivo)  
    
    try:
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

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
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

    form = FormularioCardiologico(data=planilla_data)

    if form.validate_on_submit():  
        try:
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
                'examen_fisico': form.examen_fisico.data,
                'signos_vitales': form.signos_vitales.data,
                'respiratorio': form.respiratorio.data,
                'mecanica_ventilatoria': form.mecanica_ventilatoria.data,
                'buena_entrada_aire_bilateral': form.buena_entrada_aire_bilateral.data,
                'hipoventilacion_der': form.hipoventilacion_der.data,
                'hipoventilacion_izq': form.hipoventilacion_izq.data,
                'roncus': form.roncus.data,
                'sibilancias': form.sibilancias.data,
                'rales': form.rales.data,
                'arm': form.arm.data,
                'cardiovascular': form.cardiovascular.data,
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
                'aceptable_perfusion_periferica': form.aceptable_perfusion_periferica.data,
                'shock_2': form.shock_2.data,
                'inotropicos': form.inotropicos.data,
                'abdomen': form.abdomen.data,
                'blando_depresible_indoloro': form.blando_depresible_indoloro.data,
                'rha': form.rha.data,
                'diuresis': form.diuresis.data,
                'sonda_vesical': form.sonda_vesical.data,
                'neurologico': form.neurologico.data,
                'bajo_sedoanalgesia': form.bajo_sedoanalgesia.data,
                'glasgow': form.glasgow.data,
                'pupilas': form.pupilas.data,
                'foco_motor': form.foco_motor.data,
                'laboratorio': form.laboratorio.data,
                'ecg': form.ecg.data,
                'ecocardiograma': form.ecocardiograma.data
            }

            with open(file_path, 'w') as file:
                json.dump(formulario_data, file, indent=4)

            flash('Formulario actualizado correctamente.', 'success')

        except Exception as e:
            flash(f'Error al guardar el formulario: {str(e)}', 'danger')

        return redirect(url_for('detalle_cardiologico', archivo=archivo))

    return render_template('editar_cardiologico.html', form=form, archivo=archivo)


@app.route('/editar_politraumatizado/<archivo>', methods=['GET', 'POST'])
def editar_politraumatizado(archivo):
    """
    Ruta para editar un formulario cardiológico existente.
    Los datos se cargan desde un archivo JSON y se usan para inicializar el formulario.
    """
    folder_path = os.path.join('saved_forms', 'formularios_politraumatizados')
    file_path = os.path.join(folder_path, archivo)

    print(f"URL accedida: {request.url}")
    print(f"Path del archivo: {file_path}")

    try:
        with open(file_path, 'r') as file:
            planilla_data = json.load(file)
    except Exception as e:
        return f"Error al cargar el archivo: {e}", 500

    try:
        fecha_evento_str = planilla_data.get("fecha_evento")
        planilla_data["fecha_evento"] = datetime.strptime(fecha_evento_str, "%d/%m/%Y")
    except Exception as e:
        return f"Error al procesar fecha_evento u hora: {e}", 500

    except Exception as e:
        return f"Error al procesar fecha_evento u hora: {e}", 500
      
    hora_str = planilla_data.get("hora")
    if hora_str:
        try:
            hour, minute = map(int, hora_str.split(":"))
            planilla_data["hora"] = time(hour, minute)
        except ValueError:
            planilla_data["hora"] = None
    else:
        planilla_data["hora"] = None
    
    form = FormularioPolitraumatizado(data=planilla_data)

    if form.validate_on_submit():  
        try:
            formulario_data = {
                'nombre_paciente': form.nombre_paciente.data,
            'sexo': form.sexo.data,
            'fecha_evento': form.fecha_evento.data.strftime('%d/%m/%Y'),
            'hora': form.hora.data.strftime('%H:%M') if form.hora.data else '',
            'tipo_evento': form.tipo_evento.data,
            'estado_general': form.estado_general.data,
            'temperatura': form.temperatura.data,
            'palidez': form.palidez.data,
            'cianosis': form.cianosis.data,
            'edemas': form.edemas.data,
            'lesiones_piel_partes_blandas': form.lesiones_piel_partes_blandas.data,
            'respiratorio': form.respiratorio.data,
            'trauma_torax_cerrado': form.trauma_torax_cerrado.data,
            'fracturas_costales': form.fracturas_costales.data,
            'contusiones': form.contusiones.data,
            'arm': form.arm.data,
            'sato2': form.sato2.data,
            'pafi': form.pafi.data,
            'buena_entrada_aire_bilateral': form.buena_entrada_aire_bilateral.data,
            'fr': form.fr.data,
            'hipoventilacion_derecha': form.hipoventilacion_derecha.data,
            'hipoventilacion_izquierda': form.hipoventilacion_izquierda.data,
            'neumotorax': form.neumotorax.data,
            'hemotorax': form.hemotorax.data,
            'tap': form.tap.data,
            'circulatorio': form.circulatorio.data,
            'ta': form.ta.data,
            'tam': form.tam.data,
            'pvc': form.pvc.data,
            'fc': form.fc.data,
            'relleno_capilar': form.relleno_capilar.data,
            'hemorragia_externa_activa': form.hemorragia_externa_activa.data,
            'sospecha_hemorragia_interna': form.sospecha_hemorragia_interna.data,
            'fallo_de_bomba': form.fallo_de_bomba.data,
            'derrame_pericardico': form.derrame_pericardico.data,
            'aceptable_perfusion_periferica': form.aceptable_perfusion_periferica.data,
            'shock': form.shock.data,
            'inotropicos': form.inotropicos.data,
            'requerimiento_de_transfusion': form.requerimiento_de_transfusion.data,
            'abdomen': form.abdomen.data,
            'trauma_abdominal_cerrado': form.trauma_abdominal_cerrado.data,
            'trauma_abdominal_abierto': form.trauma_abdominal_abierto.data,
            'blando_depresible_indoloro': form.blando_depresible_indoloro.data,
            'rha': form.rha.data,
            'distendido': form.distendido.data,
            'sng': form.sng.data,
            'alim_enteral': form.alim_enteral.data,
            'intervencion_quirurgica': form.intervencion_quirurgica.data,
            'detalle_intervencion': form.detalle_intervencion.data,
            'drenajes': form.drenajes.data,
            'diuresis': form.diuresis.data,
            'sonda_vesical': form.sonda_vesical.data,
            'funcion_neurologica': form.funcion_neurologica.data,
            'tec': form.tec.data,
            'trauma_columna': form.trauma_columna.data,
            'bajo_sedanalgesia': form.bajo_sedanalgesia.data,
            'glasgow': form.glasgow.data,
            'pupilas': form.pupilas.data,
            'foco_motor': form.foco_motor.data,
            'pic': form.pic.data,
            'collar_cervical': form.collar_cervical.data,
            'inmovilizacion_tabla': form.inmovilizacion_tabla.data,
            'lesion_traumatologica': form.lesion_traumatologica.data,
            'rts': form.rts.data,
            'imagenes': form.imagenes.data,
            'laboratorio': form.laboratorio.data,
            'interconsultas': form.interconsultas.data,
            'pronostico': form.pronostico.data,
            'apache_ii': form.apache_ii.data,
            'sofa': form.sofa.data
            }

            with open(file_path, 'w') as file:
                json.dump(formulario_data, file, indent=4)

            flash('Formulario actualizado correctamente.', 'success')

        except Exception as e:
            flash(f'Error al guardar el formulario: {str(e)}', 'danger')

        return redirect(url_for('detalle_politraumatizado', archivo=archivo))

    return render_template('editar_politraumatizado.html', form=form, archivo=archivo)

if __name__ == '__main__':
    app.run(debug=True)
