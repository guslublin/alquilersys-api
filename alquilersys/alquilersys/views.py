from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Libro, Plan, Rol, Usuario
from django.views.decorators.csrf import csrf_exempt
import json

def obtener_todos_los_libros(request):
    libros = Libro.objects.all()
    data = {'libros': list(libros.values())}
    return JsonResponse(data)

def obtener_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    data = {'libro': {
        'id': libro.id,
        'nombre': libro.nombre,
        'autor': libro.autor
    }}
    return JsonResponse(data)

@csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def agregar_libro(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                nombre = datos.get('nombre')
                autor = datos.get('autor')

                # Aquí puedes procesar los datos como desees
                print(f'Nombre: {nombre}, Autor: {autor}')
                libro = Libro(nombre=nombre, autor=autor)
                libro.save()
            
                # Devuelve una respuesta JSON de éxito
                return JsonResponse({'mensaje': 'Datos recibidos correctamente'})
            except json.JSONDecodeError as e:
                # Si hay un error al decodificar el JSON, devuelve un mensaje de error
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
        else:
            # Si no hay datos en el cuerpo de la solicitud, devuelve un mensaje de error
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        # Si la solicitud no es POST, devuelve un mensaje de error de método no permitido
        return JsonResponse({'error': 'Método no permitido'}, status=405)

# @csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def eliminar_libro(request, id):
    if request.method == 'DELETE':
        try:
            libro = Libro.objects.get(id=id)
            libro.delete()
            return JsonResponse({'mensaje': 'Libro eliminado correctamente'})
        except Libro.DoesNotExist:
            return JsonResponse({'error': 'El libro no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def planes(request):
    planes = Plan.objects.all()
    data = {'planes': list(planes.values())}
    return JsonResponse(data)

@csrf_exempt
def agregar_plan(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                nombre = datos.get('nombre')
                valor = datos.get('valor')
                dias = datos.get('dias')

                # Aquí puedes procesar los datos como desees
                print(f'Nombre: {nombre}, Valor: {valor}, Días: {dias}')
                plan = Plan(nombre=nombre, valor=valor, dias=dias)
                plan.save()
            
                # Devuelve una respuesta JSON de éxito
                return JsonResponse({'mensaje': 'Datos recibidos correctamente'})
            except json.JSONDecodeError as e:
                # Si hay un error al decodificar el JSON, devuelve un mensaje de error
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
        else:
            # Si no hay datos en el cuerpo de la solicitud, devuelve un mensaje de error
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        # Si la solicitud no es POST, devuelve un mensaje de error de método no permitido
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_plan(request, id):
    if request.method == 'DELETE':
        try:
            plan = Plan.objects.get(id=id)
            plan.delete()
            return JsonResponse({'mensaje': 'Plan eliminado correctamente'})
        except Plan.DoesNotExist:
            return JsonResponse({'error': 'El Plan no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)    

def roles(request):
    roles = Rol.objects.all()
    data = {'roles': list(roles.values())}
    return JsonResponse(data)

@csrf_exempt
def agregar_rol(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                nombre = datos.get('nombre')

                # Aquí puedes procesar los datos como desees
                print(f'Nombre: {nombre}')
                rol = Rol(nombre=nombre)
                rol.save()
            
                # Devuelve una respuesta JSON de éxito
                return JsonResponse({'mensaje': 'Datos recibidos correctamente'})
            except json.JSONDecodeError as e:
                # Si hay un error al decodificar el JSON, devuelve un mensaje de error
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
        else:
            # Si no hay datos en el cuerpo de la solicitud, devuelve un mensaje de error
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        # Si la solicitud no es POST, devuelve un mensaje de error de método no permitido
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def eliminar_rol(request, id):
    if request.method == 'DELETE':
        try:
            rol = Rol.objects.get(id=id)
            rol.delete()
            return JsonResponse({'mensaje': 'Rol eliminado correctamente'})
        except Rol.DoesNotExist:
            return JsonResponse({'error': 'El Rol no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def agregar_usuario(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                
                # Extrae los datos del cuerpo de la solicitud
                nombre = datos.get('nombre')
                apellido = datos.get('apellido')
                email = datos.get('email')
                fecha_nacimiento = datos.get('fecha_nacimiento')
                telefono = datos.get('telefono')
                contrasena = datos.get('contrasena')
                id_rol = datos.get('id_rol')

                # Convierte el id_rol a un entero
                id_rol = int(id_rol)

                # Obtiene el objeto Rol correspondiente al id_rol
                rol = Rol.objects.get(id=id_rol)

                # Crea un nuevo usuario con los datos recibidos
                usuario = Usuario(nombre=nombre, apellido=apellido, email=email,
                                  fecha_nacimiento=fecha_nacimiento, telefono=telefono,
                                  contrasena=contrasena, id_rol=rol)
                
                # Guarda el usuario en la base de datos
                usuario.save()

                # Devuelve una respuesta JSON de éxito
                return JsonResponse({'mensaje': 'Usuario agregado correctamente'})
            except json.JSONDecodeError as e:
                # Si hay un error al decodificar el JSON, devuelve un mensaje de error
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
            except Rol.DoesNotExist:
                # Si no se encuentra el Rol correspondiente al id_rol, devuelve un mensaje de error
                return JsonResponse({'error': 'Rol no encontrado'}, status=404)
        else:
            # Si no hay datos en el cuerpo de la solicitud, devuelve un mensaje de error
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        # Si la solicitud no es POST, devuelve un mensaje de error de método no permitido
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def usuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios': list(usuarios.values())}
    return JsonResponse(data)
