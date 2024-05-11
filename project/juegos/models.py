from django.db import models

# Create your models here.
class Juego(models.Model):
    """ Modelo de Juegos """
    titulo      = models.CharField(max_length=100, unique=True) 
    descripcion = models.TextField()
    precio      = models.DecimalField(max_digits=10, decimal_places=2)
    imagen      = models.ImageField(upload_to='juegos/')

    def __str__(self) -> str:
        return self.titulo

    class Meta: 
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"