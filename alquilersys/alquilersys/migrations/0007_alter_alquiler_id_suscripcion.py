# Generated by Django 5.0.3 on 2024-05-19 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilersys', '0006_alquiler_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='id_suscripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suscripciones', to='alquilersys.suscripcion'),
        ),
    ]
