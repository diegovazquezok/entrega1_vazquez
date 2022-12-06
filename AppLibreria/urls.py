from django.urls import path
from AppLibreria.views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path("libros/", libros, name="libros"),
    path("clientes/", clientes, name="clientes"),
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda/resultados/", resultado_busqueda, name="resultado-busqueda"),
    path("proveedores/", proveedores, name="proveedores"),
    path("stock/", Leerstock, name="stock"),
    path("stock/borrar/<id>/", eliminar_libro, name="borrar"),
    path("stock/editar/<id>/", editar_libro, name="editar"),



]