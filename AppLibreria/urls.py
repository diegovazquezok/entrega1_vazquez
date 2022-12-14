from django.urls import path
from AppLibreria.views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path("libros/", libros, name="libros"),
    
    path("clientes/", clientes, name="clientes"),
    path("clientes/Clist/", ClientesList.as_view(), name= "Clist"),
    path("clientes/Cdetalle/<pk>/", ClientesDetalle.as_view(), name="Cdetalle"),
    path("clientes/Ceditar/<pk>/", ClientesUpdate.as_view(), name="Ceditar"),
    path("clientes/Cborrar/<pk>/", ClientesDelete.as_view(), name="Cborrar"),
    
    
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda/resultados/", resultado_busqueda, name="resultado-busqueda"),
    
    path("proveedores/", proveedores, name="proveedores"),
    path("proveedores/Plist", ProveedoresList.as_view(), name="Plist"),
    path("proveedores/Pdetalle/<pk>/", ProveedoresDetalle.as_view(), name="Pdetalle"),
    path("proveedores/Peditar/<pk>/", ProveedoresUpdate.as_view(), name="Peditar"),
    path("proveedores/Pborrar/<pk>/", ProveedoresDelete.as_view(), name="Pborrar"),
    
    path("stock/", Leerstock, name="stock"),
    path("stock/borrar/<id>/", eliminar_libro, name="borrar"),
    path("stock/editar/<id>/", editar_libro, name="editar"),
    path("acerca", acerca, name="acerca"),



]