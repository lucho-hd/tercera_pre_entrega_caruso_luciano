from django.urls import path
from core.views import (
    index,
    acerca,
    CustomLoginView,
    CustomLogoutView,
    crearCuenta,
    perfil,
) 

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("acerca", acerca, name="acerca"),
    path("iniciar-sesion", CustomLoginView.as_view(),  name="iniciar-sesion"),
    path("cerrar-sesion",  CustomLogoutView.as_view(), name="cerrar-sesion"),
    path("crear-cuenta", crearCuenta, name="crear-cuenta"),
    path("perfil", perfil, name="perfil" )
]