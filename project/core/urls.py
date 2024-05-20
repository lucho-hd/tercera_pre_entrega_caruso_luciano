from django.urls import path
from core.views import (
    index,
    CustomLoginView,
    CustomLogoutView,
    crearCuenta,
) 

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("iniciar-sesion", CustomLoginView.as_view(),  name="iniciar-sesion"),
    path("cerrar-sesion",  CustomLogoutView.as_view(), name="cerrar-sesion"),
    path("crear-cuenta", crearCuenta, name="crear-cuenta"),
]