# Generated by Django 4.2.7 on 2023-12-22 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_correoscreditogrupal_monto_vacantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='correoscreditogrupal',
            name='email2',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]