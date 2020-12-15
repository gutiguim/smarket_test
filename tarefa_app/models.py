from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=70, blank=False, default='')

class Tarefa(models.Model):
    descricao = models.CharField(max_length=70, blank=False, default='')
    estadoTarefa = models.CharField(max_length=20, blank=False, default='Pendente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)