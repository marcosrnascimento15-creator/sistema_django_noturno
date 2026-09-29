from django.urls import path
from . import views  # Importa suas views

urlpatterns = [
    # Aponta para a função no arquivo views.py
    path('', views.login, name='login'), 
]