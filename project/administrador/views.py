from django.shortcuts import render
from juegos.models import Juego, Plataforma, Desarrolladora, Genero, Editor

# Create your views here.

def tabla_juegos(req):
    """ Trae los datos de los juegos desde la BD """
    query   = Juego.objects.all()
    context = {"juegos":query} 
    return render(req, "administrador/tabla_juegos.html", context)


def tabla_plataformas(req):
    """ Trae los datos de las plataformas desde la BD """
    query   = Plataforma.objects.all()
    context = {"plataformas":query} 
    return render(req, "administrador/tabla_plataformas.html", context)


def tabla_desarrolladoras(req):
    """ Trae los datos de las desarrolladoras desde la BD """
    query    = Desarrolladora.objects.all()
    context = {"desarrolladoras":query} 
    return render(req, "administrador/tabla_desarrolladoras.html", context)


def tabla_generos(req):
    """ Trae los datos de los géneros desde la BD """
    query   = Genero.objects.all()
    context = {"generos":query}
    return render(req, "administrador/tabla_generos.html", context)


def tabla_editores(req):
    """ Trae los datos de los editores desde la BD """
    query   = Editor.objects.all() 
    context = {"editores":query}
    return render(req, "administrador/tabla_editores.html", context)