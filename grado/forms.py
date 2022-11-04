from django.forms import ModelForm
from grado.models import Grado

class GradoForm(ModelForm):
    class Meta:
        model=Grado
        exclude=['Estado']