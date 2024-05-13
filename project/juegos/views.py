from django.shortcuts import render, redirect
from django.contrib import messages
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


def crear_juego(req):
    if req.method == "POST": # POST
        form = JuegosForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req, 'El juego ha sido creado exitosamente')
            return redirect("administrador:tabla_juegos")
    else:
        form = JuegosForm()
    return render(req, "juegos/crear_juego.html", {"form": form})


def editar_juego(req, id: int):
    """ Permite editar los datos de un juego mediante su ID """
    query = Juego.objects.get(id=id)
    if req.method == "POST":
        form = JuegosForm(req.POST, req.FILES, instance=query)
        if form.is_valid():
            form.save()
            messages.success(req, f'El juego "{query.titulo } ha sido editado exitosamente"')
            return redirect("administrador:tabla_juegos")
    else:
        form = JuegosForm(instance=query)
    return render(req, "juegos/crear_juego.html", {"form": form}) 


def eliminar_juego(req, id:int):
    """ Elimina el juego seleccionado de la Base de Datos """
    query = Juego.objects.get(id=id)
    if req.method == "POST":
        query.delete()
        messages.success(req, f'El juego "{query.titulo}" ha sido eliminado correctamente.')
        return redirect("administrador:tabla_juegos")
    else:
        messages.error(req, 'Ocurrió un error al intentar eliminar el juego.')
        return redirect("administrador:tabla_juegos")