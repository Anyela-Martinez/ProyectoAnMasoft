from dataclasses import FrozenInstanceError
from django.db import models
from django.utils.translation import gettext_lazy as _
from docentes.models import Docente

from usuarios.models import Usuario

# Create your models here.
class TipoPublicacion(models.Model):
    nombre=models.CharField(max_length=60, verbose_name="Nombre del Tipo de Publicación")
    
    descripcion=models.CharField(max_length=100, verbose_name="Descripción de la publicación")

class Publicacion(models.Model):
    nombrePubli=models.CharField(max_length=60, verbose_name="Nombre de la Publicación")

    descripPublic=models.CharField(max_length=60, verbose_name="Descripción de la Publicación")

    linkPubli=models.CharField(max_length=60, verbose_name="Link de la Publicación")

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class Jornada(models.TextChoices):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    Jornada=models.CharField(max_length=2,choices=Jornada.choices, default=Jornada.JM, verbose_name="Jornada")

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')

    docente=models.ForeignKey(Docente, on_delete=models.CASCADE,verbose_name='Docente')

    tipoPublicacion=models.ForeignKey(TipoPublicacion, on_delete=models.CASCADE,verbose_name='Tipo de Publicación')

    grado=models.ForeignKey(Grado, on_delete=models.CASCADE,verbose_name='Grado')

