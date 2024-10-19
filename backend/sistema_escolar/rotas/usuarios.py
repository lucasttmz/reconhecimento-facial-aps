from http import HTTPStatus
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException

from sistema_escolar.controladores.autenticacao import usuario_autenticado, possui_permissao
from sistema_escolar.controladores.usuarios import UsuarioControle
from sistema_escolar.modelos.usuario import UsuarioSchema, AtualizarUsuarioSchema, TipoUsuario
from sistema_escolar.modelos.genericos import MensagemSchema


router = APIRouter(tags=["usuarios"])
T_UsuarioControle = Annotated[UsuarioControle, Depends(UsuarioControle)]
T_Usuario = Annotated[dict[str, Any], Depends(usuario_autenticado)]


@router.get("/alunos", response_model=list[UsuarioSchema])
def listar_todos_alunos(controle: T_UsuarioControle, usuario: T_Usuario):
    """Lista todos os alunos"""

    if not possui_permissao(usuario, [TipoUsuario.PROFESSOR, TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return controle.listar_todos_alunos()


@router.get("/alunos/{id_aluno}", response_model=UsuarioSchema)
def pesquisar_aluno(id_aluno: int, controle: T_UsuarioControle, usuario: T_Usuario):
    """Exibe as informações de um aluno em específico"""

    if not possui_permissao(usuario, [TipoUsuario.PROFESSOR, TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return controle.listar_info_aluno(id_aluno)


@router.get("/professores", response_model=list[UsuarioSchema])
def listar_todos_professores(controle: T_UsuarioControle, usuario: T_Usuario):
    """Lista todos os professores"""

    if not possui_permissao(usuario, [TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return controle.listar_todos_professores()


@router.get("/professores/{id_professor}", response_model=UsuarioSchema)
def pesquisar_professor(
    id_professor: int, 
    controle: T_UsuarioControle, 
    usuario: T_Usuario
):
    """Exibe as informações de um professor em específico"""

    if not possui_permissao(usuario, [TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return controle.listar_info_professor(id_professor)


@router.put("/usuarios/{id_usuario}", response_model=MensagemSchema)
def atualizar_cargo(
    id_usuario: int, 
    tipo_atualizado: AtualizarUsuarioSchema, 
    controle: T_UsuarioControle, 
    usuario: T_Usuario
):
    """Atualiza o cargo do usuário"""

    if not possui_permissao(usuario, [TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return controle.atualizar_usuario(id_usuario, tipo_atualizado)
