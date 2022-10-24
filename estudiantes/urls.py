from django.urls import path

from estudiantes.views import adm_estudiante, estudiante

urlpatterns = [
    path('',estudiante,name="estudiante"),
    path('adm/',adm_estudiante,name="adm-estudiante"),
]