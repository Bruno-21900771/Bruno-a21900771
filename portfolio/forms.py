from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'tecnologias', 'unidade_curricular', 'imagem', 'video_demo', 'link_github']


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'logo', 'site_oficial', 'nivel_interesse', 'descricao']


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'categoria', 'nivel', 'projetos', 'tecnologias']


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'instituicao', 'data_inicio', 'data_fim', 'certificado_link']