from datetime import date

from pydantic import BaseModel

from sistema_escolar.modelos.usuario import UsuarioSchema


class Materia(BaseModel):
    """Modelo da Materia no BD"""

    id_materia: int
    id_professor: int
    nome: str
    data_inicio: date
    data_fim: date


class MateriaSchema(BaseModel):
    """Dados retornados da matéria com dados dos alunos e professor"""

    id_materia: int
    nome: str
    professor: UsuarioSchema
    data_inicio: date
    data_fim: date
    alunos: list[UsuarioSchema]


class CriarAtualizarMateriaSchema(BaseModel):
    """Dados necessários p/ atualizar ou criar uma matéria"""

    nome: str
    codigo_professor: int
    data_inicio: date
    data_fim: date
    codigo_alunos: list[int]


class MateriaPublicSchema(BaseModel):
    """Dados retornados da matéria sem dados dos alunos"""

    id_materia: int
    nome: str
    professor: str
    data_inicio: date
    data_fim: date
