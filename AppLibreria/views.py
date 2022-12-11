from AppLibreria.forms import *
from AppLibreria.models import *
from django.shortcuts import render, redirect

# * Imports de Login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request,"AppLibreria/index.html", {"imagen_url": imagen_url})


def libros(request):

    if request.method == "POST":
        formulario = libroFormulario(request.POST)

        print(formulario)

        if formulario.is_valid():

            informacion =formulario.cleaned_data

            libro = Libro (
                titulo=informacion['titulo'],
                autor_apellido=informacion['autor_apellido'],
                autor_nombre=informacion['autor_nombre'],
                categoria=informacion['categoria'],
                editorial=informacion['editorial'],
                isbn=informacion['isbn'],
                año_edicion=informacion['año_edicion'],
                paginas=informacion['paginas'],
                precio=informacion['precio'],
                unidad=informacion['unidad'],
            )
            libro.save()

            return render (request, "AppLibreria/libros.html" )
    else:
            formulario= libroFormulario()

    contexto = {"formulario":formulario}    
    return render(request,"AppLibreria/libros.html", contexto )



def clientes(request):

    if request.method == "POST":
        formulario = clienteFormulario(request.POST)

        print(formulario)

        if formulario.is_valid():

            informacion =formulario.cleaned_data

            cliente = Cliente (
                cliente_apellido=informacion['cliente_apellido'],
                cliente_nombre=informacion['cliente_nombre'],
                cliente_direccion=informacion['cliente_direccion'],
                cliente_email=informacion['cliente_email'],
                cliente_telefono=informacion['cliente_telefono'],
                cliente_cuil=informacion['cliente_cuil'],
            )
            cliente.save()

            return render (request, "AppLibreria/clientes.html" )
    else:

            formulario= clienteFormulario()

    contexto = {"formulario":formulario}    

    return render(request,"AppLibreria/clientes.html", contexto)



def busqueda(request):
    return render(request,"AppLibreria/busqueda_libros.html")

def resultado_busqueda(request):
    titulo= request.GET['titulo']

    libros = Libro.objects.filter(titulo__icontains=titulo)
    
    
    return render(request, "AppLibreria/resultado_busqueda.html", {"libros": libros})



@login_required
def proveedores(request):


    if request.method == "POST":
        formulario = proveedoresFormulario(request.POST)

        print(formulario)

        if formulario.is_valid():

            informacion =formulario.cleaned_data

            proveedores = Proveedores (
                editorial=informacion['editorial'],
                proveedor_direccion=informacion['proveedor_direccion'],
                proveedor_email=informacion['proveedor_email'],
                proveedor_telefono=informacion['proveedor_telefono'],
                proveedor_cuit=informacion['proveedor_cuit'],
            )
            proveedores.save()

            return render (request, "AppLibreria/clientes.html" )
    else:

            formulario= proveedoresFormulario()

    contexto = {"formulario":formulario}    


    return render(request,"AppLibreria/proveedores.html", contexto)




def Leerstock(request):

    stock = Libro.objects.all()

    contexto = {"Leerstock":stock}

    return render(request, "AppLibreria/Leerstock.html", contexto)


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
                return render (request, "AppLibreria/login.html", {"form": formulario1, "errors":"Credenciales Invalidas"})
        else:
            return render (request, "AppLibreria/login.html", {"form": formulario1, "errors": formulario1.errors})

    formulario = AuthenticationForm()

    return render (request, "AppLibreria/login.html", {"form": formulario})


def registrar_usuario(request):

    if request.method == "POST":

        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            return redirect ("inicio")
        
        else:
            return render (request, "AppLibreria/register.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()

    return render (request, "AppLibreria/register.html", {"form": formulario})

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
            return render(request, "AppLibreria/editarperfil.html", {"form":formulario, "errors":formulario.errors})

    else:

        formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name}) 
        return render (request, "AppLibreria/editarperfil.html", {"form":formulario})


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
            return render (request, "AppLibreria/agregar_avatar.html", {"form": formulario, "errors": formulario.errors})

    formulario = AvatarForm()

    return render(request, "AppLibreria/agregar_avatar.html", {"form": formulario})





