from django.forms import ModelForm
from .models import Videojuego

class VideojuegoForm(ModelForm):
    class Meta:
        model = Videojuego
        fields =[
        'id_juego',
        'nombre_juego',
        'año_salida',
        'pais_salida',
        'idioma_disponible',
        'genero'
        ]
        