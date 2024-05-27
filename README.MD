# Gamers Guild

Comisión Django 54140

Alumno: Luciano Caruso

## Explicación breve del proyecto
Ecommerce dedicado a la venta de juegos digitales de PS4 y PS5. En un futuro se le van a agregar las secciones de 'Registro', 'Crear cuenta', la opción de agregar al carrito de compras donde el usuario podrá ver sus productos. 

## Rutas del proyecto

`/`
Página de inicio del sitio web. Muestra una lista de juegos destacados y un slider con ofertas destacadas. Además, incluye un banner con descuentos y ofrece opciones de navegación para explorar los productos disponibles.
![Página de inicio de Gamers Guild](/capturas_sitio/inicio.png)

`/juegos/lista_juegos`
Muestra la lista de juegos disponibles en el sitio. A futuro se le agregará una sección que permitirá al usuario poder filtrar los juegos por género o tipo.
![Lista de juegos](/capturas_sitio/lista_juegos.png)

`/juegos/detalle/ID`
Muestra más información acerca del juego seleccionado, tales como la desarrolladora, fecha de publicación, descripción, etc.
![Detalle de un juego](/capturas_sitio/detalle.png)

`/administrador/tabla_juegos`
Muestra la lista de juegos que hay en el sitio, permitiendo realizar diferentes acciones como por ejemplo la eliminación y edición de un juego mediante su ID
![Panel de administración](/capturas_sitio/panel_admin.png)

`/juegos/crear_juego`
Permite al usuario crear un nuevo juego en la Base de datos
![Crear un juego](/capturas_sitio/crear_juego.png)

`/juegos/editar_juego/ID`
Permite editar el juego seleccionado mediante su ID
![Editar un juego](/capturas_sitio/editar_juego.png)

`/juegos/eliminar_juego/ID`
Realiza el despliegue de una ventana modal para la confirmación de que juego se quiere eliminar de la Base de datos 
![Eliminar un juego](/capturas_sitio/eliminar_juego.png)

`/iniciar-sesion`
Formulario para iniciar sesión en el sitio, si las credenciales ingresadas son correctas el usuario será dado de alta 
![Formulario de iniciar sesión](/capturas_sitio/iniciar-sesion.png)

`/crear-cuenta`
Formulario para registrarse en el sitio, si los campos solicitados son correctos se lo redireccionará al usuario a la vista de iniciar sesión
![Formulario para crear una nueva cuenta](/capturas_sitio/crear.cuenta.png)
