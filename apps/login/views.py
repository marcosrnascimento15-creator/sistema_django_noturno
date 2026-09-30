from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def novo_usuario(request):
    return render(request, "novo-usuario.html")

