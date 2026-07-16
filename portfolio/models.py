from django.db import models

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    grau = models.CharField(max_length=50)
    duracao_anos = models.IntegerField()
    instituicao = models.CharField(max_length=150, default="Universidade Lusófona")
    ects_totais = models.IntegerField()
    docentes = models.ManyToManyField(Docente, related_name="licenciaturas", blank=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="unidades_curriculares")
    nome = models.CharField(max_length=150)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=30)
    ects = models.IntegerField()
    docentes = models.ManyToManyField(Docente, related_name="unidades_curriculares", blank=True)

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
    
class TipoTecnologia(models.Model):
    nome = models.CharField(max_length=50)  # Frontend, Backend, Base de Dados, Storage, Outros

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoTecnologia, on_delete=models.SET_NULL, null=True, blank=True, related_name="tecnologias")
    logo = models.URLField(blank=True)
    site_oficial = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(help_text="1 a 5")
    descricao = models.TextField(blank=True, help_text="O que a tecnologia faz e permite")
    opiniao = models.TextField(blank=True, help_text="O que gostaste ou não gostaste")

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos")
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name="projetos"
    )
    imagem = models.URLField(blank=True)
    video_demo = models.URLField(blank=True)
    link_github = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)  # ex: "Técnica" ou "Soft skill"
    nivel = models.IntegerField(help_text="1 a 5")
    projetos = models.ManyToManyField(Projeto, related_name="competencias", blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="competencias", blank=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    nome = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    certificado_link = models.URLField(blank=True)

    def __str__(self):
        return self.nome