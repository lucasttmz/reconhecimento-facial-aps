from fastapi import APIRouter


router = APIRouter(prefix="/boletim", tags=["boletim"])


@router.get("/")
def boletim_do_aluno():
    """Lista todas as matérias que o aluno está cursando, incluindo notas e faltas"""
    return [
        {"materia": "matematica", "nota": 10, "faltas": 2},
        {"materia": "frances", "nota": 9, "faltas": 0},
    ]


@router.get("/{id_materia}")
def boletim_do_aluno_em_uma_materia(id_materia: int):
    """Exibe informações detalhadas do aluno em uma matéria específica, incluindo as notas e faltas"""
    return {"materia": "frances", "nota": 10, "faltas": 2}
