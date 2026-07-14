from django.contrib import admin

# Register your models here.

from .models import Categoria, Produto, Cliente, Venda


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria", "stock")
    ordering = ("nome",)
    search_fields = ("nome", "categoria__nome")


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    ordering = ("nome",)
    search_fields = ("nome", "email")


class VendaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data")
    ordering = ("-data",)
    search_fields = ("cliente__nome",)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venda, VendaAdmin)