from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Curso, Professor, Aluno


def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola_online/cursos.html', {'cursos': cursos})

def professores_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola_online/professores.html', {'professores': professores})

def alunos_view(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola_online/alunos.html', {'alunos': alunos})

def curso_view(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'escola_online/curso.html', {'curso': curso})