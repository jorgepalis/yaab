# Generated by Django 4.2.7 on 2024-02-23 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_simuladorprueba'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simuladorprueba',
            old_name='tipo_prestamo',
            new_name='nombre_prestamo',
        ),
    ]