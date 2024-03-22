from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Libro
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