from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Libro
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def agregar_libro(request):
    nombre = request.POST.get('nombre')
    autor = request.POST.get('autor')
    libro = Libro(nombre=nombre, autor=autor)
    libro.save()
    data = {'mensaje': 'Libro agregado correctamente'}
    return JsonResponse(data)
