import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Tecnologia, TipoTecnologia

tecnologias = [
    {
        "nome": "Django",
        "tipo": "Backend",
        "site_oficial": "https://www.djangoproject.com/",
        "nivel_interesse": 5,
        "descricao": "Framework web em Python que permite criar aplicações completas rapidamente, com ORM, sistema de admin automático, autenticação e routing incluídos.",
    },
    {
        "nome": "Python",
        "tipo": "Backend",
        "site_oficial": "https://www.python.org/",
        "nivel_interesse": 5,
        "descricao": "Linguagem de programação usada como base de todo o projeto Django, incluindo os scripts de webscraping e carregamento de dados.",
    },
    {
        "nome": "HTML5",
        "tipo": "Frontend",
        "site_oficial": "https://developer.mozilla.org/en-US/docs/Web/HTML",
        "nivel_interesse": 4,
        "descricao": "Linguagem de marcação usada para estruturar o conteúdo das páginas e templates Django.",
    },
    {
        "nome": "CSS3",
        "tipo": "Frontend",
        "site_oficial": "https://developer.mozilla.org/en-US/docs/Web/CSS",
        "nivel_interesse": 4,
        "descricao": "Usado para estilizar todas as páginas do projeto (cards, cores, layout responsivo).",
    },
    {
        "nome": "SQLite",
        "tipo": "Base de Dados",
        "site_oficial": "https://www.sqlite.org/",
        "nivel_interesse": 4,
        "descricao": "Base de dados usada por defeito pelo Django em desenvolvimento, guarda todos os dados do projeto num único ficheiro.",
    },
    {
        "nome": "Git",
        "tipo": "Outros",
        "site_oficial": "https://git-scm.com/",
        "nivel_interesse": 4,
        "descricao": "Sistema de controlo de versões usado para gravar o histórico de alterações do projeto.",
    },
    {
        "nome": "GitHub",
        "tipo": "Outros",
        "site_oficial": "https://github.com/",
        "nivel_interesse": 5,
        "descricao": "Plataforma onde está alojado o repositório do projeto, usada para guardar e partilhar o código.",
    },
    {
        "nome": "GitHub Codespaces",
        "tipo": "Outros",
        "site_oficial": "https://github.com/features/codespaces",
        "nivel_interesse": 4,
        "descricao": "Ambiente de desenvolvimento na cloud, baseado em VS Code, usado para programar sem instalar nada localmente.",
    },
    {
        "nome": "Visual Studio Code",
        "tipo": "Outros",
        "site_oficial": "https://code.visualstudio.com/",
        "nivel_interesse": 5,
        "descricao": "Editor de código usado (via Codespaces) para escrever todo o projeto.",
    },
]

for t in tecnologias:
    tipo_obj = TipoTecnologia.objects.get(nome=t["tipo"])
    Tecnologia.objects.get_or_create(
        nome=t["nome"],
        defaults={
            "tipo": tipo_obj,
            "site_oficial": t["site_oficial"],
            "nivel_interesse": t["nivel_interesse"],
            "descricao": t["descricao"],
        },
    )

print(f"{len(tecnologias)} tecnologias criadas.")