from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.urls import reverse
from .models import Artigo, Comentario, Avaliacao
from .forms import ArtigoForm, ComentarioForm
from accounts.forms import RegistoForm

# Create your views here.

def is_autor(user):
    return user.groups.filter(name="bloggers").exists()


autor_required = user_passes_test(is_autor, login_url="login_view")


def artigos_view(request):
    artigos = Artigo.objects.select_related("autor").order_by("-data_criacao")
    return render(request, "artigos/artigos.html", {"artigos": artigos})


def artigo_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.order_by("-data_criacao")

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.save()
            return redirect(f"{reverse('artigo_view', args=[artigo.id])}#comentarios-{artigo.id}")
    else:
        initial = {}
        if request.user.is_authenticated:
            initial["autor"] = request.user.username
        form = ComentarioForm(initial=initial)

    pode_editar = request.user.is_authenticated and request.user == artigo.autor

    return render(request, "artigos/artigo_detail.html", {
        "artigo": artigo,
        "comentarios": comentarios,
        "form": form,
        "pode_editar": pode_editar,
    })


@login_required
@autor_required
def artigo_create_view(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect("artigo_view", id=artigo.id)
    else:
        form = ArtigoForm()
    return render(request, "artigos/artigo_form.html", {"form": form, "titulo": "Novo Artigo"})


@login_required
@autor_required
def artigo_edit_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect("artigo_view", id=artigo.id)

    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect("artigo_view", id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, "artigos/artigo_form.html", {"form": form, "titulo": "Editar Artigo"})


def like_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    artigo.likes += 1
    artigo.save()
    return redirect("artigo_view", id=artigo.id)


def dislike_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    artigo.dislikes += 1
    artigo.save()
    return redirect("artigo_view", id=artigo.id)


def avaliacao_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if request.method == "POST":
        pontuacao = request.POST.get("pontuacao")
        if pontuacao and pontuacao.isdigit() and 1 <= int(pontuacao) <= 5:
            Avaliacao.objects.create(artigo=artigo, pontuacao=int(pontuacao))
    return redirect(f"{reverse('artigo_view', args=[artigo.id])}#avaliar-{artigo.id}")


def artigos_registo_view(request):
    if request.method == "POST":
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, _ = Group.objects.get_or_create(name="bloggers")
            user.groups.add(grupo)
            login(request, user)
            return redirect("artigos_view")
    else:
        form = RegistoForm()
    return render(request, "artigos/registo.html", {"form": form})