from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos_view, name='cursos_view'),
    path('curso/<int:id>', views.curso_view, name='curso_view'),
    path('professores/', views.professores_view, name='professores_view'),
    path('alunos/', views.alunos_view, name='alunos_view'),
    path('', views.cursos_view),
]