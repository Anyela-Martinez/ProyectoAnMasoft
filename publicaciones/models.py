from dataclasses import FrozenInstanceError
from django.db import models
from django.utils.translation import gettext_lazy as _
from docentes.models import Docente
from grado.models import Grado

from usuarios.models import Usuario

# Create your models here.


class Publicacion(models.Model):
    class TipoPublicacion(models.TextChoices):
        Informativa='INFORMATIVA', _('Publicación Informativa')
        Academica='ACADÉMICA', _('Publicación Academica')
        Cultural='CULTURAL', _('Publicación Cultural')
        Pedagica='PEDAGOGICA', _('Publicación Pedagógica')
    tipoPublicacion=models.CharField(max_length=20, choices=TipoPublicacion.choices , default=TipoPublicacion.Cultural, verbose_name="Tipo de Publicacion")
    
    nombrePubli=models.CharField(max_length=60, verbose_name="Nombre de la Publicación")

    descripPublic=models.CharField(max_length=100, verbose_name="Descripción de la Publicación")

    linkPubli=models.CharField(max_length=80, blank=True, verbose_name="Link de la Publicación")

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class Jornada(models.TextChoices):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    jornada=models.CharField(max_length=10,choices=Jornada.choices, blank=True, default=Jornada.JM, verbose_name="Jornada")

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, verbose_name='Usuario')

    docente=models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, verbose_name='Docente')

    grado=models.ForeignKey(Grado, on_delete=models.CASCADE, blank=True, verbose_name='Grado')

    def __str__(self)->str:
        return "%s %s" %(self.TipoPublicacion, self.nombrePubli) 