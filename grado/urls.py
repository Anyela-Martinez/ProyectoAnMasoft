from django.urls import path

from grado.views import grado, grado_crear, grado_editar, grado_eliminar

urlpatterns = [
    path('',grado,name="grado"),
    path('crear/',grado_crear,name="grado-crear"),
    path('editar/<int:pk>/',grado_editar,name="grado-editar"),
    path('eliminar/<int:pk>/',grado_eliminar,name="grado-eliminar"),

]