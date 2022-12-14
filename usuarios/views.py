from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password

# Create your views her
@login_required(login_url='login')
def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
}
    return render(request,'usuarios/usuarios.html',context) 

def usuarios_crear(request):

    titulo="Crear Usuarios"
    if request.method == "POST":
        form=UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['numDoc']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['numDoc']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['correo']
                user.password=make_password(request.POST['nombres'][0] + request.POST['apellidos'][0] + request.POST['numDoc'][-4:])
                user.save()
                user_group = User
                my_group= Group.objects.get(name='Directivo')
                my_group.user_set.add(usuario.user)
            
            else:
                user=User.objects.get(username=request.POST['numDoc'])
            
            usuario= Usuario.objects.create(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                jornada=request.POST['jornada'],
                foto=form.cleaned_data.get('foto'),
                correo=request.POST['correo'],
                tipoDoc=request.POST['tipoDoc'],
                numDoc=request.POST['numDoc'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],
                genero=request.POST['genero'],
                user=user,
                rol=request.POST['rol'],
            )
            return redirect('usuarios')   
        else:
            form = UsuarioForm(request.POST,request.FILES)
    else:
        form= UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html',context)

def usuarios_editar(request, pk):
    titulo="Usuarios - Editar"
    usuario= Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form= UsuarioForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html',context)

def usuarios_eliminar(request, pk):
    titulo='Usuarios - Eliminar'
    usuarios= Usuario.objects.all()
    Usuario.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('usuarios')
    
    context={
        'usuarios':usuarios,
        'titulo':titulo,
    }


def administradores(request):
    context={
    }
    return render(request, 'usuarios/administradores.html', context)






