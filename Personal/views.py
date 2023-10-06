from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context,loader
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Vinculando HTMLs que se van a usar.

@login_required
def pagina_principal(request):
                
    return render(request,'Personal/index.html')

@login_required
def agregar_empleado(request):

    if request.method == "POST":

        formulario = Personal_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            personal = Personal(

                nombre = info["nombre"],
                apellido = info["apellido"],
                dni = info["dni"],
                fecha_nacimiento = info["fecha_nacimiento"],
                mail = info["mail"],
                direccion = info["direccion"],
                localidad = info["localidad"],
                cp = info["cp"],
                numero_contacto = info["numero_contacto"],
                nombre_emergencia = info["nombre_emergencia"],
                apellido_emergencia = info["apellido_emergencia"],
                vinculo = info["vinculo"],
                numero_contacto_emergencia = info["numero_contacto_emergencia"],
                sector = info["sector"],
                permisos = info["permisos"]

                )
            
            personal.save()

            return render(request, 'Personal/empleado_agregado.html',{"mensaje":f"Agregaste a {personal.nombre} {personal.apellido} con exito"})

    else:
        
        formulario = Personal_form()

    return render(request, 'Personal/agregar_empleado.html', {"form":formulario})

@login_required
def buscar_empleado(request):


    return render(request,'Personal/buscar_empleado.html')

@login_required
def resultado_busqueda_empleado(request):
    
    if request.GET["apellido"]:

        apellido = request.GET["apellido"]

        personal = Personal.objects.filter(apellido__icontains=apellido)

        return render(request, 'Personal/resultado_busqueda_empleado.html', {'personal':personal, "apellido":apellido})
    
    else:

        personal = Personal.objects.all()
    
    return render(request, 'Personal/resultado_busqueda_empleado.html', {'personal':personal})

@login_required
def eliminar_empleado(request,dni_empleado):

    personal = Personal.objects.get(dni = dni_empleado)
    

    personal.delete()

    return render(request,"Personal/resultado_busqueda_empleado.html")

@login_required
def actualizar_empleado(request,dni_empleado):

    personal = Personal.objects.get(dni = dni_empleado)

    if request.method == "POST":

        formulario = Personal_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            personal.nombre = info["nombre"]
            personal.apellido = info["apellido"]
            personal.dni = info["dni"]
            personal.fecha_nacimiento = info["fecha_nacimiento"]
            personal.mail = info["mail"]
            personal.direccion = info["direccion"]
            personal.localidad = info["localidad"]
            personal.cp = info["cp"]
            personal.numero_contacto = info["numero_contacto"]
            personal.nombre_emergencia = info["nombre_emergencia"]
            personal.apellido_emergencia = info["apellido_emergencia"]
            personal.vinculo = info["vinculo"]
            personal.numero_contacto_emergencia = info["numero_contacto_emergencia"]
            personal.sector = info["sector"]
            personal.permisos = info["permisos"]

            personal.save()

            return render(request, 'Personal/empleado_agregado.html',{"mensaje":f"informacion de {personal.nombre} {personal.apellido} actualizada con exito"})

    else:
        
        formulario = Personal_form(initial={

            "nombre": personal.nombre,
            "apellido":personal.apellido,
            "dni": personal.dni,
            "fecha_nacimiento":personal.fecha_nacimiento,
            "mail":personal.mail,
            "direccion":personal.direccion,
            "localidad":personal.localidad,
            "cp":personal.cp,
            "numero_contacto":personal.numero_contacto,
            "nombre_emergencia":personal.nombre_emergencia,
            "apellido_emergencia":personal.apellido_emergencia,
            "vinculo":personal.vinculo,
            "numero_contacto_emergencia":personal.numero_contacto_emergencia,
            "sector":personal.sector,
            "permisos":personal.permisos

        })

    return render(request, 'Personal/actualizar_empleado.html', {"form":formulario,"dni": dni_empleado})