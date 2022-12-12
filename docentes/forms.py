from django.forms import ModelForm
from docentes.models import Docente

class DocenteForm(ModelForm):
    class Meta:
        model=Docente
        exclude=['estado', 'user', 'usuario']