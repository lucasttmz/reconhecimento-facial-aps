from enum import IntEnum

from pydantic import BaseModel


class TipoUsuario(IntEnum):
    ALUNO = 1
    PROFESSOR = 2
    DIRETOR = 3


class Usuario(BaseModel):
    id_usuario: int
    codigo: str
    nome: str
    tipo: TipoUsuario


class UsuarioSchema(BaseModel):
    codigo: str
    nome: str
    tipo: TipoUsuario
