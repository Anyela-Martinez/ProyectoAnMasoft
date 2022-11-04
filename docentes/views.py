from django.shortcuts import redirect, render
from docentes.forms import DocenteForm
from docentes.models import Docente
from django.contrib import messages

# Create your views her

def docente(request):
    titulo="Docente"
    docentes= Docente.objects.all()
    context={
        'titulo':titulo,
        'docentes':docentes
}
    return render(request,'docentes/docente.html',context) 

def adm_docente(request):

    context={

    }
    return render(request, 'docentes/adm-docente.html', context)


def docentes_crear(request):
    titulo="Docentes-Crear"
    if request.method == "POST":
        form=DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docente')
        else:
            print("Error")
    else:
        form=DocenteForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'docentes/docentes-crear.html',context)

def docentes_editar(request, pk):
    titulo="Docentes - Editar"
    docente= Docente.objects.get(id=pk)
    if request.method == "POST":
        form= DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docente')
        else:
            print("Error al guardar")
    else:
        form= DocenteForm(instance=docente)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'docentes/docentes-crear.html',context) 