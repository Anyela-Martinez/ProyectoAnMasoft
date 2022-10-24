from django.shortcuts import redirect, render

from publicaciones.models import Publicacion

# Create your views her

def publicacion(request):
    titulo="Publicacion"
    context={
        'titulo':titulo,
        'publicacion':publicacion

}
    return render(request,'publicaciones/publicacion.html',context) 


def adm_publicacion(request):

    context={

    }
    return render(request, 'publicaciones/adm-publicacion.html', context)
