from django.urls import path

<<<<<<< HEAD
from usuarios.views import usuarios, usuarios_crear, login, administradores, modulos, adm_usuario, usuarios_editar, usuarios_eliminar
=======
from usuarios.views import usuarios, usuarios_crear, login, administradores, usuarios_editar, usuarios_eliminar
>>>>>>> bb2dcd33c83ce5b7e683e7b9bc810ababc25e95e

urlpatterns = [
    path('',usuarios,name="usuarios"),
    path('crear/',usuarios_crear,name="usuarios-crear"),
    path('editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),
    path('login/',login,name="login"),
    path('administradores/',administradores,name="administradores"),
<<<<<<< HEAD
    path('modulos/',modulos,name="modulos"),
    path('adm/',adm_usuario,name="adm-usuario"),
=======
>>>>>>> bb2dcd33c83ce5b7e683e7b9bc810ababc25e95e
]
