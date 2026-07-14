import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import TFC, Licenciatura

with open("data/tfcs_2025.json", encoding="utf-8") as f:
    tfcs = json.load(f)

for item in tfcs:
    nome_licenciatura = item["licenciatura"].replace("Licenciatura em ", "").strip()

    licenciatura, _ = Licenciatura.objects.get_or_create(
        nome=nome_licenciatura,
        defaults={
            "grau": "Licenciatura",
            "duracao_anos": 3,
            "instituicao": "Universidade Lusófona",
            "ects_totais": 180,
        },
    )

    TFC.objects.update_or_create(
        titulo=item["titulo"],
        defaults={
            "autores": "; ".join(item.get("autores", [])),
            "orientadores": "; ".join(item.get("orientadores", [])),
            "licenciatura": licenciatura,
            "ano": item.get("ano"),
            "link_pdf": item.get("link_pdf") or "",
            "imagem": item.get("imagem") or "",
            "sumario": item.get("sumario") or "",
            "palavras_chave": item.get("palavras_chave") or "",
            "areas": item.get("areas") or "",
            "tecnologias": item.get("tecnologias") or "",
            "rating": item.get("rating") or 0,
        },
    )

print(f"{len(tfcs)} TFC(s) carregado(s)/atualizado(s) na base de dados.")