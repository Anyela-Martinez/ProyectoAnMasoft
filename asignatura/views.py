from django.shortcuts import redirect, render

from asignatura.models import Asignatura

# Create your views her

def asignatura(request):
    titulo="Asignatura"
    context={
        'titulo':titulo,
        'asignatura':asignatura

}
    return render(request,'asignatura/asignatura.html',context) 

def adm_asignatura(request):

    context={

    }
    return render(request, 'asignatura/adm-asignatura.html', context)
