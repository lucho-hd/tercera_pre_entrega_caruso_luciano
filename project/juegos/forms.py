from django import forms
from . import models

class PlataformasForm(forms.ModelForm):
    class Meta:
        model  = models.Plataforma
        fields = ["nombre"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la plataforma'})
        } 
        labels = {
            'nombre': 'Nombre'
        }


class DesarrolladorasForm(forms.ModelForm):
    class Meta:
        model  = models.Desarrolladora
        fields = ["nombre"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la desarrolladora'})
        } 
        labels = {
            'nombre': 'Nombre'
        }


class GenerosForm(forms.ModelForm):
    class Meta:
        model  = models.Genero
        fields = ["nombre"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del género'})
        } 
        labels = {
            'nombre': 'Nombre'
        }


class EditoresForm(forms.ModelForm):
    class Meta:
        model  = models.Editor
        fields = ["nombre"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del editor'})
        } 
        labels = {
            'nombre': 'Nombre'
        }


class JuegosForm(forms.ModelForm):
    class Meta:
        model = models.Juego
        fields = ["titulo", "descripcion", "fecha_lanzamiento", "precio", "imagen", "plataformas", "desarrolladoras", "generos", "editores"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Juego'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Descripción del Juego'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha de lanzamiento'}),
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
            'fecha_lanzamiento': 'Fecha de Lanzamiento',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'plataformas': 'Plataformas',
            'desarrolladoras': 'Desarrolladoras',
            'generos': 'Géneros',
            'editores': 'Editores',
        }
