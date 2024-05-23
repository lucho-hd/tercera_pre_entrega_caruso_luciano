from django.urls import path
from juegos.views import (
    JuegoLista,
    JuegoDetalle,
    JuegoCrear,
    JuegoEditar,
    JuegoEliminar,
    PlataformaCrear,
    PlataformaEditar,
    PlataformaEliminar,
    DesarrolladoraCrear,
    DesarrolladoraEditar,
    DesarrolladoraEliminar,
    GeneroCrear,
    GeneroEditar,
    GeneroEliminar,
    EditorCrear,
    EditorEditar,
    EditorEliminar,
)

app_name = "juegos"

urlpatterns = [
    path("lista_juegos",                     JuegoLista.as_view(),                name="lista_juegos"),
    path("detalle/<int:pk>",                 JuegoDetalle.as_view(),              name="detalle_juego"),
    path("crear_juego",                      JuegoCrear.as_view(),                name="crear_juego"),
    path("editar_juego/<int:pk>",            JuegoEditar.as_view(),               name="editar_juego"),
    path("eliminar_juego/<int:pk>",          JuegoEliminar.as_view(),             name="eliminar_juego"),

    #!------------------------- Urls para plataformas ---------------------------------------------
    path("crear_plataforma",                 PlataformaCrear.as_view(),           name="crear_plataforma"),
    path("editar_plataforma/<int:pk>",       PlataformaEditar.as_view(),          name="editar_plataforma"),
    path("eliminar_plataforma/<int:pk>",     PlataformaEliminar.as_view(),        name="eliminar_plataforma"),

    #!------------------------- Urls para desarrolladoras -----------------------------------------
    path("crear_desarrolladora",             DesarrolladoraCrear.as_view(),       name="crear_desarrolladora"),
    path("editar_desarrolladora/<int:pk>",   DesarrolladoraEditar.as_view(),      name="editar_desarrolladora"),
    path("eliminar_desarrolladora/<int:pk>", DesarrolladoraEliminar.as_view(),    name="eliminar_desarrolladora"),

    #!------------------------- Urls para géneros -------------------------------------------------
    path("crear_genero",                     GeneroCrear.as_view(),               name="crear_genero"),
    path("editar_genero/<int:pk>",           GeneroEditar.as_view(),              name="editar_genero"),
    path("eliminar_genero/<int:pk>",         GeneroEliminar.as_view(),            name="eliminar_genero"),

    #!------------------------- Urls para editores -----------------------------------------------
    path("crear_editor",                     EditorCrear.as_view(),               name="crear_editor"),
    path("editar_editor/<int:pk>",           EditorEditar.as_view(),              name="editar_editor"),
    path("eliminar_editor/<int:pk>",         EditorEliminar.as_view(),            name="eliminar_editor"),

]   

