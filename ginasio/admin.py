from django.contrib import admin

# Register your models here.

from .models import Socio

class SocioAdmin(admin.ModelAdmin):
    list_display = ("numero", "nome", "idade",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Socio, SocioAdmin)