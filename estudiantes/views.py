from django.shortcuts import redirect, render
from estudiantes.forms import EstudianteForm

from estudiantes.models import Estudiante

# Create your views her

def estudiante(request):
    estudiante= Estudiante.objects.all()
    titulo="Estudiante"
    context={
        'titulo':titulo,
        'estudiante':estudiante

}
    return render(request,'estudiantes/estudiante.html',context) 

def estudiantes_crear(request):
    titulo="Estudiantes - Crear"
    if request.method == "POST":
        form=EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante')
        else:
            print("Error")
    else:
        form=EstudianteForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'estudiantes/estudiantes-crear.html',context) 

def adm_estudiante(request):
    context={
    }
    return render(request, 'estudiantes/adm-estudiante.html', context)