from django.urls import path

from docentes.views import adm_docente, docente

urlpatterns = [
    path('',docente,name="docente"),
    path('adm/',adm_docente,name="adm-docente"),
]