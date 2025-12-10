import sys
import os

# Añadir la ruta del proyecto al path
sys.path.insert(0, '/var/www/alumnos/rhernandez/flask_app')

# Importar la aplicación Flask desde application.py
from application import app as application

if __name__ == "__main__":
    application.run()
