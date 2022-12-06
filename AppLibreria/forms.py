from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirme Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User

        fields = ["username", "email", "password1", "password2"]


    


