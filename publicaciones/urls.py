from django.urls import path

from publicaciones.views import publicacion, publicaciones_crear, publicaciones_editar, publicaciones_eliminar

urlpatterns = [
    path('',publicacion,name="publicacion"),
    path('crear/',publicaciones_crear,name="publicaciones-crear"),
    path('editar/<int:pk>/',publicaciones_editar,name="publicaciones-editar"),
    path('eliminar/<int:pk>/',publicaciones_eliminar,name="publicaciones-eliminar"),
]