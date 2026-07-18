from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to="artigos/", blank=True, null=True)
    link_externo = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artigos")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

    @property
    def media_avaliacoes(self):
        avaliacoes = self.avaliacoes.all()
        if avaliacoes:
            total = sum(a.pontuacao for a in avaliacoes)
            return round(total / avaliacoes.count(), 1)
        return None


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.artigo.titulo}"


class Avaliacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name="avaliacoes")
    pontuacao = models.IntegerField(help_text="1 a 5")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pontuacao} para {self.artigo.titulo}"