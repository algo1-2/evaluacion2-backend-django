from django.urls import path
from . import views

# Namespace de la aplicación home según especificación de la rúbrica
app_name = 'home'

urlpatterns = [
    # Ruta raíz del sitio (/)
    path('', views.inicio, name='inicio'),
    # Ruta amigable para acceder al detalle de cada género
    path('genero/<slug:slug_genero>/', views.detalle_genero, name='genero'),
]
