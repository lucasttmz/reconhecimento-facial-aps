from datetime import datetime, timedelta
from random import randint

from fastapi import APIRouter

from sistema_escolar.modelos import TipoUsuario


router = APIRouter(prefix="/materias", tags=["materias"])


@router.get("/")
def todas_as_materias():
    """Lista todas as matérias que o professor está ensinando"""
    return [
        {
            "nome": "portugues",
            "professor": "reverdan",
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
        },
        {
            "nome": "matematica",
            "professor": "samuel",
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
        },
    ]


@router.get("/{id_materia}")
def pesquisar_materia(id_materia: int):
    """Exibe informações da matéria e todos os alunos cursando ela"""
    return {
        "nome": f"nome da materia {id_materia}",
        "professor": f"professor da materia {id_materia}",
        "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
        "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
        "alunos": [
            {
                "matricula": "123",
                "nome": "lucas",
                "tipo": TipoUsuario.ALUNO,
            },
            {
                "matricula": "321",
                "nome": "felipe",
                "tipo": TipoUsuario.ALUNO,
            },
        ],
    }


@router.get("/{id_materia}/aluno/{id_aluno}")
def materias_do_aluno(id_materia: int, id_aluno: int):
    """Exibe o boletim do aluno na matéria"""
    return {"nota": 10, "faltas": 2}


@router.put("/{id_materia}/aluno/{id_aluno}/nota")
def lancar_nota(id_materia: int, id_aluno: int):
    """Lançar nota para o aluno"""
    return {"message": "Nota atualizada com sucesso"}


@router.put("/{id_materia}/aluno/{id_aluno}/falta")
def lancar_falta(id_materia: int, id_aluno: int):
    """Lançar falta para o aluno"""
    return {"message": "Falta atualizada com sucesso"}

