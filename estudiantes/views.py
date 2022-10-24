from django.shortcuts import redirect, render

from estudiantes.models import Estudiante

# Create your views her

def estudiante(request):
    titulo="Estudiante"
    context={
        'titulo':titulo,
        'estudiante':estudiante

}
    return render(request,'estudiantes/estudiante.html',context) 


def adm_estudiante(request):

    context={

    }
    return render(request, 'estudiantes/adm-estudiante.html', context)