from django.db import models

# Create your models here.

usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')

grado=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Grado')

nombreCurso=models.CharField(max_length=20, verbose_name="Nombre Curso") 

numCurso=models.CharField(max_length=40, verbose_name="Numero Curso") 

class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")