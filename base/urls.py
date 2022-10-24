"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from base.views import inicio, inicioAdmin, usuarios_crear
from usuarios.views import usuarios 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('adm/', inicioAdmin, name='inicio-admin'),
    path('usuarios/', include('usuarios.urls')),
<<<<<<< HEAD
    path('usuario/',usuarios,name="usuarios"),
    path('adm/', inicio, name='inicio'),
    path('crear/', usuarios_crear, name='usuarios_crear'),
=======
    path('asignatura/', include('asignatura.urls')),
    path('curso/', include('curso.urls')),
    path('docentes/', include('docentes.urls')),
    path('estudiantes/', include('estudiantes.urls')),
    path('eventos/', include('eventos.urls')),
    path('grado/', include('grado.urls')),
    path('preregistro/', include('preregistro.urls')),
    path('publicaciones/', include('publicaciones.urls')),
>>>>>>> 2242b126d18196ed62239a29f540b084b73f5a2a
]
