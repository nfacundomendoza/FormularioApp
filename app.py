from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generar_planilla')
def generar_planilla():
    return render_template('seleccionar_guia.html')

@app.route('/guia_t_cardiologico')
def guia_t_cardiologico():
    # Lógica para 'GUIA T CARDIOLÓGICO'
    return "Formulario GUIA T CARDIOLÓGICO"

@app.route('/guia_t_politraumatizado')
def guia_t_politraumatizado():
    # Lógica para 'GUIA T POLITRAUMATIZADO'
    return "Formulario GUIA T POLITRAUMATIZADO"

@app.route('/editar_planilla')
def editar_planilla():
    # Lógica para editar planilla
    return "Editar Planilla"

@app.route('/ver_planilla')
def ver_planilla():
    # Lógica para ver planilla
    return "Ver Planilla"

if __name__ == '__main__':
    app.run(debug=True)
