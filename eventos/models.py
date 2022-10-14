from dataclasses import FrozenInstanceError
from tkinter import image_names
from django.db import models

from usuarios.models import Usuario

# Create your models here.
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

