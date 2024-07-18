from django.db import models

class Pais(models.Model):
    """Clase que representa el modelo de la base de datos"""
    nombre = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    poblacion = models.BigIntegerField()
    area = models.IntegerField()
    is_active = models.BooleanField(default=True) # Borrado lógico
