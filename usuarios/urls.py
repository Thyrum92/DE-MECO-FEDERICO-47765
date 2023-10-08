"""
URL configuration for PaginaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #URLS BASE
    path('admin/', admin.site.urls),
    #URLS LOGIN Y REGISTRO
    path('login/',inicio_sesion,name='login'),
        #borrar path de regisro para proyecto de la empresa
    path('registro/',registrarse,name='registro'),
        #actualizar datos
    path('mis_datos/',actualizar_datos,name="mis datos"),
    # Avatar
    path('avatar/',agregarAvatar,name="Agregar Avatar"),
    #URL BASE
    path("",index,name='Inicio_base'),
    #URLS Apps
    path('/Personal/', include('Personal.urls')),
    path('/Sellers/', include('Sellers.urls')),
    path('/Stock/',include('Stock.urls')),
    path('logout', LogoutView.as_view(template_name='usuarios/logout.html'),name='logout')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)