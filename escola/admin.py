from django.contrib import admin

# Register your models here.

from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("numero", "nome", "turma", "idade",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Aluno, AlunoAdmin)