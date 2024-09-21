from pydantic import BaseModel

from datetime import date

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


class CriarMateriaSchema(BaseModel):
    nome: str
    codigo_professor: str
    data_inicio: date
    data_fim: date


class MateriaPublicSchema(BaseModel):
    """Matéria sem os dados do professor"""

    nome: str
    professor: str
    data_inicio: date
    data_fim: date
