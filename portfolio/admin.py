from django.contrib import admin

from .models import (
    Licenciatura, Docente, UnidadeCurricular, TFC,
    Tecnologia, Projeto, Competencia, Formacao, MakingOf,
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "grau", "duracao_anos", "instituicao", "ects_totais")
    search_fields = ("nome",)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome",)


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre", "ects", "licenciatura")
    list_filter = ("ano", "semestre")
    search_fields = ("nome",)
    filter_horizontal = ("docentes",)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autores", "orientadores", "ano", "rating")
    list_filter = ("ano", "licenciatura")
    search_fields = ("titulo", "autores")


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel_interesse")
    list_filter = ("tipo",)
    search_fields = ("nome",)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "unidade_curricular")
    search_fields = ("nome",)
    filter_horizontal = ("tecnologias",)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "nivel")
    list_filter = ("categoria",)
    search_fields = ("nome",)
    filter_horizontal = ("projetos", "tecnologias")


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao", "data_inicio", "data_fim")
    list_filter = ("instituicao",)
    search_fields = ("nome",)


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("entidade", "decisao", "data")
    list_filter = ("entidade",)