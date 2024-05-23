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
    """ Crea una nueva plataforma en la BD """
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
    """ Edita la plataforma seleccionada en la BD """
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


class PlataformaEliminar(DeleteView):
    """ Elimina la plataforma seleccionada de la Base de Datos """
    model = Plataforma
    success_url = reverse_lazy("administrador:tabla_plataformas")

    def delete(self, request):
        plataforma = self.get_object()
        messages.success(request, f'La plataforma "{plataforma}" ha sido eliminada correctamente.')
        return super().delete(request)

    def get(self, request):
        messages.error(request, 'Ocurrió un error al intentar eliminar la plataforma.')
        return redirect(self.success_url)


#!-------------------------------------- Desarrolladoras ---------------------------------------------------

class DesarrolladoraCrear(CreateView):
    """ Crea una nueva desarrolladora en la BD """
    model = Desarrolladora
    form_class = DesarrolladorasForm
    template_name = "juegos/desarrolladoras/crear_desarrolladora.html"
    success_url = reverse_lazy("administrador:tabla_desarrolladoras")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando la desarrolladora es creada """
        messages.success(self.request, 'La desarrolladora ha sido creada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear la desarrolladora. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class DesarrolladoraEditar(UpdateView):
    """ Edita la desarrolladora seleccionada en la BD """
    model = Desarrolladora
    form_class = DesarrolladorasForm
    template_name = "juegos/desarrolladoras/crear_desarrolladora.html"
    success_url = reverse_lazy("administrador:tabla_desarrolladoras")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando la desarrolladora es editada """
        desarrolladora = self.get_object()
        messages.success(self.request, f'La desarrolladora "{desarrolladora}" ha sido actualizada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al editar la desarrolladora. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class DesarrolladoraEliminar(DeleteView):
    """ Elimina la desarrolladora seleccionada de la Base de Datos """
    model = Desarrolladora
    success_url = reverse_lazy("administrador:tabla_desarrolladoras")

    def delete(self, request):
        desarrolladora = self.get_object()
        messages.success(request, f'La desarrolladora "{desarrolladora}" ha sido eliminada correctamente.')
        return super().delete(request)

    def get(self, request):
        messages.error(request, 'Ocurrió un error al intentar eliminar la desarrolladora.')
        return redirect(self.success_url)

#!-------------------------------------- Géneros ---------------------------------------------------

class GeneroCrear(CreateView):
    """ Crea un nuevo género en la BD """
    model = Genero
    form_class = GenerosForm
    template_name = "juegos/generos/crear_genero.html"
    success_url = reverse_lazy("administrador:tabla_generos")
    
    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el género es creado """
        messages.success(self.request, 'El género ha sido creado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el género. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)
    

class GeneroEditar(UpdateView):
    """ Edita el género seleccionado en la BD """
    model = Genero
    form_class = GenerosForm
    template_name = "juegos/generos/crear_genero.html"
    success_url = reverse_lazy("administrador:tabla_generos")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el género es editado """
        genero = self.get_object()
        messages.success(self.request, f'El género "{genero}" ha sido actualizado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al editar el género. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class GeneroEliminar(DeleteView):
    """ Elimina el género seleccionado de la Base de Datos """
    model = Genero
    success_url = reverse_lazy("administrador:tabla_generos")

    def delete(self, request):
        genero = self.get_object()
        messages.success(request, f'El género "{genero}" ha sido eliminado correctamente.')
        return super().delete(request)

    def get(self, request):
        messages.error(request, 'Ocurrió un error al intentar eliminar el género.')
        return redirect(self.success_url)

#!-------------------------------------- Editores ---------------------------------------------------

class EditorCrear(CreateView):
    """ Crea un nuevo editor en la BD """
    model = Editor
    form_class = EditoresForm
    template_name = "juegos/editores/crear_editor.html"
    success_url = reverse_lazy("administrador:tabla_editores")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el editor es creado """
        messages.success(self.request, 'El editor ha sido creado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el editor. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class EditorEditar(UpdateView):
    """ Edita el editor seleccionado en la BD """
    model = Editor
    form_class = EditoresForm
    template_name = "juegos/editores/crear_editor.html"
    success_url = reverse_lazy("administrador:tabla_editores")

    def form_valid(self, form):
        """ Devuelve un mensaje de éxito cuando el editor es editado """
        editor = self.get_object()
        messages.success(self.request, f'El editor "{editor}" ha sido actualizado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al editar el editor. Por favor revisa los campos e intenta nuevamente.')
        return super().form_invalid(form)


class EditorEliminar(DeleteView):
    """ Elimina el editor seleccionado de la Base de Datos """
    model = Editor
    success_url = reverse_lazy("administrador:tabla_editores")

    def delete(self, request):
        editor = self.get_object()
        messages.success(request, f'El editor "{editor}" ha sido eliminado correctamente.')
        return super().delete(request)

    def get(self, request):
        messages.error(request, 'Ocurrió un error al intentar eliminar el editor.')
        return redirect(self.success_url)