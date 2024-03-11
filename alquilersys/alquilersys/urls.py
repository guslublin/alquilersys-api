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
from .views import obtener_todos_los_libros
from .views import agregar_libro
from .views import obtener_libro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', obtener_todos_los_libros, name='libros'),
    path('libros/<int:libro_id>/', obtener_libro, name='libro'),
    path('libros/agregar/', agregar_libro, name='agregar_libro'),
]

