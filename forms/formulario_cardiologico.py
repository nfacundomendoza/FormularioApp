from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Optional

class FormularioCardiologico(FlaskForm):
    nombre_paciente = StringField('Nombre del Paciente', validators=[DataRequired()])
    # Motivo de ingreso/Diagnóstico
    motivo_ingreso_diag = TextAreaField('Motivo de Ingreso/Diagnóstico', validators=[DataRequired()])

    # Condiciones relacionadas con la cardiología
    dolor_precordial = BooleanField('Dolor Precordial')
    scaest = BooleanField('SCASEST')
    scacest = BooleanField('SCACEST')
    insuficiencia_cardiaca = BooleanField('Insuficiencia Cardíaca Descompensada')
    pericarditis = BooleanField('Pericarditis')
    emergencia_hipertensiva = BooleanField('Emergencia Hipertensiva')
    sincop = BooleanField('Síncope')
    shock = BooleanField('Shock')
    tep = BooleanField('TEP')
    arritmia = BooleanField('Arritmia')

    # Antecedentes
    antecedentes = TextAreaField('Antecedentes', validators=[Optional()])

    # Enfermedad Actual
    disnea = BooleanField('Disnea')
    dolor_precordial_tipico = BooleanField('Dolor Precordial Típico')
    hta = BooleanField('HTA')
    mareos = BooleanField('Mareos')
    palpitaciones = BooleanField('Palpitaciones')
    taquicardia = BooleanField('Taquicardia')
    bradicardia = BooleanField('Bradicardia')
    hipotension_shock = BooleanField('Hipotensión/Shock')
    cianosis = BooleanField('Cianosis')

    # Examen físico: Signos Vitales
    respiratorio = TextAreaField('Respiratorio', validators=[Optional()])
    mecanica_ventilatoria = TextAreaField('Mecánica Ventilatoria', validators=[Optional()])
    buena_entrada_aire = BooleanField('Buena Entrada de Aire Bilateral')
    hipoventilacion_der = BooleanField('Hipoventilación Der.')
    hipoventilacion_izq = BooleanField('Hipoventilación Izq.')
    roncus = BooleanField('Roncos')
    sibilancias = BooleanField('Sibilancias')
    rales = BooleanField('Rales')
    arm = BooleanField('ARM')
    
    # Cardiovascular: Signos Vitales
    ta = StringField('TA (Tensión Arterial)', validators=[DataRequired()])
    tam = StringField('TAM (Tensión Arterial Media)', validators=[DataRequired()])
    pvc = StringField('PVC (Presión Venosa Central)', validators=[DataRequired()])
    fc = StringField('FC (Frecuencia Cardíaca)', validators=[DataRequired()])
    relleno_capilar = StringField('Relleno Capilar', validators=[DataRequired()])
    
    # Otros campos
    soplos = BooleanField('Soplos')
    ingurgitacion_yugular = BooleanField('Ingurgitación Yugular')
    edemas = BooleanField('Edemas')
    pulsos_regulares = BooleanField('Pulsos Regulares')
    pulsos_irregulares = BooleanField('Pulsos Irregulares')
    fallo_bomba = BooleanField('Fallo de Bomba')
    killip_kimball = StringField('Killip-Kimball', validators=[Optional()])
    derrame_pericardico = BooleanField('Derrame Pericárdico')
    aceptable_perf_periferica = BooleanField('Aceptable Perfusión Periférica')
    shock2 = BooleanField('Shock')
    inotropicos = BooleanField('Inotrópicos')

    # Abdomen
    abdomen = StringField('Abdomen', validators=[DataRequired()])
    rha = StringField('RHA', validators=[Optional()])

    # Diuresis y sonda vesical
    diuresis = StringField('Diuresis', validators=[Optional()])
    sonda_vesical = StringField('Sonda Vesical', validators=[Optional()])

    # Neurológico
    bajo_sedoanalgesia = BooleanField('Bajo Sedoanalgesia')
    glasgow = StringField('Glasgow', validators=[Optional()])
    pupilas = StringField('Pupilas', validators=[Optional()])
    foco_motor = StringField('Foco Motor', validators=[Optional()])

    # Laboratorio
    enzimas = StringField('Enzimas', validators=[Optional()])
    rx_torax = StringField('RX de Tórax', validators=[Optional()])
    ecg = StringField('ECG', validators=[Optional()])
    ecocardiograma = StringField('Ecocardiograma', validators=[Optional()])
