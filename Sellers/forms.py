from django import forms

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