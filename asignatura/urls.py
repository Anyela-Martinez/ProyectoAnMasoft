from django.urls import path

from asignatura.views import adm_asignatura, asignatura, asignatura_crear

urlpatterns = [
    path('',asignatura,name="asignatura"),
    path('adm/',adm_asignatura,name="adm-asignatura"),
    path('crear/',asignatura_crear,name="asignatura-crear"),
]