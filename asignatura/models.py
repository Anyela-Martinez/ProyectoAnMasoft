from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario

# Create your models here.
class Asignatura(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')

    nombreAsig=models.CharField(max_length=60, verbose_name="Nombre de Asignatura")

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos) 