from django.urls import path

from curso.views import curso, curso_crear, curso_editar, curso_eliminar

urlpatterns = [
    path('',curso,name="curso"),
    path('crear/',curso_crear,name="cursos-crear"),
    path('editar/<int:pk>/',curso_editar,name="curso-editar"),
    path('eliminar/<int:pk>/',curso_eliminar,name="curso-eliminar"),
]