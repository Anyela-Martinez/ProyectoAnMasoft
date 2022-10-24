from django.urls import path

from asignatura.views import adm_asignatura, asignatura

urlpatterns = [
    path('',asignatura,name="asignatura"),
    path('adm/',adm_asignatura,name="adm-asignatura"),
]