from enum import IntEnum

from pydantic import BaseModel


class TipoUsuario(IntEnum):
    """Tipos dos usuários no BD"""

    ALUNO = 1
    PROFESSOR = 2
    DIRETOR = 3


class Usuario(BaseModel):
    """Modelo do Usuário no BD"""

    id_usuario: int
    codigo: str
    nome: str
    tipo: int


class UsuarioSchema(BaseModel):
    """Dados retornados do usuário"""

    id_usuario: int
    codigo: str
    nome: str
    tipo: TipoUsuario


class AtualizarUsuarioSchema(BaseModel):
    """Dados necessários p/ atualizar tipo de usuário"""

    tipo: TipoUsuario
