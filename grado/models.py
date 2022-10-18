from django.db import models
from usuarios.models import Usuario

class Grado(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')

    nomGrado=models.CharField(max_length=20, verbose_name="Nombre Grado") 
    numGrado=models.CharField(max_length=20, verbose_name="Número Grado") 