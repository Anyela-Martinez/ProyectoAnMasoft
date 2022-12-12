from django.urls import path

from docentes.views import docente, docentes_crear, docentes_editar, docentes_eliminar

urlpatterns = [
    path('',docente,name="docente"),
    path('crear/',docentes_crear,name="docentes-crear"),
    path('editar/<int:pk>/',docentes_editar,name="docentes-editar"),
    path('eliminar/<int:pk>/',docentes_eliminar,name="docentes-eliminar"),
]