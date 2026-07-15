from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos_view, name='cursos_view'),
    path('', views.cursos_view),  # rota que abre diretamente a página dos cursos
]