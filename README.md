![portada](banner.jpg)


# BOOK STORE


## Primer entrega del proyecto final de Python de Coder House


El proyecto fue pensado como una página que puede ser utilizada para el manejo interno de un comercio de libros. Para esto los usuarios pueden crear base de datos acerca de __stock de libros, clientes y proveedores__. También se puede realizar búsqueda de stock por título de libros. 

Para realizar el uso no hace falta crearse un usuario.

---

## FUNCIONAMIENTO 📋

La página, en esta primera version,  posee 4 funcionalidades:

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

    Una vez cargados los requisitos del formulario, por medio del submit *CARGAR* se realizar el registro en la base de datos.


* PROVEEDORES: en esta sección se crea la base de datos de los proveedores por medio de un formulario que posee los siguientes requisitos:

    * EDITORIAL
    * DIRECCION
    * EMAIL
    * TELEFONO
    * CUIT

    Una vez cargados los requisitos del formulario, por medio del submit *CARGAR* se realizar el registro en la base de datos.

---

## ENTORNO DE DESARROLLO 📋

Esta versión fue desarrollada en:

* Python 3.10.6
* Django 4.1.2

---

## COMPONENTES 🔧

Página principal:

http://127.0.0.1:8000/libreria/

Página registro de libros:

http://127.0.0.1:8000/libreria/libros/

Página de busqueda de libros:

http://127.0.0.1:8000/libreria/libros/

Página de registro de clientes:

http://127.0.0.1:8000/libreria/clientes/

Página de registro de proveedores:

http://127.0.0.1:8000/libreria/proveedores/

---

## VERSION 📌
Primera version

---

## CREADOR ✒️
Diego Javier Vazquez

---

## LICENCIA 📄

Este proyecto no está bajo Licencia.

