from django.forms import ModelForm
from preregistro.models import Preregistro

class PreregistroForm(ModelForm):
    class Meta:
        model=Preregistro
        exclude=['Estado']
    