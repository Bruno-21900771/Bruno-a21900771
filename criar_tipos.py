import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import TipoTecnologia

tipos = ["Frontend", "Backend", "Base de Dados", "Storage", "Outros"]

for nome in tipos:
    TipoTecnologia.objects.get_or_create(nome=nome)

print("Tipos criados.")