# Generated by Django 5.0.3 on 2024-05-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilersys', '0005_alter_alquiler_fecha_devolucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=255),
            preserve_default=False,
        ),
    ]
