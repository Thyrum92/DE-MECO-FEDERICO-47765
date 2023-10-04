from django.db import models

# Create your models here.

class Personal(models.Model): #Base de datos de Personal

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    dni = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=10)
    mail = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=15)
    cp = models.IntegerField()
    numero_contacto = models.IntegerField()
    nombre_emergencia = models.CharField(max_length=60)
    apellido_emergencia = models.CharField(max_length=60)
    vinculo = models.CharField(max_length=15)
    numero_contacto_emergencia = models.IntegerField()
    sector = models.CharField(max_length=15)
    permisos = models.CharField(max_length=15)

class Seller(models.Model): #Base de datos de Seller
    cust_id = models.IntegerField()
    nickname = models.CharField(max_length=25)
    razon_social = models.CharField(max_length=25)
    nombre_responsable = models.CharField(max_length=20)
    apellido_responsable = models.CharField(max_length=20)
    contacto_resonsable = models.EmailField(max_length=30)
    servicio_0 = models.CharField(max_length=15)
    servicio_1 = models.CharField(max_length=15,blank=True,null=True)
    servicio_2 = models.CharField(max_length=15,blank=True,null=True)
    servicio_3 = models.CharField(max_length=15,blank=True,null=True)
    servicio_4 = models.CharField(max_length=15,blank=True,null=True)

class Producto(models.Model): #Base de datos de Stock
    sku = models.CharField(max_length=25)
    nombre = models.CharField(max_length=20)
    pertenece_a = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=10)
    unidades = models.IntegerField()