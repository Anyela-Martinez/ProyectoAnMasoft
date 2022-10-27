from django.urls import path

from eventos.views import adm_evento, evento, eventos_crear

urlpatterns = [
    path('',evento,name="evento"),
    path('adm/',adm_evento,name="adm-evento"),
    path('crear/',eventos_crear,name="eventos-crear"),
]