from django.urls import path
from juegos.views import (
    lista_juegos
)

app_name = "juegos"

urlpatterns = [
    path("lista_juegos", lista_juegos, name="lista_juegos")
]