from django.urls import path
from AppLibreria.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="inicio"),
    path("libros/", libros, name="libros"),
    path("clientes/", clientes, name="clientes"),
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda/resultados/", resultado_busqueda, name="resultado-busqueda"),
    path("proveedores/", proveedores, name="proveedores"),
    path("stock/", Leerstock, name="stock"),
    path("login/", iniciar_sesion, name="auth_login"),
    path("logout/",LogoutView.as_view(template_name='AppLibreria/logout.html'), name="auth_logout"),
    path("register/", registrar_usuario, name="reg_user"),
    path("edit_user/", editar_perfil, name="auth_edit"),
    path("add_avatar/", agregar_avatar, name="auth_avatar"),


]