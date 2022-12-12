from django.shortcuts import redirect, render
from grado.forms import GradoForm
from grado.models import Grado
from django.contrib.auth.decorators import login_required, permission_required

# Create your views her

def grado(request):
    titulo="Grado"
    grado= Grado.objects.all()
    context={
        'titulo':titulo,
        'grado':grado
}
    return render(request,'grado/grado.html',context) 

def grado_crear(request):
    titulo="Grado - Crear"
    if request.method == "POST":
        form=GradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grado')
        else:
            print("Error")
    else:
        form=GradoForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'grado/grado-crear.html',context) 

def grado_editar(request, pk):
    titulo="Grados - Editar"
    grado= Grado.objects.get(id=pk)
    if request.method == "POST":
        form= GradoForm(request.POST, instance=grado)
        if form.is_valid():
            form.save()
            return redirect('grado')
        else:
            print("Error al guardar")
    else:
        form= GradoForm(instance=grado)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'grado/grado-crear.html',context) 

def grado_eliminar(request, pk):
    titulo= "Grado - Eliminar"
    grado= Grado.objects.all()
    Grado.objects.filter(id=pk).update(
            Estado='0'
        )
    return redirect('grado')
    
    context={
        'grado':grado,
        'titulo':titulo,
    }
