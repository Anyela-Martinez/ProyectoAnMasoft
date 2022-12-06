from django.db import models
from usuarios.models import Usuario
from django.utils.translation import gettext_lazy as _

class Grado(models.Model):
    usuario=models.ForeignKey(Usuario,  on_delete=models.CASCADE, blank=True, verbose_name='Usuario')

    nomGrado=models.CharField(max_length=20, verbose_name="Nombre Grado") 

    numGrado=models.CharField(max_length=20, verbose_name="Número Grado") 

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self)->str:
        return "%s %s" %(self.nomGrado, self.numGrado) 
