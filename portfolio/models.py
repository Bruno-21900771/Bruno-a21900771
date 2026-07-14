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


class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=300)
    orientadores = models.CharField(max_length=300)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="tfcs")
    ano = models.IntegerField()
    link_pdf = models.URLField(blank=True)
    imagem = models.URLField(blank=True)
    sumario = models.TextField(blank=True)
    palavras_chave = models.CharField(max_length=300, blank=True)
    areas = models.CharField(max_length=300, blank=True)
    tecnologias = models.CharField(max_length=300, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo