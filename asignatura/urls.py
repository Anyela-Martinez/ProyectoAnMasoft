from django.urls import path

from asignatura.views import asignatura, asignaturas_crear, asignatura_editar, asignatura_eliminar

urlpatterns = [
    path('',asignatura,name="asignatura"),
    path('crear/',asignaturas_crear,name="asignaturas-crear"),
    path('editar/<int:pk>/',asignatura_editar,name="asignaturas-editar"),
    path('eliminar/<int:pk>/',asignatura_eliminar,name="asignaturas-eliminar"),
]