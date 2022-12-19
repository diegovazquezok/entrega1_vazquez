![portada](banner.jpg)

Video explicativo proyecto : https://drive.google.com/drive/folders/1YF5grSG8EnjnjUJ-TcOAziAlKtmKeQdj?usp=sharing


# BOOK STORE


## Entrega de proyecto final para CoderHouse


El proyecto fue pensado como una página que puede ser utilizada para el manejo interno de un comercio de libros. Para esto los usuarios pueden crear base de datos acerca de __stock de libros, clientes y proveedores__. También se puede realizar búsqueda de stock por título de libros.

Con un usuario de administrador se podran crear objetos nuevos de stock, carga de proveedores y clientes.

Para realizar el uso de consulta de libros no hace falta crearse un usuario.

---

## FUNCIONAMIENTO 📋

La página posee las siguientes funcionalidades:

* LIBROS: en esta sección se crea la base de datos de los libros en stock por medio de un formulario que posee los siguientes requisitos:

    * TITULO
    * NOMBRE DE AUTOR
    * APELLIDO DE AUTOR
    * CATEGORIA
    * ISBN
    * AÑO DE EDICIÓN
    * CANTIDAD DE PÁGINAS
    * PRECIO
    * UNIDAD DE STOCK

    Una vez cargados los requisitos del formulario, por medio del submit *CARGAR* se realizar el registro en la base de datos. 

* BUSQUEDA: en el apartado busqueda, se pueden realizar busqueda de libros en stock a partir del titulo. Una vez ingresado alguna palabra clave o titulo completo y presionado el submit *BUSCAR* se devolveran los registros encontrados en la base de datos relacionados a la busqueda, junto con otros datos del libro. 

* CLIENTES: en esta sección se crea la base de datos de los clientes por medio de un formulario que posee los siguientes requisitos:

    * NOMBRE
    * APELLIDO
    * DIRECCION
    * EMAIL
    * TELEFONO
    * CUIL

    Una vez cargados los requisitos del formulario, por medio del submit *CARGAR* se realizar el registro en la base de datos. Luego, se podran listar, editar y borrar los datos que ya esten cargados.


* PROVEEDORES: en esta sección se crea la base de datos de los proveedores por medio de un formulario que posee los siguientes requisitos:

    * EDITORIAL
    * DIRECCION
    * EMAIL
    * TELEFONO
    * CUIT

    Una vez cargados los requisitos del formulario, por medio del submit *CARGAR* se realizar el registro en la base de datos. Luego, se podran listar, editar y borrar los datos que ya esten cargados.

* REGISTER/LOGIN/LOGOUT/AVATAR: Esta apliacion sirve para manejo de acceso de usuarios, creacion de cuentas nuevas y edicion de las mismas, como asi tambien para cambiar imagen de perfil. Los usuarios administradores son los que tendran acceso a las vistas para hacer cargas de stock, clientes y proveedores a la base de datos.

* CONTACTO/MENSAJERIA: Funcion que sirve para enviar un reclamo, consulta o sugerencia como un cliente a los administradores de la Bookstore.

* VISTA ACERCA: Se crea la vista "Acerca" donde hay informacion de los desarrolladores del proyecto.

---

## ENTORNO DE DESARROLLO 📋

Esta versión fue desarrollada en:

* Python 3.10.6
* Django 4.1.2

---

## COMPONENTES 🔧

Página principal:

http://127.0.0.1:8000/

Página registro de libros:

http://127.0.0.1:8000/libros/

Página de busqueda de libros:

http://127.0.0.1:8000/libros/

Página de registro de clientes:

http://127.0.0.1:8000/clientes/

Página de registro de proveedores:

http://127.0.0.1:8000/proveedores/

Página login:

http://127.0.0.1:8000/login/

Página logout:

http://127.0.0.1:8000/logout/

Página registro usuarios:

http://127.0.0.1:8000/register/

Página de edicion de usuario:

http://127.0.0.1:8000/edit_user/

Página cambio de imagen perfil:

http://127.0.0.1:8000/profile_image/

Página cambio de contraseña:

http://127.0.0.1:8000/users/change_password/

Página de contacto:

http://127.0.0.1:8000/contacto

Página 'Acerca':

http://127.0.0.1:8000/acerca


---

## VERSION 📌

FINAL 1.0

---

## CREADOR ✒️
Diego Javier Vazquez 
(Desarrollo principal de la web, vista "Acerca" y funciones (Búsqueda, Libros, Clientes, Stock y Proveedores)

---
## Colaboradores ✒️
Juan Pablo Delucca
(Desarrollo aplicación Register/Login/Logout/Avatar)

Lucio Herrera
(Desarrollo mensajeria "Contacto")

---

## LICENCIA 📄

Este proyecto no está bajo Licencia.
