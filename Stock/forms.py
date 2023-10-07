from django import forms
from .models import Producto

class Producto_form(forms.Form): #Formulario para stock
    sku = forms.CharField(max_length=25)
    nombre = forms.CharField(max_length=20)
    pertenece_a = forms.CharField(max_length=20)
    ubicacion = forms.CharField(max_length=10)
    unidades = forms.IntegerField()

class Proucto_vendido_form(forms.Form):
    sku = forms.CharField(max_length=25)
    pertenece_a = forms.ChoiceField(
        label="Seller",
        choices=[(prop, prop) for prop in Producto.objects.values_list('pertenece_a', flat=True).distinct()])
    unidades_vendidas = forms.IntegerField()