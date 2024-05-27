# Gamers Guild

Comisión Django 54140

Alumno: Luciano Caruso

## Explicación breve del proyecto
Ecommerce dedicado a la venta de juegos digitales de PS4 y PS5. En un futuro se le van a agregar las secciones de 'Registro', 'Crear cuenta', la opción de agregar al carrito de compras donde el usuario podrá ver sus productos. 

## Rutas del proyecto

`/`
Página de inicio del sitio web. Muestra una lista de juegos destacados y un slider con ofertas destacadas. Además, incluye un banner con descuentos y ofrece opciones de navegación para explorar los productos disponibles.
<br>
![Página de inicio de Gamers Guild](/capturas_sitio/inicio.png)
<br>
`/juegos/lista_juegos`
Muestra la lista de juegos disponibles en el sitio. A futuro se le agregará una sección que permitirá al usuario poder filtrar los juegos por género o tipo.
![Lista de juegos](/capturas_sitio/lista_juegos.png)
<br>
`/juegos/detalle/ID`
Muestra más información acerca del juego seleccionado, tales como la desarrolladora, fecha de publicación, descripción, etc.
<br>
![Detalle de un juego](/capturas_sitio/detalle.png)
<br>
`/administrador/tabla_juegos`
Muestra la lista de juegos que hay en el sitio, permitiendo realizar diferentes acciones como por ejemplo la eliminación y edición de un juego mediante su ID
<br>
![Panel de administración](/capturas_sitio/panel_admin.png)
<br>
`/juegos/crear_juego`
Permite al usuario crear un nuevo juego en la Base de datos
<br>
![Crear un juego](/capturas_sitio/crear_juego.png)
<br>
`/juegos/editar_juego/ID`
Permite editar el juego seleccionado mediante su ID
<br>
![Editar un juego](/capturas_sitio/editar_juego.png)
<br>
`/juegos/eliminar_juego/ID`
Realiza el despliegue de una ventana modal para la confirmación de que juego se quiere eliminar de la Base de datos 
<br>
![Eliminar un juego](/capturas_sitio/eliminar_juego.png)
<br>
`/iniciar-sesion`
Formulario para iniciar sesión en el sitio, si las credenciales ingresadas son correctas el usuario será dado de alta 
<br>
![Formulario de iniciar sesión](/capturas_sitio/iniciar-sesion.png)
<br>
`/crear-cuenta`
Formulario para registrarse en el sitio, si los campos solicitados son correctos se lo redireccionará al usuario a la vista de iniciar sesión
<br>
![Formulario para crear una nueva cuenta](/capturas_sitio/crear.cuenta.png)
