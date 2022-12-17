# Generated by Django 4.1.2 on 2022-12-17 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLibreria', '0005_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamos'], [2, 'sugerencias']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
