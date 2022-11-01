from multiprocessing import context
from django.shortcuts import render, redirect
from docentes.forms import DocenteForm
from eventos.forms import EventoForm
from publicaciones.forms import PublicacionForm
from usuarios.forms import UsuarioForm
from preregistro.forms import PreregistroForm
from django.views.defaults import page_not_found

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

def eventos_crear(request):
    titulo="Eventos-crear"
    form=EventoForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'eventos/eventos-crear.html', context)

def preregistro_crear(request):
    titulo="Preregistro-crear"
    form=PreregistroForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'preregistro/preregistro-crear.html', context)

def error_404(request,exception):
    return page_not_found(request,'404.html')

def publicaciones_crear(request):
    titulo="Publicaciones-crear"
    form=PublicacionForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'publicaciones/publicaiones-crear.html', context)