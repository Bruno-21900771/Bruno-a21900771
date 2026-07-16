from django.urls import path
from . import views

urlpatterns = [
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas_view'),
    path('unidades-curriculares/', views.ucs_view, name='ucs_view'),
    path('tfcs/', views.tfcs_view, name='tfcs_view'),
    path('projetos/', views.projetos_view, name='projetos_view'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias_view'),
    path('competencias/', views.competencias_view, name='competencias_view'),
    path('formacoes/', views.formacoes_view, name='formacoes_view'),
    path('docentes/', views.docentes_view, name='docentes_view'),
    path('', views.licenciaturas_view, name='home_view'),
    path('projetos/novo/', views.projeto_create_view, name='projeto_create'),
    path('projetos/<int:id>/editar/', views.projeto_edit_view, name='projeto_edit'),
    path('projetos/<int:id>/apagar/', views.projeto_delete_view, name='projeto_delete'),
    path('tecnologias/nova/', views.tecnologia_create_view, name='tecnologia_create'),
    path('tecnologias/<int:id>/editar/', views.tecnologia_edit_view, name='tecnologia_edit'),
    path('tecnologias/<int:id>/apagar/', views.tecnologia_delete_view, name='tecnologia_delete'),
    path('competencias/nova/', views.competencia_create_view, name='competencia_create'),
    path('competencias/<int:id>/editar/', views.competencia_edit_view, name='competencia_edit'),
    path('competencias/<int:id>/apagar/', views.competencia_delete_view, name='competencia_delete'),
    path('formacoes/nova/', views.formacao_create_view, name='formacao_create'),
    path('formacoes/<int:id>/editar/', views.formacao_edit_view, name='formacao_edit'),
    path('formacoes/<int:id>/apagar/', views.formacao_delete_view, name='formacao_delete'),
]