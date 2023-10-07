from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio_stock(request):
    return render(request,'Stock/inicio_stock.html')

@login_required
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

            return render(request, 'Stock/producto_agregado.html',{"mensaje":f"informacion de {producto.sku} {producto.nombre} agregada con exito"})

    else:
        
        formulario = Producto_form()

    return render(request, 'Stock/agregar_producto.html', {"form3":formulario})

@login_required
def proucto_agregado(request):

    return render(request, 'Stock/proucto_agregado.html')

@login_required
def buscar_producto(request):
    return render(request,"Stock/buscar_producto.html")

@login_required
def resultado_busqueda_producto(request):
    
    if request.GET["pertenece_a"]:

        pertenece_a = request.GET["pertenece_a"]

        vendedor = Producto.objects.filter(pertenece_a__icontains=pertenece_a)

        return render(request, 'Stock/resultado_busqueda_producto.html', {'vendedor':vendedor, "pertenece_a":pertenece_a})
    
    else:

        vendedor = Producto.objects.all()
    
    return render(request, 'Stock/resultado_busqueda_producto.html', {'vendedor':vendedor})

@login_required
def eliminar_producto(request,sku_producto):

    producto = Producto.objects.get(sku = sku_producto)
    

    producto.delete()

    return render(request,"Stock/resultado_busqueda_producto.html")

@login_required
def actualizar_producto(request,sku_producto):

    producto = Producto.objects.get(sku = sku_producto)

    if request.method == "POST":

        formulario = Producto_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            producto.sku = info["sku"]
            producto.nombre = info["nombre"]
            producto.pertenece_a = info["pertenece_a"]
            producto.ubicacion = info["ubicacion"]
            producto.unidades = info["unidades"]

            producto.save()

            return render(request, 'Stock/producto_agregado.html',{"mensaje":f"informacion de {producto.sku} {producto.nombre} actualizada con exito"})

    else:
        
        formulario = Producto_form(initial={

        "sku":producto.sku,
        "nombre":producto.nombre,
        "pertenece_a":producto.pertenece_a,
        "ubicacion":producto.ubicacion,
        "unidades":producto.unidades,

        })

    return render(request, 'Stock/actualizar_producto.html', {"form":formulario,"sku": sku_producto})

@login_required
def descontar_stock(request):

    if request.method == "POST":

        formulario = Proucto_vendido_form(request.POST)

        if formulario.is_valid():

            sku = formulario.cleaned_data['sku']
            pertenece_a = formulario.cleaned_data['pertenece_a']
            unidades_vendidas = formulario.cleaned_data['unidades_vendidas']

            try:
                producto = Producto.objects.get(sku = sku,pertenece_a=pertenece_a)

                if pertenece_a == formulario.cleaned_data['pertenece_a']:
                    if producto.unidades >= unidades_vendidas:
                        producto.unidades -= unidades_vendidas
                        producto.save()

                        producto_vendido = Producto_vendido(sku=producto,unidades_vendidas=unidades_vendidas)
                        producto_vendido.save()

                        return render(request, 'Stock/unidades_descontadas.html',{"mensaje":f"Quedan {producto.unidades} unidades de {producto.sku} - {producto.nombre}"})
                    else:
                        return render(request, 'Stock/unidades_descontadas.html',{"mensaje":"No hay suficientes unidades para descontar"}) 
            except Producto.DoesNotExist:
                 
                 return render(request, 'Stock/unidades_descontadas.html',{"mensaje":"El SKU ingresado no existe o no pertenece a ese seller"})  

    else:
        
        formulario = Proucto_vendido_form()
        mensaje = ""

    return render(request, 'Stock/descontar_unidades.html', {"form":formulario,"mensaje":mensaje})