# En tu_app/models.py
from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dias = models.DateField()

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

    class Meta:
        app_label = 'alquilersys'
