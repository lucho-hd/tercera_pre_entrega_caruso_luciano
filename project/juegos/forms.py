from django import forms
from . import models

class JuegosForm(forms.ModelForm):
    class Meta:
        model = models.Juego
        fields = ["titulo", "descripcion", "precio", "imagen", "plataformas", "desarrolladoras", "generos", "editores"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Juego'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Descripción del Juego'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del Juego'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione una imagen'}),
            'plataformas': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'desarrolladoras': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'generos': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'editores': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'plataformas': 'Plataformas',
            'desarrolladoras': 'Desarrolladoras',
            'generos': 'Géneros',
            'editores': 'Editores',
        }
