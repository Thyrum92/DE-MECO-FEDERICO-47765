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
    unidades_vendidas = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [(prop, prop) for prop in Producto.objects.values_list('pertenece_a', flat=True).distinct()]
        self.fields['pertenece_a'] = forms.ChoiceField(
            label="Seller",
            choices=choices
        )