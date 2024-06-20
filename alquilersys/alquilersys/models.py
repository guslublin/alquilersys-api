# En tu_app/models.py
from django.db import models

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    dias = models.IntegerField(default=0) 

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=128) 

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255)
    resumen = models.CharField(max_length=255)
    fecha_entrada = models.DateField()
    cantidad = models.IntegerField(default=0) 
    disponible = models.BooleanField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_usuario_alta = models.ForeignKey(Usuario, on_delete=models.CASCADE)   
     
class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_contrato = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField()
    estado = models.CharField(max_length=255)
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Alquiler(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=255)
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, related_name='suscripciones')
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Movimiento(models.Model):
    id = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, null=True)
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, null=True)
    fecha_movimiento = models.DateField()
    valor = models.IntegerField(default=0)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)


class Meta:
    app_label = 'alquilersys'
