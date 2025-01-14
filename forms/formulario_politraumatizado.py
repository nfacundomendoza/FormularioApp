import datetime
from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, SubmitField, TextAreaField, TimeField, IntegerField, BooleanField
from wtforms.validators import DataRequired, InputRequired

class FormularioPolitraumatizado(FlaskForm):
    nombre_paciente = TextAreaField('Nombre del Paciente', validators=[DataRequired(message="El nombre del paciente es obligatorio")])
    sexo = SelectField('SEXO', choices=[('F', 'Femenino'), ('M', 'Masculino')])

    def get_default_date():
        return datetime.date.today()

    def get_default_time():
        return datetime.datetime.now().time()

    fecha_evento = DateField('FECHA DEL EVENTO', format='%Y-%m-%d', default=get_default_date, validators=[DataRequired()])
    hora = TimeField('HORA', format='%H:%M', default=get_default_time, validators=[DataRequired()])

    tipo_evento = SelectField(
        'TIPO DE EVENTO', 
        choices=[
            ('', 'Seleccione...'),
            ('NO INTENCIONAL (ACCIDENTE)', 'NO INTENCIONAL (ACCIDENTE)'),
            ('INTENCIONAL: AGRESIÓN/VIOLENCIA', 'INTENCIONAL: AGRESIÓN/VIOLENCIA'),
            ('INTENCIONAL: AUTOINFLIGIDA', 'INTENCIONAL: AUTOINFLIGIDA'),
            ('SE DESCONOCE', 'SE DESCONOCE')
        ]
    )

    estado_general = TextAreaField('ESTADO GENERAL')
    temperatura = TextAreaField('Tº')
    palidez = BooleanField('PALIDEZ')
    cianosis = BooleanField('CIANOSIS')
    edemas = BooleanField('EDEMAS')
    lesiones_piel_partes_blandas = TextAreaField('LESIONES DE PIEL Y PARTES BLANDAS')

    respiratorio = TextAreaField('RESPIRATORIO')
    trauma_torax_cerrado = BooleanField('TRAUMA DE TORAX CERRADO')
    fracturas_costales = BooleanField('FRACTURAS COSTALES')
    contusiones = BooleanField('CONTUSIONES')
    arm = BooleanField('ARM')
    sato2 = IntegerField('SATO2', default=0, validators=[InputRequired()])
    pafi = IntegerField('PAFi', default=0, validators=[InputRequired()])
    buena_entrada_aire_bilateral = BooleanField('BUENA ENTRADA DE AIRE BILATERAL')
    fr = IntegerField('FR', default=0, validators=[InputRequired()])
    hipoventilacion_derecha = BooleanField('HIPOVENTILACION DERECHA')
    hipoventilacion_izquierda = BooleanField('HIPOVENTILACION IZQUIERDA')
    neumotorax = BooleanField('NEUMOTORAX')
    hemotorax = BooleanField('HEMOTORAX')
    tap = BooleanField('TAP')
    circulatorio = TextAreaField('CIRCULATORIO')
    ta = TextAreaField('TA')
    tam = TextAreaField('TAM')
    pvc = TextAreaField('PVC')
    fc = TextAreaField('FC')
    relleno_capilar = BooleanField('RELLENO CAPILAR')
    hemorragia_externa_activa = BooleanField('HEMORRAGIA EXTERNA ACTIVA')
    sospecha_hemorragia_interna = BooleanField('SOSPECHA DE HEMORRAGIA INTERNA')
    fallo_de_bomba = BooleanField('FALLO DE BOMBA')
    derrame_pericardico = BooleanField('DERRAME PERICARDICO')
    aceptable_perfusion_periferica = BooleanField('ACEPTABLE PERFUSION PERIFERICA')
    shock = BooleanField('SHOCK')
    inotropicos = BooleanField('INOTROPICOS')
    requerimiento_de_transfusion = BooleanField('REQUERIMIENTO DE TRANSFUSION')
    abdomen = TextAreaField('ABDOMEN')
    trauma_abdominal_cerrado = BooleanField('TRAUMA ABDOMINAL CERRADO')
    trauma_abdominal_abierto = BooleanField('TRAUMA ABDOMINAL ABIERTO')
    blando_depresible_indoloro = BooleanField('BLANDO, DEPRESIBLE, INDOLORO')
    rha = TextAreaField('RHA')
    distendido = BooleanField('DISTENDIDO')
    sng = BooleanField('SNG')
    alim_enteral = BooleanField('ALIMENTACION ENTERAL')

    intervencion_quirurgica = BooleanField('INTERVENCION QUIRURGICA')
    detalle_intervencion = TextAreaField('DETALLE DE INTERVENCION')

    drenajes = BooleanField('DRENAJES')
    diuresis = TextAreaField('DIURESIS')
    sonda_vesical = BooleanField('SONDA VESICAL')
    funcion_neurologica = TextAreaField('FUNCION NEUROLOGICA')
    tec = BooleanField('TEC')
    trauma_columna = BooleanField('TRAUMA COLUMNA')
    bajo_sedanalgesia = BooleanField('BAJO SEDOANALGESIA')
    glasgow = TextAreaField('GLASGOW')
    pupilas = TextAreaField('PUPILAS')
    foco_motor = TextAreaField('FOCO MOTOR')
    pic = IntegerField('PIC', default=0, validators=[InputRequired()])
    drenajes = BooleanField('DRENAJES')

    collar_cervical = BooleanField('COLLAR CERVICAL')
    inmovilizacion_tabla = BooleanField('INMOVILIZACIÓN CON TABLA')

    lesion_traumatologica = TextAreaField('LESION TRAMATOLÓGICA')
    rts = IntegerField('REVISED TRAUMA SCORED', default=0, validators=[InputRequired()])
    imagenes = TextAreaField('IMÁGENES')
    laboratorio = TextAreaField('LABORATORIO')
    interconsultas = TextAreaField('INTERCONSULTAS')
    pronostico = TextAreaField('PRONÓSTICO')
    apache_ii = TextAreaField('APACHE II')
    sofa = TextAreaField('SOFA')

    # Botón para enviar el formulario
    submit = SubmitField("Guardar")