from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def inicio_sesion(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contrasenia)

            if user:

                login(request,user)

                return render(request,'PaginaWeb/index.html',{"message":f"Bienvenido {user}"})
        else:

            return render(request,'PaginaWeb/login_incorrecto.html',{"message":"Usuario o contraseña incorrectos"})
    else:

        form =AuthenticationForm()

    return render(request,'Paginaweb/login.html',{"login_form":form})

# Borrar Registro para proyecto de la empresa
def registrarse(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request,'Paginaweb/confirmacion_registro.html',{'message':f'{username} fue creado correctamente'})
    else:

        form = UserCreationForm()
    
    return render(request,'Paginaweb/registro.html',{'register_form':form})

def index(request):
    return render(request,'PaginaWeb/index.html')