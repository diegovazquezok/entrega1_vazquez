# Generated by Django 4.1.3 on 2022-12-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAuth', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
