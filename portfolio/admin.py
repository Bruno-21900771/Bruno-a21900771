from django.contrib import admin

# Register your models here.

from .models import Licenciatura, Docente, UnidadeCurricular, TFC


class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "grau", "duracao_anos", "instituicao", "ects_totais")
    search_fields = ("nome",)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome",)


class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre", "ects", "licenciatura")
    list_filter = ("ano", "semestre")
    search_fields = ("nome",)
    filter_horizontal = ("docentes",)


class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autores", "orientadores", "ano", "rating")
    list_filter = ("ano", "licenciatura")
    search_fields = ("titulo", "autores")


admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(TFC, TFCAdmin)


from .models import Tecnologia, Projeto, Competencia, Formacao

admin.site.register(Tecnologia)
admin.site.register(Projeto)
admin.site.register(Competencia)
admin.site.register(Formacao)