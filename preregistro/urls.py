from django.urls import path

from preregistro.views import  preregistro, preregistro_crear, preregistro_eliminar

urlpatterns = [
    path('',preregistro,name="preregistro"),
    path('crear/',preregistro_crear,name="preregistro-crear"),
    path('eliminar/<int:pk>/',preregistro_eliminar,name="preregistro-eliminar"),
]