def is_gestor(request):
    if request.user.is_authenticated:
        return {"is_gestor": request.user.groups.filter(name="gestor-portfolio").exists()}
    return {"is_gestor": False}

def is_gestor(request):
    context = {"is_gestor": False, "is_autor": False}
    if request.user.is_authenticated:
        context["is_gestor"] = request.user.groups.filter(name="gestor-portfolio").exists()
        context["is_autor"] = request.user.groups.filter(name="autores").exists()
    return context