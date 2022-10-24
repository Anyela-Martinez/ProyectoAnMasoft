from django.urls import path

from publicaciones.views import adm_publicacion, publicacion

urlpatterns = [
    path('',publicacion,name="publicacion"),
    path('adm/',adm_publicacion,name="adm-publicacion"),
]