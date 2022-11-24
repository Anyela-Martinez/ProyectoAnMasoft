from django.shortcuts import redirect, render
from curso.forms import CursoForm
from curso.models import Curso

# Create your views her

def curso(request):
    curso= Curso.objects.all()
    titulo="Curso"
    context={
        'titulo':titulo,
        'curso':curso
}
    return render(request,'curso/curso.html',context) 

def curso_crear(request):
    titulo="Cursos - Crear"
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

def curso_editar(request, pk):
    titulo="Curso - Editar"
    curso= Curso.objects.get(id=pk)
    if request.method == "POST":
        form= CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso')
        else:
            print("Error al guardar")
    else:
        form= CursoForm(instance=curso)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'curso/curso-crear.html',context)

def curso_eliminar(request, pk):
    titulo='Curso - Eliminar'
    curso= Curso.objects.all()
    Curso.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('curso')
    
    context={
        'curso':curso,
        'titulo':titulo,
    }



