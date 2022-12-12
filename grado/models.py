from django.db import models
from usuarios.models import Usuario
from django.utils.translation import gettext_lazy as _

class Grado(models.Model):
    usuario=models.ForeignKey(Usuario,  on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario')

    nomGrado=models.CharField(max_length=60, verbose_name="Nombre Grado") 

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self)->str:
        return "%s" %(self.nomGrado)
