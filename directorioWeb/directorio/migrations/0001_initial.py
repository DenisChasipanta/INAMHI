# Generated by Django 4.2.2 on 2023-08-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_registro', models.IntegerField(unique=True)),
                ('nombres_apellidos', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=10)),
                ('puesto_institucional', models.CharField(max_length=255)),
                ('unidad_pertenece', models.CharField(max_length=255)),
                ('direccion_institucional', models.CharField(max_length=255)),
                ('ciudad_labora', models.CharField(max_length=255)),
                ('telefono_institucional', models.CharField(max_length=255)),
                ('extension_telefonica', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
        ),
    ]