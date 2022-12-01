from django.forms import ModelForm
from eventos.models import Evento

class EventoForm(ModelForm):
    class Meta:
        model=Evento
        exclude=['estado']