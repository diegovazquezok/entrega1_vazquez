# Generated by Django 4.1.3 on 2022-12-15 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppAuth', '0004_alter_avatar_imagen_alter_avatar_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
