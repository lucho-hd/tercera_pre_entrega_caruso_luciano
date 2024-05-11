from django.urls import path
from juegos.views import (
    lista_juegos,
    detalle_juego
)

app_name = "juegos"

urlpatterns = [
    path("lista_juegos", lista_juegos, name="lista_juegos"),
    path("detalle/<int:id>", detalle_juego, name="detalle_juego" ),
]