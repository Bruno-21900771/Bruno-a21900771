from ninja import NinjaAPI
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Projeto, Tecnologia, UnidadeCurricular
from .schemas import (
    ProjetoSchema, ProjetoCreateSchema,
    TecnologiaSchema, TecnologiaCreateSchema,
    UnidadeCurricularSchema,
)

api = NinjaAPI(title="Portfolio API", version="1.0.0")

# ---------- Tecnologia ----------
@api.get("/tecnologias/", response=list[TecnologiaSchema])
@paginate(PageNumberPagination, page_size=10)
def listar_tecnologias(request, nome: str = None, tipo_id: int = None):
    qs = Tecnologia.objects.all()
    if nome:
        qs = qs.filter(nome__icontains=nome)
    if tipo_id:
        qs = qs.filter(tipo_id=tipo_id)
    return qs

@api.post("/tecnologias/", response=TecnologiaSchema)
def criar_tecnologia(request, payload: TecnologiaCreateSchema):
    return Tecnologia.objects.create(**payload.dict())

@api.get("/tecnologias/{tecnologia_id}/", response=TecnologiaSchema)
def obter_tecnologia(request, tecnologia_id: int):
    return get_object_or_404(Tecnologia, id=tecnologia_id)

@api.put("/tecnologias/{tecnologia_id}/", response=TecnologiaSchema)
def atualizar_tecnologia(request, tecnologia_id: int, payload: TecnologiaCreateSchema):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    for attr, value in payload.dict().items():
        setattr(tecnologia, attr, value)
    tecnologia.save()
    return tecnologia

@api.delete("/tecnologias/{tecnologia_id}/")
def apagar_tecnologia(request, tecnologia_id: int):
    get_object_or_404(Tecnologia, id=tecnologia_id).delete()
    return {"sucesso": True}


# ---------- Projeto (com M2M tecnologias) ----------
@api.get("/projetos/", response=list[ProjetoSchema])
@paginate(PageNumberPagination, page_size=10)
def listar_projetos(request, nome: str = None, unidade_curricular_id: int = None):
    qs = Projeto.objects.all()
    if nome:
        qs = qs.filter(nome__icontains=nome)
    if unidade_curricular_id:
        qs = qs.filter(unidade_curricular_id=unidade_curricular_id)
    return qs

@api.post("/projetos/", response=ProjetoSchema)
def criar_projeto(request, payload: ProjetoCreateSchema):
    data = payload.dict()
    tecnologias_ids = data.pop("tecnologias", [])
    projeto = Projeto.objects.create(**data)
    projeto.tecnologias.set(tecnologias_ids)
    return projeto

@api.get("/projetos/{projeto_id}/", response=ProjetoSchema)
def obter_projeto(request, projeto_id: int):
    return get_object_or_404(Projeto, id=projeto_id)

@api.put("/projetos/{projeto_id}/", response=ProjetoSchema)
def atualizar_projeto(request, projeto_id: int, payload: ProjetoCreateSchema):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    data = payload.dict()
    tecnologias_ids = data.pop("tecnologias", [])
    for attr, value in data.items():
        setattr(projeto, attr, value)
    projeto.save()
    projeto.tecnologias.set(tecnologias_ids)
    return projeto

@api.delete("/projetos/{projeto_id}/")
def apagar_projeto(request, projeto_id: int):
    get_object_or_404(Projeto, id=projeto_id).delete()
    return {"sucesso": True}


# ---------- UnidadeCurricular ----------
@api.get("/unidades-curriculares/", response=list[UnidadeCurricularSchema])
@paginate(PageNumberPagination, page_size=10)
def listar_ucs(request, nome: str = None, ano: int = None):
    qs = UnidadeCurricular.objects.all()
    if nome:
        qs = qs.filter(nome__icontains=nome)
    if ano:
        qs = qs.filter(ano=ano)
    return qs

@api.post("/unidades-curriculares/", response=UnidadeCurricularSchema)
def criar_uc(request, payload: UnidadeCurricularSchema):
    return UnidadeCurricular.objects.create(**payload.dict(exclude={"id"}))

@api.get("/unidades-curriculares/{uc_id}/", response=UnidadeCurricularSchema)
def obter_uc(request, uc_id: int):
    return get_object_or_404(UnidadeCurricular, id=uc_id)

@api.put("/unidades-curriculares/{uc_id}/", response=UnidadeCurricularSchema)
def atualizar_uc(request, uc_id: int, payload: UnidadeCurricularSchema):
    uc = get_object_or_404(UnidadeCurricular, id=uc_id)
    for attr, value in payload.dict(exclude={"id"}).items():
        setattr(uc, attr, value)
    uc.save()
    return uc

@api.delete("/unidades-curriculares/{uc_id}/")
def apagar_uc(request, uc_id: int):
    get_object_or_404(UnidadeCurricular, id=uc_id).delete()
    return {"sucesso": True}