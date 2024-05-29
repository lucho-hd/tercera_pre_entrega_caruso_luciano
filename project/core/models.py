from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime

# Create your models here.
def pathUsuario(instance, archivo):
    """ 
    Crea un path para la foto de perfil del usuario, tomando la fecha y el nombre de usuario.
    """

    archivo_base, extension = os.path.splitext(archivo)
    nuevo_archivo = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{instance.usuario.username}{extension}"
    return f"avatares/{nuevo_archivo}"

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    imagen_perfil = models.ImageField(upload_to=pathUsuario, blank=True, null=True)

    def __str__(self) -> str:
        return self.usuario.username