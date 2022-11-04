from django.urls import path

from estudiantes.views import adm_estudiante, estudiante, estudiantes_crear

urlpatterns = [
    path('',estudiante,name="estudiante"),
    path('adm/',adm_estudiante,name="adm-estudiante"),
    path('crear/',estudiantes_crear,name="estudiantes-crear"),
]