from django.contrib import admin

# Register your models here.

from .models import Festival, Dia, Palco, Banda, Concerto, Espectador, Bilhete


class DiaInline(admin.TabularInline):
    model = Dia
    extra = 1


class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [DiaInline]


class ConcertoAdmin(admin.ModelAdmin):
    list_display = ("banda", "dia", "palco", "hora")
    ordering = ("dia", "hora")
    search_fields = ("banda__nome",)


class BilheteAdmin(admin.ModelAdmin):
    list_display = ("espectador", "dia")
    search_fields = ("espectador__nome",)


admin.site.register(Festival, FestivalAdmin)
admin.site.register(Dia)
admin.site.register(Palco)
admin.site.register(Banda)
admin.site.register(Concerto, ConcertoAdmin)
admin.site.register(Espectador)
admin.site.register(Bilhete)