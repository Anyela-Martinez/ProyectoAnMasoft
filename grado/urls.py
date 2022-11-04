from django.urls import path

from grado.views import adm_grado, grado, grado_crear

urlpatterns = [
    path('',grado,name="grado"),
    path('adm/',adm_grado,name="adm-grado"),
    path('crear/',grado_crear,name="grado-crear"),
]