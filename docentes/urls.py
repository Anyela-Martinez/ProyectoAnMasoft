from django.urls import path

from docentes.views import adm_docente, docente, docentes_crear

urlpatterns = [
    path('',docente,name="docente"),
    path('adm/',adm_docente,name="adm-docente"),
    path('crear/',docentes_crear,name="docentes-crear"),
]