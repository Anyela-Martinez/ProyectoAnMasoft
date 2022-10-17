from django.db import models
from django.utils.translation import gettext_lazy as _

from usuarios.models import Usuario




# Create your models here.
class Curso(models.Model):
        usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')

        grado=models.ForeignKey(Grado, on_delete=models.CASCADE,verbose_name='Grado')

        nombreCurso=models.CharField(max_length=20, verbose_name="Nombre Curso") 

        numCurso=models.CharField(max_length=40, verbose_name="Número Curso") 

        class GradoPerte(models.TextChoices):
                Sexto='Sexto', _('Sexto')
                Septimo='Septimo', _('Séptimo')
                Octavo='Octavo', _('Octavo')
                Noveno='Noveno', _(' Noveno')
                Decimo='Decimo', _('Décimo')
                Once='Once', _('Once')
        GradoPerte=models.CharField(max_length=1,choices=GradoPerte.choices, default=GradoPerte.ACTIVO, verbose_name="Grado al que pertenece")

        class Estado(models.TextChoices):
                ACTIVO='1', _('Activo')
                INACTIVO='0', _('Inactivo')
        Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")