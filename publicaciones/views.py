from django.shortcuts import redirect, render
from publicaciones.forms import PublicacionForm
from publicaciones.models import Publicacion

# Create your views her

def publicacion(request):
    titulo="Publicacion"
    publicacion= Publicacion.objects.all()
    context={
        'titulo':titulo,
        'publicacion':publicacion
}
    return render(request,'publicaciones/publicacion.html',context) 

def publicaciones_crear(request):
    titulo="Publicacion - Crear"
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

def publicaciones_editar(request, pk):
    titulo="Publicacion - Editar"
    publicacion= Publicacion.objects.get(id=pk)
    if request.method == "POST":
        form= PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('publicacion')
        else:
            print("Error al guardar")
    else:
        form= PublicacionForm(instance=publicacion)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'publicaciones/publicaciones-crear.html',context) 

def publicaciones_eliminar(request, pk):
    titulo= "Publicacion - Eliminar"
    publicacion= Publicacion.objects.all()
    Publicacion.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('publicacion')
    
    context={
        'publicacion':publicacion,
        'titulo':titulo,
    }
