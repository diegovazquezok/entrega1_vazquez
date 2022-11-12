from django.db import models

# Create your models here.
# se crean tres modelos para la libreria
class Libro(models.Model):

    titulo=models.CharField(max_length=50)
    autor_apellido=models.CharField(max_length=40)
    autor_nombre=models.CharField(max_length=40)
    categoria=models.CharField(max_length=40)
    editorial=models.CharField(max_length=40)
    isbn=models.IntegerField()
    año_edicion=models.IntegerField()
    paginas=models.IntegerField()
    precio=models.IntegerField()
    unidad=models.IntegerField()


class Proveedores(models.Model):

    editorial=models.CharField(max_length=40)
    proveedor_direccion=models.CharField(max_length=40)
    proveedor_telefono=models.CharField(max_length=40)
    proveedor_email=models.EmailField()
    proveedor_cuit=models.IntegerField()


class Cliente(models.Model):

    cliente_apellido=models.CharField(max_length=40)
    cliente_nombre=models.CharField(max_length=40)
    cliente_direccion=models.CharField(max_length=40)
    cliente_email=models.EmailField()
    cliente_telefono=models.CharField(max_length=40)
    cliente_cuil=models.IntegerField()


