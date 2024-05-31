from typing import Any
from django.shortcuts import render, redirect
from juegos.models import Juego
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PerfilUsuario

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

@login_required
def perfil(req: HttpRequest) -> HttpResponse:
    """
    Formulario para editar los datos de un usuario.
    @returns HttpResponse
    """
    perfil, created = PerfilUsuario.objects.get_or_create(usuario=req.user)

    if req.method == 'POST':
        user_form = UserForm(req.POST, instance=req.user) #type: ignore
        profile_form = UserProfileForm(req.POST, req.FILES, instance=perfil)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(req, '¡Tu perfil ha sido actualizado!')
            return redirect('core:perfil')
    else:
        user_form = UserForm(instance=req.user) #type: ignore
        profile_form = UserProfileForm(instance=perfil)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(req, 'core/perfil.html', context)