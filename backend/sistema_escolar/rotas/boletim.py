from http import HTTPStatus
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException

from sistema_escolar.modelos.boletim import BoletimParaAlunoSchema
from sistema_escolar.modelos.usuario import TipoUsuario
from sistema_escolar.controladores.boletim import BoletimControle
from sistema_escolar.controladores.autenticacao import usuario_autenticado, possui_permissao


router = APIRouter(prefix="/boletim", tags=["boletim"])
T_BoletimControle = Annotated[BoletimControle, Depends(BoletimControle)]
T_Usuario = Annotated[dict[str, Any], Depends(usuario_autenticado)]

@router.get("/", response_model=list[BoletimParaAlunoSchema])
def boletim_do_aluno(controle: T_BoletimControle, usuario: T_Usuario):
    """Lista todas as matérias que o aluno está cursando, incluindo notas e faltas"""

    if not possui_permissao(usuario, permitidos=[TipoUsuario.ALUNO]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)
    
    id_aluno_atual = usuario.get("id", 0)
    return controle.listar_boletim_aluno(id_aluno_atual)


@router.get("/{id_materia}", response_model=BoletimParaAlunoSchema)
def boletim_do_aluno_em_uma_materia(id_materia: int, controle: T_BoletimControle, usuario: T_Usuario):
    """Exibe informações detalhadas do aluno em uma matéria específica, incluindo as notas e faltas"""

    if not possui_permissao(usuario, permitidos=[TipoUsuario.ALUNO]):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)

    id_aluno_atual = usuario.get("id", 0)
    return controle.listar_boletim_aluno_em_materia(id_aluno_atual, id_materia)
