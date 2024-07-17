from django.apps import AppConfig

# Configuramos la aplicación 'base'
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
