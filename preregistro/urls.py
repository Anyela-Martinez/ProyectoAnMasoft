from django.urls import path

from preregistro.views import adm_preregistro, preregistro, preregistro_crear, preregistro_editar

urlpatterns = [
    path('',preregistro,name="preregistro"),
    path('adm/',adm_preregistro,name="adm-preregistro"),
    path('crear/',preregistro_crear,name="preregistro-crear"),
     path('editar/<int:pk>/',preregistro_editar,name="preregistro-editar"),
]