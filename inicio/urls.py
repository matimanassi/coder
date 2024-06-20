from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
]