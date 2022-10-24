from django.urls import path

from eventos.views import adm_evento, evento

urlpatterns = [
    path('',evento,name="evento"),
    path('adm/',adm_evento,name="adm-evento"),
]