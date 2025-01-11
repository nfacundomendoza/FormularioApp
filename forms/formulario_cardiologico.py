from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Optional

class FormularioCardiologico(FlaskForm):
    nombre_paciente = StringField('Nombre del Paciente', validators=[DataRequired()])
    # Primera sección de campos
    motivo_ingreso_diag = StringField("Motivo de Ingreso/Diag:", validators=[DataRequired()])
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
    antecedentes = StringField("Antecedentes:", validators=[DataRequired()])
    enfermedad_actual = StringField("Enfermedad Actual:", validators=[DataRequired()])
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
    examen_fisico = StringField("Examen Físico:", validators=[DataRequired()])
    signos_vitales = StringField("Signos Vitales:", validators=[DataRequired()])
    respiratorio = StringField("Respiratorio:", validators=[DataRequired()])
    mecanica_ventilatoria = BooleanField("Mecánica Ventilatoria")
    buena_entrada_aire_bilateral = BooleanField("Buena Entrada de Aire Bilateral")
    hipoventilacion_der = BooleanField("Hipoventilación DER")
    hipoventilacion_izq = BooleanField("Hipoventilación IZQ")
    roncus = BooleanField("Roncus")
    sibilancias = BooleanField("Sibilancias")
    rales = BooleanField("Rales")
    arm = BooleanField("ARM")
    
    # Cuarta sección de campos
    cardiovascular = StringField("Cardiovascular:", validators=[DataRequired()])
    ta = BooleanField("TA")
    tam = BooleanField("TAM")
    pvc = BooleanField("PVC")
    fc = BooleanField("FC")
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
    abdomen = StringField("Abdomen:", validators=[DataRequired()])
    blando_depresible_indoloro = BooleanField("Blando, Depresible, Indoloro")
    rha = BooleanField("RHA")

    # Séptima sección de campos
    diuresis = StringField("Diuresis:", validators=[DataRequired()])
    sonda_vesical = BooleanField("Sonda Vesical")

    # Octava sección de campos
    neurologico = StringField("Neurológico:", validators=[DataRequired()])
    bajo_sedoanalgesia = BooleanField("Bajo Sedoanalgesia")
    glasgow = BooleanField("Glasgow")
    pupilas = BooleanField("Pupilas")
    foco_motor = BooleanField("Foco Motor")
   
   # Campos de texto adicionales
    laboratorio = StringField("Laboratorio:", validators=[DataRequired()])
    ecg = StringField("ECG:", validators=[DataRequired()])
    ecocardiograma = StringField("Ecocardiograma:", validators=[DataRequired()])

    # Botón para enviar el formulario
    submit = SubmitField("Guardar")
