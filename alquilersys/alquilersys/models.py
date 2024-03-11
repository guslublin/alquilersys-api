# En tu_app/models.py
from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)

    class Meta:
        app_label = 'alquilersys'
