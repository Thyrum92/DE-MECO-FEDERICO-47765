from django.db import models

# Create your models here.
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