from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from eventos.models import Evento
from django.contrib import messages
from django.contrib.auth import logout


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

def noticias(request):
    titulo = 'Eventos'
    eventos= Evento.objects.filter(estado='1')
    context={  
        'eventos': eventos,
        'titulo':titulo
    }
    
    return render(request,'noticias.html', context)


def logout_user(request):
    logout(request)
    return redirect('inicio')