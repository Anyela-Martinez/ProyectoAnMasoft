from django.shortcuts import redirect, render
from preregistro.forms import PreregistroForm
from preregistro.models import Preregistro
from django.contrib import messages

# Create your views her

def preregistro(request):
    titulo="Preregistro"
    preregistro= Preregistro.objects.all()
    context={
        'titulo':titulo,
        'preregistro':preregistro
}
    return render(request,'preregistro/preregistro.html',context) 


def preregistro_crear(request):
    titulo="Preregistro-Crear"
    if request.method == "POST":
        form=PreregistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preregistro')
        else:
            print("Error")
    else:
        form=PreregistroForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'preregistro/preregistro-crear.html',context) 

def preregistro_editar(request, pk):
    titulo="Preregistros - Editar"
    preregistro= Preregistro.objects.get(id=pk)
    if request.method == "POST":
        form= PreregistroForm(request.POST, instance=preregistro)
        if form.is_valid():
            form.save()
            return redirect('preregistro')
        else:
            print("Error al guardar")
    else:
        form= PreregistroForm(instance=preregistro)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'preregistro/preregistro-crear.html',context) 

def preregistro_eliminar(request, pk):
    titulo= "Preregistro - Eliminar"
    preregistro= Preregistro.objects.all()
    Preregistro.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('preregistro')
    
    context={
        'preregistro':preregistro,
        'titulo':titulo,
    }