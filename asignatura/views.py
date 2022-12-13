from django.shortcuts import redirect, render
from asignatura.forms import AsignaturaForm

from asignatura.models import Asignatura

# Create your views her

def asignatura(request):
    asignatura= Asignatura.objects.all()
    titulo="Asignaturas"
    context={
        'titulo':titulo,
        'asignatura':asignatura

}
    return render(request,'asignatura/asignatura.html',context) 

def asignaturas_crear(request):
    titulo="Asignaturas - Crear"
    if request.method == "POST":
        form=AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignatura')
        else:
            print("Error")
    else:
        form=AsignaturaForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'asignatura/asignatura-crear.html',context) 

def asignatura_editar(request, pk):
    titulo="Asignaturas - Editar"
    asignatura= Asignatura.objects.get(id=pk)
    if request.method == "POST":
        form= AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('asignatura')
        else:
            print("Error al guardar")
    else:
        form= AsignaturaForm(instance=asignatura)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'asignatura/asignatura-crear.html',context) 

def asignatura_eliminar(request, pk):
    titulo='Asignaturas - Eliminar'
    asignaturas= Asignatura.objects.all()
    Asignatura.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('asignatura')
    
    context={
        'asignaturas':asignaturas,
        'titulo':titulo,
    }
