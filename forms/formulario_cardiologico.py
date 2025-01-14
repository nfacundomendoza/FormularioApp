from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class FormularioCardiologico(FlaskForm):
    nombre_paciente = TextAreaField('Nombre del Paciente', validators=[DataRequired()])

    # Primera sección de campos
    motivo_ingreso_diag = TextAreaField("Motivo de Ingreso/Diag:")
    dolor_precordial = BooleanField("Dolor Precordial")
    scasest = BooleanField("SCASEST")
    scacest = BooleanField("SCACEST")
    insuficiencia_cardiaca_descompensada = BooleanField("Insuficiencia Cardíaca Descompensada")
    pericarditis = BooleanField("Pericarditis")
    emergencia_hipertensiva = BooleanField("Emergencia Hipertensiva")
    sincope = BooleanField("Síncope")
    shock = BooleanField("Shock")
    tep = BooleanField("TEP")
    arritmia = BooleanField("Arritmia")
    
    # Segunda sección de campos
    antecedentes = TextAreaField("Antecedentes:")
    enfermedad_actual = TextAreaField("Enfermedad Actual:")
    disnea = BooleanField("Disnea")
    dolor_precordial_tipico = BooleanField("Dolor Precordial Típico")
    hta = BooleanField("HTA")
    mareos = BooleanField("Mareos")
    palpitaciones = BooleanField("Palpitaciones")
    taquicardia = BooleanField("Taquicardia")
    bradicardia = BooleanField("Bradicardia")
    hipotension_shock = BooleanField("Hipotensión/Shock")
    cianosis = BooleanField("Cianosis")

    # Tercera sección de campos
    examen_fisico = TextAreaField("Examen Físico:")
    signos_vitales = TextAreaField("Signos Vitales:")
    respiratorio = TextAreaField("Respiratorio:")
    mecanica_ventilatoria = BooleanField("Mecánica Ventilatoria")
    buena_entrada_aire_bilateral = BooleanField("Buena Entrada de Aire Bilateral")
    hipoventilacion_der = BooleanField("Hipoventilación DER")
    hipoventilacion_izq = BooleanField("Hipoventilación IZQ")
    roncus = BooleanField("Roncus")
    sibilancias = BooleanField("Sibilancias")
    rales = BooleanField("Rales")
    arm = BooleanField("ARM")
    
    # Cuarta sección de campos
    cardiovascular = TextAreaField("Cardiovascular:")
    ta = TextAreaField("TA")
    tam = TextAreaField("TAM")
    pvc = TextAreaField("PVC")
    fc = TextAreaField("FC")
    relleno_capilar = BooleanField("Relleno Capilar")

    r1_r2_normofoneticos = BooleanField("R1 y R2 Normofonéticos")
    soplos = BooleanField("Soplos")
    ingurgitacion_yugular = BooleanField("Ingurgitación Yugular")
    edemas = BooleanField("Edemas")
    pulsos_regulares = BooleanField("Pulsos Regulares")
    pulsos_irregulares = BooleanField("Pulsos Irregulares")

    fallo_bomba = BooleanField("Fallo de Bomba")
    killip_kimball = BooleanField("Killip-Kimball")
    derrame_pericardico = BooleanField("Derrame Pericárdico")
    aceptable_perfusion_periferica = BooleanField("Aceptable Perfusión Periférica")
    shock_2 = BooleanField("Shock")
    inotropicos = BooleanField("Inotrópicos")

    # Sexta sección de campos
    abdomen = TextAreaField("Abdomen:")
    blando_depresible_indoloro = BooleanField("Blando, Depresible, Indoloro")
    rha = BooleanField("RHA")

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
