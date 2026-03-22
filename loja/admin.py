from django.contrib import admin

# Register your models here.

from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "stock",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Produto, ProdutoAdmin)