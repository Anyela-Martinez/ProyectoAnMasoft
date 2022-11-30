from django.shortcuts import redirect, render
from estudiantes.forms import EstudianteForm
from estudiantes.models import Estudiante
from django.contrib import messages

# Create your views her

def estudiantes(request):
    titulo="Estudiantes"
    estudiantes= Estudiante.objects.all()
    context={
        'titulo':titulo,
        'estudiantes':estudiantes

}
    return render(request,'estudiantes/estudiante.html',context) 

def estudiantes_crear(request):
    titulo="Estudiantes - Crear"
    if request.method == "POST":
        form=EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')
        else:
            print("Error")
    else:
        form=EstudianteForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'estudiantes/estudiantes-crear.html',context) 

def estudiantes_editar(request, pk):
    titulo="Estudiantes - Editar"
    estudiante= Estudiante.objects.get(id=pk)
    if request.method == "POST":
        form= EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')
        else:
            print("Error al guardar")
    else:
        form= EstudianteForm(instance=estudiante)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'estudiantes/estudiantes-crear.html',context) 

def estudiantes_eliminar(request, pk):
    titulo= "Estudiantes - Eliminar"
    estudiante= Estudiante.objects.all()
    Estudiante.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('estudiantes')
    
    context={
        'estudiante':estudiante,
        'titulo':titulo,
    }