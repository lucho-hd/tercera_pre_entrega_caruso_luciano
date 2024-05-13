from django.urls import path
from juegos.views import (
    lista_juegos,
    detalle_juego,
    crear_juego,
    editar_juego,
    eliminar_juego,
)

app_name = "juegos"

urlpatterns = [
    path("lista_juegos",             lista_juegos,   name="lista_juegos"),
    path("detalle/<int:id>",         detalle_juego,  name="detalle_juego"),
    path("crear_juego"     ,         crear_juego,    name="crear_juego"),  # type: ignore
    path("editar_juego/<int:id>",    editar_juego,   name="editar_juego"),  
    path("eliminar_juego/<int:id>",  eliminar_juego, name="eliminar_juego"), # type: ignore
]