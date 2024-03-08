from django.db import models
from django.contrib.auth.models import User

# Create your models here.

OPCIONES_IDIOMA = [
    ('es', 'Español'),
    ('en', 'Inglés'),
    ('fr', 'Francés'),
    ('de', 'Alemán'),
    ('cn', 'Chino'),
]

class Videojuego(models.Model):
    id_juego = models.IntegerField()
    nombre_juego = models.CharField(max_length = 512)
    año_salida = models.IntegerField()
    pais_salida = models.CharField(max_length = 512)
    idioma_disponible = models.CharField(max_length = 512)
    genero = models.CharField(max_length = 512)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre_juego} - {self.idioma_disponible} - {self.genero}'