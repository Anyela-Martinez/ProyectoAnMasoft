from django.shortcuts import redirect, render
from grado.forms import GradoForm
from grado.models import Grado

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

def adm_grado(request):
    context={
    }
    return render(request,'grado/adm-grado.html', context)
