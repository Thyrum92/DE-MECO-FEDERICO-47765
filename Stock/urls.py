from django.urls import path
from Stock.views import *

urlpatterns = [
    path('', inicio_stock, name="inicio_stock"),
    path("Agregar_producto/",agregar_producto,name="Agregar Producto"),
    path("buscar_producto/",buscar_producto,name="buscar_producto"),
    path("resultado_busqueda_producto/",resultado_busqueda_producto,name="resultado_busqueda_producto"),
    path("borrar/<sku_producto>/",eliminar_producto,name="Eliminar Producto"),
    path("actualizar/<sku_producto>/",actualizar_producto,name="Actualizar Producto"),
    path("descontar_unidades",descontar_stock,name="Descontar Unidades")

]