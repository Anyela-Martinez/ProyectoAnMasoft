from django.shortcuts import redirect, render

from curso.models import Curso

# Create your views her

def curso(request):
    titulo="curso"
    context={
        'titulo':titulo,
        'curso':curso

}
    return render(request,'curso/curso.html',context) 


def adm_curso(request):

    context={

    }
    return render(request, 'curso/adm-curso.html', context)

