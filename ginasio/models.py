from django.db import models

# Create your models here.

from django.db import models

class Socio(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.numero} - {self.nome}'