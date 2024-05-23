from django.urls import path
from administrador.views import (
    tabla_juegos,
    tabla_plataformas,
    tabla_desarrolladoras,
    tabla_generos,
    tabla_editores,
)

app_name = "administrador"

urlpatterns = [
    path("tabla_juegos",          tabla_juegos,          name="tabla_juegos"),
    path("tabla_plataformas",     tabla_plataformas,     name="tabla_plataformas"),
    path("tabla_desarrolladoras", tabla_desarrolladoras, name="tabla_desarrolladoras"),
    path("tabla_generos",         tabla_generos,         name="tabla_generos"),
    path("tabla_editores",        tabla_editores,        name="tabla_editores"),
]