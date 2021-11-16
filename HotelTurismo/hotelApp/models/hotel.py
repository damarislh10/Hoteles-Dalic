from django.db   import models
from .user       import User

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombreHotel = models.CharField(max_length=40, blank=True)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=70, blank=True)
    calificacion = models.FloatField(blank=True) 
    precio = models.FloatField(default=0, null=True)