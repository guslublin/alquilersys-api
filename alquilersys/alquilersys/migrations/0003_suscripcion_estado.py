# Generated by Django 5.0.3 on 2024-05-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilersys', '0002_alter_plan_valor_suscripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscripcion',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=255),
            preserve_default=False,
        ),
    ]