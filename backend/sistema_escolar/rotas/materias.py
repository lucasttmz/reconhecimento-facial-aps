from http import HTTPStatus
from typing import Annotated, Any, Union

from fastapi import APIRouter, Depends, HTTPException

from sistema_escolar.modelos.materia import (
    MateriaSchema,
    MateriaPublicSchema,
    CriarAtualizarMateriaSchema,
)
from sistema_escolar.modelos.boletim import (
    BoletimParaProfessorSchema,
    AtualizarBoletimSchema,
)
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.modelos.usuario import TipoUsuario
from sistema_escolar.controladores.autenticacao import possui_permissao, usuario_autenticado
from sistema_escolar.controladores.materias import MateriaControle
from sistema_escolar.controladores.boletim import BoletimControle


router = APIRouter(prefix="/materias", tags=["materias"])
T_MateriaControle = Annotated[MateriaControle, Depends(MateriaControle)]
T_BoletimControle = Annotated[BoletimControle, Depends(BoletimControle)]
T_Usuario = Annotated[dict[str, Any], Depends(usuario_autenticado)]


@router.get("/", response_model=Union[list[MateriaSchema], list[MateriaPublicSchema]])
def todas_as_materias(controle: T_MateriaControle, usuario: T_Usuario):
    """Lista todas as matérias"""

    if not possui_permissao(usuario, [TipoUsuario.PROFESSOR, TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)
    
    # Diretor pode ver todas as materias
    if usuario.get("permissoes") == TipoUsuario.DIRETOR:
        return controle.listar_todas_materias()
    
    # Professor somente ve as materias que ele ensina
    return controle.listar_todas_materias_do_professor(usuario.get("id", 0))


@router.post("/", response_model=MensagemSchema)
def criar_materia(
    materia: CriarAtualizarMateriaSchema, 
    mat_controle: T_MateriaControle, 
    bol_controle: T_BoletimControle,
    usuario: T_Usuario
):
    """Cria uma nova matéria associada a um professor"""

    if not possui_permissao(usuario, [TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return mat_controle.criar_materia(materia, bol_controle)


@router.get("/{id_materia}", response_model=MateriaSchema)
def pesquisar_materia(id_materia: int, controle: T_MateriaControle, usuario: T_Usuario):
    """Exibe informações da matéria e todos os alunos cursando ela"""

    if not possui_permissao(usuario, [TipoUsuario.PROFESSOR, TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)
    
    # Diretor pode ver todas as materias
    if usuario.get("permissoes") == TipoUsuario.DIRETOR:
        return controle.listar_materia(id_materia)

    # Professor somente ve as materias que ele ensina
    return controle.listar_materia_do_professor(id_materia, usuario.get("id", 0))


@router.put("/{id_materia}", response_model=MensagemSchema)
def atualizar_materia(
    id_materia: int, 
    materia: CriarAtualizarMateriaSchema, 
    mat_controle: T_MateriaControle, 
    bol_controle: T_BoletimControle,
    usuario: T_Usuario
):
    """Cria uma nova matéria associada a um professor"""

    if not possui_permissao(usuario, [TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return mat_controle.atualizar_materia(id_materia, materia, bol_controle)


@router.get("/{id_materia}/aluno/{id_aluno}", response_model=BoletimParaProfessorSchema)
def materia_do_aluno(
    id_materia: int, 
    id_aluno: int, 
    boletim: T_BoletimControle,
    materia: T_MateriaControle,
    usuario: T_Usuario
):
    """Exibe o boletim do aluno na matéria"""

    if not possui_permissao(usuario, [TipoUsuario.PROFESSOR, TipoUsuario.DIRETOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)
    
    # Professores somente podem ver matérias que ele ensina
    if (
        usuario.get("permissoes") == TipoUsuario.PROFESSOR
        and not materia.professor_ensina_materia(usuario.get("id", 0), id_materia)
    ):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return boletim.listar_boletim_para_professores(id_aluno, id_materia)


@router.put("/{id_materia}/aluno/{id_aluno}", response_model=MensagemSchema)
def lancar_nota_e_faltas(
    id_materia: int,
    id_aluno: int,
    boletim: AtualizarBoletimSchema,
    controle: T_MateriaControle,
    usuario: T_Usuario
):
    """Lançar nota e faltas para o aluno"""

    if not possui_permissao(usuario, [TipoUsuario.PROFESSOR]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)
    
    # Somente pode alterar matérias que ele ensina
    if not controle.professor_ensina_materia(usuario.get("id", 0), id_materia):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    return controle.atualizar_nota_e_faltas(
        id_materia, id_aluno, boletim.nota, faltas=boletim.faltas
    )
