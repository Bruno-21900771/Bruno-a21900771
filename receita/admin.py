from django.contrib import admin

# Register your models here.

from .models import Categoria, Ingrediente, Receita


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "tempo_preparo")
    ordering = ("nome",)
    search_fields = ("nome", "categoria__nome")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)
