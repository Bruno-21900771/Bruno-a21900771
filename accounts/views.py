import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.


def login_view(request):
    erro = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("licenciaturas_view")
        erro = "Utilizador ou password incorretos"
    return render(request, "accounts/login.html", {"erro": erro})


def logout_view(request):
    logout(request)
    return redirect("landing_view")


def registo_view(request):
    if request.method == "POST":
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("licenciaturas_view")
    else:
        form = RegistoForm()
    return render(request, "accounts/registo.html", {"form": form})


signer = TimestampSigner()


def get_base_url():
    codespace_name = os.environ.get("CODESPACE_NAME")
    domain = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "app.github.dev")
    if codespace_name:
        return f"https://{codespace_name}-8000.{domain}"
    return "http://localhost:8000"


def magic_link_request_view(request):
    mensagem = None
    if request.method == "POST":
        email = request.POST["email"]
        try:
            user = User.objects.get(email=email)
            token = signer.sign(user.email)
            link = get_base_url() + reverse("magic_link_verify_view", args=[token])
            send_mail(
                "O teu link de login",
                f"Clica neste link para entrares: {link}\n\n(válido por 5 minutos)",
                "noreply@portfolio.com",
                [user.email],
            )
            mensagem = "Link enviado! Como estamos em modo de desenvolvimento, vai ver o terminal do Codespace para encontrares o link (aparece impresso ali)."
        except User.DoesNotExist:
            mensagem = "Não existe nenhuma conta com esse email."
    return render(request, "accounts/magic_link_request.html", {"mensagem": mensagem})


def magic_link_verify_view(request, token):
    try:
        email = signer.unsign(token, max_age=300)  # 5 minutos
        user = User.objects.get(email=email)
        login(request, user)
        return redirect("licenciaturas_view")
    except (BadSignature, SignatureExpired, User.DoesNotExist):
        return render(request, "accounts/magic_link_invalid.html")