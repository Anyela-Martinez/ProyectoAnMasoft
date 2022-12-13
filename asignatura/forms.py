from django.forms import ModelForm
from asignatura.models import Asignatura

class AsignaturaForm(ModelForm):
    class Meta:
        model= Asignatura 
        exclude=['estado', 'usuario']