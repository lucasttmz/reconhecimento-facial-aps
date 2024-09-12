from random import randint
from typing import Annotated

from fastapi import APIRouter, Depends

from sistema_escolar.modelos.materia import MateriaSchema
from sistema_escolar.modelos.boletim import (
    BoletimParaProfessorSchema,
    NotaSchema,
    FaltaSchema,
)
from sistema_escolar.modelos.genericos import MensagemSchema
from sistema_escolar.controladores.materias import MateriaControle
from sistema_escolar.controladores.boletim import BoletimControle


router = APIRouter(prefix="/materias", tags=["materias"])
T_MateriaControle = Annotated[MateriaControle, Depends(MateriaControle)]
T_BoletimControle = Annotated[BoletimControle, Depends(BoletimControle)]


@router.get("/", response_model=list[MateriaSchema])
def todas_as_materias(controle: T_MateriaControle):
    """
    Professor: Lista todas as matérias que o professor está ensinando.
    Diretor: Lista todas as matérias registradas.
    """

    # TODO: Pegar o id do usuário logado
    id_aluno_atual = randint(0, 5)
    return controle.listar_todas_materias(id_aluno_atual)
    

@router.get("/{id_materia}", response_model=MateriaSchema)
def pesquisar_materia(id_materia: int, controle: T_MateriaControle):
    """Exibe informações da matéria e todos os alunos cursando ela"""

    return controle.listar_materia(id_materia)


@router.get("/{id_materia}/aluno/{id_aluno}", response_model=BoletimParaProfessorSchema)
def materia_do_aluno(id_materia: int, id_aluno: int, controle: T_BoletimControle):
    """Exibe o boletim do aluno na matéria"""

    return controle.listar_boletim_para_professores(id_aluno, id_materia)


@router.put("/{id_materia}/aluno/{id_aluno}/nota", response_model=MensagemSchema)
def lancar_nota(id_materia: int, id_aluno: int, nota: NotaSchema, controle: T_MateriaControle):
    """Lançar nota para o aluno"""
    
    return controle.atualizar_nota(id_materia, id_aluno, nota.nota)


@router.put("/{id_materia}/aluno/{id_aluno}/falta", response_model=MensagemSchema)
def lancar_falta(id_materia: int, id_aluno: int, faltas: FaltaSchema, controle: T_MateriaControle):
    """Lançar falta para o aluno"""

    return controle.atualizar_qtd_faltas(id_materia, id_aluno, faltas.faltas)
