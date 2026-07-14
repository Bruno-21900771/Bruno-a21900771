from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="vendas")
    produtos = models.ManyToManyField(Produto, related_name="vendas")
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id} - {self.cliente}"