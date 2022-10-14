from django.db import models

from usuarios.models import Usuario

# Create your models here.
class Asignatura(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')
    nombreAsig=models.CharField(max_Length=20, verbose_name="Nombre de Asignatura")