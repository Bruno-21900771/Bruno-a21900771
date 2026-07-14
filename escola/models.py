from django.db import models

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano_letivo = models.CharField(max_length=9)  # ex: "2025/2026"

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(unique=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="notas")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}: {self.valor}"