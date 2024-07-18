# Nombre del Proyecto

Breve descripción del proyecto y su propósito.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)


## Instalación

Instrucciones para instalar y configurar el proyecto.

Clona el repositorio
```bash
git clone https://github.com/usuario/nombre-del-proyecto.git
```
Navega al directorio del proyecto
```bash
cd Fullstack_Prueba_Tecnica
```
Crea y activa un entorno virtual

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
```

Instala las dependencias
```bash
pip install -r requirements.txt
``` 

Navega al directorio del proyecto en django
```bash
cd prueba_tecnica
```

Modifica el archivo '/prueba_tecnica/settings.py' para conectarse con tus credenciales de PostgreSQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',    }
}
```

Realiza las migraciones
```bash
python manage.py migrate
```

Inicia el servidor de desarrollo
```bash
python manage.py runserver
```
Ingresa al servidor local con 'http://127.0.0.1:8000/'
