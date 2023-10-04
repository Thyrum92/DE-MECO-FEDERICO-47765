from django.urls import path
from Personal.views import *

urlpatterns = [
    path("", pagina_principal, name="Inicio"),
    path("agregar_empleado/",agregar_empleado, name="Agregar Empleado"),
    path("buscar_empleado/",buscar_empleado, name="Buscar Empleado"),
    path("resultado_busqueda_empleado/",resultado_busqueda_empleado, name="Busqueda Empleado"),
    path("Agregar_seller/",agregar_seller,name="Agregar Seller"),
    path("buscar_seller/",buscar_seller,name="buscar_seller"),
    path("resultado_busqueda_seller/",resultado_busqueda_seller,name="resultado_busqueda_seller"),
    path("Agregar_producto/",agregar_producto,name="Agregar Producto"),
    path("buscar_producto/",buscar_producto,name="buscar_producto"),
    path("resultado_busqueda_producto/",resultado_busqueda_producto,name="resultado_busqueda_producto"),

]
