# En tu_app/models.py
from django.db import models

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
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
     

class Meta:
    app_label = 'alquilersys'
