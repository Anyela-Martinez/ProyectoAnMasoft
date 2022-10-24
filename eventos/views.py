from django.shortcuts import redirect, render

from eventos.models import Evento

# Create your views her
def evento(request):
    titulo="Evento"
    context={
        'titulo':titulo,
        'evento':evento

}
    return render(request,'eventos/evento.html',context) 

def adm_evento(request):

    context={

    }
    return render(request, 'eventos/adm-evento.html', context)
