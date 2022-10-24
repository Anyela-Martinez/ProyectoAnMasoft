from django.urls import path

from preregistro.views import adm_preregistro, preregistro

urlpatterns = [
    path('',preregistro,name="preregistro"),
    path('adm/',adm_preregistro,name="adm-preregistro"),
]