# Generated by Django 4.2.7 on 2024-04-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0066_registrocreditosmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocreditosmodel',
            name='identificador_unico',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]