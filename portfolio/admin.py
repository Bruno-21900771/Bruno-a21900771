from django.contrib import admin

# Register your models here.

from .models import Licenciatura


class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "grau", "duracao_anos", "instituicao", "ects_totais")
    list_filter = ("grau", "instituicao")
    search_fields = ("nome",)


admin.site.register(Licenciatura, LicenciaturaAdmin)

from .models import TFC

class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autores", "orientadores", "ano", "rating")
    list_filter = ("ano", "licenciatura")
    search_fields = ("titulo", "autores", "palavras_chave")


admin.site.register(TFC, TFCAdmin)