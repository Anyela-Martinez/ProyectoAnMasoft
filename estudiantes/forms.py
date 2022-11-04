from django.forms import ModelForm
from estudiantes.models import Estudiante

class EstudianteForm(ModelForm):
    class Meta:
        model=Estudiante
        exclude=['Estado']