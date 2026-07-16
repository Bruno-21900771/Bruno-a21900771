from django.urls import path
from . import views

urlpatterns = [
    path("", views.artigos_view, name="artigos_view"),
    path("registo/", views.artigos_registo_view, name="artigos_registo_view"),
    path("novo/", views.artigo_create_view, name="artigo_create_view"),
    path("<int:id>/", views.artigo_view, name="artigo_view"),
    path("<int:id>/editar/", views.artigo_edit_view, name="artigo_edit_view"),
    path("<int:id>/like/", views.like_view, name="like_view"),
    path("<int:id>/dislike/", views.dislike_view, name="dislike_view"),
]