from ninja import Schema
from typing import List, Optional

class TecnologiaSchema(Schema):
    id: int
    nome: str
    nivel_interesse: int
    descricao: Optional[str] = None

class TecnologiaCreateSchema(Schema):
    nome: str
    nivel_interesse: int
    descricao: Optional[str] = None
    tipo_id: Optional[int] = None

class UnidadeCurricularSchema(Schema):
    id: int
    nome: str
    ano: int
    ects: int

class ProjetoSchema(Schema):
    id: int
    nome: str
    descricao: str
    unidade_curricular_id: Optional[int] = None
    tecnologias: List[int] = []

class ProjetoCreateSchema(Schema):
    nome: str
    descricao: str
    unidade_curricular_id: Optional[int] = None
    tecnologias: List[int] = []