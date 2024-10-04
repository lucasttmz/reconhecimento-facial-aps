from random import randint
from typing import Annotated

from fastapi import APIRouter, Depends

from sistema_escolar.modelos.boletim import BoletimParaAlunoSchema
from sistema_escolar.controladores.boletim import BoletimControle


router = APIRouter(prefix="/boletim", tags=["boletim"])
T_BoletimControle = Annotated[BoletimControle, Depends(BoletimControle)]

@router.get("/", response_model=list[BoletimParaAlunoSchema])
def boletim_do_aluno(controle: T_BoletimControle):
    """Lista todas as matérias que o aluno está cursando, incluindo notas e faltas"""

    # TODO: Pegar o id do usuário logado
    id_aluno_atual = randint(3, 5)
    return controle.listar_boletim_aluno(id_aluno_atual)


@router.get("/{id_materia}", response_model=BoletimParaAlunoSchema)
def boletim_do_aluno_em_uma_materia(id_materia: int, controle: T_BoletimControle):
    """Exibe informações detalhadas do aluno em uma matéria específica, incluindo as notas e faltas"""

    # TODO: Pegar o id do usuário logado
    id_aluno_atual = 3
    return controle.listar_boletim_aluno_em_materia(id_aluno_atual, id_materia)
