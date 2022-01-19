from pyexpat import model
from django.db import models

# Create your models here.

class Eventos (models.Model):
    nombre_evento = models.CharField(max_length=50) 
    fecha = models.DateField()
    alarma=models.BooleanField()
    