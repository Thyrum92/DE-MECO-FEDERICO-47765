from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class Usuario_registro(UserCreationForm):
    email = forms.CharField(max_length=25)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]

class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ["imagen"]
    
    imagen = forms.ImageField(
        label = "",
        widget = forms.ClearableFileInput(attrs={'class': 'form-input'})
    )