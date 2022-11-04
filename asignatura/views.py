from django.shortcuts import redirect, render
from asignatura.forms import AsignaturaForm

from asignatura.models import Asignatura

# Create your views her

def asignatura(request):
    asignatura= Asignatura.objects.all()
    titulo="Asignatura"
    context={
        'titulo':titulo,
        'asignatura':asignatura

}
    return render(request,'asignatura/asignatura.html',context) 

def asignatura_crear(request):
    titulo="Asignatura - Crear"
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

def adm_asignatura(request):
    context={
    }
    return render(request, 'asignatura/adm-asignatura.html', context)
