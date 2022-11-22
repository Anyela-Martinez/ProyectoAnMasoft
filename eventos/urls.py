from django.urls import path

from eventos.views import evento, evento_eliminar, evento_crear, evento_editar

urlpatterns = [
    path('',evento,name="evento"),
    path('crear/',evento_crear,name="evento-crear"),
    path('editar/<int:pk>/',evento_editar,name="evento-editar"),
    path('eliminar/<int:pk>/',evento_eliminar,name="evento-eliminar"),
]