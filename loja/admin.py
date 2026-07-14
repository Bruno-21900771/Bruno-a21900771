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
    list_display = ("id", "cliente", "get_produtos", "data")
    ordering = ("-data",)
    search_fields = ("cliente__nome",)

    def get_produtos(self, obj):
        return ", ".join(p.nome for p in obj.produtos.all())
    get_produtos.short_description = "Produtos"


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venda, VendaAdmin)