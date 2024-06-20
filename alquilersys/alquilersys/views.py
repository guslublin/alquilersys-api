from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Autor, Categoria, Libro, Plan, Rol, Usuario, Suscripcion, Alquiler, Movimiento
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core import serializers
from django.utils.dateparse import parse_date

def obtener_todos_los_libros(request):
    libros = Libro.objects.all()
    data = {'libros': list(libros.values())}
    return JsonResponse(data)

def obtener_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    data = {
        'libro': {
            'id': libro.id,
            'titulo': libro.titulo,
            'editorial': libro.editorial,
            'resumen': libro.resumen,
            'fecha_entrada': libro.fecha_entrada,
            'cantidad': libro.cantidad,
            'disponible': libro.disponible,
            'categoria': {
                'id': libro.id_categoria.id,
                'nombre': libro.id_categoria.nombre
            },
            'autor': {
                'id': libro.id_autor.id,
                'nombre': libro.id_autor.nombre
            },
            'id_usuario_alta': libro.id_usuario_alta.id
        }
    }
    return JsonResponse(data)

@csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def agregar_libro(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                # Extrae los datos del cuerpo de la solicitud
                titulo = datos.get('titulo')
                editorial = datos.get('editorial')
                resumen = datos.get('resumen')
                fecha_entrada = datos.get('fecha_entrada')
                cantidad = datos.get('cantidad')
                disponible = datos.get('disponible')
                id_autor = int(datos.get('id_autor'))
                id_categoria = int(datos.get('id_categoria'))
                id_usuario_alta = int(datos.get('id_usuario_alta'))

                autor = Autor.objects.get(id=id_autor)
                categoria = Categoria.objects.get(id=id_categoria)
                usuario = Usuario.objects.get(id=id_usuario_alta)


                # Crea un nuevo objeto Libro y guárdalo en la base de datos
                libro = Libro(
                    titulo=titulo,
                    editorial=editorial,
                    resumen=resumen,
                    fecha_entrada=fecha_entrada,
                    cantidad=cantidad,
                    disponible=disponible,
                    id_categoria=categoria,
                    id_autor=autor,
                    id_usuario_alta=usuario
                )
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

def editar_libro(request, id):
    print(request.body)
    if request.method == 'PUT':
        try:
            libro = get_object_or_404(Libro, id=id)
            data = json.loads(request.body)
            
            libro.titulo = data.get('titulo', libro.titulo)
            libro.editorial = data.get('editorial', libro.editorial)
            libro.resumen = data.get('resumen', libro.resumen)
            libro.fecha_entrada = data.get('fecha_entrada', libro.fecha_entrada)
            libro.cantidad = data.get('cantidad', libro.cantidad)
            libro.disponible = data.get('disponible', libro.disponible)

            id_categoria = data.get('id_categoria')
            id_autor = data.get('id_autor')
            
            if id_categoria:
                libro.id_categoria = get_object_or_404(Categoria, id=id_categoria)
            if id_autor:
                libro.id_autor = get_object_or_404(Autor, id=id_autor)

            libro.save()
            return JsonResponse({'message': 'Libro editado correctamente.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Planes
def planes(request):
    planes = Plan.objects.all()
    data = {'planes': list(planes.values())}
    return JsonResponse(data)

def obtener_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    data = {
        'id': plan.id,
        'nombre': plan.nombre,
        'valor': plan.valor,
        'dias': plan.dias,

        # Agrega otros campos del plan que desees incluir
    }
    return JsonResponse({'plan': data})

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

# @csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def eliminar_usuario(request, id):
    if request.method == 'DELETE':
        try:
            usuario = Usuario.objects.get(id=id)
            usuario.delete()
            return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'El usuario no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def usuarios_login(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                
                # Extrae los datos del cuerpo de la solicitud
                email = datos.get('username')
                contrasena = datos.get('password')
                
                # Busca el usuario en la base de datos por email
                usuario = Usuario.objects.get(email=email)
                
                # Verifica si el usuario existe y si la contraseña coincide
                # Verifica si el usuario existe y si la contraseña coincide
                # Verifica si el usuario existe y si la contraseña coincide
                if (usuario.contrasena == contrasena):
                    # Obtener el id del usuario y del rol
                    id_usuario = usuario.id
                    id_rol = usuario.id_rol.id

                    # Devolver un JsonResponse con los ids del usuario y del rol
                    return JsonResponse({'success': True, 'id_usuario': id_usuario, 'id_rol': id_rol})
                else:
                    # Si el usuario o la contraseña son incorrectos, devuelve un mensaje de error
                    return JsonResponse({'error': 'Credenciales inválidas'}, status=401)
                
            except Usuario.DoesNotExist:
                # Si el usuario no existe, devuelve un mensaje de error
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
            except json.JSONDecodeError as e:
                # Si hay un error al decodificar el JSON, devuelve un mensaje de error
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
            
# Categoria
def obtener_todas_las_categorias(request):
    categorias = Categoria.objects.all()
    data = {'categorias': list(categorias.values())}
    return JsonResponse(data)

def obtener_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    data = {'categoría': {
        'id': categoria.id,
        'nombre': categoria.nombre,
    }}
    return JsonResponse(data)

@csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def agregar_categoria(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                nombre = datos.get('nombre')

                # Aquí puedes procesar los datos como desees
                print(f'Nombre: {nombre}')
                categoria = Categoria(nombre=nombre)
                categoria.save()
            
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
def eliminar_categoria(request, id):
    if request.method == 'DELETE':
        try:
            categoria = Categoria.objects.get(id=id)
            categoria.delete()
            return JsonResponse({'mensaje': 'Categoría eliminada correctamente'})
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'La categoría no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


# Autor
def obtener_todos_los_autores(request):
    autores = Autor.objects.all()
    data = {'autores': list(autores.values())}
    return JsonResponse(data)

def obtener_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    data = {'autor': {
        'id': autor.id,
        'nombre': autor.nombre,
    }}
    return JsonResponse(data)

@csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def agregar_autor(request):
    if request.method == 'POST':
        # Verifica que la solicitud tenga datos en el cuerpo
        if request.body:
            try:
                # Convierte el cuerpo de la solicitud de JSON a un objeto Python
                datos = json.loads(request.body)
                nombre = datos.get('nombre')

                # Aquí puedes procesar los datos como desees
                print(f'Nombre: {nombre}')
                autor = Autor(nombre=nombre)
                autor.save()
            
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
def eliminar_autor(request, id):
    if request.method == 'DELETE':
        try:
            autor = Autor.objects.get(id=id)
            autor.delete()
            return JsonResponse({'mensaje': 'Autor eliminado correctamente'})
        except autor.DoesNotExist:
            return JsonResponse({'error': 'El autor no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
# Suscripción
# Obtener todas las suscripciones
def obtener_todas_las_suscripciones(request):
    suscripciones = Suscripcion.objects.all()
    data = {'suscripciones': list(suscripciones.values())}
    return JsonResponse(data)

# Obtener una suscripción específica
def obtener_suscripcion(request, suscripcion_id):
    suscripcion = get_object_or_404(Suscripcion, id=suscripcion_id)
    data = {'suscripcion': {
        'id': suscripcion.id,
        'fecha_contrato': suscripcion.fecha_contrato,
        'fecha_fin': suscripcion.fecha_fin,
        'activo': suscripcion.activo,
        'estado': suscripcion.estado,
        'id_plan': suscripcion.id_plan.id,
        'id_usuario': suscripcion.id_usuario.id,
    }}
    return JsonResponse(data)

@csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def agregar_suscripcion(request):
    if request.method == 'POST':
        if request.body:
            try:
                datos = json.loads(request.body)
                print('datos')
                print(datos)
                fecha_contrato = datos.get('fecha_contrato')
                fecha_fin = datos.get('fecha_fin')
                activo = datos.get('activo')
                estado = datos.get('estado')
                id_plan = datos.get('id_plan_id')
                id_usuario = datos.get('id_usuario')

                # Aquí puedes procesar los datos como desees
                print(f'Fecha Contrato: {fecha_contrato}, Fecha Fin: {fecha_fin}, Activo: {activo}, Estado: {estado}, ID Plan: {id_plan}, ID Usuario: {id_usuario}')
                
                suscripcion = Suscripcion(
                    fecha_contrato=fecha_contrato,
                    fecha_fin=fecha_fin,
                    activo=activo,
                    estado=estado,
                    id_plan_id=id_plan,
                    id_usuario_id=id_usuario
                )
                suscripcion.save()
            
                return JsonResponse({'mensaje': 'Suscripción agregada correctamente'})
            except json.JSONDecodeError as e:
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
        else:
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt  # Asegúrate de importar csrf_exempt si no lo has hecho ya
def eliminar_suscripcion(request, id):
    if request.method == 'DELETE':
        try:
            suscripcion = Suscripcion.objects.get(id=id)
            suscripcion.delete()
            return JsonResponse({'mensaje': 'Suscripción eliminada correctamente'})
        except Suscripcion.DoesNotExist:
            return JsonResponse({'error': 'La suscripción no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def aprobar_suscripcion(request, id):
    suscripcion = get_object_or_404(Suscripcion, id=id)
    
    # Actualizar el estado y el campo activo
    suscripcion.estado = 'Activo'
    suscripcion.activo = True
    suscripcion.save()

    return JsonResponse({'mensaje': 'Suscripción aprobada correctamente'})

def obtener_suscripciones(request, id_usuario):
    if id_usuario:
        suscripciones = Suscripcion.objects.filter(id_usuario=id_usuario)
    else:
        suscripciones = []
    data = {'suscripciones': list(suscripciones.values())}
    return JsonResponse(data)

def obtener_suscripciones(request, id_usuario):
    suscripciones = Suscripcion.objects.filter(id_usuario=id_usuario)
    data = {'suscripciones': list(suscripciones.values())}
    return JsonResponse(data)

def obtener_suscripciones_por_usuario(request, id_usuario):
    suscripciones = Suscripcion.objects.filter(id_usuario=id_usuario)
    suscripciones_data = [
        {
            'id': suscripcion.id,
            'fecha_contrato': suscripcion.fecha_contrato,
            'fecha_fin': suscripcion.fecha_fin,
            'activo': suscripcion.activo,
            'estado': suscripcion.estado,
            'id_plan_id': suscripcion.id_plan.id,
            'id_usuario_id': suscripcion.id_usuario.id,
        }
        for suscripcion in suscripciones
    ]
    return JsonResponse({'suscripciones': suscripciones_data})

# Alquileres
# Obtener todos los alquileres
def obtener_todos_los_alquileres(request):
    alquileres = Alquiler.objects.all()
    data = {'alquileres': list(alquileres.values())}
    return JsonResponse(data)

def obtener_alquileres(request):
    alquileres = Alquiler.objects.select_related('id_libro').all()
    alquileres_data = [{'id': alquiler.id, 'fecha_inicio': alquiler.fecha_inicio, 'fecha_fin': alquiler.fecha_fin, 'fecha_devolucion': alquiler.fecha_devolucion, 'estado': alquiler.estado, 'id_libro': alquiler.id_libro.id, 'nombre_libro': alquiler.id_libro.titulo} for alquiler in alquileres]
    data = {'alquileres': alquileres_data}
    return JsonResponse(data)

def obtener_alquileres_por_usuario(request, id_usuario):
    alquileres = Alquiler.objects.filter(id_usuario=id_usuario).values()
    return JsonResponse({'alquileres': list(alquileres)})

# Obtener un alquiler específico
def obtener_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)
    data = {'alquiler': {
        'id': alquiler.id,
        'fecha_inicio': alquiler.fecha_inicio,
        'fecha_fin': alquiler.fecha_fin,
        'fecha_devolucion': alquiler.fecha_devolucion,
        'id_suscripcion': alquiler.id_suscripcion.id,
        'id_libro': alquiler.id_libro.id,
        'estado':alquiler.estado
    }}
    return JsonResponse(data)

@csrf_exempt
def agregar_alquiler(request):
    if request.method == 'POST':
        if request.body:
            try:
                datos = json.loads(request.body)
                fecha_inicio = datos.get('fecha_inicio')
                fecha_fin = datos.get('fecha_fin')
                fecha_devolucion = datos.get('fecha_devolucion')
                id_suscripcion = datos.get('id_suscripcion')
                id_libro = datos.get('id_libro')
                estado = datos.get('estado')
                id_usuario = datos.get('id_usuario')

                alquiler = Alquiler(
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin,
                    fecha_devolucion=fecha_devolucion,
                    id_suscripcion_id=id_suscripcion,
                    id_libro_id=id_libro,
                    estado=estado,
                    id_usuario_id=id_usuario
                )
                alquiler.save()
            
                return JsonResponse({'mensaje': 'Alquiler agregado correctamente'})
            except json.JSONDecodeError as e:
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
        else:
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def eliminar_alquiler(request, id):
    if request.method == 'DELETE':
        try:
            alquiler = Alquiler.objects.get(id=id)
            alquiler.delete()
            return JsonResponse({'mensaje': 'Alquiler eliminado correctamente'})
        except Alquiler.DoesNotExist:
            return JsonResponse({'error': 'El alquiler no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def aprobar_alquiler(request, id):
    if request.method == 'PUT':
        alquiler = get_object_or_404(Alquiler, id=id)
        
        # Obtener el libro asociado al alquiler
        libro = alquiler.id_libro
        
        # Verificar si hay suficiente cantidad disponible
        if libro.cantidad > 0:
            # Restar 1 a la cantidad de libros disponibles
            libro.cantidad -= 1
            
            # Verificar si la cantidad llega a 0 para actualizar el campo disponible
            if libro.cantidad == 0:
                libro.disponible = False
            
            libro.save()
            
            # Cambiar el estado del alquiler a 'Aprobado'
            alquiler.estado = 'Aprobado'
            alquiler.save()
            
            return JsonResponse({'mensaje': 'Alquiler aprobado correctamente'})
        else:
            return JsonResponse({'error': 'No hay suficientes libros disponibles'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@csrf_exempt
def devolver_alquiler(request, alquiler_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            alquiler = Alquiler.objects.get(id=alquiler_id)
            
            # Obtener el libro asociado al alquiler
            libro = alquiler.id_libro
            
            # Sumar 1 a la cantidad de libros disponibles
            libro.cantidad += 1
            
            # Verificar si la cantidad es mayor a 0 para actualizar el campo disponible
            if libro.cantidad > 0:
                libro.disponible = True
            
            libro.save()
            
            # Actualizar la fecha de devolución y el estado del alquiler
            alquiler.fecha_devolucion = parse_date(data['fecha_devolucion'])
            alquiler.estado = data['estado']
            alquiler.save()
            
            return JsonResponse({'message': 'Alquiler devuelto correctamente'}, status=200)
        except Alquiler.DoesNotExist:
            return JsonResponse({'error': 'Alquiler no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
# Movimientos
@csrf_exempt
def obtener_todos_los_movimientos(request):
    movimientos = Movimiento.objects.all()
    data = {'movimientos': list(movimientos.values())}
    return JsonResponse(data)

@csrf_exempt
def obtener_movimiento(request, movimiento_id):
    movimiento = get_object_or_404(Movimiento, id=movimiento_id)
    data = {'movimiento': {
        'id': movimiento.id,
        'id_alquiler': movimiento.id_alquiler,
        'id_suscripcion': movimiento.id_suscripcion,
        'fecha_movimiento': movimiento.fecha_movimiento,
        'valor': movimiento.valor,
        'id_usuario': movimiento.id_usuario,
        'descripcion': movimiento.descripcion
    }}
    return JsonResponse(data)

@csrf_exempt
def agregar_movimiento(request):
    if request.method == 'POST':
        if request.body:
            try:
                datos = json.loads(request.body)
                id_alquiler = datos.get('id_alquiler')
                id_suscripcion = datos.get('id_suscripcion')
                fecha_movimiento = datos.get('fecha_movimiento')
                valor = datos.get('valor')
                id_usuario = datos.get('id_usuario')
                descripcion = datos.get('descripcion')

                movimiento = Movimiento(id_alquiler_id=id_alquiler, fecha_movimiento=fecha_movimiento, valor=valor, id_usuario_id=id_usuario, descripcion=descripcion, id_suscripcion_id=id_suscripcion)
                movimiento.save()

                return JsonResponse({'mensaje': 'Movimiento agregado correctamente'})
            except json.JSONDecodeError as e:
                return JsonResponse({'error': 'Error al decodificar JSON'}, status=400)
        else:
            return JsonResponse({'error': 'No se proporcionaron datos en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def eliminar_movimiento(request, movimiento_id):
    if request.method == 'DELETE':
        try:
            movimiento = Movimiento.objects.get(id=movimiento_id)
            movimiento.delete()
            return JsonResponse({'mensaje': 'Movimiento eliminado correctamente'})
        except Movimiento.DoesNotExist:
            return JsonResponse({'error': 'El movimiento no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
