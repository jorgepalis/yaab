# Generated by Django 4.2.7 on 2024-01-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_alter_user_imagen_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]