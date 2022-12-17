from AppLibreria.forms import *
from AppLibreria.models import *
from django.shortcuts import render, redirect
from AppAuth.models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# * Imports de Login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request,"AppLibreria/index.html")


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

            return render (request, "AppLibreria/libros.html")
    else:
            formulario= libroFormulario()

    contexto = {"formulario":formulario}   
   
    return render(request,"AppLibreria/libros.html", contexto)



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

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()

    return redirect("stock")


def editar_libro(request, id):
    libro = Libro.objects.get(id=id)

    if request.method == "POST":
        formulario = libroFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            libro.titulo = data ["titulo"]
            libro.autor_apellido = data ["autor_apellido"]
            libro.autor_nombre = data ["autor_nombre"]
            libro.categoria = data ["categoria"]
            libro.editorial = data ["editorial"]
            libro.isbn = data ["isbn"]
            libro.año_edicion = data ["año_edicion"]
            libro.paginas = data ["paginas"]
            libro.precio = data ["precio"]
            libro.unidad = data ["unidad"]
            libro.save()
            return redirect("stock")
        else:
            return render(request, "AppLibreria/editar_libro.html", {"formulario": formulario, "errores": formulario.errors})    

    else:
        formulario = libroFormulario(initial={"titulo": libro.titulo,
                                              "autor_apellido": libro.autor_apellido,
                                              "autor_nombre": libro.autor_nombre,
                                              "categoria": libro.categoria, 
                                              "editorial": libro.editorial,
                                              "isbn": libro.isbn,
                                              "año_edicion": libro.año_edicion,
                                              "paginas":libro.paginas, 
                                              "precio": libro.precio, 
                                              "unidad": libro.unidad})
        return render(request, "AppLibreria/editar_libro.html", {"formulario": formulario, "errores": ""})

def acerca(request):
    return render(request,"AppLibreria/acerca.html")

class ProveedoresList(ListView):
    model = Proveedores
    template_name = "AppLibreria/proveedores_list.html"

class ProveedoresDetalle(DetailView):
    model = Proveedores
    template_name = "AppLibreria/proveedores_detalle.html"

class ProveedoresUpdate(UpdateView):
    
    model = Proveedores
    success_url = "/libreria/proveedores/"
    fields = ["proveedor_direccion", "proveedor_email", "proveedor_telefono"]

class ProveedoresDelete(DeleteView):
    
    model = Proveedores
    success_url = "/libreria/proveedores/"


class ClientesList(ListView):
    model = Cliente
    template_name = "AppLibreria/Clientes_list.html"

class ClientesDetalle(DetailView):
    model = Cliente
    template_name = "AppLibreria/cliente_detalle.html"

class ClientesUpdate(UpdateView):
    
    model = Cliente
    success_url = "/libreria/clientes/"
    fields = ["cliente_direccion", "cliente_email", "cliente_telefono"]

class ClientesDelete(DeleteView):
    
    model = Cliente
    success_url = "/libreria/clientes/"
