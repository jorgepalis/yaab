# Generated by Django 4.2.7 on 2024-02-23 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_remove_simuladorprueba_nombre_prestamo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='tiempo_pago',
        ),
    ]