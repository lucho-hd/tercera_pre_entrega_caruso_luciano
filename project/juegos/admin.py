from django.contrib import admin
from .models import Juego, Plataforma, Genero, Desarrolladora, Editor

# Register your models here.

admin.site.register(Plataforma)
admin.site.register(Desarrolladora)
admin.site.register(Genero)
admin.site.register(Editor)
admin.site.register(Juego)