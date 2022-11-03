from django.urls import path

from usuarios.views import usuarios, usuarios_crear, login, administradores, administrar, adm_usuario, usuarios_editar

urlpatterns = [
    path('',usuarios,name="usuarios"),
    path('crear/',usuarios_crear,name="usuarios-crear"),
    path('editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('login/',login,name="login"),
    path('administradores/',administradores,name="administradores"),
    path('administrar/',administrar,name="administrar"),
    path('adm/',adm_usuario,name="adm-usuario"),
]
