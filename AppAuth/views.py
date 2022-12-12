from django.shortcuts import render
from AppAuth.forms import *
from AppAuth.models import *
from django.shortcuts import render, redirect

# * Imports de Login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


# * REGISTER | LOGIN | LOGOUT | EDIT

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":

        formulario1 = AuthenticationForm(request, data = request.POST)

        if formulario1.is_valid():
            data = formulario1.cleaned_data

            user = authenticate(username = data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect ("inicio")
            
            else:
                return render (request, "AppAuth/login.html", {"form": formulario1, "errors":"Credenciales Invalidas"})
        else:
            return render (request, "AppLAuth/login.html", {"form": formulario1, "errors": formulario1.errors})

    formulario = AuthenticationForm()

    return render (request, "AppAuth/login.html", {"form": formulario})


def registrar_usuario(request):

    if request.method == "POST":

        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            return redirect ("inicio")
        
        else:
            return render (request, "AppAuth/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()

    return render (request, "AppAuth/register.html", {"form": formulario})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()    

            return redirect("inicio")

        else:
            return render(request, "AppAuth/editarperfil.html", {"form":formulario, "errors":formulario.errors})

    else:

        formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name}) 
        return render (request, "AppAuth/editarperfil.html", {"form":formulario})


@login_required
def agregar_avatar(request):

    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("inicio")

        else:
            return render (request, "AppAuth/agregar_avatar.html", {"form": formulario, "errors": formulario.errors})

    formulario = AvatarForm()

    return render(request, "AppAuth/agregar_avatar.html", {"form": formulario})