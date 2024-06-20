from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('listar_autores/', views.listar_autores, name='listar_autores'),
    path('editar_autor/<int:autor_id>/', views.editar_autor, name='editar_autor'),
    path('borrar_autor/<int:autor_id>/', views.borrar_autor, name='borrar_autor'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('borrar_libro/<int:libro_id>/', views.borrar_libro, name='borrar_libro'),
    path('agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('listar_editoriales/', views.listar_editoriales, name='listar_editoriales'),
    path('editar_editorial/<int:editorial_id>/', views.editar_editorial, name='editar_editorial'),
    path('borrar_editorial/<int:editorial_id>/', views.borrar_editorial, name='borrar_editorial'),
]