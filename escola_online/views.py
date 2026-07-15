from django.shortcuts import render

# Create your views here.

from .models import Curso


def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola_online/cursos.html', {'cursos': cursos})