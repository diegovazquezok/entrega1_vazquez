# Generated by Django 4.1.2 on 2022-11-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_apellido', models.CharField(max_length=40)),
                ('cliente_nombre', models.CharField(max_length=40)),
                ('cliente_direccion', models.CharField(max_length=40)),
                ('cliente_email', models.EmailField(max_length=254)),
                ('cliente_telefono', models.CharField(max_length=40)),
                ('cliente_cuil', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor_apellido', models.CharField(max_length=40)),
                ('autor_nombre', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('editorial', models.CharField(max_length=40)),
                ('isbn', models.IntegerField()),
                ('año_edicion', models.IntegerField()),
                ('paginas', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('unidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editorial', models.CharField(max_length=40)),
                ('proveedor_direccion', models.CharField(max_length=40)),
                ('proveedor_telefono', models.CharField(max_length=40)),
                ('proveedor_email', models.EmailField(max_length=254)),
                ('proveedor_cuit', models.IntegerField()),
            ],
        ),
    ]
