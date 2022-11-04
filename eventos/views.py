from django.shortcuts import redirect, render
from eventos.forms import EventoForm

from eventos.models import Evento

# Create your views her
def evento(request):
    titulo="Evento"
    eventos= Evento.objects.all()
    context={
        'titulo':titulo,
        'eventos':eventos

}
    return render(request,'eventos/evento.html',context) 

def adm_evento(request):

    context={

    }
    return render(request, 'eventos/adm-evento.html', context)

def eventos_crear(request):
    titulo="Eventos - Crear"
    if request.method == "POST":
        form=EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento')
        else:
            print("Error")
    else:
        form=EventoForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'eventos/eventos-crear.html',context) 

def eventos_editar(request, pk):
    titulo="Eventos - Editar"
    evento= Evento.objects.get(id=pk)
    if request.method == "POST":
        form= EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento')
        else:
            print("Error al guardar")
    else:
        form= EventoForm(instance=evento)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'eventos/eventos-crear.html',context) 