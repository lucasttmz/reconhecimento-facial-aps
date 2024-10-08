from typing import Annotated

from fastapi import APIRouter, Depends

from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.modelos.usuario import UsuarioSchema


router = APIRouter(tags=["usuarios"])
T_UsuarioControle = Annotated[UsuarioControle, Depends(UsuarioControle)]


@router.get("/alunos", response_model=list[UsuarioSchema])
def listar_todos_alunos(controle: T_UsuarioControle):
    """Lista todos os alunos"""

    return controle.listar_todos_alunos()


@router.get("/alunos/{id_aluno}", response_model=UsuarioSchema)
def pesquisar_aluno(id_aluno: int, controle: T_UsuarioControle):
    """Exibe as informações de um aluno em específico"""

    return controle.listar_info_aluno(id_aluno)


@router.get("/professores", response_model=list[UsuarioSchema])
def listar_todos_professores(controle: T_UsuarioControle):
    """Lista todos os professores"""

    return controle.listar_todos_professores()


@router.get("/professores/{id_professor}", response_model=UsuarioSchema)
def pesquisar_professor(id_professor: int, controle: T_UsuarioControle):
    """Exibe as informações de um professor em específico"""

    return controle.listar_info_professor(id_professor)
