import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Tecnologia, Projeto, Competencia

# Atualiza a descrição do projeto "Portfólio Django" se já existir, ou cria-o
projeto_portfolio, _ = Projeto.objects.get_or_create(
    nome="Portfólio Django",
    defaults={"descricao": ""},
)
projeto_portfolio.descricao = (
    "Aplicação de portfólio pessoal desenvolvida em Django, com arquitetura MVT completa. "
    "Inclui CRUD para Projetos, Tecnologias, Competências e Formações, autenticação de "
    "utilizadores, e uma API RESTful construída com django-ninja. A base de dados PostgreSQL "
    "está alojada na Neon e os ficheiros de media na Cloudinary. O deploy é automatizado "
    "através de uma pipeline de CI/CD com GitHub Actions."
)
projeto_portfolio.link_github = "https://github.com/Bruno-21900771/Bruno-a21900771"
projeto_portfolio.save()

django_tec = Tecnologia.objects.filter(nome="Django").first()
python_tec = Tecnologia.objects.filter(nome="Python").first()
if django_tec and python_tec:
    projeto_portfolio.tecnologias.add(django_tec, python_tec)

# Cria as competências, ligando por nome
competencias = [
    {
        "nome": "Desenvolvimento Backend com Django",
        "categoria": "Backend",
        "nivel": 4,
        "projetos": ["Portfólio Django", "API RESTful Biblioteca"],
        "tecnologias": ["Django", "Python"],
    },
    {
        "nome": "Containerização e Deploy",
        "categoria": "DevOps",
        "nivel": 3,
        "projetos": ["Portfólio Django"],
        "tecnologias": ["Docker"],
    },
    {
        "nome": "Construção de Interfaces Web",
        "categoria": "Frontend",
        "nivel": 3,
        "projetos": ["Portfólio Django"],
        "tecnologias": ["HTML5", "CSS3"],
    },
]

for c in competencias:
    comp, _ = Competencia.objects.get_or_create(
        nome=c["nome"], defaults={"categoria": c["categoria"], "nivel": c["nivel"]},
    )
    projetos_obj = Projeto.objects.filter(nome__in=c["projetos"])
    tecnologias_obj = Tecnologia.objects.filter(nome__in=c["tecnologias"])
    comp.projetos.set(projetos_obj)
    comp.tecnologias.set(tecnologias_obj)

print("Competências e projeto de exemplo criados/atualizados.")