from django.shortcuts import render
from juegos.models import Juego

# Create your views here.

def tabla_juegos(req):
    """ Trae los datos de los juegos desde la BD """
    query   = Juego.objects.all()
    context = {"juegos":query} 
    return render(req, "administrador/tabla_juegos.html", context)