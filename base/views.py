from multiprocessing import context
from django.shortcuts import render, redirect
from docentes.forms import DocenteForm

from usuarios.forms import UsuarioForm

def inicio(request):
    context={    
    }
    return render(request,'inicio.html', context)

def usuarios_crear(request):
    titulo="Usuarios-crear"
    form=UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html', context)

def inicioAdmin(request):
    titulo="Tablero Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index-admin.html', context)

def docentes_crear(request):
    titulo="Docentes-crear"
    form=DocenteForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'docentes/docentes-crear.html', context)
