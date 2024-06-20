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
from .views import agregar_plan, editar_libro, obtener_alquileres_por_usuario, obtener_todos_los_libros, planes, obtener_plan
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
from .views import eliminar_usuario
from .views import usuarios_login

from .views import obtener_todas_las_categorias
from .views import obtener_categoria
from .views import agregar_categoria
from .views import eliminar_categoria

from .views import obtener_todos_los_autores
from .views import obtener_autor
from .views import agregar_autor
from .views import eliminar_autor

from .views import obtener_todas_las_suscripciones
from .views import obtener_suscripcion
from .views import agregar_suscripcion
from .views import eliminar_suscripcion
from .views import aprobar_suscripcion
from .views import obtener_suscripciones

from .views import obtener_todos_los_alquileres
from .views import obtener_alquiler
from .views import agregar_alquiler
from .views import eliminar_alquiler
from .views import aprobar_alquiler
from .views import obtener_alquileres
from .views import devolver_alquiler
from .views import obtener_suscripciones_por_usuario
from .views import obtener_todos_los_movimientos
from .views import obtener_movimiento
from .views import agregar_movimiento
from .views import eliminar_movimiento


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('libros/', obtener_todos_los_libros, name='libros'),
    path('libros/<int:libro_id>/', obtener_libro, name='libro'),
    path('libros/agregar/', agregar_libro, name='agregar_libro'),
    path('libros/eliminar_libro/<int:id>/', eliminar_libro, name='eliminar_libro'),
    # path('libros/editar/<int:libro_id>/', editar_libro, name='editar_libro'),  # Nueva ruta para editar libro
    path('libros/editar/<int:id>/', editar_libro, name='editar_libro'),

    path('planes/', planes, name='planes'),
    path('planes/<int:plan_id>/', obtener_plan, name='plan'),
    path('planes/agregar/', agregar_plan, name='agregar_plan'),
    path('planes/eliminar_plan/<int:id>/', eliminar_plan, name='eliminar_plan'),

    path('roles/', roles, name='roles'),
    path('roles/agregar/', agregar_rol, name='agregar_rol'),
    path('roles/eliminar_rol/<int:id>/', eliminar_rol, name='eliminar_rol'),

    path('usuarios/', usuarios, name='usuarios'),
    path('usuarios/agregar/', agregar_usuario, name='agregar_usuario'),
    path('usuarios/eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/login/', usuarios_login, name='usuarios_login'),


    path('categorias/', obtener_todas_las_categorias, name='categorias'),
    path('categorias/<int:categoria_id>/', obtener_categoria, name='categoria'),
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categorias/eliminar_categoria/<int:id>/', eliminar_categoria, name='eliminar_categoria'),


    path('autores/', obtener_todos_los_autores, name='autores'),
    path('autores/<int:autor_id>/', obtener_autor, name='autor'),
    path('autores/agregar/', agregar_autor, name='agregar_autor'),
    path('autores/eliminar_autor/<int:id>/', eliminar_autor, name='eliminar_autor'),

    path('suscripciones/', obtener_todas_las_suscripciones, name='suscripciones'),
    path('suscripciones/<int:suscripcion_id>/', obtener_suscripcion, name='suscripcion'),
    path('suscripciones/agregar/', agregar_suscripcion, name='agregar_suscripcion'),
    path('suscripciones/eliminar_suscripcion/<int:id>/', eliminar_suscripcion, name='eliminar_suscripcion'),
    path('suscripciones/aprobar_suscripcion/<int:id>/', aprobar_suscripcion, name='aprobar_suscripcion'),
    path('suscripciones/obtener_suscripcion/<int:id_usuario>', obtener_suscripciones, name='obtener_suscripciones'),
    path('suscripciones/usuario/<int:id_usuario>/', obtener_suscripciones_por_usuario, name='obtener_suscripciones_por_usuario'),

    path('alquileres/', obtener_todos_los_alquileres, name='alquileres'),
    path('obtener_alquileres/', obtener_alquileres, name='alquileres'),
    path('alquileres/<int:alquiler_id>/', obtener_alquiler, name='alquiler'),
    path('alquileres/agregar/', agregar_alquiler, name='agregar_alquiler'),
    path('alquileres/eliminar_alquiler/<int:id>/', eliminar_alquiler, name='eliminar_alquiler'),
    path('alquileres/aprobar/<int:id>/', aprobar_alquiler, name='aprobar_alquiler'),
    path('alquileres/devolver/<int:alquiler_id>/', devolver_alquiler, name='devolver_alquiler'),
    path('alquileres/obtener_por_usuario/<int:id_usuario>/', obtener_alquileres_por_usuario, name='obtener_alquileres_por_usuario'),

    path('movimientos/', obtener_todos_los_movimientos, name='movimientos'),
    path('movimientos/<int:movimiento_id>/', obtener_movimiento, name='movimiento'),
    path('movimientos/agregar/', agregar_movimiento, name='agregar_movimiento'),
    path('movimientos/eliminar/<int:movimiento_id>/', eliminar_movimiento, name='eliminar_movimiento'),


]

