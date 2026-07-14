from django.db import models

# Create your models here.

class Festival(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Dia(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name="dias")
    data = models.DateField()

    class Meta:
        ordering = ["data"]

    def __str__(self):
        dias_festival = list(self.festival.dias.order_by("data"))
        numero = dias_festival.index(self) + 1
        return f"Dia {numero} ({self.data:%d/%m/%Y}) - {self.festival}"


class Palco(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    estilo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Concerto(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name="concertos")
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="concertos")
    palco = models.ForeignKey(Palco, on_delete=models.CASCADE, related_name="concertos")
    hora = models.TimeField()

    def __str__(self):
        return f"{self.banda} - {self.dia}"


class Espectador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Bilhete(models.Model):
    espectador = models.ForeignKey(Espectador, on_delete=models.CASCADE, related_name="bilhetes")
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name="bilhetes")

    def __str__(self):
        return f"{self.espectador} - {self.dia}"