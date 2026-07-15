from django.shortcuts import render

# Create your views here.

from .models import Licenciatura, UnidadeCurricular, TFC, Projeto, Tecnologia, Competencia, Formacao


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('docentes').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/unidades_curriculares.html', {'ucs': ucs})


def tfcs_view(request):
    tfcs = TFC.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias').select_related('unidade_curricular').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos', 'tecnologias').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})