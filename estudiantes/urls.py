from django.urls import path

from estudiantes.views import estudiantes, estudiantes_crear, estudiantes_editar, estudiantes_eliminar

urlpatterns = [
    path('',estudiantes,name="estudiantes"),
    path('crear/',estudiantes_crear,name="estudiantes-crear"),
    path('editar/<int:pk>/',estudiantes_editar,name="estudiantes-editar"),
    path('eliminar/<int:pk>/',estudiantes_eliminar,name="estudiantes-eliminar"),
] 
