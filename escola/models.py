from django.db import models

# Create your models here.

class Aluno(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=10)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.numero} - {self.nome}'