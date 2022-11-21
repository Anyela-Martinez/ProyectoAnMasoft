
from statistics import correlation
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Preregistro(models.Model):
    class TipoDoc(models.TextChoices):
        RC='RC', _('Registro Civil')
        TI='TI', _('Tarjeta de Identidad')
        CC='CC', _('Cédula de Ciudadanía')
        NES='NES', _('Número de Secretaria')
        PP='PP', _('Pasaporte')
        PV='PV', _('Pasaporte Venezolano')
    TipoDoc=models.CharField(max_length=6,choices=TipoDoc.choices, default=TipoDoc.RC, verbose_name="Tipo de Documento") 

    numDoc=models.CharField(max_length=60, verbose_name="Número de Documento") 

    nombres=models.CharField(max_length=60, verbose_name="Nombres")

    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")

    class JornadaInt(models.TextChoices):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    JornadaInt=models.CharField(max_length=10,choices=JornadaInt.choices, default=JornadaInt.JM, verbose_name="Jornada que le interesa")

    class GradoInt(models.TextChoices):
        SEX='6', _('Grado Sexto')
        SEP='7', _('Grado Séptimo')
        OCT='8', _('Grado Octavo')
        NOV='9', _('Grado Noveno')
        DEC='10', _('Grado Décimo')
    GradoInt=models.CharField(max_length=5,choices=GradoInt.choices, default=GradoInt.SEX, verbose_name="Grado que le interesa")

    direccion=models.CharField(max_length=40, verbose_name="Dirección") 

    correo=models.CharField(max_length=40, verbose_name="Correo Electrónico") 

    class TipoDocAcu(models.TextChoices):
            CC='CC', _('Cédula de Ciudadanía')
            CE='CE', _('Cédula de Extranjería')
            PP='PP', _('Pasaporte')
    TipoDocAcu=models.CharField(max_length=3,choices=TipoDocAcu.choices, default=TipoDocAcu.CC, verbose_name="Tipo de Documento del Acudiente") 

    numDocAcu=models.CharField(max_length=60, verbose_name="Número de Documento del Acudiente")

    nombresAcu=models.CharField(max_length=60, verbose_name="Nombres del Acudiente")

    apellidosAcu=models.CharField(max_length=60, verbose_name="Apellidos del Acudiente")

    telefonoAcu=models.CharField(max_length=20, verbose_name="Teléfono del Acudiente") 

    correoAcu=models.CharField(max_length=40, verbose_name="Correo Electrónico del Acudiente")

    colProce=models.CharField(max_length=60, verbose_name="Colegio de Porecedencia") 
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

