from django.urls import path

from grado.views import adm_grado, grado

urlpatterns = [
    path('',grado,name="grado"),
    path('adm/',adm_grado,name="adm-grado"),
]