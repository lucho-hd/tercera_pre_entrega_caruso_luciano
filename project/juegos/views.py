from django.shortcuts import render, redirect
from juegos.models import Juego
from juegos.forms import JuegosForm

# Create your views here.

def lista_juegos(req):
    """ Trae la lista de juegos desde la Base de Datos """
    busqueda = req.GET.get("busqueda", None)
    if busqueda:
        query = Juego.objects.filter(titulo__icontains=busqueda)
    else:
        query = Juego.objects.all()
    
    if not query.exists():
        mensaje = "No hubo resultados para tu búsqueda. Prueba con otro juego."
    else:
        mensaje = None
    context = {"juegos": query, "mensaje": mensaje} 
    return render(req, "juegos/lista_juegos.html", context)

def detalle_juego(req, id: int):
    """ Muestra la información de un juego en específico mediante su 'id: int' """
    query   = Juego.objects.get(id=id)
    context = {"juego":query} 
    return render(req, "juegos/detalle_juego.html", context)
