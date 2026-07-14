from django.db import models

# Create your models here.

class Socio(models.Model):
    nome = models.CharField(max_length=100)
    numero_socio = models.IntegerField(unique=True)
    data_inscricao = models.DateField()

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    nome = models.CharField(max_length=50)
    instrutor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="inscricoes")
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name="inscricoes")
    data_inicio = models.DateField()

    def __str__(self):
        return f"{self.socio} - {self.modalidade}"
