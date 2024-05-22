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