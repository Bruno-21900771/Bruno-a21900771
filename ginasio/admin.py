from django.contrib import admin

# Register your models here.

from .models import Socio, Modalidade, Inscricao


class SocioAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero_socio", "data_inscricao")
    ordering = ("nome",)
    search_fields = ("nome", "numero_socio")


class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "instrutor")
    ordering = ("nome",)
    search_fields = ("nome",)


class InscricaoAdmin(admin.ModelAdmin):
    list_display = ("socio", "modalidade", "data_inicio")
    ordering = ("socio",)
    search_fields = ("socio__nome", "modalidade__nome")


admin.site.register(Socio, SocioAdmin)
admin.site.register(Modalidade, ModalidadeAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
