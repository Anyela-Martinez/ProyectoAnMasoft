from django.db import models

from usuarios.models import Usuario

# Create your models here.
class Grado(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')
    nombreGrado=models.CharField(max_length=20, verbose_name="Nombre de grado")
    numGrado=models.CharField(max_length=20, verbose_name="Numero de grado")
    