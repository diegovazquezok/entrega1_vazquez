from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# * Creacion y edicion de usuarios/avatars

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Usuario", max_length=20)
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User

        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User

        fields = ["email", "first_name", "last_name", "password1", "password2"]

        help_texts = {k: "" for k in fields}

class AvatarForm(forms.Form):
    
    imagen = forms.ImageField()