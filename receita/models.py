from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="receitas")
    ingredientes = models.ManyToManyField(Ingrediente, related_name="receitas")
    tempo_preparo = models.IntegerField(help_text="minutos")
    modo_preparo = models.TextField()

    def __str__(self):
        return self.nome