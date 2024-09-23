from pydantic import BaseModel

from datetime import datetime, date

from sistema_escolar.modelos.usuario import UsuarioSchema


class Materia(BaseModel):
    id_materia: int
    id_professor: int
    nome: str
    data_inicio: date
    data_fim: date


class MateriaSchema(BaseModel):
    nome: str
    professor: UsuarioSchema
    data_inicio: date
    data_fim: date
    alunos: list[UsuarioSchema]


class CriarAtualizarMateriaSchema(BaseModel):
    nome: str
    codigo_professor: str
    data_inicio: date
    data_fim: date
    codigo_alunos: list[str]


class MateriaPublicSchema(BaseModel):
    """Matéria sem os dados do professor e alunos"""

    nome: str
    professor: str
    data_inicio: date
    data_fim: date
