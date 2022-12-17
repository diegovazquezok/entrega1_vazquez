from django.urls import include, path
from AppLibreria.views import *
from django.contrib.auth.views import LogoutView
from AppAuth.views import *
from django.conf import settings
from django.conf.urls.static import static


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
    path("contacto", contacto, name="contacto"),
    
# * PATHS LOGIN 
    path("login/", iniciar_sesion, name="auth_login"),
    path("logout/",LogoutView.as_view(template_name='AppAuth/logout.html'), name="auth_logout"),
    path("register/", registrar_usuario, name="reg_user"),
    path("edit_user/", editar_perfil, name="auth_edit"),
    path("users/", include('AppAuth.urls', namespace="AppAuth")),
    path('profile_image/', profile, name="add_avatar"),

]