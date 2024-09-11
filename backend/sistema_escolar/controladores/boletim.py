from datetime import datetime, timedelta
from random import randint

from fastapi import APIRouter

from sistema_escolar.modelos.boletim import BoletimParaAlunoSchema


router = APIRouter(prefix="/boletim", tags=["boletim"])


@router.get("/", response_model=list[BoletimParaAlunoSchema])
def boletim_do_aluno():
    """Lista todas as matérias que o aluno está cursando, incluindo notas e faltas"""
    return [
        {
            "materia": {
                "nome": "matematica",
                "professor": "Maria",
                "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
                "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
            },
            "nota": 10,
            "faltas": 2,
        },
        {
            "materia": {
                "nome": "portugues",
                "professor": "Joao",
                "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
                "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
            },
            "nota": 9,
            "faltas": 0,
        },
    ]


@router.get("/{id_materia}", response_model=BoletimParaAlunoSchema)
def boletim_do_aluno_em_uma_materia(id_materia: int):
    """Exibe informações detalhadas do aluno em uma matéria específica, incluindo as notas e faltas"""
    return {
        "materia": {
            "nome": f"nome materia {id_materia}",
            "professor": f"prof da materia {id_materia}",
            "data_inicio": datetime.now().date() - timedelta(days=randint(0, 10)),
            "data_fim": datetime.now().date() + timedelta(days=randint(0, 10)),
        },
        "nota": 5,
        "faltas": 30,
    }
