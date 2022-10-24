from django.shortcuts import redirect, render

from docentes.models import Docente

# Create your views her

def docente(request):
    titulo="Docente"
    context={
        'titulo':titulo,
        'docente':docente

}
    return render(request,'docentes/docente.html',context) 

def adm_docente(request):

    context={

    }
    return render(request, 'docentes/adm-docente.html', context)
