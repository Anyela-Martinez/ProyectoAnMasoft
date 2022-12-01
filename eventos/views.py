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

def evento_crear(request):
    titulo="Evento - Crear"
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



def evento_editar(request, pk):
    titulo="Evento - Editar"
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

def evento_eliminar(request, pk):
    titulo= "Evento - Eliminar"
    evento= Evento.objects.all()
    Evento.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('evento')
    
    context={
        'evento':evento,
        'titulo':titulo,
    }
