from django import forms
from . import models

class JuegosForm(forms.ModelForm):
    class Meta:
        model  = models.Juego
        fields = ["titulo", "descripcion", "precio", "imagen"] 