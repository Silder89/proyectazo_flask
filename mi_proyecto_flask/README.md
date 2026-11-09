# nombre del proyecto: santiago-flask

Este proyecto se hizo a base del manual de practicas del submodulo 1 en donde aprendemos a instalar y ejecutar los programas instalados para hacer paginas con flask

## requisitos
black==26.10.0
blinker==1.9.0
click==8.5.0
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
mypy_extensions==1.1.0
packaging==26.3
pathspec==1.1.1
platformdirs==4.12.3
python-dotenv==1.2.4
pytokens==0.4.1
Werkzeug==3.1.9

## instalacion
1.Clonar el repositorio
2.python -m venv .venv
3.Activar el entorno virtual
4.pip install -r requirements.txt

## Ejecucion
python app.py

## Estructura del proyecto
v mi_proyecto_flask
  v .venv
    >Include
    >Lib
    >Scripts
    .gitignore
    pyvenv.cfg
  v static  
    style.css
  v templates
    about.html
    base.html
    index.html
    .env.example
    app.py
    flasky .env.example
    flasky.env
    README.md
    requirements.txt
    san.gitignore


## Addons utilizados

| Addon | Para qué sirve |
|-------|----------------|
| Flask-WTF | Formularios con validaciones |
| Bootstrap-Flask | Estilo visual de las páginas |
| Flask-SQLAlchemy | Base de datos SQLite |
| Flask-login | Para iniciar sesion |
| Flask-Mail | envia un correo de confirmacion |
| Flask-Migrate | agrega nuevas columnas sin perder informacion |

## Cómo instalarlo

1. Clona el repositorio y entra a la carpeta.
2. Crea y activa un entorno virtual.
3. Instala las dependencias: `pip install -r requirements.txt`
4. Copia `.env.example` a `.env` y escribe tu propia `SECRET_KEY`.
5. Ejecuta la aplicación: `python app.py`
6. Abre http://127.0.0.1:5000

## Cómo ejecutar las pruebas

`python test_app.py`
