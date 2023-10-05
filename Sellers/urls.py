from django.urls import path
from Sellers.views import *

urlpatterns = [
    path("", inicio_sellers, name="inicio_sellers"),
    path("Agregar_seller/",agregar_seller,name="Agregar Seller"),
    path("buscar_seller/",buscar_seller,name="buscar_seller"),
    path("resultado_busqueda_seller/",resultado_busqueda_seller,name="resultado_busqueda_seller"),
    path("borrar/<custID>/",eliminar_seller,name="Eliminar Seller")

]