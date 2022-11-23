from django.urls import path

from usuarios.views import usuarios, usuarios_crear, login, administradores, usuarios_editar, usuarios_eliminar

urlpatterns = [
    path('',usuarios,name="usuarios"),
    path('crear/',usuarios_crear,name="usuarios-crear"),
    path('editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),
    path('login/',login,name="login"),
    path('administradores/',administradores,name="administradores"),
]
