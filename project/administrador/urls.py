from django.urls import path
from administrador.views import (
    tabla_juegos,
    tabla_plataformas,
)

app_name = "administrador"

urlpatterns = [
    path("tabla_juegos",      tabla_juegos,      name="tabla_juegos"),
    path("tabla_plataformas", tabla_plataformas, name="tabla_plataformas"),
]