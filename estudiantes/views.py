from django.shortcuts import redirect, render
from estudiantes.forms import EstudianteForm
from estudiantes.models import Estudiante
from django.contrib import messages
from curso.models import Curso


from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password

# Create your views her
@login_required(login_url='login')
def estudiantes(request):
    titulo="Estudiantes"
    estudiantes= Estudiante.objects.all()
    context={
        'titulo':titulo,
        'estudiantes':estudiantes

}
    return render(request,'estudiantes/estudiante.html',context) 

def estudiantes_crear(request):
    titulo="Crear Estudiantes"
    if request.method == "POST":
        form=EstudianteForm(request.POST, request.FILES)
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
                my_group= Group.objects.get(name='Estudiante')
                my_group.user_set.add(estudiante.user)
            
            else:
                user=User.objects.get(username=request.POST['numDoc'])
            
            estudiante= Estudiante.objects.create(
                tipoDoc=request.POST['tipoDoc'],
                numDoc=request.POST['numDoc'],
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                jornada=request.POST['jornada'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],
                correo=request.POST['correo'],
                genero=request.POST['genero'],

                tipoDocAcu=request.POST['tipoDocAcu'],
                numDocAcu=request.POST['numDocAcu'],
                nombresAcu=request.POST['nombresAcu'],
                apellidosAcu=request.POST['apellidosAcu'],
                telefonoAcu=request.POST['telefonoAcu'],
                correoAcu=request.POST['correoAcu'],
                foto=form.cleaned_data.get('foto'),

                
                user=user,
            )
            return redirect('estudiantes')
        else:
            form = EstudianteForm(request.POST,request.FILES)
    else:
        form= EstudianteForm()
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