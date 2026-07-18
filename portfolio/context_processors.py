def is_gestor(request):
    context = {"is_gestor": False, "is_autor": False}
    if request.user.is_authenticated:
        context["is_gestor"] = request.user.groups.filter(name="gestor-portfolio").exists()
        context["is_autor"] = request.user.groups.filter(name="bloggers").exists()
    return context