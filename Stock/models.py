from django.db import models

# Create your models here.
class Producto(models.Model): #Base de datos de Stock
    sku = models.CharField(max_length=25)
    nombre = models.CharField(max_length=20)
    pertenece_a = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=10)
    unidades = models.IntegerField()