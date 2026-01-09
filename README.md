# FormularioApp

FormularioApp es una aplicación que permite completar, editar e imprimir formularios con información de pacientes del Hospital de Pinamar. La información se guarda de manera local, específicamente en la carpeta `saved_forms`.

## Instalación

### En Windows (usando PowerShell):

1. Activa el entorno virtual:
    .\venv\Scripts\Activate

2. Instala las dependencias necesarias:
    pip install -r requirements.txt

3. Configura la aplicación Flask:
    set FLASK_APP=app.py

4. Ejecuta la aplicación:
    flask run

### Usando el ejecutable

Si prefieres, puedes ejecutar la aplicación directamente desde el ejecutable que se encuentra en la carpeta `dist`. Este ejecutable fue creado utilizando PyInstaller con el siguiente comando:

pyinstaller --onefile --noconsole --icon "static/images/logo_pinamar.ico" --add-data "templates;templates" --add-data "static;static" --add-data "forms;forms" --add-data "saved_forms;saved_forms" --name "FormularioApp" app.py

## Requisitos
La aplicación fue desarrollada para computadoras con arquitectura de 64 bits. No se garantiza que funcione correctamente en sistemas de 32 bits.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Contribuir
¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

### Haz un fork del repositorio.
1. Crea una nueva rama para tu característica o corrección de error:
ej: git checkout -b feature/mi-nueva-caracteristica
2. Realiza tus cambios y haz commit de ellos:
ej: git commit -am 'Añadir nueva característica'
3. Haz push a tu rama:
git push origin feature/mi-nueva-caracteristica
4. Abre un pull request en este repositorio para que revisemos tus cambios.

## Contacto
Para cualquier duda o sugerencia, puedes ponerte en contacto a través de:
n.facundomendoza@gmail.com o gubia1263@gmail.com