from datetime import datetime, timedelta
from random import randint

from fastapi import APIRouter

from sistema_escolar.modelos.usuario import TipoUsuario
from sistema_escolar.modelos.materia import MateriaSchema
from sistema_escolar.modelos.boletim import (
    BoletimParaProfessorSchema,
    NotaSchema,
    FaltaSchema,
)
from sistema_escolar.modelos.genericos import Mensagem


router = APIRouter(prefix="/materias", tags=["materias"])


@router.get("/", response_model=list[MateriaSchema])
def todas_as_materias():
    """
    Professor: Lista todas as matérias que o professor está ensinando.
    Diretor: Lista todas as matérias.
    """
    return [
        {
            "nome": "portugues",
            "professor": {
                "codigo": "PF_J040",
                "nome": "João",
                "tipo": TipoUsuario.PROFESSOR,
            },
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
            "alunos": [],
        },
        {
            "nome": "matematica",
            "professor": {
                "codigo": "PF_M4R14",
                "nome": "Maria",
                "tipo": TipoUsuario.PROFESSOR,
            },
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
            "alunos": [
                {
                    "codigo": "AL_LUC4S",
                    "nome": "lucas",
                    "tipo": TipoUsuario.ALUNO,
                },
                {
                    "codigo": "AL_F3L1P3",
                    "nome": "felipe",
                    "tipo": TipoUsuario.ALUNO,
                },
            ],
        },
    ]


@router.get("/{id_materia}", response_model=MateriaSchema)
def pesquisar_materia(id_materia: int):
    """Exibe informações da matéria e todos os alunos cursando ela"""
    return {
        "nome": f"nome da materia {id_materia}",
        "professor": {
            "codigo": f"PF_COD{id_materia}",
            "nome": f"Prof. da matéria {id_materia}",
            "tipo": TipoUsuario.PROFESSOR,
        },
        "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
        "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
        "alunos": [
            {
                "codigo": "AL_LUC4S",
                "nome": "lucas",
                "tipo": TipoUsuario.ALUNO,
            },
            {
                "codigo": "AL_F3L1P3",
                "nome": "felipe",
                "tipo": TipoUsuario.ALUNO,
            },
        ],
    }


@router.get("/{id_materia}/aluno/{id_aluno}", response_model=BoletimParaProfessorSchema)
def materias_do_aluno(id_materia: int, id_aluno: int):
    """Exibe o boletim do aluno na matéria"""
    return {
        "aluno": {
            "codigo": f"AL_{id_aluno}",
            "nome": f"nome de {id_aluno}",
            "tipo": TipoUsuario.ALUNO,
        },
        "materia": {
            "nome": "matematica",
            "professor": "Maria",
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
        },
        "nota": 10,
        "faltas": 2,
    }


@router.put("/{id_materia}/aluno/{id_aluno}/nota", response_model=Mensagem)
def lancar_nota(id_materia: int, id_aluno: int, nota: NotaSchema):
    """Lançar nota para o aluno"""
    return {"mensagem": f"Nota atualizada com sucesso: {nota.nota}"}


@router.put("/{id_materia}/aluno/{id_aluno}/falta", response_model=Mensagem)
def lancar_falta(id_materia: int, id_aluno: int, faltas: FaltaSchema):
    """Lançar falta para o aluno"""
    return {"mensagem": f"Falta atualizada com sucesso: {faltas.faltas}"}
