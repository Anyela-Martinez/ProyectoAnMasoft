from django.urls import path

from publicaciones.views import adm_publicacion, publicacion, publicaciones_crear

urlpatterns = [
    path('',publicacion,name="publicacion"),
    path('adm/',adm_publicacion,name="adm-publicacion"),
    path('crear/',publicaciones_crear,name="publicaciones-crear"),
]