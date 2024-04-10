# Generated by Django 4.2.7 on 2024-02-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_alter_tipoprestamo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_credito', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Periodo',
                'verbose_name_plural': 'Periodos',
            },
        ),
        migrations.RenameField(
            model_name='tipoprestamo',
            old_name='grupal',
            new_name='tipo_credito',
        ),
        migrations.RemoveField(
            model_name='tipoprestamo',
            name='personal',
        ),
    ]