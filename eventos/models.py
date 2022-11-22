from dataclasses import FrozenInstanceError
from tkinter import image_names
from django.db import models
from django.utils.translation import gettext_lazy as _


from usuarios.models import Usuario

# Create your models here.

class Evento(models.Model):
    class TipoEvento(models.TextChoices):
        Cultural='CUL', _('Evento Cultural')
        Academico='ACA', _('Evento Academico')
        Pedagogico='PEDA', _('Evento Pedagogico')
        Recreativo='RECRE', _('Evento Recreativo')
    TipoEvento=models.CharField(max_length=20, choices=TipoEvento.choices , default=TipoEvento.Cultural, verbose_name="Tipo de Evento")

    nombreEve=models.CharField(max_length=60, verbose_name="Nombre del evento")

    fechaEve=models.DateField(verbose_name="Fecha del Evento", help_text=u"MM/DD/AAAA")

    horaEve=models.TimeField(verbose_name="Hora del Evento", help_text=u"00:00:00")

    lugarEve=models.CharField(max_length=60, verbose_name="Lugar del Evento")

    encagEve=models.CharField(max_length=60, verbose_name="Encargados del Evento")

    duracionEve=models.CharField(max_length=60, verbose_name="Duración del Evento")

    invitados=models.CharField(max_length=60, verbose_name="Invitados al Evento")
    
    # Falta imagen

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
   

