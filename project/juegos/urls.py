from django.urls import path
from juegos.views import (
    JuegoLista,
    JuegoDetalle,
    JuegoCrear,
    JuegoEditar,
    JuegoEliminar,
)

app_name = "juegos"

urlpatterns = [
    path("lista_juegos",            JuegoLista.as_view(),    name="lista_juegos"),
    path("detalle/<int:pk>",        JuegoDetalle.as_view(),  name="detalle_juego"),
    path("crear_juego",             JuegoCrear.as_view(),    name="crear_juego"),
    path("editar_juego/<int:pk>",   JuegoEditar.as_view(),   name="editar_juego"),
    path("eliminar_juego/<int:pk>", JuegoEliminar.as_view(), name="eliminar_juego"),
]