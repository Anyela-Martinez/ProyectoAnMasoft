from django.forms import ModelForm
from publicaciones.apps import PublicacionesConfig


class EventoForm(ModelForm):
    class Meta:
        model=PublicacionesConfig
        exclude=['Estado']