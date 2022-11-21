from django.urls import path

from preregistro.views import  preregistro, preregistro_crear, preregistro_editar, preregistro_eliminar

urlpatterns = [
    path('',preregistro,name="preregistro"),
    path('crear/',preregistro_crear,name="preregistro-crear"),
    path('editar/<int:pk>/',preregistro_editar,name="preregistro-editar"),
    path('eliminar/<int:pk>/',preregistro_eliminar,name="preregistro-eliminar"),
]