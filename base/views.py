from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found

def inicio(request):
    context={    
    }
    return render(request,'inicio.html', context)

def inicioAdmin(request):
    titulo="Tablero Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index-admin.html', context)

def error_404(request,exception):
    return page_not_found(request,'404.html')

def modulos(request):
    context={
    }
    return render(request, 'modulos.html', context)

def educacion(request):
    context={    
    }
    
    return render(request,'educacion.html', context)