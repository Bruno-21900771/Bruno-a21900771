from django.core.management.base import BaseCommand
from portfolio.models import Licenciatura, UnidadeCurricular, TipoTecnologia, Tecnologia, Projeto
import random

class Command(BaseCommand):
    help = "Carrega dados de teste para a API"

    def handle(self, *args, **options):
        lic, _ = Licenciatura.objects.get_or_create(
            nome="Engenharia Informática",
            defaults={"grau": "Licenciatura", "duracao_anos": 3, "ects_totais": 180},
        )

        ucs_nomes = [
            ("Programação Web", 2, "2º Semestre", 6),
            ("Bases de Dados", 2, "1º Semestre", 6),
            ("Sistemas Operativos", 2, "1º Semestre", 6),
            ("Redes de Computadores", 2, "2º Semestre", 6),
            ("Inteligência Artificial", 3, "1º Semestre", 6),
        ]
        ucs = []
        for nome, ano, sem, ects in ucs_nomes:
            uc, _ = UnidadeCurricular.objects.get_or_create(
                licenciatura=lic, nome=nome,
                defaults={"ano": ano, "semestre": sem, "ects": ects},
            )
            ucs.append(uc)

        tipos = {n: TipoTecnologia.objects.get_or_create(nome=n)[0]
                 for n in ["Frontend", "Backend", "Base de Dados", "Storage", "Outros"]}

        tecnologias_dados = [
            ("Django", "Backend", 5, "Framework web em Python"),
            ("React", "Frontend", 4, "Biblioteca JS para interfaces"),
            ("PostgreSQL", "Base de Dados", 5, "SGBD relacional"),
            ("Neon", "Base de Dados", 4, "Postgres serverless"),
            ("Cloudinary", "Storage", 4, "Storage de media na cloud"),
            ("Docker", "Outros", 4, "Containers"),
            ("TypeScript", "Frontend", 4, "JS com tipagem estática"),
            ("Tauri", "Outros", 4, "Framework para apps desktop"),
            ("Python", "Backend", 5, "Linguagem de programação"),
            ("Git", "Outros", 5, "Controlo de versões"),
        ]
        tecnologias = []
        for nome, tipo_nome, nivel, desc in tecnologias_dados:
            tec, _ = Tecnologia.objects.get_or_create(
                nome=nome, defaults={"tipo": tipos[tipo_nome], "nivel_interesse": nivel, "descricao": desc},
            )
            tecnologias.append(tec)

        projetos_dados = [
            ("Portfólio Django", "Aplicação de portfólio académico com Django."),
            ("Ária - Assistente Pessoal", "Assistente pessoal com Tauri, React e API Anthropic."),
            ("API RESTful Biblioteca", "API REST para gestão de biblioteca."),
            ("Sistema de Reservas", "Sistema web de reservas de salas."),
            ("Dashboard de Análise", "Dashboard de visualização de dados."),
        ]
        for nome, desc in projetos_dados:
            projeto, created = Projeto.objects.get_or_create(
                nome=nome, defaults={"descricao": desc, "unidade_curricular": random.choice(ucs)},
            )
            if created:
                projeto.tecnologias.set(random.sample(tecnologias, k=random.randint(2, 4)))

        self.stdout.write(self.style.SUCCESS("Dados de teste carregados."))