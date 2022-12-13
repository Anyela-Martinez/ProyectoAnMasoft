from django.db import models
from django.utils.translation import gettext_lazy as _
from curso.models import Curso

from usuarios.models import Usuario

# Create your models here.
class Estudiante(models.Model):
    class TipoDoc(models.TextChoices):
        RC='RC', _('Registro Civil')
        TI='TI', _('Tarjeta de Identidad')
        CC='CC', _('Cédula de Ciudadanía')
        NES='NES', _('Número de Secretaria')
        PP='PP', _('Pasaporte')
    tipoDoc=models.CharField(max_length=6,choices=TipoDoc.choices, default=TipoDoc.RC, verbose_name="Tipo de Documento") 

    numDoc=models.CharField(max_length=60, verbose_name="Número de Documento") 

    nombres=models.CharField(max_length=60, verbose_name="Nombres")

    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")

    class Jornada(models.TextChoices):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    jornada=models.CharField(max_length=10,choices=Jornada.choices, default=Jornada.JM, verbose_name="Jornada")
    
    telefono=models.CharField(max_length=20, verbose_name="Teléfono ")  
    
    direccion=models.CharField(max_length=40, verbose_name="Dirección") 

    correo=models.CharField(max_length=40, verbose_name="Correo Electrónico")
     
    class Genero(models.TextChoices):
        M='M', _('Masculino')
        F='F', _('Femenino')
        I='I', _('Indefinido')
    genero=models.CharField(max_length=3,choices=Genero.choices, default=Genero.M, verbose_name="Género")
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=3,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    class TipoDocAcu(models.TextChoices):
            CC='CC', _('Cédula de Ciudadanía')
            CE='CE', _('Cédula de Extranjería')
            PP='PP', _('Pasaporte')
    tipoDocAcu=models.CharField(max_length=3,choices=TipoDocAcu.choices, default=TipoDocAcu.CC, verbose_name="Tipo de Documento del Acudiente") 

    numDocAcu=models.CharField(max_length=60, verbose_name="Número de Documento del Acudiente")

    nombresAcu=models.CharField(max_length=60, verbose_name="Nombres del Acudiente")

    apellidosAcu=models.CharField(max_length=60, verbose_name="Apellidos del Acudiente")

    telefonoAcu=models.CharField(max_length=20, verbose_name="Teléfono del Acudiente") 

    correoAcu=models.CharField(max_length=40, verbose_name="Correo Electrónico del Acudiente")
    
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')
    
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE,verbose_name='Curso')

    foto=models.ImageField(upload_to='images/usuarios',blank=True, default='images/usuarios/default.png')

    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos) 

    
