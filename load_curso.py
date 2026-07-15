import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Licenciatura, Docente, UnidadeCurricular

with open("files/ULHT260-PT.json", encoding="utf-8") as f:
    dados = json.load(f)

curso = dados["courseDetail"]

licenciatura, _ = Licenciatura.objects.get_or_create(
    nome=curso["courseName"],
    defaults={
        "grau": "Licenciatura",
        "duracao_anos": 3,
        "ects_totais": curso["courseECTS"],
    },
)

for professor in dados["teachers"]:
    nome_professor = professor.get("academicName") or professor.get("fullName")
    docente, _ = Docente.objects.get_or_create(
        nome=nome_professor,
        defaults={"email": professor.get("email", "")},
    )
    licenciatura.docentes.add(docente)

for uc in dados["courseFlatPlan"]:
    UnidadeCurricular.objects.get_or_create(
        nome=uc["curricularUnitName"],
        licenciatura=licenciatura,
        defaults={
            "ano": uc["curricularYear"],
            "semestre": uc["semester"],
            "ects": uc["ects"],
        },
    )

print("Curso e UCs carregados.")