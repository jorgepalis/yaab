# Generated by Django 4.2.7 on 2024-01-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_grupocreditopersonal_firma_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupocreditopersonal',
            name='firma_imagen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
