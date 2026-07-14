from django.contrib import admin

# Register your models here.

from .models import Turma, Aluno, Disciplina, Nota


class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_letivo")
    ordering = ("nome",)
    search_fields = ("nome",)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero", "turma")
    ordering = ("nome",)
    search_fields = ("nome", "numero")


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "professor")
    ordering = ("nome",)
    search_fields = ("nome",)


class NotaAdmin(admin.ModelAdmin):
    list_display = ("aluno", "disciplina", "valor")
    ordering = ("aluno",)
    search_fields = ("aluno__nome", "disciplina__nome")


admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Nota, NotaAdmin)