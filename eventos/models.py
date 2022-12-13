from dataclasses import FrozenInstanceError
from tkinter import image_names
from django.db import models
from django.utils.translation import gettext_lazy as _


from usuarios.models import Usuario

# Create your models here.

class Evento(models.Model):
    class TipoEvento(models.TextChoices):
        Cultural='CULTURAL', _('Evento Cultural')
        Academico='ACADÉMICO', _('Evento Académico')
        Pedagogico='PEDAGÓGICO', _('Evento Pedagógico')
        Informativo='INFORMATIVO', _('Evento Informativo')
    tipoEvento=models.CharField(max_length=20, choices=TipoEvento.choices , default=TipoEvento.Cultural, verbose_name="Tipo de Evento")

    nombreEve=models.CharField(max_length=60, verbose_name="Nombre del evento")

    descripEve=models.TextField(max_length=10000, verbose_name="Descripción del evento")

    fechaEve=models.DateField(verbose_name="Fecha del Evento", help_text=u"MM/DD/AAAA")

    horaEve=models.TimeField(verbose_name="Hora del Evento", blank=True, null=True, help_text=u"00:00:00")

    lugarEve=models.CharField(max_length=60, blank=True, null=True, verbose_name="Lugar del Evento")

    encagEve=models.CharField(max_length=60, blank=True, null=True, verbose_name="Encargados del Evento")

    duracionEve=models.CharField(max_length=60, blank=True, null=True, verbose_name="Duración del Evento")

    invitados=models.CharField(max_length=60, blank=True, null=True, verbose_name="Invitados al Evento")

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario')
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    foto=models.ImageField(upload_to='images/eventos',blank=True, default='images/eventos/default.jpg')

    def __str__(self)->str:
        return "%s %s" %(self.TipoEvento, self.nombreEve) 
    
   

