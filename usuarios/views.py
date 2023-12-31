from django.shortcuts import render
from django.template import Template, Context,loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *

def inicio_sesion(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contrasenia)

            if user:

                login(request,user)

                return render(request,'usuarios/index.html',{"message":f"Bienvenido {user}"})
        else:

            return render(request,'usuarios/login_incorrecto.html',{"message":"Usuario o contraseña incorrectos"})
    else:

        form =AuthenticationForm()

    return render(request,'usuarios/login.html',{"login_form":form})

# Borrar Registro para proyecto de la empresa
def registrarse(request):
    if request.method == "POST":

        form = Usuario_registro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request,'usuarios/confirmacion_registro.html',{'message':f'{username} fue creado correctamente'})
    else:

        form = Usuario_registro()
    
    return render(request,'usuarios/registro.html',{'register_form':form})

@login_required
def agregarAvatar(request):
    usuario_activo = User.objects.get(username=request.user)

    if request.method == "POST":

        form = AvatarForm(request.POST,request.FILES)

        if form.is_valid():

            try:
                avatarActivo = Avatar.objects.get(usuario = usuario_activo)
                avatarActivo.imagen = form.cleaned_data["imagen"]
                avatarActivo.save()
            except:

                avatar = Avatar(
                    usuario = usuario_activo,
                    imagen=form.cleaned_data["imagen"]
                )

                avatar.save()

            return render(request,'usuarios/index.html')
    else:

        form = AvatarForm()
    
    return render(request,"usuarios/agregar_avatar.html", {"form": form}) 

@login_required
def index(request):
    return render(request,'usuarios/index.html')

@login_required
def actualizar_datos(request):

    usuario = User.objects.get(username = request.user)

    if request.method == "POST":

        formulario = Usuario_actualizar(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]


            usuario.save()

            return render(request, 'usuarios/confirmacion_actualizacion.html',{"mensaje":f"informacion de {usuario.username} actualizada con exito"})

    else:
        
        formulario = Usuario_actualizar(initial={

            "first_name": usuario.first_name,
            "last_name":usuario.last_name,


        })

    return render(request, 'usuarios/mis_datos.html', {"form":formulario,"user": usuario.username})

@login_required
def acerca_de_mi(request):
    return render(request,'usuarios/acerca_de_mi.html')