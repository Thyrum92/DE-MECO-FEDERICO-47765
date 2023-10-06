from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio_sellers(request):
    return render(request,'Sellers/inicio_sellers.html')

@login_required
def agregar_seller(request):

    if request.method == "POST":

        formulario = Seller_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            seller = Seller(

                cust_id = info["cust_id"],
                nickname = info["nickname"],
                razon_social = info["razon_social"],
                nombre_responsable = info["nombre_responsable"],
                apellido_responsable = info["apellido_responsable"],
                contacto_resonsable = info["contacto_resonsable"],
                servicio_0 = info["servicio_0"],
                servicio_1 = info["servicio_1"],
                servicio_2 = info["servicio_2"],
                servicio_3 = info["servicio_3"],
                servicio_4 = info["servicio_4"],

                )
            
            seller.save()

            return render(request, 'Sellers/seller_agregado.html',{"mensaje":f"informacion de {seller.cust_id} - {seller.nickname} agregada con exito"})

    else:
        
        formulario = Seller_form()

    return render(request, 'Sellers/agregar_seller.html', {"form2":formulario})

@login_required
def seller_agregado(request):

    return render(request, 'Sellers/seller_agregado.html')

@login_required
def buscar_seller(request):
    return render(request,"Sellers/buscar_seller.html")

@login_required
def resultado_busqueda_seller(request):
    
    if request.GET["nickname"]:

        nickname = request.GET["nickname"]

        sellers = Seller.objects.filter(nickname__icontains=nickname)

        return render(request, 'Sellers/resultado_busqueda_seller.html', {'seller':sellers, "nickname":nickname})
    
    else:

        sellers = Seller.objects.all()
    
    return render(request, 'Sellers/resultado_busqueda_seller.html', {'seller':sellers})

@login_required
def eliminar_seller(request,custID):

    seller = Seller.objects.get(cust_id = custID)
    

    seller.delete()

    return render(request,"Sellers/resultado_busqueda_seller.html")

@login_required
def actualizar_seller(request,custID):

    seller = Seller.objects.get(cust_id = custID)

    if request.method == "POST":

        formulario = Seller_form(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            seller.cust_id = info["cust_id"]
            seller.nickname = info["nickname"]
            seller.razon_social = info["razon_social"]
            seller.nombre_responsable = info["nombre_responsable"]
            seller.apellido_responsable = info["apellido_responsable"]
            seller.contacto_resonsable = info["contacto_resonsable"]
            seller.servicio_0 = info["servicio_0"]
            seller.servicio_1 = info["servicio_1"]
            seller.servicio_2 = info["servicio_2"]
            seller.servicio_3 = info["servicio_3"]
            seller.servicio_4 = info["servicio_4"]

            seller.save()

            return render(request, 'Sellers/seller_agregado.html',{"mensaje":f"informacion de {seller.cust_id} - {seller.nickname} actualizada con exito"})

    else:
        
        formulario = Seller_form(initial={

            "cust_id": seller.cust_id,
            "nickname":seller.nickname,
            "razon_social":seller.razon_social,
            "nombre_responsable":seller.nombre_responsable,
            "apellido_responsable":seller.apellido_responsable,
            "contacto_resonsable":seller.contacto_resonsable,
            "servicio_0":seller.servicio_0,
            "servicio_1":seller.servicio_1,
            "servicio_2":seller.servicio_2,
            "servicio_3":seller.servicio_3,
            "servicio_4":seller.servicio_4

        })

    return render(request, 'Sellers/actualizar_seller.html', {"form":formulario,"cust_id": custID})