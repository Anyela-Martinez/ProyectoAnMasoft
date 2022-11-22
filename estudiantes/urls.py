from django.urls import path

from estudiantes.views import estudiante, estudiantes_crear, estudiantes_editar, estudiantes_eliminar

urlpatterns = [
    path('',estudiante,name="estudiante"),
    path('crear/',estudiantes_crear,name="estudiantes-crear"),
    path('editar/<int:pk>/',estudiantes_editar,name="estudiantes-editar"),
    path('eliminar/<int:pk>/',estudiantes_eliminar,name="estudiantes-eliminar"),
] 
