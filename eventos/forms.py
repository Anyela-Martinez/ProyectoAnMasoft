from django.forms import ModelForm, widgets
from eventos.models import Evento

class EventoForm(ModelForm):
    class Meta:
        model=Evento
        exclude=['estado', 'usuario']
        widgets={
            'fechaEve': widgets.DateInput(attrs={'type':'date'})
              }
    