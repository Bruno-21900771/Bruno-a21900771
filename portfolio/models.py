from django.db import models

# Create your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    grau = models.CharField(max_length=50)  # ex: "Licenciatura"
    duracao_anos = models.IntegerField()
    instituicao = models.CharField(max_length=150, default="Universidade Lusófona")
    ects_totais = models.IntegerField()

    def __str__(self):
        return self.nome