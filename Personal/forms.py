from django import forms

class Personal_form(forms.Form): #Formulario de personal

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    dni = forms.IntegerField()
    fecha_nacimiento = forms.CharField(max_length=10)
    mail = forms.CharField(max_length=70)
    direccion = forms.CharField(max_length=100)
    localidad = forms.CharField(max_length=15)
    cp = forms.IntegerField()
    numero_contacto = forms.IntegerField()
    nombre_emergencia = forms.CharField(max_length=60)
    apellido_emergencia = forms.CharField(max_length=60)
    vinculo = forms.CharField(max_length=15)
    numero_contacto_emergencia = forms.IntegerField()
    sector = forms.CharField(max_length=15)
    permisos = forms.CharField(max_length=15)