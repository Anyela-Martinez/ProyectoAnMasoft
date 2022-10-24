from django.shortcuts import redirect, render

from preregistro.models import Preregistro

# Create your views her

def preregistro(request):
    titulo="Preregistro"
    context={
        'titulo':titulo,
        'preregistro':preregistro
}
    return render(request,'preregistro/preregistro.html',context) 


def adm_preregistro(request):

    context={

    }
    return render(request, 'preregistro/adm-preregistro.html', context)