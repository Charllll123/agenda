# Generated by Django 3.2.12 on 2023-12-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, unique=True)),
                ('apellido', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono_1', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('telefono_2', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('compañia', models.CharField(blank=True, max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
