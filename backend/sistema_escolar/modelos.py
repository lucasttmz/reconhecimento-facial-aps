from datetime import date
from enum import IntEnum

from pydantic import BaseModel


class TipoUsuario(IntEnum):
    ALUNO = 1
    PROFESSOR = 2
    DIRETOR = 3


class Usuario(BaseModel):
    id_usuario: int
    matricula: str
    nome: str
    tipo: TipoUsuario


class UsuarioSchema(BaseModel):
    matricula: str
    nome: str
    tipo: TipoUsuario


class MateriaSchema(BaseModel):
    nome: str
    professor: str
    data_inicio: date
    data_fim: date
