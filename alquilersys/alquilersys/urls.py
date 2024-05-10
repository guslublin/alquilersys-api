"""
URL configuration for alquilersys project.

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
from django.urls import path
from .views import agregar_plan, obtener_todos_los_libros, planes
from .views import agregar_libro
from .views import obtener_libro
from .views import eliminar_libro
from .views import agregar_rol
from .views import roles
from .views import eliminar_rol
from .views import agregar_rol
from .views import eliminar_plan
from .views import usuarios
from .views import agregar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', obtener_todos_los_libros, name='libros'),
    path('libros/<int:libro_id>/', obtener_libro, name='libro'),
    path('libros/agregar/', agregar_libro, name='agregar_libro'),
    path('libros/eliminar_libro/<int:id>/', eliminar_libro, name='eliminar_libro'),
    
    path('planes/', planes, name='planes'),
    path('planes/agregar/', agregar_plan, name='agregar_plan'),
    path('planes/eliminar_plan/<int:id>/', eliminar_plan, name='eliminar_plan'),

    path('roles/', roles, name='roles'),
    path('roles/agregar/', agregar_rol, name='agregar_rol'),
    path('roles/eliminar_rol/<int:id>/', eliminar_rol, name='eliminar_rol'),

    path('usuarios/', usuarios, name='usuarios'),
    path('usuarios/agregar/', agregar_usuario, name='agregar_usuario'),


]

