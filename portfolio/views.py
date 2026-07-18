import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Licenciatura, Docente, UnidadeCurricular, TFC, Projeto, Tecnologia, Competencia, Formacao
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

# Create your views here.


def is_gestor(user):
    return user.groups.filter(name="gestor-portfolio").exists()


gestor_required = user_passes_test(is_gestor, login_url="login_view")


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('docentes').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
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


def docentes_view(request):
    docentes = Docente.objects.prefetch_related('licenciaturas').all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})


@login_required
@gestor_required
def projeto_create_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos_view')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Criar Projeto'})


@login_required
@gestor_required
def projeto_edit_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos_view')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})


@login_required
@gestor_required
def projeto_delete_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos_view')
    return render(request, 'portfolio/projeto_confirm_delete.html', {'projeto': projeto})


@login_required
@gestor_required
def tecnologia_create_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tecnologias_view')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Criar Tecnologia'})


@login_required
@gestor_required
def tecnologia_edit_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias_view')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Editar Tecnologia'})


@login_required
@gestor_required
def tecnologia_delete_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias_view')
    return render(request, 'portfolio/tecnologia_confirm_delete.html', {'tecnologia': tecnologia})


@login_required
@gestor_required
def competencia_create_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias_view')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Criar Competência'})


@login_required
@gestor_required
def competencia_edit_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias_view')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Editar Competência'})


@login_required
@gestor_required
def competencia_delete_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias_view')
    return render(request, 'portfolio/competencia_confirm_delete.html', {'competencia': competencia})


@login_required
@gestor_required
def formacao_create_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacoes_view')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Criar Formação'})


@login_required
@gestor_required
def formacao_edit_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes_view')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Editar Formação'})


@login_required
@gestor_required
def formacao_delete_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes_view')
    return render(request, 'portfolio/formacao_confirm_delete.html', {'formacao': formacao})


def sobre_view(request):
    tecnologias = Tecnologia.objects.select_related('tipo').all()
    tecnologias_por_tipo = {}
    for tecnologia in tecnologias:
        tipo_nome = tecnologia.tipo.nome if tecnologia.tipo else "Outros"
        tecnologias_por_tipo.setdefault(tipo_nome, []).append(tecnologia)
    return render(request, 'portfolio/sobre.html', {'tecnologias_por_tipo': tecnologias_por_tipo})

def landing_view(request):
    return render(request, 'portfolio/landing.html')

def videotutoriais_view(request):
    return render(request, 'portfolio/videotutoriais.html')

def videotutoriais_view(request):
    return render(request, 'portfolio/videotutoriais.html')


def api_colega_view(request):
    url = "https://tiagoamaro.pw.deisi.ulusofona.pt/api/unidadesCurriculares/"
    try:
        response = requests.get(url, verify=False, timeout=5)
        if response.status_code == 200:
            data = response.json()
            dados = data.get("items", data) if isinstance(data, dict) else data
        else:
            dados = []
    except requests.exceptions.RequestException:
        dados = []
    return render(request, 'portfolio/api_colega.html', {'dados': dados, 'erro': not dados})