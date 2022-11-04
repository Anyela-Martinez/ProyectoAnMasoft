from django.urls import path

from curso.views import adm_curso, curso, curso_crear

urlpatterns = [
    path('',curso,name="curso"),
    path('crear/',curso_crear,name="curso-crear"),
    path('adm/',adm_curso,name="adm-curso"),
]