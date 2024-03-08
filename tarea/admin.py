from django.contrib import admin
from .models import Videojuego

class VideojuegoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)

admin.site.register(Videojuego, VideojuegoAdmin)