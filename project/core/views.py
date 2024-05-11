from django.shortcuts import render
from juegos.models import Juego

# Create your views here.
def index(req):
    query   = Juego.objects.all()
    context = {"juegos": query} 
    return render(req, "core/index.html", context)