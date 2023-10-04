from django import forms

class Producto_form(forms.Form): #Formulario para stock
    sku = forms.CharField(max_length=25)
    nombre = forms.CharField(max_length=20)
    pertenece_a = forms.CharField(max_length=20)
    ubicacion = forms.CharField(max_length=10)
    unidades = forms.IntegerField()