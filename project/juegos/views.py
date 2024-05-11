from django.shortcuts import render
from juegos.models import Juego

# Create your views here.

def lista_juegos(req):
    """ Trae la lista de juegos desde la Base de Datos """
    query   = Juego.objects.all()
    context = {"juegos": query} 
    return render(req, "juegos/lista_juegos.html", context)

def detalle_juego(req, id: int):
    """ Muestra la información de un juego en específico mediante su 'id: int' """
    query   = Juego.objects.get(id=id)
    context = {"juego":query} 
    return render(req, "juegos/detalle_juego.html", context)
