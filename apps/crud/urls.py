from django.urls import path
from.import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('novo-paciente/', views.novo_paciente, name='novo_paciente'),
    path('novo-paciente-sucesso/', login_required(views.novo_paciente_sucesso), name='novo_paciente_sucesso'),
    path('alterar_paciente/<int:codigo_paciente>/', login_required(views.alterar_paciente), name='alterar_paciente'),
    path('excluirPaciente/<int:codigo_paciente>/', login_required(views.excluir_paciente), name='excluir_paciente'),
    path('buscar/', views.buscar_paciente, name='buscar_paciente'),
]