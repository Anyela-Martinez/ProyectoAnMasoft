from django.forms import ModelForm
from publicaciones.models import Publicacion


class PublicacionForm(ModelForm):
    class Meta:
        model=Publicacion
        exclude=['estado']