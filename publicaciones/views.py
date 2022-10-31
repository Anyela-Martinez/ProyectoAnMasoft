from django.shortcuts import redirect, render


from publicaciones.models import Publicacion

# Create your views her

def publicacion(request):
    titulo="Publicacion"
    context={
        'titulo':titulo,
        'publicacion':Publicacion

}
    return render(request,'publicaciones/publicacion.html',context) 


def adm_publicacion(request):

    context={

    }
    return render(request, 'publicaciones/adm-publicacion.html', context)

def publicaciones_crear(request):
    titulo="publicaciones - Crear"
    if request.method == "POST":
        form=PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publicacion')
        else:
            print("Error")
    else:
        form=PublicacionForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'publicaciones/publicaciones-crear.html',context) 