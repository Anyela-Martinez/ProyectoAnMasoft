from dataclasses import FrozenInstanceError
from tkinter import image_names
from django.db import models
from django.utils.translation import gettext_lazy as _


from usuarios.models import Usuario

# Create your models here.
class TipoEvento(models.Model):
    nombre=models.CharField(max_length=60, verbose_name="Nombre del Tipo de Evento")
    
    descripcion=models.CharField(max_length=100, verbose_name="Descripción del Evento")

class Evento(models.Model):
    nombreEve=models.CharField(max_length=60, verbose_name="Nombre del Evento")

    fechaHrEve=models.DateTimeField(verbose_name="Fecha y Hora del Evento", help_text=u"MM/DD/AAAA 00:00:00")

    lugarEve=models.CharField(max_length=60, verbose_name="Lugar del Evento")

    encagEve=models.CharField(max_length=60, verbose_name="Encargados del Evento")

    duracionEve=models.CharField(max_length=60, verbose_name="Duración del Evento")

    invitados=models.CharField(max_length=60, verbose_name="Invitados al Evento")
      
    # Falta imagen

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')
    
    tipoEvento=models.ForeignKey(TipoEvento, on_delete=models.CASCADE,verbose_name='Tipo de Evento')

