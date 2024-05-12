from django import forms
from . import models

class JuegosForm(forms.ModelForm):
    class Meta:
        model = models.Juego
        fields = ["titulo", "descripcion", "precio", "imagen"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Juego'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Descripción del Juego'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del Juego'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione una imagen'})
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'imagen': 'Imagen'
        }
