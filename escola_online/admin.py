from django.contrib import admin

# Register your models here.

from .models import Professor, Aluno, Curso


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome",)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero")
    search_fields = ("nome", "numero")


class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "professor")
    search_fields = ("nome",)
    filter_horizontal = ("alunos",)


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)