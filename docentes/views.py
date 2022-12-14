from django.shortcuts import redirect, render
from docentes.forms import DocenteForm
from docentes.models import Docente
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password

# Create your views her
@login_required(login_url='login')
def docente(request):
    titulo="Docente"
    docentes= Docente.objects.all()
    context={
        'titulo':titulo,
        'docentes':docentes
}
    return render(request,'docentes/docente.html',context) 


def docentes_crear(request):
    titulo="Crear Docentes"
    if request.method == "POST":
        form=DocenteForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['numDoc']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['numDoc']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['correo']
                user.password=make_password(request.POST['nombres'][0] + request.POST['apellidos'][0] + "123")
                user.save()
                user_group = User
                my_group= Group.objects.get(name='Docente')
                my_group.user_set.add(docente.user)
            
            else:
                user=User.objects.get(username=request.POST['numDoc'])
            
            docente= Docente.objects.create(
                tipoDoc=request.POST['tipoDoc'],
                numDoc=request.POST['numDoc'],
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                genero=request.POST['genero'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],
                correo=request.POST['correo'],
                jornada=request.POST['jornada'],
                foto=form.cleaned_data.get('foto'),
                user=user,
            )
            return redirect('docente')
        else:
            form = DocenteForm(request.POST,request.FILES)
    else:
        form= DocenteForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'docentes/docentes-crear.html',context)

def docentes_editar(request, pk):
    titulo="Docentes - Editar"
    docente= Docente.objects.get(id=pk)
    if request.method == "POST":
        form= DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docente')
        else:
            print("Error al guardar")
    else:
        form= DocenteForm(instance=docente)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'docentes/docentes-crear.html',context) 

def docentes_eliminar(request, pk):
    titulo='Docentes - Eliminar'
    docentes= Docente.objects.all()
    Docente.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('docente')
    
    context={
        'docentes':docentes,
        'titulo':titulo,
    }