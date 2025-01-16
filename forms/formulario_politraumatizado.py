import datetime
from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, SubmitField, TextAreaField, TimeField, IntegerField, BooleanField
from wtforms.validators import DataRequired, InputRequired

class FormularioPolitraumatizado(FlaskForm):
    nombre_paciente = TextAreaField('Nombre del Paciente', validators=[DataRequired(message="El nombre del paciente es obligatorio")])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'),('F', 'Femenino')])

    def get_default_date():
        return datetime.date.today()

    def get_default_time():
        return datetime.datetime.now().time()

    fecha_evento = DateField('Fecha del Evento', format='%Y-%m-%d', default=get_default_date, validators=[DataRequired()])
    hora = TimeField('Hora', format='%H:%M', default=get_default_time, validators=[DataRequired()])

    tipo_evento = SelectField(
    'Tipo de evento', 
    choices=[
        ('', 'Seleccione...'),
        ('NO INTENCIONAL (ACCIDENTE)', 'No intencional (accidente)'),
        ('INTENCIONAL: AGRESIÓN/VIOLENCIA', 'Intencional: agresión/violencia'),
        ('INTENCIONAL: AUTOINFLIGIDA', 'Intencional: autoinfligida'),
        ('SE DESCONOCE', 'Se desconoce')
    ]
    )

    estado_general = TextAreaField('Estado general')
    temperatura = TextAreaField('Tº')
    palidez = BooleanField('Palidez')
    cianosis = BooleanField('Cianosis')
    edemas = BooleanField('Edemas')
    lesiones_piel_partes_blandas = TextAreaField('Lesiones de piel y partes blandas')

    respiratorio = TextAreaField('Respiratorio')
    trauma_torax_cerrado = BooleanField('Trauma de tórax cerrado')
    fracturas_costales = BooleanField('Fracturas costales')
    contusiones = BooleanField('Contusiones')
    arm = BooleanField('ARM')
    sato2 = IntegerField('Sato2', default=0, validators=[InputRequired()])
    pafi = IntegerField('Pafi', default=0, validators=[InputRequired()])
    buena_entrada_aire_bilateral = BooleanField('Buena entrada de aire bilateral')
    fr = IntegerField('FR', default=0, validators=[InputRequired()])
    hipoventilacion_derecha = BooleanField('Hipoventilación derecha')
    hipoventilacion_izquierda = BooleanField('Hipoventilación izquierda')
    neumotorax = BooleanField('Neumotórax')
    hemotorax = BooleanField('Hemotórax')
    tap = BooleanField('TAP')
    circulatorio = TextAreaField('Circulatorio')
    ta = TextAreaField('TA')
    tam = TextAreaField('TAM')
    pvc = TextAreaField('PVC')
    fc = TextAreaField('FC')
    relleno_capilar = BooleanField('Relleno capilar')
    hemorragia_externa_activa = BooleanField('Hemorragia externa activa')
    sospecha_hemorragia_interna = BooleanField('Sospecha de hemorragia interna')
    fallo_de_bomba = BooleanField('Fallo de bomba')
    derrame_pericardico = BooleanField('Derrame pericárdico')
    aceptable_perfusion_periferica = BooleanField('Aceptable perfusión periférica')
    shock = BooleanField('Shock')
    inotropicos = BooleanField('Inotrópicos')
    requerimiento_de_transfusion = BooleanField('Requerimiento de transfusión')
    abdomen = TextAreaField('Abdomen')
    trauma_abdominal_cerrado = BooleanField('Trauma abdominal cerrado')
    trauma_abdominal_abierto = BooleanField('Trauma abdominal abierto')
    blando_depresible_indoloro = BooleanField('Blando, depresible, indoloro')
    rha = TextAreaField('RHA')
    distendido = BooleanField('Distendido')
    sng = BooleanField('SNG')
    alim_enteral = BooleanField('Alimentación enteral')

    intervencion_quirurgica = BooleanField('Intervención quirúrgica')
    detalle_intervencion = TextAreaField('Detalle de intervención')


    drenajes = BooleanField('Drenajes')
    diuresis = TextAreaField('Diuresis')
    sonda_vesical = BooleanField('Sonda vesical')
    funcion_neurologica = TextAreaField('Función neurológica')
    tec = BooleanField('TEC')
    trauma_columna = BooleanField('Trauma columna')
    bajo_sedanalgesia = BooleanField('Bajo sedoanalgesia')
    glasgow = TextAreaField('Glasgow')
    pupilas = TextAreaField('Pupilas')
    foco_motor = TextAreaField('Foco motor')
    pic = IntegerField('PIC', default=0, validators=[InputRequired()])
    drenajes = BooleanField('Drenajes')

    collar_cervical = BooleanField('Collar cervical')
    inmovilizacion_tabla = BooleanField('Inmovilización con tabla')

    lesion_traumatologica = TextAreaField('Lesión traumatológica')
    rts = IntegerField('Revised trauma score', default=0, validators=[InputRequired()])
    imagenes = TextAreaField('Imágenes')
    laboratorio = TextAreaField('Laboratorio')
    interconsultas = TextAreaField('Interconsultas')
    pronostico = TextAreaField('Pronóstico')
    apache_ii = TextAreaField('Apache II')
    sofa = TextAreaField('SOFA')

    # Botón para enviar el formulario
    submit = SubmitField("Guardar")