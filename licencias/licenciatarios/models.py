from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Licenciatarios(models.Model):
    folio = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=200)
    nombre_comercial = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    entidad = models.CharField(max_length=200)
    cp = models.IntegerField()
    latlng = models.CharField(max_length=200, blank=True)
    telefono = models.IntegerField()
    correo = models.EmailField()
    rfc = models.CharField(max_length=200)
    actividad = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    expedicion_fecha = models.DateField()
    vencimiento_fecha = models.DateField()



    def __str__(self):
        space = ' '
        return self.nombre_comercial+space+'('+self.nombre+')'
