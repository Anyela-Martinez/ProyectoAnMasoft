from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
from django.contrib import messages

# Create your views her

def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
}
    return render(request,'usuarios/usuarios.html',context) 

def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error")
    else:
        form=UsuarioForm()
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
            Estado='0'
        )
    return redirect('usuarios')
    
    context={
        'usuarios':usuarios,
        'titulo':titulo,
    }

def login(request):
    context={
    }
    return render(request, 'usuarios/login.html', context)

def administradores(request):
    context={
    }
    return render(request, 'usuarios/administradores.html', context)



