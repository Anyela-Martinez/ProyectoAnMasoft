from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario

# Create your models here.

class Docente(models.Model):
    class TipoDoc(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
    TipoDoc=models.CharField(max_length=3,choices=TipoDoc.choices, default=TipoDoc.CC, verbose_name="Tipo de Documento") 
    
    numDoc=models.CharField(max_length=60, verbose_name="Número de Documento")
    
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    
    class Genero(models.TextChoices):
        M='M', _('Masculino')
        F='F', _('Femenino')
        I='I', _('Indefinido')
    Genero=models.CharField(max_length=3,choices=Genero.choices, default=Genero.M, verbose_name="Género")
    
    telefono=models.CharField(max_length=20, verbose_name="Teléfono") 
    
    direccion=models.CharField(max_length=40, verbose_name="Dirección") 
    
    correo=models.CharField(max_length=40, verbose_name="Correo Electrónico") 
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    class Jornada(models.TextChoices):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    Jornada=models.CharField(max_length=10,choices=Jornada.choices, default=Jornada.JM, verbose_name="Jornada")
    
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')