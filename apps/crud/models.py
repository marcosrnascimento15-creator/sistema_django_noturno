from django.db import models

# Create your models here.
class Paciente(models.Model):
    codigo_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(null=True, max_length=100)
    cpf = models.CharField(unique=True, max_length=14, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sintomas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"