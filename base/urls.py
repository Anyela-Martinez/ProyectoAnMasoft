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
from django.conf.urls import handler404
from base.views import error_404, inicio, inicioAdmin
from usuarios.views import usuarios 


handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('adm/', inicioAdmin, name='inicio-admin'),
    path('usuarios/', include('usuarios.urls')),
    path('asignatura/', include('asignatura.urls')),
    path('curso/', include('curso.urls')),
    path('docentes/', include('docentes.urls')),
    path('estudiantes/', include('estudiantes.urls')),
    path('eventos/', include('eventos.urls')),
    path('grado/', include('grado.urls')),
    path('preregistro/', include('preregistro.urls')),
    path('publicaciones/', include('publicaciones.urls')),
]
