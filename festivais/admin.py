from django.contrib import admin

# Register your models here.

from .models import Festival, Banda, Genero

class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero",)
    search_fields = ("nome",)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "data", "local", "banda",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)