from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f"{self.titulo} --> {self.editorial} --> ${self.precio} --> Cant: {self.unidad}"



class Proveedores(models.Model):

    editorial=models.CharField(max_length=40)
    proveedor_direccion=models.CharField(max_length=40)
    proveedor_telefono=models.CharField(max_length=40)
    proveedor_email=models.EmailField()
    proveedor_cuit=models.IntegerField()

    def __str__(self):
        return f"{self.editorial} --> Tel: {self.proveedor_telefono} --> {self.proveedor_email} --> CUIT: {self.proveedor_cuit}"


class Cliente(models.Model):

    cliente_apellido=models.CharField(max_length=40)
    cliente_nombre=models.CharField(max_length=40)
    cliente_direccion=models.CharField(max_length=40)
    cliente_email=models.EmailField()
    cliente_telefono=models.CharField(max_length=40)
    cliente_cuil=models.IntegerField()

    def __str__(self):
        return f"{self.cliente_apellido}, {self.cliente_nombre} --> Tel:  {self.cliente_telefono} --> {self.cliente_email} --> CUIL: {self.cliente_cuil}"
