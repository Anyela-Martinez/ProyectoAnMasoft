from django.db import models
from django.utils.translation import gettext_lazy as _
from grado.models import Grado

from usuarios.models import Usuario
from docentes.models import Docente

# Create your models here.
class Curso(models.Model):
        usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, verbose_name='Usuario')

        grado=models.ForeignKey(Grado, on_delete=models.CASCADE,verbose_name='Grado')

        nombreCurso=models.CharField(max_length=20, verbose_name="Nombre Curso") 

        numCurso=models.CharField(max_length=40, verbose_name="Número Curso") 

        docente=models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name='Docente')

        class Estado(models.TextChoices):
                ACTIVO='1', _('Activo')
                INACTIVO='0', _('Inactivo')
        estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

        def __str__(self)->str:
           return "%s %s" %(self.nombreCurso, self.numCurso) 