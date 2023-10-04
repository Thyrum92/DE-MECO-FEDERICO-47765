from django.urls import path
from Personal.views import *

urlpatterns = [
    path("", pagina_principal, name="Personal"),
    path("agregar_empleado/",agregar_empleado, name="Agregar Empleado"),
    path("buscar_empleado/",buscar_empleado, name="Buscar Empleado"),
    path("resultado_busqueda_empleado/",resultado_busqueda_empleado, name="Busqueda Empleado"),

]
