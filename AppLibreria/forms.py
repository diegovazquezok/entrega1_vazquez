from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto

class libroFormulario(forms.Form):

    titulo=forms.CharField()
    autor_apellido=forms.CharField()
    autor_nombre=forms.CharField()
    categoria=forms.CharField()
    editorial=forms.CharField()
    isbn=forms.IntegerField()
    año_edicion=forms.IntegerField()
    paginas=forms.IntegerField()
    precio=forms.IntegerField()
    unidad=forms.IntegerField()


class clienteFormulario(forms.Form):

    cliente_apellido=forms.CharField()
    cliente_nombre=forms.CharField()
    cliente_direccion=forms.CharField()
    cliente_email=forms.EmailField()
    cliente_telefono=forms.CharField()
    cliente_cuil=forms.IntegerField()

class proveedoresFormulario(forms.Form):

    editorial=forms.CharField()
    proveedor_direccion=forms.CharField()
    proveedor_telefono=forms.CharField()
    proveedor_email=forms.EmailField()
    proveedor_cuit=forms.IntegerField()

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'