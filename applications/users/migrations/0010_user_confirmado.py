# Generated by Django 4.2.7 on 2023-12-07 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_aviso_privacidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
