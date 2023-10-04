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

class Seller_form(forms.Form): #Formulario de seller
    cust_id = forms.IntegerField()
    nickname = forms.CharField(max_length=25)
    razon_social = forms.CharField(max_length=25)
    nombre_responsable = forms.CharField(max_length=20)
    apellido_responsable = forms.CharField(max_length=20)
    contacto_resonsable = forms.EmailField(max_length=30)
    servicio_0 = forms.CharField(max_length=15)
    servicio_1 = forms.CharField(max_length=15,required=False)
    servicio_2 = forms.CharField(max_length=15,required=False)
    servicio_3 = forms.CharField(max_length=15,required=False)
    servicio_4 = forms.CharField(max_length=15,required=False)

class Producto_form(forms.Form): #Formulario para stock
    sku = forms.CharField(max_length=25)
    nombre = forms.CharField(max_length=20)
    pertenece_a = forms.CharField(max_length=20)
    ubicacion = forms.CharField(max_length=10)
    unidades = forms.IntegerField()