# Generated by Django 4.2.7 on 2024-01-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_grupocreditopersonal_firma_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupocreditopersonal',
            name='firma_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='firma/'),
        ),
    ]