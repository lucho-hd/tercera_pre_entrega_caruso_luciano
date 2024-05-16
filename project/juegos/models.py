from django.db import models
from datetime import datetime

class Plataforma(models.Model):
    """ Modelo de plataformas """
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"


class Desarrolladora(models.Model):
    """ Modelo de desarrolladoras """
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Desarrolladora"
        verbose_name_plural = "Desarrolladoras"


class Genero(models.Model):
    """ Modelo de géneros """
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"


class Editor(models.Model):
    """ Modelo de editores """

    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Editor"
        verbose_name_plural = "Editores"


class Juego(models.Model):
    """ Modelo de Juegos """
    titulo            = models.CharField(max_length=100, unique=True) 
    descripcion       = models.TextField()
    fecha_lanzamiento = models.DateField(default=datetime.now) 
    precio            = models.DecimalField(max_digits=10, decimal_places=2)
    imagen            = models.ImageField(upload_to='juegos/')
    plataformas       = models.ManyToManyField(Plataforma, verbose_name="plataformas", related_name="juegos")
    desarrolladoras   = models.ManyToManyField(Desarrolladora, related_name="juegos")
    generos           = models.ManyToManyField(Genero, related_name="juegos")
    editores          = models.ManyToManyField(Editor, related_name="juegos")

    def __str__(self) -> str:
        return self.titulo

    class Meta: 
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
