from django.shortcuts import render
from juegos.models import Juego

# Create your views here.

def lista_juegos(req):
    query   = Juego.objects.all()
    context = {"juegos": query} 
    return render(req, "juegos/lista_juegos.html", context)