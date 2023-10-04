from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def inicio_stock(request):
    return render(request,'Stock/inicio_stock.html')

def agregar_producto(request):

    if request.method == "POST":

        formulario = Producto_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            producto = Producto(

                sku = info["sku"],
                nombre = info["nombre"],
                pertenece_a = info["pertenece_a"],
                ubicacion = info["ubicacion"],
                unidades = info["unidades"],
                )
            
            producto.save()

            return render(request, 'Stock/producto_agregado.html',{"sku":producto.sku,"nombre":producto.nombre,"unidades":producto.unidades})

    else:
        
        formulario = Producto_form()

    return render(request, 'Stock/agregar_producto.html', {"form3":formulario})

def proucto_agregado(request):

    return render(request, 'Stock/proucto_agregado.html')

def buscar_producto(request):
    return render(request,"Stock/buscar_producto.html")

def resultado_busqueda_producto(request):
    
    if request.GET["pertenece_a"]:

        pertenece_a = request.GET["pertenece_a"]

        vendedor = Producto.objects.filter(pertenece_a__icontains=pertenece_a)

        return render(request, 'Stock/resultado_busqueda_producto.html', {'vendedor':vendedor, "pertenece_a":pertenece_a})
    
    else:

        vendedor = Producto.objects.all()
    
    return render(request, 'Stock/resultado_busqueda_producto.html', {'vendedor':vendedor})