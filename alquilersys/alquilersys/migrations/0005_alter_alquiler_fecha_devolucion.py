# Generated by Django 5.0.3 on 2024-05-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilersys', '0004_alquiler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='fecha_devolucion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
