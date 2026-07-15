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
]