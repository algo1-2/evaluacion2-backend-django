from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<slug:slug_genero>/', views.detalle_genero, name='genero'),
]
