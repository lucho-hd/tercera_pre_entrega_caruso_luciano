from django.urls import path
from administrador.views import (
    tabla_juegos
)

app_name = "administrador"

urlpatterns = [
    path("tabla_juegos", tabla_juegos, name="tabla_juegos"),
]