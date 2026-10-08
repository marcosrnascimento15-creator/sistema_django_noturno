from webbrowser import get
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, redirect
from .models import Paciente

#create your views here.
@login_required
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, "index.html", {"pacientes": pacientes})

@login_required
def novo_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        Paciente.objects.create(
        nome=request.POST.get('nome'),
        cpf=request.POST.get('cpf'),
        email=request.POST.get('email'),
        telefone=request.POST.get('telefone'),
        data_nascimento=request.POST.get('data_nascimento'),
    )
        return redirect('novo-paciente-sucesso')
    return render(request, "novo-paciente.html")

@login_required
def novo_paciente_sucesso(request):
    return render(request, "novo-paciente-sucesso.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente

@login_required
def alterar_paciente(request, codigo_paciente):
    paciente = get_object_or_404(Paciente, codigo_paciente=codigo_paciente)
    
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.email = request.POST.get('email')
        paciente.telefone = request.POST.get('telefone')
        paciente.data_nascimento = request.POST.get('data_nascimento')

        paciente.save()
        return redirect('index') 
        
    return render(request, 'alterar_paciente.html', {'paciente': paciente})

@login_required
def excluir_paciente(request, codigo_paciente):
    paciente = Paciente.objects.get(codigo_paciente=codigo_paciente)
    paciente.delete()
    return redirect('index')

def buscar_paciente(request):
    query = request.GET.get('buscar','')
    pacientes = Paciente.objects.filter(nome__icontains=query)
    return render(request, 'index.html', {'pacientes': pacientes, 'query': query})
    