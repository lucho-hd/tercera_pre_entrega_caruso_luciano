from django.shortcuts import render, redirect
from juegos.models import Juego, Plataforma, Desarrolladora, Genero, Editor
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def tabla_juegos(req):
    """ Trae los datos de los juegos desde la BD """
    if not req.user.is_staff:
        messages.error(req, 'No tienes los permisos suficientes para realizar esta acción.')
        return redirect('core:index')
    query   = Juego.objects.all()
    context = {"juegos":query} 
    return render(req, "administrador/tabla_juegos.html", context)

@login_required
def tabla_plataformas(req):
    """ Trae los datos de las plataformas desde la BD """
    if not req.user.is_staff:
        messages.error(req, 'No tienes los permisos suficientes para realizar esta acción.')
        return redirect('core:index')
    query   = Plataforma.objects.all()
    context = {"plataformas":query} 
    return render(req, "administrador/tabla_plataformas.html", context)

@login_required
def tabla_desarrolladoras(req):
    """ Trae los datos de las desarrolladoras desde la BD """
    if not req.user.is_staff:
        messages.error(req, 'No tienes los permisos suficientes para realizar esta acción.')
        return redirect('core:index')
    query    = Desarrolladora.objects.all()
    context = {"desarrolladoras":query} 
    return render(req, "administrador/tabla_desarrolladoras.html", context)

@login_required
def tabla_generos(req):
    """ Trae los datos de los géneros desde la BD """
    if not req.user.is_staff:
        messages.error(req, 'No tienes los permisos suficientes para realizar esta acción.')
        return redirect('core:index')
    query   = Genero.objects.all()
    context = {"generos":query}
    return render(req, "administrador/tabla_generos.html", context)

@login_required
def tabla_editores(req):
    """ Trae los datos de los editores desde la BD """
    if not req.user.is_staff:
        messages.error(req, 'No tienes los permisos suficientes para realizar esta acción.')
        return redirect('core:index')
    query   = Editor.objects.all() 
    context = {"editores":query}
    return render(req, "administrador/tabla_editores.html", context)