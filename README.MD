# Gamers Guild

Comisión Django 54140

Alumno: Luciano Caruso

## Explicación breve del proyecto
Ecommerce dedicado a la venta de juegos digitales de PS4 y PS5. En un futuro se le van a agregar las secciones de 'Registro', 'Crear cuenta', la opción de agregar al carrito de compras donde el usuario podrá ver los sus productos. 

## Rutas del proyecto

`/`
Página de inicio del sitio web. Muestra una lista de juegos destacados y un slider con ofertas destacadas. Además, incluye un banner con descuentos y ofrece opciones de navegación para explorar los productos disponibles.

`/juegos/lista_juegos`
Muestra la lista de juegos disponibles en el sitio. A futuro se le agregará una sección que permitirá al usuario poder filtrar los juegos por género o tipo.

`/juegos/detalle/ID`
Muestra más información acerca del juego seleccionado, tales como la desarrolladora, fecha de publicación, descripción, etc. 

`/juegos/crear_juego`
Permite al usuario crear un nuevo juego en la Base de datos

`/juegos/editar_juego/ID`
Permite editar el juego seleccionado mediante su ID

`/juegos/eliminar:juego/ID`
Realiza el despliegue de una ventana modal para la confirmación de que juego se quiere eliminar de la Base de datos 

`/administrador/tabla_juegos`
Muestra la lista de juegos que hay en el sitio, permitiendo realizar diferentes acciones como por ejemplo la eliminación y edición de un juego mediante su ID
