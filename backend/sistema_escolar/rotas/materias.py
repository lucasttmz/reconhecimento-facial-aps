from random import randint
from typing import Annotated

from fastapi import APIRouter, Depends

from sistema_escolar.modelos.materia import MateriaSchema, CriarAtualizarMateriaSchema
from sistema_escolar.modelos.boletim import (
    BoletimParaProfessorSchema,
    AtualizarBoletimSchema,
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
    return controle.listar_todas_materias()


@router.post("/", response_model=MensagemSchema)
def criar_materia(materia: CriarAtualizarMateriaSchema, controle: T_MateriaControle):
    """Cria uma nova matéria associada a um professor"""

    return controle.criar_nova_materia(materia)
    

@router.get("/{id_materia}", response_model=MateriaSchema)
def pesquisar_materia(id_materia: int, controle: T_MateriaControle):
    """Exibe informações da matéria e todos os alunos cursando ela"""

    return controle.listar_materia(id_materia)
    

@router.put("/{id_materia}", response_model=MensagemSchema)
def atualizar_materia(id_materia: int, materia: CriarAtualizarMateriaSchema, controle: T_MateriaControle):
    """Cria uma nova matéria associada a um professor"""
    return controle.atualizar_materia(id_materia, materia)


@router.get("/{id_materia}/aluno/{id_aluno}", response_model=BoletimParaProfessorSchema)
def materia_do_aluno(id_materia: int, id_aluno: int, controle: T_BoletimControle):
    """Exibe o boletim do aluno na matéria"""

    return controle.listar_boletim_para_professores(id_aluno, id_materia)


@router.put("/{id_materia}/aluno/{id_aluno}", response_model=MensagemSchema)
def lancar_nota_e_faltas(id_materia: int, id_aluno: int, boletim: AtualizarBoletimSchema, controle: T_MateriaControle):
    """Lançar nota e faltas para o aluno"""
    
    return controle.atualizar_nota_e_faltas(id_materia, id_aluno, boletim.nota, faltas=boletim.faltas)
