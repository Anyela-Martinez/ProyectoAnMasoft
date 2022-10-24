from django.urls import path

from curso.views import adm_curso, curso

urlpatterns = [
    path('',curso,name="curso"),
    path('adm/',adm_curso,name="adm-curso"),
]