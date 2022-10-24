from django.shortcuts import redirect, render

from grado.models import Grado

# Create your views her

def grado(request):
    titulo="Grado"
    context={
        'titulo':titulo,
        'grado':grado
}
    return render(request,'grados/grado.html',context) 


def adm_grado(request):

    context={

    }
    return render(request,'grado/adm-grado.html', context)
