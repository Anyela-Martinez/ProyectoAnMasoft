from django.shortcuts import redirect, render
from curso.forms import CursoForm

from curso.models import Curso

# Create your views her

def curso(request):
    curso= Curso.objects.all()
    titulo="curso"
    context={
        'titulo':titulo,
        'curso':curso
}
    return render(request,'curso/curso.html',context) 

def curso_crear(request):
    titulo="Curso - Crear"
    if request.method == "POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso')
        else:
            print("Error")
    else:
        form=CursoForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'curso/curso-crear.html',context) 

def adm_curso(request):
    context={
    }
    return render(request, 'curso/adm-curso.html', context)

