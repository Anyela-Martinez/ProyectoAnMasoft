from django.shortcuts import redirect, render
from docentes.forms import DocenteForm

from docentes.models import Docente

# Create your views her


def docente(request):
    titulo="Docente"
    docente= Docente.objects.all()
    context={
        'titulo':titulo,
        'docente':docente

}
    return render(request,'docentes/docente.html',context) 

def adm_docente(request):

    context={

    }
    return render(request, 'docentes/adm-docente.html', context)


def docentes_crear(request):
    titulo="Docentes - Crear"
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