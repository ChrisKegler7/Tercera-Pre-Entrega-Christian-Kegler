from django.urls import path
from . import views

app_name = 'libreria'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('agregar_autor_libro/', views.agregar_autor_libro, name='agregar_autor_libro'),
    path('buscar_libro/', views.buscar_libro_view, name='buscar_libro'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('reviews/', views.reviews, name='reviews'),
]
