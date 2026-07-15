import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import UnidadeCurricular, Docente

url = "https://informatica.ulusofona.pt/ensino/licenciaturas/engenharia-informatica/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

blocos_docentes = soup.find_all(["strong", "b", "span"], string=lambda s: s and s.strip() == "Docentes")

atualizados = 0
nao_encontrados = set()

for span in blocos_docentes:
    li = span.find_parent("li")
    if not li:
        continue

    titulo_tag = li.find("a", class_="uk-accordion-title")
    if not titulo_tag:
        continue

    nome_uc = titulo_tag.get_text(strip=True)

    p = span.find_parent("p")
    nomes_docentes = [a.get_text(strip=True) for a in p.find_all("a")]

    try:
        uc = UnidadeCurricular.objects.get(nome=nome_uc)
    except UnidadeCurricular.DoesNotExist:
        nao_encontrados.add(nome_uc)
        continue

    for nome_docente in nomes_docentes:
        docente, _ = Docente.objects.get_or_create(nome=nome_docente)
        uc.docentes.add(docente)

    atualizados += 1

print(f"Blocos processados: {atualizados}")
print(f"UCs não encontradas na base de dados: {nao_encontrados}")