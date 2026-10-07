from django.urls import path
from.import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('novo-paciente/', views.novo_paciente, name='novo-paciente'),
    path('novo-paciente-sucesso/', login_required(views.novo_paciente_sucesso), name='novo-paciente-sucesso'),
    path('alterar-paciente/<int:codigo_paciente>/', login_required(views.alterar_paciente), name='alterar-paciente'),
]