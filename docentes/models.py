from tabnanny import verbose
from django.db import models

from usuarios.models import Usuario

# Create your models here.
usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')