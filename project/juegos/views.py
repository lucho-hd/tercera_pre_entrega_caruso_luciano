from django.shortcuts import render, redirect
from django.contrib import messages
from juegos.models import Juego, Plataforma, Desarrolladora, Editor, Genero
from juegos.forms import JuegosForm, PlataformasForm, DesarrolladorasForm, GenerosForm, EditoresForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from typing import Any

# Create your views here.

class JuegoLista(ListView):
    """ Trae la lista de juegos desde la Base de Datos """
    model = Juego
    context_object_name = "juegos"
    template_name = "juegos/lista_juegos.html"
    
    def get_queryset(self) -> Any:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(titulo__icontains=busqueda)
            )
        return queryset
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        mensaje = "No hubo resultados para tu búsqueda. Prueba con otro juego." if not queryset.exists() else None
        context['mensaje'] = mensaje
        return context


class JuegoDetalle(DetailView):
    """ Muestra la información de un juego en específico mediante su 'pk: int' """
    model = Juego
    context_object_name = "juego"
    template_name = "juegos/detalle_juego.html"


class JuegoCrear(CreateView):
    """ Permite la creación de un juego en la Base de datos """
    model = Juego
    template_name = "juegos/crear_juego.html"
    form_class = JuegosForm
    success_url = reverse_lazy("administrador:tabla_juegos")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el juego es creado """
        messages.success(self.request, 'El juego ha sido creado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el juego. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class JuegoEditar(UpdateView):
    """ Permite la edición de un juego en la Base de datos mediante su <int:pk> """
    model =  Juego
    template_name = "juegos/crear_juego.html"
    form_class = JuegosForm
    success_url = reverse_lazy("administrador:tabla_juegos")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el juego es editado """
        juego = self.get_object()
        messages.success(self.request, f'El juego "{juego}" ha sido actualizado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al editar el juego. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class JuegoEliminar(DeleteView):
    """ Elimina el juego seleccionado de la Base de Datos """
    model = Juego
    success_url = reverse_lazy("administrador:tabla_juegos")

    def delete(self, request):
        juego = self.get_object()
        messages.success(request, f'El juego "{juego}" ha sido eliminado correctamente.')
        return super().delete(request)

    def get(self, request):
        messages.error(request, 'Ocurrió un error al intentar eliminar el juego.')
        return redirect(self.success_url)


#!-------------------------------------- Plataformas ---------------------------------------------------

class PlataformaCrear(CreateView):
    model = Plataforma
    form_class = PlataformasForm
    template_name = "juegos/plataformas/crear_plataforma.html"
    success_url = reverse_lazy("administrador:tabla_plataformas")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el juego es creado """
        messages.success(self.request, 'La plataforma ha sido creada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear la plataforma. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class PlataformaEditar(UpdateView):
    model = Plataforma
    form_class = PlataformasForm
    template_name = "juegos/plataformas/crear_plataforma.html"
    success_url = reverse_lazy("administrador:tabla_plataformas")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el juego es editado """
        plataforma = self.get_object()
        messages.success(self.request, f'La plataforma "{plataforma}" ha sido actualizada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al editar la plataforma. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)