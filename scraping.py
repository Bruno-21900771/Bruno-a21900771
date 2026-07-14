import requests
import re
import json
from bs4 import BeautifulSoup

url = "https://informatica.ulusofona.pt/investigacao/tfcs-dissertacoes-teses/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


def get_campo(content, label):
    for p in content.find_all("p"):
        span = p.find("span")
        if span and label in span.get_text():
            texto = p.get_text(separator=" ", strip=True)
            return texto.replace(span.get_text(strip=True), "", 1).strip(" :")
    return None


tfcs = []

for titulo_tag in soup.find_all("a", class_="uk-accordion-title"):
    italic = titulo_tag.find("span", style=lambda s: s and "italic" in s)
    if not italic:
        continue

    texto_licenciatura = italic.get_text(strip=True)

    # só entra se for Licenciatura (exclui Mestrado/Doutoramento)
    if "Licenciatura" not in texto_licenciatura:
        continue

    match = re.search(r"(20\d{2})", texto_licenciatura)
    if not match or match.group(1) != "2025":
        continue

    li = titulo_tag.find_parent("li")
    content = li.find("div", class_="uk-accordion-content")

    spans_titulo = titulo_tag.find_all("span", recursive=False)
    titulo = spans_titulo[0].get_text(strip=True) if spans_titulo else None

    bloco_info = titulo_tag.find("span", style=lambda s: s and "font-weight:100" in s)
    coloridos = bloco_info.find_all("span", style=lambda s: s and "bold" in s) if bloco_info else []
    autores_txt = coloridos[0].get_text(strip=True) if len(coloridos) > 0 else ""
    orientador_txt = coloridos[1].get_text(strip=True) if len(coloridos) > 1 else ""

    autores = [a.strip() for a in autores_txt.split(";") if a.strip()]
    orientadores = [o.strip() for o in orientador_txt.split(",") if o.strip()]

    licenciatura = texto_licenciatura.split(".")[0].strip()

    link_tag = content.find("a", download=True) if content else None
    link = link_tag["href"] if link_tag else None

    img_tag = content.find("img") if content else None
    imagem = img_tag["src"] if img_tag else None

    resumo = get_campo(content, "Resumo") if content else None
    palavras_chave = get_campo(content, "Palavras chave") if content else None
    areas = get_campo(content, "Áreas") if content else None
    tecnologias = get_campo(content, "Tecnologias") if content else None

    tfcs.append({
        "titulo": titulo,
        "autores": autores,
        "orientadores": orientadores,
        "licenciatura": licenciatura,
        "ano": 2025,
        "link_pdf": link,
        "imagem": imagem,
        "sumario": resumo,
        "palavras_chave": palavras_chave,
        "areas": areas,
        "tecnologias": tecnologias,
        "rating": None
    })

print(f"Total de TFCs de 2025 encontrados: {len(tfcs)}")

with open("tfcs_2025.json", "w", encoding="utf-8") as f:
    json.dump(tfcs, f, ensure_ascii=False, indent=2)

print("Ficheiro tfcs_2025.json criado com sucesso!")