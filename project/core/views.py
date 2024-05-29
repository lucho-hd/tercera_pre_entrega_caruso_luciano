from typing import Any
from django.shortcuts import render
from juegos.models import Juego
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def index(req):
    query   = Juego.objects.all()
    context = {"juegos": query} 
    return render(req, "core/index.html", context)


class CustomLoginView(LoginView):
    """ Formulario para iniciar sesión """
    authentication_form = CustomAuthenticationForm
    template_name = "core/iniciar-sesion.html"

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"Has iniciado sesión con éxito. ¡Bienvenido de nuevo {user.username}!")
        return super().form_valid(form)


class CustomLogoutView(LogoutView): 
    """ Cerrar sesión """
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Has cerrado sesión con éxito. ¡Vuelve pronto!")
        return super().dispatch(request, *args, **kwargs)



def crearCuenta(req: HttpRequest) -> HttpResponse:
    """ Formulario para registrarse en el sitio """
    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(req, f"La cuenta {username} ha sido creada exitosamente!")
            return render(req, "core/index.html")
    else:
        form = CustomUserCreationForm()
    return render(req, "core/crear-cuenta.html",{"form": form})